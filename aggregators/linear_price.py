def lin_aggregate(belief_profile, endowment_profile):
    #indices ordered from highest belief to lowest belief
    order = sorted(range(len(belief_profile)), key = lambda k: belief_profile[k])
    order.reverse()
    
    p = 0
    for i in order:
        if belief_profile[i] <= p:
            return p
        p += endowment_profile[i]
        if belief_profile[i] <= p:
            return belief_profile[i]
    return "ERROR, either endowments don't sum to one, or an agent has a belief greater than one."
