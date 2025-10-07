#1. (incomplete)

def hollow_square(n):
    if n < 1:
        return ""
    
    first_last = "*" * n

    middle = ""
    for i in range(n-2):
        middle+= "*" + ("" * (n+2)) + "*\n"

    if n == 1:
        return "*"
    else:
        return first_last + "\n" + middle + first_last
n = int(input("Enter n: "))
print(hollow_square(n))

#2. (incomplete)
def number_pattern(n):
    count = 1
    while count <= n:
        print(count)
        count += 1
n = int(input("Enter n: "))
print(number_pattern(n))

#3.
def sum_of_natural_numbers(n):
    total = 0
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            if j == i:
                total +=i
            j +=1
        i += 1
    print("Sum = ", "+",  total)
n = int(input("Enter n :"))
sum_of_natural_numbers(n)