import math

def kolikoOstalo(širina, višina, polmer):
    '''Na tri decimalke natančno vrne, koliko litrov vode je ostalo v posodi'''
    volumenKrogle = 4 * math.pi * (polmer/10)**3 / 3
    
    volumenPosode = širina ** 2 * višina/1000
    ostanekVode = round(volumenPosode - volumenKrogle, 3)
    return ostanekVode

print(kolikoOstalo(10,10,5))