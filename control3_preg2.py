def es_binario(var):
    if var == "":
        return True
    elif var[0] != '0' and var[0] != '1':
        return False
    else:
        return es_binario(var[1:])


print(es_binario("101010")) 
print(es_binario("12345"))  
print(es_binario("001100")) 
print(es_binario("abc"))  
