#Que es la recursividad. Que elementos se deben cumplir para que un algoritmo recursivo sea correcto.
#Escribe una función recursiva que devuelva la suma del valor absoluto de una lista de números. Escribe un código de prueba con una llamada a la función.

def suma_valor_absoluto(lista, i=0):
    # Caso base: si ya recorrimos toda la lista
    if i == len(lista):
        return 0
    else:
        return abs(lista[i]) + suma_valor_absoluto(lista, i + 1)

# --- Código de prueba ---
numeros = [-3, 5, -2, 7, -1]
resultado = suma_valor_absoluto(numeros)
print(f"La suma del valor absoluto de {numeros} es {resultado}")


