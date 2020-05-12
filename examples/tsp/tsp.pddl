(define (domain tsp)
  (:requirements :strips :negative-preconditions :typing)
  (:types 
    position - object
  )
  (:predicates
    (at ?pos)
    (connected ?start ?finish)
    (visited ?finish)
  )

  (:action move
    :parameters (?start - position ?finish - position)
    :precondition (and
      (at ?start)
      (connected ?start ?finish)
      ; (not (visited ?finish)) ; This makes some problems unsolvable
    )
    :effect (and
      (at ?finish)
      (visited ?finish)
      (not (at ?start))
    )
  )
)