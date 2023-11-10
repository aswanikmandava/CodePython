# While dict.copy() and dict(dict1) generates a copy, they are only shallow copies. 
# If you want a deep copy, copy.deepcopy(dict1) is required.

import copy

source = {'a': 1, 'b': {'m': 4, 'n': 5, 'o': 6}, 'c': 3}
copy1 = source.copy()
copy2 = dict(source)
copy3 = copy.deepcopy(source)
source['a'] = 10  # a change to first-level properties won't affect copies
print(f"TEST_1: source: {source}, copy1: {copy1}, copy2: {copy2}, copy3: {copy3}")
source['b']['m'] = 40  # a change to deep properties WILL affect shallow copies 'b.m' property
# Deep copy's 'b.m' property is unaffected

print(f"TEST_2: source: {source}, copy1: {copy1}, copy2: {copy2}, copy3: {copy3}")