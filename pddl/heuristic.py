from pddl.benchmark import PlanningBenchmark, InstanceStats


class Heuristic:

    def __init__(self, stats=None):
        self.stats = stats

    def __call__(self, actions, initial_state, goals):
        if self.stats: self.stats.h_calls += 1
        return self.h(actions, initial_state, goals)

    def h(self, domain, initial_state, goals):
        """
        :param domain:
        :param initial_state:
        :param goals:
        :return:
        :rtype float
        """
        raise NotImplementedError("Unimplemented")