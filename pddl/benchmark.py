import matplotlib.pyplot as plt


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class InstanceStats:

    def __init__(self, domain_name="problem.pddl", problem_name="pb.pddl"):
        self.domain_name = domain_name
        self.problem_name = problem_name
        self.nodes = 0
        self.h_calls = 0
        self.action_space = 0
        self.time = 0

    def __str__(self):
        return '%s, %s, %d, %d, %d, %f s'%(self.domain_name,self.problem_name, self.nodes, self.h_calls, self.action_space, self.time)

    def __repr__(self):
        return str(self)


class PlanningBenchmark(metaclass=Singleton):

    def __init__(self):
        self.stat_instances = {}

    def reset_stats(self):
        self.stat_instances = {}

    def get_instance(self, domain_name, problem_name):
        if domain_name not in self.stat_instances.keys():
            self.stat_instances[domain_name] = {}
        domain = self.stat_instances[domain_name]

        if problem_name not in domain:
            domain[problem_name] = InstanceStats(domain_name, problem_name)
        return domain[problem_name]

    def get_stats(self, domain_name, stat='time', xaxis='action', approach=None):
        if stat == 'time':
            y = [instance.time for k, instance in self.stat_instances[domain_name].items()]
        elif stat == 'nodes':
            y = [instance.nodes for k, instance in self.stat_instances[domain_name].items()]
        elif stat == 'h_calls':
            y = [instance.h_calls for k, instance in self.stat_instances[domain_name].items()]

        if xaxis == 'action':
            x = [instance.action_space for k, instance in self.stat_instances[domain_name].items()]
        elif xaxis == 'problem':
            x = [instance.problem_name[instance.problem_name.rfind('/')+1:] for k, instance in self.stat_instances[domain_name].items()]

        return x,y

    def plot_stat(self, domain_name, stat='time', xaxis='action', label='', approach=None):
        if label == '':
            label = '%s: %s by %s (%s)'%(xaxis,stat,domain_name,approach)

        if stat == 'time':
            y = [instance.time for k, instance in self.stat_instances[domain_name].items()]
        elif stat == 'nodes':
            y = [instance.node for k, instance in self.stat_instances[domain_name].items()]
        elif stat == 'h_calls':
            y = [instance.problem_name[instance.problem_name.rfind('/')+1:] for k, instance in self.stat_instances[domain_name].items()]
        plt.figure()

        if xaxis == 'action':
            # for instance in self.stat_instances[domain_name]:
            #     print(instance)
            x = [instance.action_space for k, instance in self.stat_instances[domain_name].items()]
            plt.plot(x, y, label=label)
            # plt.plot(x, y, xlabel='\# Actions', ylabel='Time (s)', label='Actions vs Time')
        elif xaxis == 'problem':
            x = [instance.problem_name for k, instance in self.stat_instances[domain_name].items()]
            # plt.bar(x,y, xlabel='Problem', ylabel='Time (s)', label='Problems vs Time')
            plt.bar(x, y, label=label)
        # plt.show(block=False)
        plt.show()

