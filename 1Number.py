class Matrix():
    def __init__(self, x):
        self.matrix = (x)

    def __add__(self, other, result):
        other = m(other)
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result
    def __str__(self):
        return self.result


matrix_1 = Matrix ( [[1,2],[3,4]])
matrix_2 = Matrix ( [[3,4],[1,5]])
m = Matrix
print(m)
