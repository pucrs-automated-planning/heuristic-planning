from pddl.pddl_parser import PDDL_Parser
from pddl.state import applicable

class PDDL_Planner:

    #-----------------------------------------------
    # Initialize
    #-----------------------------------------------

    def __init__(self):
        self.parser = PDDL_Parser()

    #-----------------------------------------------
    # Solve
    #-----------------------------------------------

    def solve_file(self, domainfile, problemfile, verbose=True):
        # Parser
        import time
        start_time = time.time()
        parser = PDDL_Parser()
        parser.parse_domain(domainfile)
        parser.parse_problem(problemfile)
        # Test if first state is not the goal
        if applicable(parser.state, parser.positive_goals, parser.negative_goals):
            return [], 0
        # Grounding process
        ground_actions = []
        for action in parser.actions:
            for act in action.groundify(parser.objects):
                ground_actions.append(act)
        plan = self.solve(ground_actions, parser.state, parser.positive_goals, parser.negative_goals)
        final_time = time.time() - start_time
        if verbose:
            print('Time: ' + str(final_time) + 's')
            if plan:
                print('plan:')
                for act in plan:
                    print('(' + act.name + ''.join(' ' + p for p in act.parameters) + ')')
            else:
                print('No plan was found')
        return plan, final_time

    def solve(self, domain, initial_state, positive_goals, negative_goals):
        raise NotImplementedError("PDDL Planners need to implement solve")