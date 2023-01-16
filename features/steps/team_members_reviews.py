from behave import *


@step('el miembro "{name}" participo en el proyecto "Find my project"')
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    """
    context.vars[f"{name}_uid"] = str(len(name)) + name[0]


@step('finalizo el proyecto "{project_name}"')
def step_impl(context, project_name):
    """
    :type context: behave.runner.Context
    """
    context.vars["pid"] = str(len(project_name))


@when(
    'el miembro "{reviewer_name}" califica la participacion de "{member_name}" con {rating} estrellas'
)
def step_impl(context, reviewer_name, member_name, rating):
    """
    :type context: behave.runner.Context
    """
    pid = context.vars["pid"]
    tid = context.vars["tid"]
    member_reviewer = context.vars[f"{reviewer_name}_uid"]
    member_reviewed = context.vars[f"{member_name}_uid"]
    body = {
        "pid": pid,
        "tid": tid,
        "rating": rating,
        "member_reviewer": member_reviewer,
        "member_reviewed": member_reviewed,
    }

    url = "/team_members_reviews"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    context.response = context.client.post(url, json=body, headers=headers)
    assert context.response.status_code == 201


@then(
    'si pido las review del miembro "{name}" veo que la calificacion es de {rating} estrellas'
)
def step_impl(context, name, rating):
    """
    :type context: behave.runner.Context
    """
    uid = context.vars[f"{name}_uid"]
    url = f"/team_members_reviews/?member_reviewed={uid}"
    response = context.client.get(url)
    assert response.status_code == 200
    review = response.json()
    assert len(review) == 1
    assert review[0].get("rating") == int(rating)
