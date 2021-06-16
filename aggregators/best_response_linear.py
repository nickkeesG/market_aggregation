import math

def get_best_response_lin(p_hat, q_hat, belief, endowment, policy):
    #The math below assumes that the agent initially prefers alpha securities. If that is not the case, the math is very similar, but it's just easier to exploit the symmetry of the securities and solve assuming it prefers alpha securities
    initial_price = p_hat / (p_hat + q_hat)
    if not belief >= initial_price:
        s_b, s_a = get_best_response_lin(q_hat, p_hat, (1-belief), endowment, policy)
        return s_a, s_b

    Z = math.sqrt((belief/(1-belief)) * (p_hat / q_hat))
    p = Z / (Z + 1)
    s_min = (Z*q_hat - p_hat)/endowment

    s_a = s_min + (1-s_min)*p*policy
    s_b = (1-s_min)*(1-p)*policy

    s_a = max(0,s_a)
    s_b = max(0,s_b)
    s_a = min(1,s_a)
    s_b = min(1,s_b)

    return s_a, s_b    
