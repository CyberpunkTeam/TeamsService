Feature: CRUD Team members reviews

  Scenario: Create team member review
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And el miembro "Gonzalo Marino" participo en el proyecto "Find my project"
    And el miembro "Matias Fonseca" participo en el proyecto "Find my project"
    And finalizo el proyecto "Find my project"
    When el miembro "Gonzalo Marino" califica la participacion de "Matias Fonseca" con 5 estrellas
    And el miembro "Matias Fonseca" califica la participacion de "Gonzalo Marino" con 4 estrellas
    Then si pido las review del miembro "Matias Fonseca" veo que la calificacion es de 5 estrellas
    And si pido las review del miembro "Gonzalo Marino" veo que la calificacion es de 4 estrellas
