import random

k = 5
n = 10

def numbersNot(num):
    nums = [i+1 for i in range(n)]
    nums.remove(num)
    return nums

def random1(size):
    return [k for i in range(size)]

def random2(size):
    return [random.randint(1, n) for i in range(size)]

def random3(size):
    retval = [random.randint(1, n) for i in range(size)]
    return sorted(retval)

def random4(size):
    retval = []
    replace = random.choice(numbersNot(k))
    for i in range(size):
        if i % 2 == 0: retval.append(replace)
        else: retval.append(random.randint(1, n))
    return retval

def random5(size):
    retval = []
    if size < n: 
        b = 1
        for a in range(size):
            retval.append(b)
            b+=1
    else:
        for a in range(int(size/n)):
            for b in range(1, n+1):
                retval.append(b)
    return retval

def random6(size):
    retval = []
    c = 0
    while c < size:
        x = random.randint(1, n)
        if x != k: 
            retval.append(x)
            c+=1
    return retval  

def random7(size):
    retval = [random.randint(1, n) for i in range(size)]
    deletions = 0
    for x in retval:
        if (x==k):
            if deletions % 2 == 0:
                retval.remove(x)
                retval.append(random.choice(numbersNot(k)))
            deletions += 1
    return retval

def random8(size):
    retval = []
    c = 0
    while c < size:
        x = random.randint(1, n)
        if c % 2 == 0:
            while x % 2 != 0:
                x = random.randint(1, n)
        else:
            while x % 2 != 1:
                x = random.randint(1, n)
        retval.append(x)
        c += 1
    return retval

def random9(size):
    retval = []
    c = 0
    if k == n:
        while c < size:
            x = random.randint(1, n)
            if x != k-1: 
                retval.append(x)
                c+=1
    else:
        while c < size:
            x = random.randint(1, n)
            if x != k+1: 
                retval.append(x)
                c+=1
    return retval

def random10(size):
    retval = []
    if random.choice([True, False]):
        for i in range(size):
            x = random.randint(1, n)
            while x % 2 == 0:
                x = random.randint(1, n)
            retval.append(x)
    else:
        for i in range(size):
            x = random.randint(1, n)
            while x % 2 != 0:
                x = random.randint(1, n)
            retval.append(x)
    return retval

