#      *
#     ***
#    *****
#   *******
#  *********

for i in range(1, 6): # 1,2,3,4,5
    for j in range(5-i): # 4,3,2,1,0
        print(" ", end="")
    for k in range(2*i-1): # 1,3,5,7,9
        print("*", end="")
    print()
    