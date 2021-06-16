from .linear_price import lin_aggregate
from .log_price import log_aggregate
from .nash import best_response_dynamics

class Market:
    def __init__(self, equilibrium_type, utility_function):
        self.equilibrium_type = equilibrium_type
        self.utility_function = utility_function

        if equilibrium_type == "price" and utility_function == "linear":
            self.aggregate = lin_aggregate
        if equilibrium_type == "price" and utility_function == "log":
            self.aggregate = log_aggregate
        if equilibrium_type == "nash":
            def nash_aggregate(belief_profile, endowment_profile, policy_profile = None, hill_climbing=False, verbose=False):
                #the default policy profile if none are given
                if policy_profile == None:
                    policy_profile = [1 for b in belief_profile]
                return best_response_dynamics(belief_profile, endowment_profile, policy_profile, self.utility_function, hill_climbing, verbose)
            self.aggregate = nash_aggregate
