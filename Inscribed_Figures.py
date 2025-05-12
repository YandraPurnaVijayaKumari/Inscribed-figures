import math
import sys
def areaCircle(diagonal):
    radius = diagonal/2
    return (f'{math.pi * (radius**2):.2f}')

def squarearea(diameter):
    side = diameter / math.sqrt(2)
    area = side*side
    return (f'{area:.2f}')
 
def findarea(diagonal,shape):
    if diagonal>=0:
        if shape=='cir':
            area = areaCircle(diagonal)
        elif shape== 'sqr':
            area = squarearea(diagonal)
        else:
            print('enter valid shape')
    else:
        area = 'enter valid values'
    return area

def diagonal(n,r):
    t_side = n-2*r
    t_hypo = math.sqrt(2)*(t_side)
    dia = t_hypo-2*r
    return dia

n = int(sys.argv[1])
r = int(sys.argv[2])
shape = sys.argv[3]
dia = diagonal(n,r)
area = findarea(dia,shape)
print(area)