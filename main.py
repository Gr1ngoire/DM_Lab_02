from Actions.Algorythms import Utils
from Actions import PropertyString
from Actions.Algorythms import RelationProperties
boolMatrix = [[0, 0, 0, 0, 1],
              [0, 0, 1, 1, 0],
              [1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0]]
Utils.print_matrix(boolMatrix)
print('\n')
print(RelationProperties.reflection_antireflection(boolMatrix), RelationProperties.symmetric_antisymmetric_asymmetric(boolMatrix), RelationProperties.transitive(boolMatrix))
print('\n')
print(PropertyString.type_of_matrix(boolMatrix))