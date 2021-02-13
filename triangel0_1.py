import re, ast
import math

file = open("triangel.txt","r")

summa = 0

for list in file:


    if list[0] == 'T':
        res = re.findall('\d+,-?\d+', list)
        l = []

        for r in res:
                l.append(ast.literal_eval(r))

    s = float(0.5 * ( ( l[0][0]  -  l[2][0] ) * ( l[1][1]  - l[2][1] ) - ( l[1][0] - l[2][0] ) * ( l[0][1] - l[2][1])))
    s = math.fabs(s)
    summa += s
    print ('Координаты точек '+ str(l))
    print ('Площадь треугольника S =',s)
    print ('------------------------------------')



print('общая площадь треуголников S =', summa)

import matplotlib.pyplot as plt
lx,ly = [],[]
for l1 in l:
    lx.append(l1[0])
    ly.append(l1[1])
lx.append(lx[0])
ly.append(ly[0])
s1 = str(s)
plt.title('Площадь Фигуры S = ' + s1, fontsize=20,
          color="green")

plt.plot(lx,ly,"r")
plt.show()
