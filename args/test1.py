def sum_args(*args):
    if not args:
        return 0
    return sum(args)
print(sum_args(1, 2, 3))            #output : 6
print(sum_args(10, 20, 30, 40))     #output : 100
print(sum_args())                   #output : 0
print(sum_args(5.5, 4.5, -10))      #output : 0