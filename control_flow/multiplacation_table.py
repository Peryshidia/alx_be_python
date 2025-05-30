number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}") 