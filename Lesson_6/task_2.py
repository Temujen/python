class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        print(f"{self._length}м * {self._width}м * 25кг * 5см = {round(self._length * self._width * 25 * 5 / 1000)}т")


a = Road(20, 5000)
a.mass()
b = Road(30, 100)
b.mass()
