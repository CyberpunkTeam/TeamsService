Feature: CRUD Team invitations

  Scenario: Crear invitacion a equipo
    Given ya existe un equipo con nombre "lambda team"
    When invitan al usuario "Gonzalo Marino" al equipo "lambda team"
    Then veo que se crea la invitacion de "Gonzalo Marino" al equipo "lambda team"

  Scenario: Obtener invitaciones a equipo de un usuario
    Given ya existe un equipo con nombre "lambda team"
    And ya existe un equipo con nombre "beta team"
    And invitaron al usuario "Gonzalo Marino" al equipo "lambda team"
    And invitaron al usuario "Gonzalo Marino" al equipo "beta team"
    When pido las invitaciones del usuario "Gonzalo Marino"
    Then veo que tiene 2 invitaciones a equipo

  Scenario: Aceptar invitacion a equipo
    Given ya existe un equipo con nombre "lambda team"
    And invitaron al usuario "Gonzalo Marino" al equipo "lambda team"
    When cuando el usuario "Gonzalo Marino" "acepta" la invitacion
    Then la invitacion se marca como "aceptada"

  Scenario: Rechazar invitacion a equipo
    Given ya existe un equipo con nombre "lambda team"
    And invitaron al usuario "Gonzalo Marino" al equipo "lambda team"
    When cuando el usuario "Gonzalo Marino" "rechaza" la invitacion
    Then la invitacion se marca como "rechazada"

  Scenario: Obtener invitaciones a equipo de un equipo
    Given ya existe un equipo con nombre "lambda team"
    And invitaron al usuario "Gonzalo Marino" al equipo "lambda team"
    And invitaron al usuario "Matias Fonseca" al equipo "lambda team"
    When pido las invitaciones del enviadas del equipo "lambda team"
    Then veo que tiene 2 invitaciones a equipo enviadas
