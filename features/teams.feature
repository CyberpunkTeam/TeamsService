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

    Scenario: Creacion invalida por campo preferencias de proyecto faltante
    Given que quiero crear un equipo

    When completo el formulario de alta de equipo y no completo el "preferencias de proyecto"

    And confirmo el alta de equipo

    Then se me informa el campo "preferencias de proyecto" es obligatorio
