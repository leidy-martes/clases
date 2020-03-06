def factors(value):
    list_of_factors = []

    def concurent(v):        

        if v == 1:
            return None

        i = 2

        while i < v+1:
            if v % i == 0:
                list_of_factors.append(i)
                concurent(v / i)
                break
            i +=1

    concurent(value)

    return list_of_factors

