increment_by_i = [lambda x: x + i for i in range(10)]
my_iter = iter(increment_by_i)
# print(next(my_iter)(3))
# print(next(my_iter)(3))

def outer_scope():
    a = 10
    b = 5
    c = 100
    d = 1000
    def inner_scope(x):
        return x * a * b * c * d

    return inner_scope

closure = outer_scope()
print(closure.__closure__[3].cell_contents)
print(closure(1))