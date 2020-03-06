def convert(number):
    namelist = [[3, "Pling"], [5, "Plang"], [7, "Plong"]]
    templist = [i[1] for i in namelist if not number % i[0]]
    return "".join(templist) if templist else str(number)
