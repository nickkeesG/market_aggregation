import random
import pandas as pd
import numpy as np
import math

import sys
sys.path.append(".")
sys.path.append("..")

from aggregators import Market

price_lin = Market("price", "linear")
price_log = Market("price", "log")
nash_lin = Market("nash", "linear")
nash_log = Market("nash", "log")

def get_random_prob(p):
    b = math.log(p / (1-p))
    new_b = np.random.normal(b, 1, 1)[0]
    new_p = 2**new_b / (2**new_b + 1)
    return new_p

def election(belief_profile, endowment_profile):
    return sum([int(round(belief_profile[i]))*endowment_profile[i] for i in range(len(belief_profile))])

def trial(n):
    expert = 8/9
    #probability_profile = [(mean_p - expert/(n-1)) for i in range(n)]
    #belief_profile = [random.choices([2/3, 1/3], weights =[p, 1-p])[0] for p in probability_profile]
    #belief_profile[0] = random.choices([0.8, 0.2], weights =[0.8, 0.2])[0]
    belief_profile = [random.uniform(0.2, 0.8) for i in range(n)]
    belief_profile[0] = expert
    endowment_profile = [1/n for i in range(n)]

    p_lin = price_lin.aggregate(belief_profile, endowment_profile)
    p_lin = round(p_lin)
    p_log = price_log.aggregate(belief_profile, endowment_profile)
    p_log = round(p_log)
    n_lin = nash_lin.aggregate(belief_profile, endowment_profile)
    n_lin = round(n_lin)
    n_log = nash_log.aggregate(belief_profile, endowment_profile)
    n_log = round(n_log)

    elec = election(belief_profile, endowment_profile)
    elec = round(elec)

    return [p_lin, p_log, n_lin, n_log, elec]

data = []
for n in range(3, 51, 2):
    results = []
    for i in range(1000):
        r = trial(n)
        results.append(r) 
    p_lin_avg = sum(r[0] for r in results)/len(results)
    p_log_avg = sum(r[1] for r in results)/len(results)
    n_lin_avg = sum(r[2] for r in results)/len(results)
    n_log_avg = sum(r[3] for r in results)/len(results)
    elec_avg = sum(r[4] for r in results)/len(results)
    
    print(n)
    print("%.3f, %.3f, %.3f, %.3f, %.3f" % (p_lin_avg, p_log_avg, n_lin_avg, n_log_avg, elec_avg))
    data.append([p_lin_avg, p_log_avg, n_lin_avg, n_log_avg, elec_avg])

dataf = pd.DataFrame(data, columns=['p_lin', 'p_log', 'n_lin', 'n_log', 'elec'])

import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = parentdir + "/results/expert_1.csv"
dataf.to_csv(path)
