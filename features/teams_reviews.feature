Feature: CRUD Teams reviews

  Scenario: Create review
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    When el proyecto finaliza su owner escribe la review del equipo
    Then veo que la review se cargo correctamente

  Scenario: Get review by project
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And el owner del equipo ya escribio la review
    When pido la review del equipo
    Then me trae la review
