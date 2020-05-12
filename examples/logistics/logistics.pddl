;Header and description

(define (domain logistics)

;remove requirements that are not needed
(:requirements :strips :negative-preconditions)

; (:types ;todo: enumerate types and their hierarchy here, e.g. car truck bus - vehicle
; )

; un-comment following line if constants are needed
(:constants truck)

(:predicates ;todo: define predicates here
    (truckpos ?pos)
    (package ?pos)
    (connected ?pos1 ?pos2)
)


;define actions here

(:action drive
    :parameters (?from ?to)
    :precondition (and (truckpos ?from) (connected ?from ?to))
    :effect (and (not (truckpos ?from)) (truckpos ?to))
)

(:action load
    :parameters (?pos)
    :precondition (and (truckpos ?pos) (package ?pos))
    :effect (and (not (package ?pos)) (package truck) )
)

(:action unload
    :parameters (?pos)
    :precondition (and (package truck) (truckpos ?pos))
    :effect (and (not (package truck)) (package ?pos) )
)



)