from Actions.Algorythms import Utils
from Actions import PropertyString
from Actions.Algorythms import RelationProperties
from Actions import Closures

boolMatrix = [[0, 0, 0, 0, 1],
              [0, 0, 1, 1, 0],
              [1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0]]
Utils.print_matrix(boolMatrix)
print('\n Task 1')
print(RelationProperties.reflection_antireflection(boolMatrix),
      RelationProperties.symmetric_antisymmetric_asymmetric(boolMatrix),
      RelationProperties.transitive(boolMatrix))
print('\n Task 2')
print(PropertyString.type_of_matrix(boolMatrix))
print('\n Task 3')
Utils.print_matrix(Closures.reflective_closure(boolMatrix))
print('\n')
Utils.print_matrix(Closures.symmetric_closure(boolMatrix))
print('\n')
Utils.print_matrix(Closures.transitive_closure(boolMatrix))
