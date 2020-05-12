(define (problem pb2)
  (:domain tsp)
  (:objects Sydney Adelaide Brisbane Perth Darwin - position)
  (:init
    ; Directed graph
    (connected Sydney Brisbane)
    (connected Brisbane Sydney)
    (connected Sydney Adelaide)
    (connected Adelaide Sydney)
    (connected Adelaide Perth)
    (connected Perth Adelaide)
    (connected Adelaide Darwin)
    (connected Darwin Adelaide)
    ; Start
    (at Sydney)
  )

  (:goal (and
    (at Sydney)
    (visited Sydney)
    (visited Adelaide)
    (visited Brisbane)
    (visited Perth)
    (visited Darwin)
  ))
)