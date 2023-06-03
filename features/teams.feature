Feature: CRUD Team


  Scenario: Creacion de equipo
    Given que quiero crear un equipo

    When completo el formulario de alta de equipo con nombre "DevArmy" , tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".

    And confirmo el alta de equipo

    Then se me informa que el equipo se creo con exito

  Scenario: Creacion invalida por campo nombre faltante
    Given que quiero crear un equipo

    When completo el formulario de alta de equipo y no completo el "nombre"

    And confirmo el alta de equipo

    Then se me informa el campo "nombre" es obligatorio


  Scenario: Creacion de equipo con nombre ya existente
    Given que quiero crear un equipo

    And ya existe un equipo con nombre "DevArmy"

    When completo el formulario de alta de equipo con nombre "DevArmy" , tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".

    And confirmo el alta de equipo

    Then se me informa que ya existe un equipo con ese nombre

  Scenario: Agregar miembro a equipo
    Given que quiero agregar a un miembro a un equipo

    And ya existe un equipo con nombre "DevArmy"

    When agrego a un miembro a el equipo con nombre "DevArmy"

    Then se me informa que se agrego correctamente

    And el equipo tiene un miembro mas

  Scenario: Actualizar equipo
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".

    When cuando actualizo el equipo a nombre "DevArmy 2", tecnologias "Java" y preferencia de proyectos de tipo "Web".

    Then se me informa que se actualizo correctamente

    And puedo ver que el equipo se actualizo a nombre "DevArmy 2", tecnologias "Java" y preferencia de proyectos de tipo "Web".


  Scenario: Buscar equipo por creador
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And ya existe un equipo con nombre "DevArmy 2", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And ya existe un equipo con nombre "Gonzalitos", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    And soy dueño de estos equipos
    When busco mis equipos

    Then me retorna al equipo con nombre "DevArmy"
    And me retorna al equipo con nombre "DevArmy 2"
    And me retorna al equipo con nombre "Gonzalitos"


  Scenario: Buscar equipo por creador
    Given ya existe un equipo con nombre "DevArmy", tecnologias "Python, Django, React" y preferencia de proyectos de tipo "Web, AI, Crypto".
    When pido las metricas
    Then me retorna que se creo un equipo
