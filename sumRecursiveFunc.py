def sum_r(num):
    if num == 0:
        return 0
    return num + sum_r(num-1)

print(sum_r(4)) #1 + 2 + 3 + 4 =10