import math


def check_min_rate(cur_rate, min_rate, delta_rate):
    return  cur_rate + delta_rate < min_rate or math.isclose(cur_rate + delta_rate, min_rate)

