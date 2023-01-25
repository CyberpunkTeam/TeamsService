from behave import *


@when('creo un position para el equipo "{team_name}"')
def step_impl(context, team_name):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    body = {
        "tid": context.vars["tid"],
        "title": "Software developer",
        "description": "We are looking for professionals who have a passion for learning, leading and feel the innovative spirit.",
    }
    url = "/teams_positions"

    context.response = context.client.post(url, json=body, headers=headers)


@then("se me informa que se creo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@when('existe un position para el equipo "{team_name}"')
def step_impl(context, team_name):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    body = {
        "tid": context.vars["tid"],
        "title": "Software developer",
        "description": "We are looking for professionals who have a passion for learning, leading and feel the innovative spirit.",
    }
    url = "/teams_positions"

    context.response = context.client.post(url, json=body, headers=headers)
    assert context.response.status_code == 201


@then("existen {amount} posiciones abiertas")
def step_impl(context, amount):
    """
    :type context: behave.runner.Context
    """
    url = "/teams_positions/?state=OPEN"
    response = context.client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == int(amount)
