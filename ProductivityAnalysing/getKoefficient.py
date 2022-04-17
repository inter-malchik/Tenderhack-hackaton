from math import exp


def find_koefficient(cur_rate, delta_rate, delta_time,  min_total_rate, delta_min_total_rate):

    # нормировка скорости убывания
    v_total_min_rate = ((delta_min_total_rate * 100) / min_total_rate) / delta_time
    v_cur_rate = ((delta_rate * 100) / cur_rate) / delta_time
    v_norm = 1 - exp(1 - v_cur_rate / v_total_min_rate)

    # нормировка цены
    cost_norm = 1 - exp(1 - cur_rate / min_total_rate)

    # коэффициент выгоды цчастия в тендере(рентабельности)
    k = f(v_norm, cost_norm)

    return round(k, 5)


# целевая функция
def f(v_, cur_rate_):
    return cur_rate_ * (1 - v_)

