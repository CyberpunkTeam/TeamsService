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
