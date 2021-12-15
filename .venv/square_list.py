import math

# n = input("Enter the first integer: ")
# dam = int(float(n))
# if dam < 20:
#     for dam in range(1, dam):
#         result = int(math.pow(dam, 2))
#         print(result)

n = input("Enter the integer: ")
dam = int(float(n))
if 1 < dam < 150:
    for dam in range(1, dam+1):
        print(dam, end="")
