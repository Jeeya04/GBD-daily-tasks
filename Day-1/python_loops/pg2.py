# pg2: Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
else:
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
