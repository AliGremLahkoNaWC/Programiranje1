'''def prijatelji_dolgovi(dolgovi,prijatelji):
    tabela = []
    tabela_tabel = []
    for elt in range(len(prijatelji)):
        i1 = int(prijatelji[elt][0])
        i2 = int(prijatelji[elt][1])
        tabela.append(dolgovi[i1])
        tabela.append(dolgovi[i2])
        tabela_tabel.append(tabela)
        tabela = []
    return tabela_tabel'''

def prazna_tabela(m):
    tab = []
    for stvar in range(m):
        tab.append(0)
    return tab



def money_matters(n,m,dolgovi,prijatelji):
        
    for ind in range(len(prijatelji)):
        enka = int(prijatelji[ind][0])
        dvojka = int(prijatelji[ind][1])
        if dolgovi[enka] > 0 and dolgovi[dvojka] < 0:
            dolgovi[dvojka] = dolgovi[dvojka] + dolgovi[enka]

            if dolgovi[dvojka] < 0:
                prijatelji[ind].append(False)
        elif dolgovi[enka] < 0 and dolgovi[dvojka] < 0:
            pass
        else:
            dolgovi[enka] = dolgovi[enka] + dolgovi[dvojka]

            if dolgovi[enka] < 0:
                
                prijatelji[ind].append(False)

    for resnica in prijatelji:
        if False in resnica:
            return 'IMPOSSIBLE'
    return 'POSSIBLE' 


            
            
        

# če je vsota tabele kombinacij vračil dolgov enaka 0, je možno vračilo











n = 0
m = 0
o = 0
dolgovi = []
prijatelji = []

with open('besedilo.txt','r') as f:
    nista=f.read().splitlines()
    n = nista[0].split()
    m = int(n[1])
    n = int(n[0])
    nista.remove(nista[0])
    for neki in range(0,n):
        dolgovi.append(int(nista.pop(0)))
    for neki in nista:
        jao = neki.split()
        prijatelji.append(jao)

print(money_matters(n,m,dolgovi,prijatelji))   
