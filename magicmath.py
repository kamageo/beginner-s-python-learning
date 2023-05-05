class SuperInt:
    def __init__(self, n):
        self.n = n

    def __add__(self, m):
        print("Производится сложение")
        return self.n + m

    def __sub__(self, m):
        print("Производится вычитание")
        return self.n - m

    def __mul__(self, m):
        print("Производится умножение")
        return self.n * m

    def __truediv__(self, m):
        print("Производится деление")
        return self.n / m


SuperInt(10) + 3
SuperInt(10) - 3
SuperInt(10) * 3
SuperInt(10) / 3