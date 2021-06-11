import math

def get_best_response_log(p_hat, q_hat, belief, endowment, policy):
    #The math below assumes that the agent initially prefers alpha securities. If that is not the case, the math is very similar, but it's just easier to exploit the symmetry of the securities and solve assuming it prefers alpha securities
    initial_price = p_hat / (p_hat + q_hat)
    if not belief >= initial_price:
        s_b, s_a = get_best_response(q_hat, p_hat, (1-belief), endowment, policy)
        return s_a, s_b

    C = p_hat * q_hat / (2*endowment)
    Q = (belief*p_hat - p_hat -C + math.sqrt(C*(C + 2*(p_hat + q_hat + endowment)*belief*(1-belief)))) / ((1-belief)*(q_hat + endowment))
    p = (p_hat + Q*endowment) / (p_hat + q_hat + Q*endowment)

    s_a = Q + (1-Q)*p*policy
    s_b = (1-Q)*(1-p)*policy

    return s_a, s_b    
