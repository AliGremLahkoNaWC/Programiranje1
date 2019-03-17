


def hex_pars(tabela):

    for elt in tabela:
        stevilo = int(elt,0)
        if stevilo < 0:
            pass
        else:
            print('{} {}' .format(elt,stevilo))



jao = input()
#with open('Besedilo.txt','r') as line:
#    jao = line.read()
    
hex_variante = '0123456789ABCDEFabcdef'
xX = 'xX'
tab_hex = []
for ind in range(len(jao)):
    if jao[ind] == '0' and jao[ind+1] in xX:
        nov_jao = jao[ind:]
        niz = ''
        stev = 0
        for char in nov_jao:
            if char in hex_variante:
                niz = niz + char
            elif char in xX and stev == 0:
                niz = niz + char
                stev = 1
            else:
                break
        tab_hex.append(niz)

hex_pars(tab_hex)


