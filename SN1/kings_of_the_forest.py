def manjse_letnice(marko,seznam):
    leto_karla = marko[0]
    nov_seznam = []
    
    for x in seznam:
        if x[0] >= leto_karla:
            nov_seznam.append(x)
        else:
            pass
    return nov_seznam

def kralji_gozdnih_ulic(penis,karl,ostali):
    
    leto_karla = karl[0]
    moc_karl = karl[1]
    istoletni_ostali = []
    if int(leto_karla) >= penis:
        return 'unknown'
    for elt in range(0,len(ostali)):
        
        var1 = ostali[elt]
        if var1[0] == leto_karla:
            istoletni_ostali.append(ostali[elt])
           
    stevec = 0
    if len(istoletni_ostali) == 0:
        return leto_karla
    else:
        for elt in istoletni_ostali:
            if elt[1] >= moc_karl:
                stevec = 1
                break
    if stevec == 0:
        return leto_karla
    else:
        leto_karla = str(int(leto_karla) + 1)

    karl[0] = leto_karla
    return kralji_gozdnih_ulic(penis,karl,manjse_letnice(karl,ostali))
    
        
    









    
with open('besedilo.txt','r') as f:
    nista=f.read().splitlines()
    stev=0
    zivali=[]
    for line in nista:
        
        if stev==0:
            turnament_size=line
            turnament_size=turnament_size.split()
            
            stev=1
        elif stev==1:
            marko=line
            marko=marko.split()
            
            stev=2
        else:
            primer=line.strip().split()
            zivali.append(primer)
            


neki = int(marko[0]) + int(turnament_size[1])    
print(kralji_gozdnih_ulic(neki,marko,manjse_letnice(marko,zivali)))



    
