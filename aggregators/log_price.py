def log_aggregate(belief_profile, endowment_profile):

    p = sum([belief_profile[i]*endowment_profile[i] for i in range(len(belief_profile))])
    return p
