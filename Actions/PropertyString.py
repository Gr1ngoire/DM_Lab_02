from Actions.Algorythms import RelationProperties


def type_of_matrix(matrix):
    if RelationProperties.reflection_antireflection(matrix) == "Reflective" and (
            RelationProperties.symmetric_antisymmetric_asymmetric(matrix) == "Symmetric") and (
            RelationProperties.transitive(matrix) == "Transitive"):
        return "This relation is an equivalence relation"
    elif RelationProperties.reflection_antireflection(matrix) == "Reflective" and (
            RelationProperties.symmetric_antisymmetric_asymmetric(matrix) == "Antisymmetric") and (
            RelationProperties.transitive(matrix) == "Transitive"):
        return "This relation is a partial order relation"
    elif RelationProperties.reflection_antireflection(matrix) == "Antireflective" and (
            RelationProperties.symmetric_antisymmetric_asymmetric(matrix) == "Asymmetric") and (
            RelationProperties.transitive(matrix) == "Transitive"):
        return "This relation is a total order relation"
    else:
        return "This relation has no special definitions"
