(define (problem pb2) (:domain logistics)
(:objects A B C D
)

(:init
    (connected A B)
    (connected B A)
    (connected B C)
    (connected C B)
    (connected C D)
    (connected D C)
    (package C)
    (truckpos A)
)

(:goal (and
    (truckpos D)
    (package D)
))

)
