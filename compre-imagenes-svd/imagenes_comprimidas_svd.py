from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

imagen=Image.open(r'c:\Users\Usuario\Desktop\PythonAvanzado\compre-imagenes-svd\imagenpaisaje4k.jpg')

imagen_gris=imagen.convert('LA')

plt.figure(1)
plt.imshow(imagen)
plt.title('Imagen original')
plt.gca().invert_yaxis()  # Opcional: muestra los ejes


# Convertir la imagen a escala de grises
plt.figure(2)
plt.imshow(imagen_gris,cmap='gray')
plt.title('Imagen en escala de grises')
plt.gca().invert_yaxis()  # Opcional: muestra los ejes


#Convierte los datos en una matriz numpy, que no afecta a los datos de la imagen:
plt.figure(3)
imgmat=np.array(list(imagen_gris.getdata(band=0)), float)
imgmat.shape=(imagen_gris.size[1], imagen_gris.size[0])
imgmat=np.matrix(imgmat)
plt.imshow(imgmat,cmap='gray')
plt.gca().invert_yaxis()  # Opcional: muestra los ejes
plt.title('Imagen en escala de grises en matriz')


#Calcular la SVD de la imagen:

U, sigma, V = np.linalg.svd(imgmat)

#Reconstruir la imagen con diferentes valores de k:

#Al igual que los valores propios se ordenan en orden descendente en diag(λ), también los valores singulares,
# por convención, se ordenan en orden descendente en D (o, en este código, diag(σ)). Así, el primer vector singular
# izquierdo de U y el primer vector singular derecho de V pueden representar la característica más prominente de
# la imagen:

#para k=1
plt.figure(4)
reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
plt.imshow(reconstimg,cmap='gray')
plt.gca().invert_yaxis()  # Opcional: muestra los ejes
plt.title('Imagen reconstruida con k=1')

#para varios valores de k
j=4
for i in [2,4,6,8,16,32,64]:
    plt.figure(j)
    reconstimg=np.matrix(U[:,:i]*np.diag(sigma[:i])*np.matrix(V[:i,:]))
    plt.imshow(reconstimg,cmap='gray')
    plt.gca().invert_yaxis()  # Opcional: muestra los ejes
    plt.title('Imagen reconstruida con k=%d' % i)
    j+=1
    
plt.tight_layout()
plt.show()

#La dimencion de lamatriz de la imagen original es de 3840x2160

print('-'*80)
imgmat_dim=imgmat.shape
print('Dimensiones de la matriz de la imagen original:',imgmat_dim)
full_presentacion=1200*1920
print('Número de elementos de la matriz de la imagen original:',full_presentacion)
svd64_presentacion=64*(1200+1920+1)
print('Número de elementos de la matriz de la imagen reconstruida con k=64:',svd64_presentacion)    
porcentaje=(svd64_presentacion/full_presentacion)*100
print('Porcentaje de la matriz de la imagen reconstruida con k=64:',porcentaje,'%')
print('-'*80)

