def count(n):
    list = []
    for i in range(n+1):
        t = []
        while i > 0:
            rest = i % 2      # converting a number to the binary system without bin
            t.append(rest)    # by saving the remainder of division by two
            i //= 2
        if sum(t) > 1:
            list.append(sum(t))
        else:
            list.append(sum(t))
    return list
