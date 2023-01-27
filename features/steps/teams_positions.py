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


@step('existe un position para el equipo "{team_name}"')
def step_impl(context, team_name):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    body = {
        "tid": context.vars[f"{team_name}_tid"],
        "title": "Software developer",
        "description": "We are looking for professionals who have a passion for learning, leading and feel the innovative spirit.",
    }
    url = "/teams_positions"

    context.response = context.client.post(url, json=body, headers=headers)
    assert context.response.status_code == 201
    context.vars[f"{team_name}_tpid"] = context.response.json()["tpid"]


@then("existen {amount} posiciones abiertas")
def step_impl(context, amount):
    """
    :type context: behave.runner.Context
    """
    url = "/teams_positions/?state=OPEN"
    context.response = context.client.get(url)

    assert context.response.status_code == 200
    assert len(context.response.json()) == int(amount)


@step('la posicion del equipo "{team_name}" se cierra')
def step_impl(context, team_name):
    """
    :param team_name: str
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    tpid = context.vars[f"{team_name}_tpid"]
    state_updated = "CLOSED"
    body = {"state": state_updated}
    url = f"/teams_positions/{tpid}"
    response = context.client.put(url, json=body, headers=headers)
    assert response.status_code == 200
    team_position = response.json()
    assert team_position.get("state") == state_updated


@then("recibo {amount} posicion abierta")
def step_impl(context, amount):
    """
    :poram amount: str
    :type context: behave.runner.Context
    """
    assert len(context.response.json()) == int(amount)


@when("pido las posiciones abiertas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = "/teams_positions/?state=OPEN"
    context.response = context.client.get(url)

    assert context.response.status_code == 200


@when('pido las posiciones abiertas para el team "{team_name}"')
def step_impl(context, team_name):
    """
    :type context: behave.runner.Context
    """
    tid = context.vars[f"{team_name}_tid"]
    url = f"/teams_positions/?state=OPEN&tid={tid}"
    context.response = context.client.get(url)

    assert context.response.status_code == 200
    context.vars[f"{team_name}_open_positions"] = context.response.json()


@then('recibo {amount} posicion abierta para el equipo "{team_name}"')
def step_impl(context, amount, team_name):
    """
    :type context: behave.runner.Context
    """
    positions = context.vars[f"{team_name}_open_positions"]
    assert len(positions) == int(amount)
