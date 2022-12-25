from behave import *


@when('invitan al usuario "{name}" al equipo "{team_name}"')
def step_impl(context, name, team_name):
    """
    :param name:str
    :param team_name:str
    :type context: behave.runner.Context
    """
    context.vars[f"{name}_uid"] = "u1"

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    body = {
        "tid": context.vars[f"{team_name}_tid"],
        "team_owner_uid": "u5",
        "postulant_uid": context.vars[f"{name}_uid"],
    }
    url = "/team_invitations/"

    context.response = context.client.post(url, json=body, headers=headers)


@then('veo que se crea la invitacion de "{name}" al equipo "lambda team"')
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@given('invitaron al usuario "{name}" al equipo "{team_name}"')
def step_impl(context, name, team_name):
    """
    :param name:str
    :param team_name:str
    :type context: behave.runner.Context
    """
    context.vars[f"{name}_uid"] = "u1"

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    body = {
        "tid": context.vars[f"{team_name}_tid"],
        "team_owner_uid": "u5",
        "postulant_uid": context.vars[f"{name}_uid"],
    }
    url = "/team_invitations/"

    context.response = context.client.post(url, json=body, headers=headers)

    assert context.response.status_code == 201
    context.vars["tiid"] = context.response.json()["tiid"]


@when('pido las invitaciones del usuario "{name}"')
def step_impl(context, name):
    """
    :param name:str
    :type context: behave.runner.Context
    """
    postulant_uid = context.vars[f"{name}_uid"]
    url = f"/team_invitations/?postulant_uid={postulant_uid}"

    context.response = context.client.get(url)

    assert context.response.status_code == 200


@then("veo que tiene {amount} invitaciones a equipo")
def step_impl(context, amount):
    """
    :param amount:int
    :type context: behave.runner.Context
    """
    invitations = context.response.json()
    assert len(invitations) == int(amount)


@when('cuando el usuario "{name}" "{action}" la invitacion')
def step_impl(context, name, action):
    """
    :param action: str
    :param name: str
    :type context: behave.runner.Context
    """
    actions = {"acepta": "ACCEPTED", "rechaza": "REJECTED"}
    tiid = context.vars["tiid"]
    url = f"/team_invitations/{tiid}"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    body = {"state": actions[action]}
    context.response = context.client.put(url, headers=headers, json=body)

    assert context.response.status_code == 200


@then('la invitacion se marca como "{state}"')
def step_impl(context, state):
    """
    :param state:str
    :type context: behave.runner.Context
    """
    states = {"aceptada": "ACCEPTED", "rechazada": "REJECTED"}

    assert context.response.json()["state"] == states[state]


@when('pido las invitaciones del enviadas del equipo "{team_name}"')
def step_impl(context, team_name):
    """
    :param team_name: str
    :type context: behave.runner.Context
    """
    tid = context.vars[f"{team_name}_tid"]
    url = f"/team_invitations/?tid={tid}"

    context.response = context.client.get(url)

    assert context.response.status_code == 200


@then("veo que tiene {amount} invitaciones a equipo enviadas")
def step_impl(context, amount):
    """
    :param amount: int
    :type context: behave.runner.Context
    """
    invitations = context.response.json()
    assert len(invitations) == int(amount)
