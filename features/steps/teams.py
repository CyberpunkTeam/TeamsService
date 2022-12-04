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
