from itertools import permutations, product

n = input()

result = 0
for bits in product([0, 1], repeat=len(n)):
    a = [x for bit, x in zip(bits, n) if bit == 1]
    if not a: continue
    b = [x for bit, x in zip(bits, n) if bit == 0]
    if not b: continue
    
    for a1 in permutations(a):
        for b1 in permutations(b):
            result = max(result, int(''.join(a1)) * int(''.join(b1)))
print(result)