from behave import *

use_step_matcher("re")


@step("el owner del equipo invita a este equipo temporal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pid = "mock_pid"
    tid = context.vars["tid"]
    context.vars["pid"] = pid
    body = {"pid": pid, "tid": tid}
    url = "/temporal_teams_registers"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    context.response = context.client.post(url, json=body, headers=headers)


@then("veo que el registro se cargo correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@when("pido los registros de equipo temporal del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = f"/temporal_teams_registers/?pid={context.vars['pid']}"
    context.response = context.client.get(url)


@then("me trae un registro")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    json = context.response.json()
    assert len(json) > 0
