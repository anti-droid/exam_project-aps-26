import random

c = 1
n = 1000
i = 1
g = 100
s = 100
m = 1
medical_facility = 101
r = 1000

#100 edge path from 1-101, with p=1 and t=1
roads = []
for u in range(1, 101):
    roads.append((u, u + 1, 1, 1))

# Add remaining edges randomly
all_vertices = list(range(1, n + 1))
while len(roads) < r:
    u, v = random.sample(all_vertices, 2)
    # Avoid duplicates
    if (u, v) not in [(x, y) for x, y, _, _ in roads]:
        roads.append((u, v, 1, 1))  # p=1, t=1

print(c)
print(n)
print(i, g, s)
print(m)
print(medical_facility)
print(r)
for u, v, p, t in roads:
    print(u, v, p, t)
