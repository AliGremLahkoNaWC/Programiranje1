import math
import sys

def virus(prej, po):
    '''Funkcija vrne minimalno zaporedno sekvenco vstavljeno v DNK.'''

    prej = set(prej)
    po = set(po)
    dna = set('ACTG')

    #čim se sekvenca neha ujemat, nastopi vstavljena sekvenca.
    #to sekvenco štejemo

    #split ko se sekvenci nehata ujemati
    #možen način:
	#število sprememb. dolžina PO - Prej + unikatni znaki vstavljeni
    #unikatni znaki je presek neujemajočih z možnimi

    for znak in range(len(prej)):
        if prej[znak] == po[znak]:
            pass
        else:
            prej = prej[znak:]
            po = po[znak:]
            break

    stev_sprememb = abs(len(prej)-len(po))
    nov_dna = set()

    if len(prej) > len(po):
        for znak in range(len(prej)):
            if prej[znak] != po[znak]:
                
            
    else:
        for znak in range(len(po))

    

    
        
