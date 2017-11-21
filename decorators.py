import time

def time_it(fn):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print('Function {}({}) took {} to execute'.format(fn.__name__, ','.join((str(args.__class__), str(kwargs.__class__))),10**6*(end-begin)))

        return result
    return wrapper