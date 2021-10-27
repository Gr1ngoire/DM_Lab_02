from Algorythms import Utils


def get_diagonal_matrix(matrix):
    result_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(1 if i == j else 0)
        result_matrix.append(row)
    return result_matrix


def closure(matrix, special_matrix):
    result_closure = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(1 if matrix[i][j] == 1 or special_matrix[i][j] == 1 else 0)
        result_closure.append(row)


def reflective_closure(matrix):
    return closure(matrix, get_diagonal_matrix(matrix))


def symmetric_closure(matrix):
    return closure(matrix, Utils.transponate_matrix(matrix))


def transitive_closure(matrix):
    return closure(matrix, Utils.compose_matrix(matrix, matrix, len(matrix[0])))
