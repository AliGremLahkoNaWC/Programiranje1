import turtle, math


def hisa(zelvak, d):
    '''funkcija rise hiso s stranico kvadrata dolzine d'''
    zelvak.left(45)
    zelvak.forward(math.sqrt((d/2)**2 + (d/2)**2))
    zelvak.right(90)
    zelvak.forward(math.sqrt((d/2)**2 + (d/2)**2))
    zelvak.right(45)
    zelvak.forward(d)
    zelvak.right(90)
    zelvak.forward(d)
    zelvak.right(90)
    zelvak.forward(d)
    zelvak.right(90)
    zelvak.forward(d)


zelvak = turtle.Turtle()
#hisa(zelvak, 50)


def nKotnik(zelvak, n, d, barva):
    '''funkcija izrise n-kotnik in ga pobarva'''
    kot = 180 - 2*(360/n)
    zelvak.left(kot)
    zelvak.forward(d)
    for i in range(n-1):
        zelvak.right(kot/2)
        zelvak.forward(d)

    

nKotnik(zelvak, 7, 70, 'red')
