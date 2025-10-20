Ejercicio 1 (1 punto) Tiempo estimado: 10 minutos.  
Teoría: Que es la recursividad. Que elementos se deben cumplir para que un algoritmo recursivo sea correcto.
Práctica: Escribe una función recursiva que devuelva la suma del valor absoluto de una lista de números. Escribe un código de prueba con una llamada a la función.
 
Ejercicio 3 (1,5 puntos): 15 minutos. 
Teoría: Compara el comportamiento de los siguientes métodos. Indica en que casos se usan y cual es su complejidad temporal. 
1.	Búsqueda secuencial.
2.	Búsqueda binaria.
Práctica: Escribe el código de al menos uno de ellos.
 
Ejercicio  ( 2,5 puntos): 20 minutos. Análisis de ventas de libros con listas y diccionarios
Descripción:
En este ejercicio, deberás demostrar tu comprensión de las estructuras de datos en Python, específicamente listas y diccionarios. Se te proporcionará una lista de libros con su número de ventas. Tu tarea será consultar las ventas de un libro específico y determinar cuál ha sido el libro más vendido.
Enunciado:
Dada la siguiente lista de diccionarios, donde cada diccionario representa un libro y su número de ventas:
ventas = [
    {"titulo": "Cien años de soledad", "ventas": 120},
    {"titulo": "Don Quijote de la Mancha", "ventas": 150},
    {"titulo": "La sombra del viento", "ventas": 95},
    {"titulo": "El principito", "ventas": 180}
]
Parte Teórica:
1. Explica brevemente las diferencias entre una lista y un diccionario en Python.
2. ¿Cuándo es más apropiado usar una lista y cuándo un diccionario? Justifica tu respuesta en función del tipo de acceso, la estructura de los datos y la eficiencia.
Parte Práctica:
Escribe una función consultar_ventas(ventas): que reciba la lista de libros y retorne el libro más vendido con sus ventas.
resultado = libro_mas_vendido(ventas)
print(resultado)
# {'titulo': 'El principito', 'ventas': 180}




 
Ejercicio 4: (3,5 puntos) Gestión de atletas en una competición
Se desea desarrollar un sistema básico para gestionar la participación de atletas en una competición deportiva.
Para ello, se propone modelar dos clases:
•	Atleta: representa a un deportista que participa en la competición.
•	Competición: representa el evento deportivo que agrupa a varios atletas.
La relación entre las clases debe ser de agregación, ya que la competición incluye atletas, pero estos pueden existir independientemente de la competición.
Requisitos:
1.	La clase Atleta debe tener al menos los siguientes atributos:
o	nombre (cadena de texto)
o	pais (cadena de texto)
o	edad (entero)
o	disciplina (cadena de texto, por ejemplo: 100m, salto largo, natación)
2.	La clase Competición debe tener:
o	Una lista de atletas
o	Métodos para: 
	Agregar un atleta a la competición
	Eliminar un atleta por nombre
	Mostrar todos los atletas inscritos
	Buscar atletas por disciplina
3.	Implementa un pequeño programa que:
o	Cree varios atletas
o	Los agregue a una competición
o	Realice algunas operaciones como búsqueda y eliminación
o	Muestre la lista final de participantes
