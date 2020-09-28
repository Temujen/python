class Cell:
    def __init__(self, cell):
        self.cell = int(abs(cell))

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        result = self.cell - other.cell
        if result > 0:
            return result
        else:
            return other.cell - self.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        result = self.cell // other.cell
        if result > 1:
            return result
        else:
            return other.cell // self.cell

    def make_order(self, rows):
        part_1 = self.cell // rows
        part_2 = self.cell % rows
        result = "\n".join(['*' * rows for i in range(part_1)])
        result += "\n" + ("*" * part_2)
        return result


cell_1 = Cell(20)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(4))
