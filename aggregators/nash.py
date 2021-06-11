import random
from .best_response_linear import get_best_response_lin
from .best_response_log import get_best_response_log

EPSILON_1 = 0.000001 #Artificially add this to p_hat & q_hat, as if an extra agent were investing this in both securities
EPSILON_2 = 0.000001 #stop when the difference between current and preferred strategy drops below this
MAX_STEP = 100000   #maximum number of steps before quiting best response
STEP_SIZE = 1/50    #parameter for hill climbing

def init_investment_profile(length):
    investment_profile_a = [0.5 for i in range(length)]                   
    investment_profile_b = [0.5 for i in range(length)]
    
    return investment_profile_a, investment_profile_b

def best_response_dynamics(belief_profile, endowment_profile, policy_profile, utility, hill_climbing, verbose):

    investment_profile_a, investment_profile_b = init_investment_profile(len(belief_profile))

    if utility == "linear":
        get_best_response = get_best_response_lin
    elif utility == "log":
        get_best_response = get_best_response_log
    else:
        return "ERROR, please give a valid utility function"

    if hill_climbing == False:
        STEP_SIZE = 1 

    idx = 0
    continue_best_response = True
    while continue_best_response:
        continue_best_response = False

        if idx > MAX_STEP:
            return "ERROR, best response failed to converge"

        order = [i for i in range(len(belief_profile))]
        random.shuffle(order)
        for i in order:
            p_hat = sum([investment_profile_a[j]*endowment_profile[j] for j in range(len(investment_profile_a)) if not i == j]) 
            q_hat = sum([investment_profile_b[j]*endowment_profile[j] for j in range(len(investment_profile_b)) if not i == j]) 

            #This prevents p_hat or q_hat from ever equaling zero exactly.
            p_hat += EPSILON_1
            q_hat += EPSILON_1

            s_a, s_b = get_best_response(p_hat, q_hat, belief_profile[i], endowment_profile[i], policy_profile[i])
            if not (abs(s_a - investment_profile_a[i]) < EPSILON_2 and abs(s_b - investment_profile_b[i]) < EPSILON_2):
                continue_best_response = True
            
            investment_profile_a[i] += (s_a - investment_profile_a[i])*STEP_SIZE
            investment_profile_b[i] += (s_b - investment_profile_b[i])*STEP_SIZE
           
            if verbose:
                print(i, investment_profile_a[i], investment_profile_b[i])

            idx += 1

    #if best response terminates:
    strats = []
    for i in range(len(belief_profile)):
        strats.append([investment_profile_a[i], investment_profile_b[i]])
    
    p_hat = sum([investment_profile_a[j]*endowment_profile[j] for j in range(len(investment_profile_a))])
    q_hat = sum([investment_profile_b[j]*endowment_profile[j] for j in range(len(investment_profile_b))])

    return p_hat / (p_hat + q_hat), strats
