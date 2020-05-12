(define (domain dompteur)
    (:requirements :strips :negative-preconditions)
    (:predicates 
        (alive)
        (haveTiger)
        (tamedTiger)
        (haveJump)
    )

    (:action getTiger
        :parameters ()
        :precondition (and (alive))
        :effect (and (haveTiger))
    )

    (:action tameTiger
        :parameters ()
        :precondition (and (alive) (haveTiger))
        :effect (and (tamedTiger))
    )
    
    (:action jumpTamedTiger
        :parameters ()
        :precondition (and (alive) (tamedTiger))
        :effect (and (haveJump) )
    )
    
    (:action jumpTiger
        :parameters ()
        :precondition (and (alive) (haveTiger))
        :effect (and (haveJump) (not (alive)))
    )
    
    
)