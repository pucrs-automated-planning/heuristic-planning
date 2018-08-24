class Heuristic:
    def __call__(self, actions, initial_state, positive_g, negative_g):
        self.h(actions,initial_state, positive_g, negative_g)

    def h(self, domain, initial_state, positive_goals, negative_goals):
        raise NotImplementedError("Unimplemented")