Feature: CRUD position

  Scenario: Create position
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    When creo un position para el equipo "DevArmy"
    Then se me informa que se creo correctamente

  Scenario: List open positions
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    Given ya existe un equipo con nombre "Alfa", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    When existe un position para el equipo "DevArmy"
    And existe un position para el equipo "Alfa"
    Then existen 2 posiciones abiertas

  Scenario: List open positions
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    Given ya existe un equipo con nombre "Alfa", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And existe un position para el equipo "DevArmy"
    And existe un position para el equipo "Alfa"
    And la posicion del equipo "Alfa" se cierra
    When pido las posiciones abiertas
    Then recibo 1 posicion abierta

  Scenario: List open positions by team
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    Given ya existe un equipo con nombre "Alfa", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And existe un position para el equipo "DevArmy"
    And existe un position para el equipo "Alfa"
    And la posicion del equipo "Alfa" se cierra
    When pido las posiciones abiertas para el team "Alfa"
    And pido las posiciones abiertas para el team "DevArmy"
    Then recibo 0 posicion abierta para el equipo "Alfa"
    And  recibo 1 posicion abierta para el equipo "DevArmy"

  Scenario: Add candidate to position
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And existe un position para el equipo "DevArmy"
    When cuando agrego al candidato "Matias Fonseca" al puesto del equipo "DevArmy"
    Then cuando pido los candidatos, encuentro 1 candidato/s

  Scenario: Remove candidate to position
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And existe un position para el equipo "DevArmy"
    And "Matias Fonseca" es candidato al puesto del equipo "DevArmy"
    When cuando elimino "Matias Fonseca" del puesto del equipo "DevArmy"
    Then cuando pido los candidatos, encuentro 0 candidato/s

  Scenario: Filter team positions
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And ya existe un equipo con nombre "Alfa", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And existe una posicion para el equipo "DevArmy" con requerimientos de lenguajes "Python,Java", frameworks "Django"
    And existe una posicion para el equipo "Alfa" con requerimientos de lenguajes "Ruby", frameworks "Ruby on rails"
    When posiciones de lenguaje "Python"
    Then devuelve 1 posicion abierta
