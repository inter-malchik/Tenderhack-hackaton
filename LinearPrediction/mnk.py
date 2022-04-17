import datetime


class Stats:
    def __init__(self, dt, step, percent, initvalue):
        self.dt = dt
        self.step = step
        self.data = [0] * step
        self.values = [0] * self.step
        self.current = 0
        self.percent = percent
        self.initial = datetime.datetime.now().replace(microsecond=0)
        self.initvalue = initvalue
        self.approximation_func = None

    def add_bet(self):
        current_time = datetime.datetime.now().replace(microsecond=0)
        print(current_time, self.current)
        self.current = ((current_time - self.initial).seconds // self.dt)
        if self.current > self.step:
            self.current %= self.step
            for i in range(self.current + 1):
                self.initvalue *= (1 - self.percent) ** self.data[self.current]
                self.data[i] = 0
            self.data[self.current] = 1
        else:
            self.data[self.current] += 1

    def approximate(self):
        self.values[0] = round(self.initvalue * (1 - self.percent) ** self.data[0], 2)
        for i in range(1, len(self.values)):
            self.values[i] = round(self.values[i - 1] * (1 - self.percent) ** self.data[i], 2)

        m_x, m_y = sum(range(len(self.values))) / len(self.values), sum(self.values) / len(self.values)
        b = (sum((xi - m_x) * (yi - m_y) for xi, yi in enumerate(self.values)) / (
            sum((xi - m_x) ** 2 for xi in range(len(self.values)))))
        a = m_y - b * m_x
        self.approximation_func = lambda x: a + b * x
        return

    def get_predict(self, step_forward=0):
        if not self.approximation_func:
            self.approximate()
        return round(self.approximation_func(self.step + step_forward), 2)

    def get_approximation(self, step_forward=0):
        if not self.approximation_func:
            self.approximate()
        dp = self.approximation_func(self.step + step_forward) - self.approximation_func(self.step + step_forward - 1)
        return round(dp, 2)
