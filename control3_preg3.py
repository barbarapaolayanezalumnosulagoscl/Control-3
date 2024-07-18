def potencia(num, exp):
    if exp == 0:
        return 1
   
    else:
        return num * potencia(num, exp - 1)

print(potencia(2, 3))  
print(potencia(5, 0))  
print(potencia(3, 4))  
print(potencia(7, 2)) 