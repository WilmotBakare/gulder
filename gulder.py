import fileinput, sys
#import numpy
from collections import Counter

with open('.input', 'r') as f:

 class Chest:
    pass

 max_key = 200
 T = int(f.readline())
 #T_list = list(T)

 def solve(chests, keys):
    keys = T.copy(keys)
    keys_across_universe = keys + sum(chest.inside for chest in chests)
    required = Counter(chest.lock for chest in chests)
    required = numpy.array([required[key] for key in range(max_key+1)])
    if any(required > keys_across_universe):
        return False



 for case in range(1,T+1):
    K, N = [int(x) for x in f.readline().split()]
    initial_keys = [int(x) for x in f.readline().split()]
    assert len(initial_keys) == K
    initial_keys = Counter(initial_keys)

    initial_keys = f([initial_keys[key] for key in range(max_key+1)])

    chests = list()

    for i in range(N):
        numbers = [int(x) for x in f.readline().split()]
        Ti = numbers[0]
        Ki = numbers[1]
        inside = numbers[2:]
        assert len(inside) == Ki
        inside = Counter(inside)
        inside = f([inside[key] for key in range(max_key+1)])
        assert inside[0] == 0

        chest = Chest()
        chest.lock = Ti
        chest.inside = inside
        chests.append(chest)

    solution = solve(chests, initial_keys)
    if solution:
        answer = " ".join(str(n+1) for n in solution)
    else:
        answer = "IMPOSSIBLE"

    print "Case #%d: %s" % (case, answer)
