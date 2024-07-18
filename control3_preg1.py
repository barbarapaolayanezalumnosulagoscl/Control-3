def digitos(num):
    cont = 0
    while num > 0:
        num = num // 10
        cont += 1
    return cont

numero = int(input("Ingrese un numero: "))

cant_digitos = digitos(numero)
print("El numero", numero, "tiene", cant_digitos, "digitos.")
