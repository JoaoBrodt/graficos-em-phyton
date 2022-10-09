import numpy as np
import matplotlib.pyplot as plt 
from turtle import onclick
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def calcula_m(yc,yp,xc,xp):
  return (yp-yc)/(xp-xc)

def calcula_b(m,xc,yc):
    return -1*(m*yc)+xc

def calcula_X(xc1,yc1,xc2,yc2,mr1,mr2):
    return (-1*(mr2*xc2)+yc2+(mr1*xc1)-yc1)/(mr1-mr2)

def calcula_Y(mr1,xo1,xc1,yc1):
    return (mr1*xo1)-(mr1*xc1)+yc1

xc1 = float(input("Coordenada x da primeira câmera: "))
yc1 = float(input("Coordenada y da primeira câmera: "))
zc1 = float(input("Coordenada z da primeira câmera: "))
 
xp1 = float(input("Coordenada x da primeira projeção: "))
yp1 = float(input("Coordenada y da primeira projeção: "))
zp1 = float(input("Coordenada z da primeira projeção: "))

xc2 = float(input("Coordenada x da segunda câmera: "))
yc2 = float(input("Coordenada y da segunda câmera: "))
zc2 = float(input("Coordenada z da segunda câmera: "))
 
xp2 = float(input("Coordenada x da segunda projeção: "))
yp2 = float(input("Coordenada y da segunda projeção: "))
zp2 = float(input("Coordenada z da segunda projeção: "))


#cálculo do coeficiente angular
mxyc1= calcula_m(yc1,yp1,xc1,xp1)
mxzc1= calcula_m(zc1,zp1,xc1,xp1)
mzyc1= calcula_m(yc1,yp1,zc1,zp1)
mxyc2= calcula_m(yc2,yp2,xc2,xp2)
mxzc2= calcula_m(zc2,zp2,xc2,xp2)
mzyc2= calcula_m(yc2,yp2,zc2,zp2)


#cálculo da posição dos objetos
xo1=calcula_X(xc1,yc1,xc2,yc2,mxyc1,mxyc2)
yo1=calcula_X(xc1,zc1,xc2,zc2,mxzc1,mxzc2)
zo1=calcula_X(zc1,yc1,zc2,yc2,mzyc1,mzyc2)
xo2=calcula_Y(mxyc1, xo1, xc1, yc1 )
yo2=calcula_Y(mxzc1, yo1, xc1, zc1 )
zo2=calcula_Y(mzyc1, zo1, zc1, yc1 )
x=(xo1+yo1)/2
y=(xo2+zo2)/2
z=(zo1+yo2)/2

#tabela com coeficiente angular
fig, ax =plt.subplots(1,1)
data=[[mxyc1],
      [mxzc1],
      [mzyc1],
      [mxyc2],
      [mxzc2],
      [mzyc2]]
column_labels=["Coeficiente angular (m)"]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data,colLabels=column_labels,rowLabels=["XY1","XZ1","ZY1","XY2","XZ2","ZY2"],loc="center")
plt.show()


#plotando grafico
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

X = [xc1, x, xp1]
Y = [yc1, y, yp1]
Z = [zc1, z, zp1]

X2 = [xc2, x, xp2]
Y2 = [yc2, y, yp2]
Z2 = [zc2, z, zp2]

plt.plot(X, Y, Z)
plt.plot(X2, Y2, Z2)
plt.show()




  
  
  
  