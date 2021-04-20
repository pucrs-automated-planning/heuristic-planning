from pddl.benchmark import PlanningBenchmark, InstanceStats


class Heuristic:

    def __init__(self, is_safe=False, is_goal_aware=True, is_consistent=False, stats=None):
        self.stats = stats
        # Ensure that you document heuristics properties correctly
        self.is_safe = is_safe
        self.is_goal_aware = is_goal_aware
        self.is_consistent = is_consistent

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