x = input("Input number ")
n = input("Input degree ")

x = int(x)
n = int(n)

result = 1
for i in range (n):
    result *=x
print('x**n ==', result)
