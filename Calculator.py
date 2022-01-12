
def Add(*args):
    total_sum = 0
    for i in args:
        total_sum += i
    return total_sum
    
def Subtraction(*args):
    total_sub = args[0]
    for i in args[1:]:
        total_sub -= i
    return total_sub
    
def Multiplication(*args):
    total_mul=1
    for i in args:
        total_mul *= i
    return total_mul
    
def Division(*args):
    total_div = args[0]
    for i in args[1:]:
        total_div /= i
    return total_div

def AND_op(a,b):
    return a and b

def OR_op(a,b):
    return a or b

def NOR_op(a, b):
    return not (a or b)

def fact(a):
    factorial = 1
    for i in range(1,a+1):
        factorial *= i
    return factorial

def fibonacci(a):
    if(a==0 or a==1):
        return a
    return fibonacci(a-1) + fibonacci(a-2)
    
def print_fibo(a):
    first_num=0
    print(first_num)
    sec_num = 1
    print(sec_num)
    for i in range(a-2):
        temp = first_num
        first_num = sec_num
        sec_num = temp+sec_num
        print(sec_num)
    return 
    
def int_rev(a):
    stra = str(a)
    stra = stra[::-1]
    inta = int(stra)
    return inta

def mean(a):
    suma = 0
    for i in a:
        suma+=i
    return suma/len(a)

def median(a):
    A = sorted(a)
    n = len(a)
    m = n-1
    if n%2 == 1:
        return (A[int(n/2)]+A[int(m/2)])/2
    else:
        return (A[int(m/2)]+A[int(n/2)])/2

def mode(a):
    return (max(set(a) , key=a.count))

def create_dict(key,value):
    dict = {}
    dict[key] = value
    return dict

def variance(a):
    mn = mean(a)
    var=0
    for i in a:
        s = (i-mn)**2
        var += s/(len(a)-1)
    return var

def std_dev(a):
    var = variance(a)
    std_var= var**(0.5)
    return std_var

def permute(a):
    from itertools import permutations 
    perm = permutations(a)
    for i in perm:
        print(i)

def comb(a,b):
    from itertools import combinations
    comb = combinations(a,b)
    for i in comb:
        print(i)