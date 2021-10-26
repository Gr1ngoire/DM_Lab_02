def print_matrix(matrix_to_print):
    for el in matrix_to_print:
        output = ""
        for elEl in el:
            output += '{}\t'.format(elEl)
        print(output)


def compose_matrix(matrix_a, matrix_b, power, calls=1):
    result_arr = []
    for j in range(len(matrix_a)):
        row = []
        for i in range(len(matrix_a[j])):
            element = 0
            for o in range(len(matrix_b[0])):
                element += matrix_a[j][o] * matrix_b[o][i]
            row.append(0 if element == 0 else 1)
        result_arr.append(row)
    calls += 1
    if calls >= power:
        return result_arr
    else:
        return compose_matrix(result_arr, matrix_a, power, calls)
