from itertools import combinations

arr = [(1,1),(2,2),(3,3),(4,4),(5,5)]
for a,b in combinations(arr, 2):
    print(a, b)