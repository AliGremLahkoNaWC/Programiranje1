import math
def kolikoOstalo(širina, višina):
        '''Na tri decimalke natančno vrne, koliko litrov vode je ostalo v posodi'''
        volumenKrogle = 4/ 3 * math.pi * 0.125
        volumenPosode = širina ** 2 * višina / 1000
        ostanekVode = round(volumenPosode - volumenKrogle, 3)
        return ostanekVode
    
print(kolikoOstalo(10,10))