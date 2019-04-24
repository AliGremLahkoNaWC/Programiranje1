import os
def poisci_rime(seznam, datoteka):
    '''zapise besede ki se rimajo v datoteko'''
    samoglasniki = 'aeiouAEIOU'
    nov_seznam = []
    for beseda in seznam:
        nov_seznam.append(beseda[::-1])
    slovar_koncnic = dict()
    
    for beseda in nov_seznam:
        niz = ''
        for char in beseda:
            if char not in samoglasniki:
                niz = niz + char
                
            else:
                niz = niz + char
                
                if niz[::-1] not in slovar_koncnic:
                    slovar_koncnic[niz[::-1]] = []
                    slovar_koncnic[niz[::-1]] = slovar_koncnic[niz[::-1]] + [beseda[::-1]]
                else:
                    slovar_koncnic[niz[::-1]] = slovar_koncnic[niz[::-1]] + [beseda[::-1]]
                break

    dat = open(datoteka, 'w+')
    for key, val in slovar_koncnic.items():
        print(key + ': ' + str(val), file=dat)
    dat.close()
    with open(datoteka, 'r') as vsb:
        vsebina = vsb.read()
        print(vsebina)
    return dat

poisci_rime(["zob", "miš", "rob", "grob", "piš"], 'rime.txt')

if __name__ == '__main__':
    if poisci_rime(["zob", "miš", "rob", "grob", "piš"], 'rime.txt'):
        if 'rime.txt' not in os.listdir():
            print('Napacno ime datoteke, kolega!')
        else:
            datoteka = poisci_rime(["zob", "miš", "rob", "grob", "piš"], 'rime.txt')
            with open(datoteka, 'r') as vsebina:
                vsb = vsebina.read()
            #if vsb != 'ob: ['zob', 'rob', 'grob'] iš: ['miš', 'piš']'



        
