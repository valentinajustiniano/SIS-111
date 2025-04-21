#Edad minima para votar 

edad = int(input("Ingresar tu edad: "))

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")


#Numero mayor entre dos 


numero1 = int(input("Ingresar el primer numero: "))
numero2= int(input("Ingresar el segundo numero: "))

if numero1 > numero2:
    print(f"El numero mayor es {numero1}")
elif numero2 > numero1:
    print(f"El numero mayor es {numero2}")
else:
    print("Ambos números son iguales")


#Validador de Rango de calidad 

calidad = int(input("Ingresar un valor de calidad entre 0 y 100: "))

if calidad >= 80 and calidad <= 90:
    print("Calidad Aceptable")
else:
    print("Sin mensaje")


#Clasificacion de Producto de Peso
peso = int(input("Ingresar el peso del producto (kg):"))

if peso < 5:
    print("Peso ligero")
elif peso < 20:
    print("Peso medio")
else:
    print("Peso pesado")


#Evaluación de Bonificación
salario = float(input("Ingresa tu salario:"))
antiguedad = int(input("Ingresar tu antiguedad: "))

if antiguedad > 10:
    bono = salario * 0.20
elif antiguedad >= 5:
    bono = salario * 0.10
else:
    bono = 0 

salario_final = salario + bono 
print(f"salario con bono: {salario_final}Bs")


#Multiplo común
numero1 = int(input("Ingresar el primer numero: "))
numero2= int(input("Ingresar el segundo numero: "))

if numero1 % 3 == 0 and numero1 % 5 == 0 and numero2 % 3 == 0 and numero2 % 5 == 0:
    print("Ambos números son multiplos de 3 y 5")
else:
    print("No son multiplos de 3 y 5")


#Calculadora de Formula de Ingenieria 
x = int(input("Ingresar el valor de x: "))
y = int(input("Ingresar el valor de y: "))


