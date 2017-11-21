def foo(u, v, *args):
    print('u, v = ' + str((u,v)))
    for i in range(len(args)):
        print('args {} = {}'.format(str(i), str(args[i])))

args = (2.71, [6, 28])
# foo(1, 'euler', *args)

def foo():
    pass

bar = foo
del foo
# print(bar.__name__)

print((lambda x, y: x if x > y else y)(3,2))
print(sorted(range(-5, 6), key=lambda x: -x))
class Car:
    rev = lambda self: print('Wroom!')
    crash = lambda self: print('Boom!')

my_car = Car()
my_car.crash()
