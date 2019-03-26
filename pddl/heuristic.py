class Heuristic:
    def __call__(self, actions, initial_state, goals):
        self.h(actions,initial_state, goals)

    def h(self, domain, initial_state, goals):
        raise NotImplementedError("Unimplemented")
