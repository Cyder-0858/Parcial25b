#Que es la recursividad. Que elementos se deben cumplir para que un algoritmo recursivo sea correcto.
#Escribe una función recursiva que devuelva la suma del valor absoluto de una lista de números. Escribe un código de prueba con una llamada a la función.

numeros = [0,1,2,3,4,5,6,7,8,9]

def suma_va(lista, i=0):
    if i == len(lista):
        return 0
    else:
        resultado = (lista[i]**2)**0.5 + suma_va(lista, i + 1)
        return resultado

prueba1 = suma_va(numeros)
print(prueba1)


