# Multiplication table using for loop and .join(str)

n = int(input("Assign a positive integer <= 100: "))
print(f"Multiplication Table of the first {n} digits:")
for row in range(1,n+1):
        print('\t'.join(str(row*col) for col in range(1,n+1)))
