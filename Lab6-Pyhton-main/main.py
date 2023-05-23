print("Enter a number")
number = int(input())

Lambda = lambda x: (x - 3) / x ** 2
List = []
for x in range(1, number + 1):
    List.append(Lambda(x))

print("Sum:", sum(List))


def function(n):
    if n == 0:
        return 1
    else:
        return ((n / (n + 2)) - 10) * function(n - 1)


print("Enter number")
num = int(input())
print(function(num))
