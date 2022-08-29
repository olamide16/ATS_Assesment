def print_factors(x,y):
    l = []
    for i in range (1,x+1):
        if x % i == 0:
            l.append(i)
    # print(l)
    m = []
    for j in range (1,y +1):
        if y % j ==0:
            m.append(j)
    
    # n = []
    # for k in range(1,z +1):
    #     if z % k == 0:
    #         n.append(k)
    # print(n)
    common_factors = list(set(l).intersection(m))
    # new = list(set(common_factors).intersection(n))
    print(common_factors)
print_factors(8,16)