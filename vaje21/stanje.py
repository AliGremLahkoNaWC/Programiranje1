def stanje(denar):
    ''' funkcija vrne financo stanje, slovnicno pravilno izpisano '''
    for banka in denar:
        try:
            if banka < -300:
                return 'Ti si navadna zguba!'
            if banka >= 1000000:
                return 'Tajkun!'
            elif abs(banka)//10 == 0:
                if abs(banka) == 1:
                    return 'Stanje je ' + str(banka) + ' evr.'
                if abs(banka) == 2:
                    return 'Stanje je ' + str(banka) + ' evra.'
                if abs(banka) == 3 or abs(banka) == 4:
                    return 'Stanje je ' + str(banka) + ' evri.'
            elif banka//10 != 0:
                if banka//10 == 1:
                    return 'Stanje je ' + str(banka) + ' evrov.'
                elif int(str(banka)[-1]) == 1:
                    return 'Stanje je ' + str(banka) + ' evro.'
                elif int(str(banka)[-1]) == 2:
                    return 'Stanje je ' + str(banka) + ' evra.'
                else:
                    return 'Stanje je ' + str(banka) + ' evrov.'
        except:
            print('Podano ni število.')
            
if __name__ == '__main__':
    if stanje([-1]) != 'Stanje je -1 evro.':
        print('Namesto: ', stanje([-1]), ' Bi moralo pisati: Stanje je -1 evro.')
    if stanje([-2]) != 'Stanje je -2 evra.':
        print('Namesto: ', stanje([-2]), ' Bi morali pisati: Stanje je -2 evra.')
    if stanje([-3]) != 'Stanje je -3 evri.':
        print('Namesto: ', stanje([-3]), ' Bi moralo pisati: Stanje je -3 evri.')
    if stanje([-4]) != 'Stanje je -4 evri.':
        print('Namesto: ', stanje([-4]), ' Bi moralo pisati: Stanje je -4 evri.')
    if stanje([11]) != 'Stanje je 11 evrov.':
        print('Namesto: ', stanje([11]), ' Bi moralo pisati: Stanje je 11 evrov.')
    if stanje([101]) != 'Stanje je 101 evro.':
        print('Namesto: ', stanje([101]), ' Bi moralo pisati: Stanje je 101 evro.')
    if stanje([102]) != 'Stanje je 102 evra.':
        print('Namesto: ', stanje([102]), ' Bi moralo pisati: Stanje je 102 evra.')
    if stanje([-303]) != 'Ti si navadna zguba!':
        print('Namesto: ', stanje([-303]), ' Bi moralo pisati: Ti si navadna zguba!')
    if stanje([1000000]) != 'Tajkun!':
        print('Namesto: ', stanje([1000000]), ' Bi morali pisati: Tajkun!')
        
    
			

                

denar = [int(vrstica.strip()) for vrstica in open('stanje_test.txt', 'r')]
stanje(denar)
