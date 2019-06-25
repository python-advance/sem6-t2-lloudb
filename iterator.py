import itertools

# итератор позволяющий получить очередное число Фибоначчи
def fibo_iterator():
    a0 = 0
    a1 = 1
    while True:           
        yield a0
        a0, a1 = a1, a0 + a1

def get_fibo_list(max_value):
    result = list()
    for fi in fibo_iterator():
        result = result + [fi]
        if(fi >= max_value):
            break
    return result

# итератор позволяющий получить очередное число Фибоначчи методом рекурсии
def fibo_recur_iterator():
    yield 0
    yield 1
    f, tf = itertools.tee(fibo_recur_iterator()) 
    next(tf)
    for a0, a1 in zip(f, tf):
        yield a0 + a1

def get_fibo_recur_list(max_value):
    result = list()
    for fi in fibo_recur_iterator():
        result = result + [fi]
        if(fi >= max_value):
            break
    return result

if __name__ == '__main__':
    # Tests:
    test_list = [0, 1, 1, 2, 3, 5, 8]
    fibo_list = get_fibo_list(7)
    fibo_list_recur = get_fibo_recur_list(4)
    for i in range(0, len(fibo_list) - 1):
        assert(fibo_list[i] == fibo_list_recur[i])
        assert(fibo_list[i] == test_list[i])

    print("fibo list:")
    for fi in get_fibo_list(300):
        print(str(fi))

    print("\nrecur fibo list:")
    for fi in get_fibo_recur_list(300):
        print(str(fi))
