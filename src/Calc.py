import math
def calc_probability(x,count):
    # 切り捨て桁
    if x <= 0:
        return 100.0

    n = 10
    prob = math.floor((100 - 100 * pow(x,count)) * 10**n) / (10**n)
    return prob
