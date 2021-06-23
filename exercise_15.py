# Implementation of a Matrix class.
# The __init__ method takes 1 argument — a string that represents a matrix
# — and converts it to list of lists that represents rows of matrix
# Example: string = """1 2 3\n4 5 6\n7 8 9""" ===> obj.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# __repr__ method is implemented to display matrix in columns and rows
# row and column methods return a row or a column respectively

class Matrix:

    def __init__(self, strMatrix):

        self.matrix = list()

        for matrixRow in strMatrix.split(sep='\n'):
            inner_list = [int(number) for number in matrixRow if number != ' ']
            self.matrix.append(inner_list)

    def __repr__(self):
        return '\n'.join([(' '.join([str(elem) for elem in row])) for row in self.matrix])

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [elem[index] for elem in self.matrix]


m = Matrix("1 2 3\n4 5 6\n7 8 9")
print(m.matrix)
print(m)
print(m.row(2))
print(m.column(0))
