num = 20
for i in range(num):
    str = "|"*(num-i-1)
    print(str + "-"*(1+(i*2)) + str)