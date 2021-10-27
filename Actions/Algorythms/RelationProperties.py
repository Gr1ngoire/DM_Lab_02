from Actions.Algorythms import Utils


def reflection_antireflection(matrix):
    reflection_marker = True
    antireflection_marker = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j and matrix[i][j] == 0:
                reflection_marker = False
            if i == j and matrix[i][j] == 1:
                antireflection_marker = False
    if reflection_marker:
        result = "Reflective"
    elif antireflection_marker:
        result = "Antireflective"
    else:
        result = "Neither reflective, nor antireflective"
    return result


def symmetric_antisymmetric_asymmetric(matrix):
    if Utils.equal(matrix, Utils.transponate_matrix(matrix)):
        return "Symmetric"
    elif (reflection_antireflection(matrix) == "Antireflective") and (
            not Utils.equal(matrix, Utils.transponate_matrix(matrix))):
        return "Asymmetric"
    elif not Utils.equal(matrix, Utils.transponate_matrix(matrix)):
        return "Antisymmetric"
    else:
        return "Neither symmetric, nor asymmetric, nor Antisymmetric"


def transitive(matrix):
    if Utils.equal(Utils.compose_matrix(matrix, matrix, 2), matrix):
        return "Transitive"
    else:
        return "Not transitive"
