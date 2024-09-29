def MakeDate(d,m,y):
    return [d,m,y]

def Day(D):
    return D[0]

def Month(D):
    return D[1]

def Year(D):
    return D[2]

def isEqD(D1,D2):
    return D1 == D2

def IsBeafore(D1,D2):
    if Year(D1) != Year(D2):
        return  Year(D2) < Year(D1)
    else:
        if Month(D1) != Month(D2):
            return Month(D2) < Month(D1)
        else:
            return Day(D2) < Day(D1)

def IsBeafore(D1,D2):
    if Year(D1) != Year(D2):
        return  Year(D2) > Year(D1)
    else:
        if Month(D1) != Month(D2):
            return Month(D2) > Month(D1)
        else:
            return Day(D2) > Day(D1)
        
def IsKabisat(T):
    return T % 4 == 0 and (T % 100 != 0 or T % 400 == 0)

def NextDay(D):
    # bulan yang terdiri dari 30 hari kecuali desember
    if Month(D) == 1 or Month(D) == 3 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10:
        if Day(D) < 31:
            return MakeDate(Day(D) + 1, Month(D), Year(D))
        else:
            return MakeDate(1, Month(D) + 1, Year(D))
    # bulan februari
    elif Month(D) == 2:
        if Day(D)< 28:
            return MakeDate(Day(D) + 1, Month(D), Year(D))
        else:
            if IsKabisat(Year(D)):
                if Day(D) == 28:
                    return MakeDate(Day(D) + 1, Month(D), Year(D))
                else:
                    return MakeDate(1, Month(D) + 1, Year(D))
            else:
                return MakeDate(1, Month(D) + 1, Year(D))
    # Bulan yang terdiri dari 30 hari
    elif Month(D) == 4 or Month == 6 or Month == 9 or Month == 11:
        if Day(D) < 30:
            return MakeDate(Day(D) + 1, Month(D), Year(D))
        else:
            return MakeDate(1, Month(D) + 1, Year(D))
    # bulan desember
    elif Month(D) == 12:
        if Day(D) < 31:
            return MakeDate(Day(D) + 1, Month(D), Year(D))
        else:
            return MakeDate(1,1,Year(D) + 1)
            
def Yesteday(D):
    if Day(D) == 1:
        if  Month(D) == 12 or Month(D) == 5 or Month(D) == 7 or Month(D) == 10:
            return MakeDate(30, Month(D) + 1, Year(D))
        elif Month(D) == 3:
            if IsKabisat(Year(D)):
                return MakeDate(29, 2, Year(D))
            else:
                return MakeDate(28, 2, Year(D))
        elif Month(D) == 2 or Month(D) == 6 or Month(D) == 8 or Month(D) == 9 or Month(D) == 11:
            return MakeDate(31, Month(D) + 1, Year(D))
        elif Month(D) == 1:
            return MakeDate(31,12,Year(D) - 1)
    else:
        return MakeDate(Day(D) - 1, Month(D), Year(D))
        
print(NextDay(MakeDate(30,3,2006)))