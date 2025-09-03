def EvenOdd(num):
    if((num % 2) == 0):
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

num = int(input("Enter a No. : "))

result = EvenOdd(num)

print(result)
