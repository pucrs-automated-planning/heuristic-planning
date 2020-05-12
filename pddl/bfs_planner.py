#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from pddl.pddl_parser import PDDLParser
from pddl.pddl_planner import PDDLPlanner
from pddl.state import applicable, apply


class BFS_Planner(PDDLPlanner):

    def __init__(self, verbose=False):
        super().__init__(verbose)

    #-----------------------------------------------
    # Solve
    #-----------------------------------------------

    def solve(self, domain, initial_state, goals):
        (positive_goals, negative_goals) = goals
        # Search
        visited = set([initial_state])
        fringe = [initial_state, None]
        while fringe:
            initial_state = fringe.pop(0)
            plan = fringe.pop(0)
            for act in domain:
                if applicable(initial_state, act.positive_preconditions, act.negative_preconditions):
                    new_initial_state = apply(initial_state, act.add_effects, act.del_effects)
                    if new_initial_state not in visited:
                        if applicable(new_initial_state, positive_goals, negative_goals):
                            full_plan = [act]
                            while plan:
                                act, plan = plan
                                full_plan.insert(0, act)
                            if self.stats: self.stats.nodes = len(visited)
                            return full_plan
                        visited.add(new_initial_state)
                        fringe.append(new_initial_state)
                        fringe.append((act, plan))
        if self.stats: self.stats.nodes = len(visited)
        return None

# ==========================================
# Main
# ==========================================


if __name__ == '__main__':
    import sys
    domain = sys.argv[1]
    problem = sys.argv[2]
    planner = BFS_Planner()
    plan, time = planner.solve_file(domain, problem)