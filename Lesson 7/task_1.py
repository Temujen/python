class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(["\t".join([str(i) for i in j]) for j in self.matrix])

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            if len(self.matrix[0]) == len(other.matrix[0]):
                sum_matrix = []
                for i in range(len(self.matrix)):
                    sum_line = []
                    for j in range(len(self.matrix[i])):
                        sum_line.append(self.matrix[i][j] + other.matrix[i][j])
                    sum_matrix.append(sum_line)
                return Matrix(sum_matrix)
            else:
                print("wrong number row, please enter equal matrix")
                return
        else:
            print("Wrong number string, please enter equal matrix")
            return


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[7, 8, 2], [11, 12, 4]])
print(a + b)
