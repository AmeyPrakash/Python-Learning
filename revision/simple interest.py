def simple_interest(p, t, r):
    return (p * t * r) / 100
p, t, r = 3, 4, 5
sim = simple_interest(p, t, r)
print(sim)


si = lambda x, y, z: (x * y * z) / 100
x, y, z = 3, 4, 5
simp = si(x, y, z)
print(simp)

a, b, c = 3, 4, 5
interest = [a * b * c / 100][0]
print(interest)