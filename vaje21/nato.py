nato = ['alfa', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel',
        'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra',
        'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']
nato_slovar = dict()

for beseda in nato:
    nato_slovar[beseda[0]] = beseda
    
def crkujNATO(beseda):
    '''funkcija pretovri besedo v skupek NATO besed'''
    niz = ''

    for char in beseda:
        if char in nato_slovar:
            niz = niz + nato_slovar[char] + ' '
        elif char == ' ':
            niz = niz + ' '

    #odstranim presledek na koncu niza
    niz = niz[:-1]
    return niz

def razberiNATO(niz):
    '''funkcija pretvori iz NATO besednjaka v normalno besedo'''
    besed = ''
    niz = niz.split()
    
    for beseda in niz:
        if beseda.isalpha():
            besed = besed + beseda[0]
        else:
            besed = besed + beseda

    return besed

if __name__ == '__main__':
    if crkujNATO('zaspan sem') != 'zulu alfa sierra papa alfa november  sierra echo mike':
        print('Namesto:', crkujNATO('zaspan sem'), '\nBi moralo pisati: zulu alfa sierra papa alfa november  sierra echo mike')
    if crkujNATO('nisem zaspan') != 'november india sierra echo mike  zulu alfa sierra papa alfa november':
        print('Namesto:', crkujNATO('nisem zaspan'), '\nBi moralo pisati: november india sierra echo mike  zulu alfa sierra papa alfa november')
    if crkujNATO('gauss je bozanstvo') != 'golf alfa uniform sierra sierra  juliett echo  bravo oscar zulu alfa november sierra tango victor oscar':
        print('Namesto:', crkujNATO('gauss je bozanstvo'), '\nBi moralo pisati: golf alfa uniform sierra sierra  juliett echo  bravo oscar zulu alfa november sierra tango victor oscar')
        

    if razberiNATO('zulu alfa sierra papa alfa november - sierra echo mike') != 'zaspan-sem':
        print('Namesto:', razberiNATO('zulu alfa sierra papa alfa november - sierra echo mike'), '\nBi moralo pisati: zaspan-sem')
    if razberiNATO('golf alfa uniform sierra sierra - juliett echo - bravo oscar zulu alfa november sierra tango victor oscar') != 'gauss-je-bozanstvo':
        print('Namesto:', razberiNATO('golf alfa uniform sierra sierra - juliett echo - bravo oscar zulu alfa november sierra tango victor oscar'), '\nBi moralo pisati: gauss je bozanstvo')



