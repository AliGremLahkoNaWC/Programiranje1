import os

def zdruzi(vh1, vh2, ex):
    '''funkcija v izhodno datoteko v i- to vrstico zapiše združeni i-ti vrstici
    obeh vhodnih datotek'''
    try:    
        vh_1,vh_2, ans = open(vh1,'r',encoding='utf-8'), open(vh2, 'r',encoding='utf-8'),open(ex,'w+',encoding='utf-8')    

        for vrstica1, vrstica2 in zip(vh_1,vh_2):
            print(vrstica1.strip() + ' .' + vrstica2.strip(), file=ans)
            
        vh_1.close()
        vh_2.close()
        ans.close()
    
    except:
        raise

os.chdir(os.path.dirname(__file__))
pot = os.getcwd()
vh1 = os.path.join(pot, 'prva.txt')
vh2 = os.path.join(pot, 'druga.txt')
ex = os.path.join(pot, 'pavcek.txt')

zdruzi(vh1,vh2,ex)

if __name__ == '__main__':
    try:
        if os.stat(ex).st_size == 0:
            print('V datoteko ni bilo nic zapisano')
        else:
            eks = open(ex,'r', encoding='utf-8').readlines()
            if eks != ['Na svetu si, da gledaš sonce,\n', ' \n', 'na svetu si, da greš za soncem,\n', ' \n', 'na svetu si, da sam si sonce\n', ' \n', 'in da s sveta odganjaš – sence.\n']:
                niz = ''
                for stavek in eks:
                    niz = niz + stavek
                print('Namesto: \n' + niz + '\nBi moralo pisati:\n'+'Na svetu si, da gledaš sonce,\n'+ ' \n'+ 'na svetu si, da greš za soncem,\n'+ ' \n'+'na svetu si, da sam si sonce\n'+' \n'+'in da s sveta odganjaš – sence.\n')

    except:
        raise ValueError
