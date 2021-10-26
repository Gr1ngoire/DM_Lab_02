from Utils import Utils

boolMatrix = [[0, 0, 0, 0, 1],
              [0, 0, 1, 1, 0],
              [1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0]]
Utils.print_matrix(boolMatrix)
print('\n')
Utils.print_matrix(Utils.compose_matrix(boolMatrix, boolMatrix, 3))
