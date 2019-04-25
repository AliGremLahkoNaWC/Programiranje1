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
    # namesto datoteka.txt, vstaviš samo datoteka, kot je podan argument
    # pri klicu funkcije
    for key, val in slovar_koncnic.items():
        print(key + ': ' + str(val), file=dat)
    dat.close()

    return dat
    


poisci_rime(["zob", "miš", "rob", "grob", "piš"], 'rime.txt')
poisci_rime(['kri','dni','bri','lonec','smolec','grdobec'], 'slabe_rime.txt')
poisci_rime(['jezus','bezus','kvezus','pistola', 'minola','lubenica'], 'domiselnost.txt')

if __name__ == '__main__':

    if poisci_rime(["zob", "miš", "rob", "grob", "piš"], 'rime.txt'):
        #os.chdir(os.path.dirname(__file__))
        #pot = os.getcwd()
        if 'rime.txt' not in os.listdir():
            print('Napacno ime datoteke, kolega!')
        else:
            niz = open('rime.txt','r').readlines()        
            if niz != ["ob: ['zob', 'rob', 'grob']\n", "iš: ['miš', 'piš']\n"]:
                print('Namesto: \n' + str(niz) + "\nBi moralo pisati: \nob: ['zob', 'rob', 'grob']\niš: ['miš', 'piš']\n")

    if poisci_rime(['kri','dni','bri','lonec','smolec','grdobec'], 'slabe_rime.txt'):
        if 'slabe_rime.txt' not in os.listdir():
            print('Napacno ime datoteke, kolega! \n')
        else:
            niz = open('slabe_rime.txt', 'r').readlines()
            if niz != ["i: ['kri', 'dni', 'bri']\n", "ec: ['lonec', 'smolec', 'grdobec']\n"]:
                print('Namesto: \n' + str(niz) + "\nBi moralo pisati: \ni: ['kri', 'dni', 'bri']\nec: ['lonec', 'smolec', 'grdobec']\n")

    if poisci_rime(['jezus','bezus','kvezus','pistola', 'minola','lubenica'], 'domiselnost.txt'):
        if 'domiselnost.txt' not in os.listdir():
            print('Napacno ime datoteke, kolega!')
        else:
            niz = open('domiselnost.txt', 'r').readlines()
            if niz != ["us: ['jezus', 'bezus', 'kvezus']\n", "a: ['pistola', 'minola', 'lubenica']\n"]:
                print('Namesto: \n' + str(niz) + "\nBi moralo pisati: \nus: ['jezus', 'bezus', 'kvezus']\na: ['pistola', 'minola', 'lubenica']\n")
