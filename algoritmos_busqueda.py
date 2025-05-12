
#Llamar a la función
def lista_precios(precios):

    menor = precios[0] #suponer que el primer elemento es el menor
    for precio in precios:
       if precio < menor:
          menor = precio

    return menor

precios = [400, 250, 310, 280]
print(lista_precios(precios))




#Busqueda binaria 

def busqueda_binaria(lista, objetivos):
    izquierda = 0
    derecha = len(lista) -1
    while izquierda <= derecha:
       medio = (izquierda + derecha) // 2

       if lista[medio] == objetivos:
          return medio
       elif lista[medio] == objetivos:
          izquierda = medio +1
       else:
          derecha = medio -1
       
    
    return -1 #No encontrado

datos =[12, 23, 34, 45, 67] #ordenar antes
buscado = 45

posicion = busqueda_binaria(datos, buscado)

if posicion != -1:
   print(f"Elemento encontrado en la posición {posicion}")
else:
   print("Elemento no encontrado")



#Busqueda Lineal
def busqueda_lineal(lista,objetivo):
   for i in range(len(lista)):
      if lista[i] == objetivo:
         return i #Devuelve la posicion donde se encontró
   return -1

datos = [23, 45, 12, 67, 34]
buscado = 67

posicion = busqueda_lineal(datos, buscado)

if posicion != 1:
   print(f"Elemento encontrado en la posición {posicion}")
else:
   print("Elemento no encontrado")

















