from collections import Counter

n = int(input('Enter Value of n :'))
di = {}
for i in range(1, n+1):
    di[i] = i*i
print("(a) Dictionary for (n = %d) :\n" %n, di)

d1 = Counter({'a':100, 'b':200, 'c':300})
d2 = Counter({'a':300, 'b':200, 'c':400})
out = d1 + d2
print("\n(b)\nd1 =", d1, "\nd2 =", d2, "\nOutput =", out)
