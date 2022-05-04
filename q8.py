#Part (a)
print("(a)\n")
num1 = 0
num2 = 1
max = 50
fib = (num1, num2,)
for i in range(2,max):
    num = num1 + num2
    num1 = num2
    num2 = num
    fib = fib + (num,)

print('Fibonacci Series till %dth term is as follows:' %max)
print(fib)

#Part (b)
print("\n(b)\n")
n = int(input('Enter the number for the multiplication table generation: '))
print("Multiplication Table of", n,":")
for i in range(10):
    k = i + 1
    print(n, 'X', k, '=', n*k)
