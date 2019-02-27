

def vse_moznosti():
    operatorji = ['+','-','*','//']
    moznosti = {}

    for ena in operatorji:
        for dva in operatorji:
            for tri in operatorji:
                racun = "4 {:s} 4 {:s} 4 {:s} 4".format(ena,dva,tri)
                vrednost = int(eval(racun))
                moznosti[vrednost] = racun.replace('//','/') + ' = {:d}'.format(vrednost)
    return moznosti

def for_thot(m, rezultati):
    
    moznosti = vse_moznosti()
    
    for cifra in range(0,m):
        n = int(rezultati[cifra])
        if n < -60 or n > 256 or n not in moznosti:
            print('no solution')
        else:
            print(moznosti[n])

m = int(input())
rezultati = []
for x in range(0,m):    
    rezultat = int(input())
    rezultati.append(rezultat)
##m = 5
##rezultati = [9,0,7,11,24]
for_thot(m,rezultati)
