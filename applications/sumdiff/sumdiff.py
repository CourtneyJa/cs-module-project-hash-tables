"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
#q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
cache = {}
add2cache = {}
minus_cache = {}
answers = {}

for i in q:
    if i not in cache:
        cache[i] = f(i)
cachedList = sorted(cache.items())
for f in range(len(cachedList)):
    add2cache[(cachedList[f][0], cachedList[f][0])] = cachedList[f][1] + cachedList[f][1]
    for s in range(len(cachedList)):
        add2cache[(cachedList[f][0], cachedList[s][0])] = cachedList[f][1] + cachedList[s][1]
    if f != s and s < len(cachedList):
        minus_cache[(cachedList[s][0], cachedList[f][0])] = cachedList[s][1] + cachedList[f][1]
for value in add2cache.items():
    if value[1] in minus_cache.values():
        keys = list(minus_cache.keys())[list(minus_cache.values()).index(value[1])]
        for key in range(1, len(keys)):
            answers[(value[0], value[1])] = ((keys[key - 1], keys[key]), minus_cache[(keys[key - 1], keys[key])])

listResults = sorted(answers.items()) 

for r in listResults:
    a = r[0][0][0]
    b = r[0][0][1]
    c = r[1][0][0]
    d = r[1][0][1]

    a_final = cache[a]
    b_final = cache[b]
    c_final = cache[c]
    d_final = cache[d]

print(f'f({a}) + f({b}) = f({c}) - f({d}) \t {a_final} + {b_final} = {c_final} - {d_final}')