import time
from datetime import datetime

from behave import *


@given("que quiero crear un equipo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    'completo el formulario de alta de equipo con nombre "{name}" , tecnologias "{technologies}" y preferencia de '
    'proyectos de tipo "{project_preferences}".'
)
def step_impl(context, name, technologies, project_preferences):
    """
    :param name:
    :param technologies:
    :param project_preferences:
    :type context: behave.runner.Context
    """
    technologies_list = technologies.split(",")
    project_preferences_list = project_preferences.split(",")

    context.vars["team_to_save"] = {
        "name": name,
        "technologies": technologies_list,
        "project_preferences": project_preferences_list,
        "owner": "1234",
    }


@step("confirmo el alta de equipo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/teams"

    context.response = context.client.post(
        url, json=context.vars["team_to_save"], headers=headers
    )


@then("se me informa que el equipo se creo con exito")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201
    local = datetime.now()
    team = context.response.json()
    assert team.get("created_date").split(":")[0] == local.strftime("%d-%m-%Y")
    assert team.get("updated_date").split(":")[0] == local.strftime("%d-%m-%Y")


@when('completo el formulario de alta de equipo y no completo el "{field_name}"')
def step_impl(context, field_name):
    """
    :param field_name:
    :type context: behave.runner.Context
    """
    field_spanish_to_english = {
        "nombre": "name",
        "tecnologias": "technologies",
        "preferencias de proyecto": "project_preferences",
    }
    team_to_save = {
        "name": "GreenTeam",
        "technologies": ["Python", "JS"],
        "project_preferences": ["Web", "AI"],
        "owner": "1234",
    }
    del team_to_save[field_spanish_to_english[field_name]]
    context.vars["team_to_save"] = team_to_save


@then('se me informa el campo "{field_name}" es obligatorio')
def step_impl(context, field_name):
    """
    :param field_name:
    :type context: behave.runner.Context
    """
    field_spanish_to_english = {
        "nombre": "name",
        "tecnologias": "technologies",
        "preferencias de proyecto": "project_preferences",
    }
    assert context.response.status_code >= 422
    json_body = context.response.json()
    msg = json_body["detail"][0]["msg"]
    missing_fields = json_body["detail"][0]["loc"]
    assert field_spanish_to_english[field_name] in missing_fields
    assert msg == "field required"


@step('ya existe un equipo con nombre "{name}"')
def step_impl(context, name):
    """
    :param name:
    :type context: behave.runner.Context
    """
    team_to_save = {
        "name": name,
        "technologies": ["Python", "JS"],
        "project_preferences": ["Web", "AI"],
        "owner": "1234",
    }

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/teams"

    response = context.client.post(url, json=team_to_save, headers=headers)

    assert response.status_code == 201
    context.vars["tid"] = response.json()["tid"]
    context.vars[f"{name}_tid"] = response.json()["tid"]


@then("se me informa que ya existe un equipo con ese nombre")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 400
    assert context.response.json()["detail"] == "Team name is not available"


@given("que quiero agregar a un miembro a un equipo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.vars["new_member_uid"] = "456667787"


@when('agrego a un miembro a el equipo con nombre "{name}"')
def step_impl(context, name):
    """
    :param name:
    :type context: behave.runner.Context
    """
    url = "/teams/" + context.vars["tid"]
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    response = context.client.get(url, headers=headers)

    team = response.json()
    context.vars["members_amount"] = len(team["members"])

    url = "/teams/" + context.vars["tid"] + "/members/" + context.vars["new_member_uid"]
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    time.sleep(1)  # test created_date vs updated_date
    context.response = context.client.post(url, headers=headers)


@then("se me informa que se agrego correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@step("el equipo tiene un miembro mas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = "/teams/" + context.vars["tid"]
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    response = context.client.get(url, headers=headers)

    team = response.json()
    assert len(team["members"]) == context.vars["members_amount"] + 1
    assert team.get("created_date") < team.get("updated_date")


@given(
    'ya existe un equipo con nombre "{name}", tecnologias "{technologies}" y preferencia de proyectos de tipo "{project_preferences}".'
)
def step_impl(context, name, technologies, project_preferences):
    """
    :param name: str
    :param technologies: str
    :param project_preferences:str
    :type context: behave.runner.Context
    """
    technologies_list = technologies.split(",")
    project_preferences_list = project_preferences.split(",")
    owner = "1234"
    team_to_save = {
        "name": name,
        "technologies": technologies_list,
        "project_preferences": project_preferences_list,
        "owner": owner,
    }
    context.vars["owner"] = owner
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/teams"

    response = context.client.post(url, json=team_to_save, headers=headers)

    assert response.status_code == 201
    context.vars["tid"] = response.json()["tid"]


@when(
    'cuando actualizo el equipo a nombre "{name}", tecnologias "{technologies}" y preferencia de proyectos de tipo "{project_preferences}".'
)
def step_impl(context, name, technologies, project_preferences):
    """
    :param name: str
    :param technologies: str
    :param project_preferences:str
    :type context: behave.runner.Context
    """
    technologies_list = technologies.split(",")
    project_preferences_list = project_preferences.split(",")
    team_to_update = {
        "name": name,
        "technologies": technologies_list,
        "project_preferences": project_preferences_list,
    }
    context.vars["team_to_update"] = team_to_update


@then("se me informa que se actualizo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/teams/" + context.vars["tid"]

    response = context.client.put(
        url, json=context.vars["team_to_update"], headers=headers
    )

    assert response.status_code == 200


@step(
    'puedo ver que el equipo se actualizo a nombre "{name}", tecnologias "{technologies}" y preferencia de proyectos de tipo "{project_preferences}".'
)
def step_impl(context, name, technologies, project_preferences):
    """
    :param name: str
    :param technologies: str
    :param project_preferences:str
    :type context: behave.runner.Context
    """
    url = "/teams/" + context.vars["tid"]
    technologies_list = technologies.split(",")
    project_preferences_list = project_preferences.split(",")
    response = context.client.get(url)

    assert response.status_code == 200

    team_updated = response.json()

    assert team_updated.get("name") == name
    assert team_updated.get("technologies") == technologies_list
    assert team_updated.get("project_preferences") == project_preferences_list
    assert team_updated.get("tid") == context.vars["tid"]
    assert team_updated.get("owner") == context.vars["owner"]


@when('busco "{word}"')
def step_impl(context, word):
    """
    :param word: str
    :type context: behave.runner.Context
    """
    url = f"/teams/?search={word}"
    context.response = context.client.get(url)

    assert context.response.status_code == 200


@then('me retorna al equipo con nombre "{name}"')
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    values = []
    for team in context.response.json():
        values.append(team.get("name"))

    assert name in values


@step("soy dueño de estos equipos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("busco mis equipos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = f"/teams/?owner={context.vars['owner']}"
    context.response = context.client.get(url)

    assert context.response.status_code == 200
