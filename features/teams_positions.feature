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