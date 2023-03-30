from math import pi

r1, r2, r3 = map(int, input().split())

# S = pi * R ** 2
s1 = pi * r1 ** 2
s2 = pi * r2 ** 2
s3 = pi * r3 ** 2

print("%.2f %.2f %.2f" % (s1, s2, s3))    