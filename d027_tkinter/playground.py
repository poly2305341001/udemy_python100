def add(*args):     # args는 튜플
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,4,6,7,3,6,24537,4,5622,4,4,239566,34957937))