Feature: CRUD Teams reviews

  Scenario: Create temporal team register
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    When el owner del equipo invita a este equipo temporal
    Then veo que el registro se cargo correctamente

  Scenario: Get review by project
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And el owner del equipo invita a este equipo temporal
    When pido los registros de equipo temporal del proyecto
    Then me trae un registro
