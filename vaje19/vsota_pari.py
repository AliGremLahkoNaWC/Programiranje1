def vsota_pari(tabela):
    '''funkcija paroma sešteva števila in jih lepi v novo tabelo'''
    tab1 = []
    stev = 0
    vsota = 0
    for dig in tabela:
        if stev % 2 == 0:
            try:
                vsota = int(dig)
            except:
                pass
            stev += 1
        elif stev % 2 != 0:
            try:
                vsota = vsota + int(dig)
            except:
                pass
            stev += 1
            tab1.append(vsota)
            vsota = 0
    return tab1


tabela = [1,'2',None,4,5,'6',7,8,9,12]
print(vsota_pari(tabela))
