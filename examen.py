# Lista para almacenar las temperaturas diarias
dias = []

# a) Solicitar al usuario 7 temperaturas, una por día
for i in range(7):
    dia = int(input(f"Ingrese la temperatura del día {i + 1}: "))
    dias.append(dia)

# b) Calcular la temperatura promedio semanal
suma = 0
for temp in dias:
    suma += temp
promedio = suma / len(dias)

# c) Contar cuántos días tuvieron temperatura mayor al promedio
mayores = 0
for temp in dias:
    if temp > promedio:
        mayores += 1

# d) Buscar el número de día con la temperatura más baja
dias_menores = []
for i in range(len(dias)):
    if dias[i] < promedio:
        dias_menores.append(i + 1)

print(f"\nPromedio semanal: {promedio:.2f}°C")
print(f"Días con temperatura mayor al promedio: {mayores}")
print(f"Día con la temperatura más baja: {dias_menores}")

#EJERCICIO 2
# PIN predefinido
PIN_CORRECTO = "1234"
saldo = 500  # Saldo inicial

# a) Intentos limitados
intentos = 3
acceso_concedido = False

while intentos > 0:
    pin_ingresado = input("Ingrese su PIN: ")

    if pin_ingresado == PIN_CORRECTO:
        acceso_concedido = True
        break
    else:
        intentos -= 1
        print(f"PIN incorrecto. Intentos restantes: {intentos}")

if acceso_concedido:
    print("Bienvenido. ¿Qué desea hacer?")

    while True:
        # b) Menú de opciones
        print("\n1. Ver saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Su saldo actual es: ${saldo}")

        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            if monto > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${saldo}")

        elif opcion == "3":
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")

        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
else:
    print("PIN incorrecto. Acceso denegado.")
#ejercicio 3
# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Número inválido. Debe ser un entero positivo.")
else:
    original = numero  # Guardamos una copia para mostrar resultados si se necesita
    cantidad_digitos = 0
    suma_digitos = 0
    pares = 0
    impares = 0
    digito_mayor = 0

    while numero > 0:
        digito = numero % 10  # Último dígito
        suma_digitos += digito
        cantidad_digitos += 1

        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1

        if digito > digito_mayor:
            digito_mayor = digito

        numero //= 10  # Quitar el último dígito

    # Mostrar resultados
    print(f"\nCantidad de dígitos: {cantidad_digitos}")
    print(f"Suma de dígitos: {suma_digitos}")
    print(f"Dígitos pares: {pares}")
    print(f"Dígitos impares: {impares}")
    print(f"Dígito mayor: {digito_mayor}")
# 4
# a) Ingresar 10 notas (valores entre 0 y 100)
notas = []
i = 0
while i < 10:
    try:
        nota = float(input(f"Ingrese nota {i + 1}: "))
        if 0 <= nota <= 100:
            notas.append(nota)
            i += 1
        else:
            print("La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")

# b) Ordenar usando algoritmo de Burbuja
n = len(notas)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if notas[j] > notas[j + 1]:
            notas[j], notas[j + 1] = notas[j + 1], notas[j]

# c) Mostrar la lista ordenada
print(f"\nLista ordenada: {notas}")

# d) Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.1f}")
