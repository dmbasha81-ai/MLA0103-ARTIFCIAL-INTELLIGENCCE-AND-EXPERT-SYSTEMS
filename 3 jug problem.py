j12 = 12
j8 = 0
j5 = 0

print("Initial State:", (j12, j8, j5))

t = min(j12, 8 - j8)
j12 -= t
j8 += t
print((j12, j8, j5))

t = min(j8, 5 - j5)
j8 -= t
j5 += t
print((j12, j8, j5))

j5 = 0
print((j12, j8, j5))

t = min(j8, 5 - j5)
j8 -= t
j5 += t
print((j12, j8, j5))

t = min(j12, 8 - j8)
j12 -= t
j8 += t
print((j12, j8, j5))

t = min(j8, 5 - j5)
j8 -= t
j5 += t
print((j12, j8, j5))

j5 = 0
print((j12, j8, j5))

t = min(j8, 5 - j5)
j8 -= t
j5 += t
print((j12, j8, j5))

print("Goal Achieved:", (j12, j8, j5))
