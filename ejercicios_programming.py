

#Palindromo
def es_palindromo(num):
    #Validar que un palindromo solo acpeta numeros positivos
    if num < 0: return False

    num_original = num
    num_invertido = 0

    #Recorrer todos los digitos del numero
    while num > 0:
        dig = num % 10
        num_invertido = num_invertido * 10 + dig
        num = num // 10

    return num_original == num_invertido

#Llamar a la función es_palindromo(NUM):
var_num = int(input("Ingrese su número: "))
var_palindromo = es_palindromo(var_num)
if var_palindromo:
    print("Es palindromo")
else:
    print("No es palindromo")



#Palindromo sin return
def es_palindromo_sin_return(num):
    #Validar que un palindromo solo acpeta numeros positivos
    if num < 0: print("No se aceptan negativos")

    num_original = num
    num_invertido = 0

    #Recorrer todos los digitos del numero
    while num > 0:
        dig = num % 10
        num_invertido = num_invertido * 10 + dig
        num = num // 10

    if num_original == num_invertido:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Llamar a la función es_palindromo(NUM):
var_num = int(input("Ingrese su número: "))
es_palindromo_sin_return(var_num)
