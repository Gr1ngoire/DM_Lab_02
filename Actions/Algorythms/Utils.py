def print_matrix(matrix_to_print):
    for el in matrix_to_print:
        output = ""
        for el_el in el:
            output += '{}\t'.format(el_el)
        print(output)


def equal(matrix_a, matrix_b):
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False
    return True


def compose_matrix(matrix_a, matrix_b, power, calls=1):
    result_arr = []
    for j in range(len(matrix_a)):
        row = []
        for i in range(len(matrix_b[j])):
            element = 0
            for o in range(len(matrix_b)):
                element += matrix_a[j][o] * matrix_b[o][i]
            row.append(0 if element == 0 else 1)
        result_arr.append(row)
    calls += 1
    if calls >= power:
        return result_arr
    else:
        return compose_matrix(result_arr, matrix_a, power, calls)


def transponate_matrix(matrix):
    result_matrix = []
    for i in range(len(matrix)):
        to_push = []
        for j in range(len(matrix[i])):
            to_push.append(matrix[j][i])
        result_matrix.append(to_push)
    return result_matrix


def invert_matrix(matrix):
    result_matrix = []
    for row in matrix:
        row_to_insert = []
        for j in row:
            row_to_insert.append(1 if j == 0 else 0)
        result_matrix.append(row_to_insert)
    return result_matrix


def has_symmetry(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 0 and matrix[j][i] == 1) or (matrix[i][j] == 1 and matrix[j][i] == 0):
                return False
    return True
