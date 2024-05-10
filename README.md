# Juan De Leon Garcia
## Explicación del algoritmo del Ejercicio de Recursividad: Cálculo del Factorial.
### El algoritmo utiliza una función llamada factorial(n) para calcular el factorial de un número entero n. Esta función se define de manera recursiva, lo que significa que se llama a sí misma dentro de su propia definición.
### El caso base de la recursión se establece para n = 0. Si n es 0, el factorial es 1, por lo que la función devuelve 1.
### En el caso recursivo, si n es mayor que 0, la función calcula n * factorial(n-1). Esto significa que multiplica n por el factorial del número n-1. Este proceso se repite recursivamente hasta que n alcanza el caso base (0), momento en el que la recursión se detiene.
### La función main simplemente imprime el resultado del factorial de 5 para verificar que el programa funciona correctamente. En este caso, el resultado impreso será "The factorial of 5 is: 120", lo que indica que el cálculo del factorial de 5 se realizó correctamente utilizando la función factorial.



## Bubble Sort 
### El método Bubble Sort es un algoritmo de ordenación simple. Este algoritmo funciona recorriendo repetidamente la lista de elementos que se desean ordenar, comparando elementos adyacentes y realizando intercambios si están en el orden incorrecto. Se suele utilizar para ordenar listas pequeñas o como ejercicio didáctico para entender los conceptos básicos de los algoritmos de ordenación.
### El funcionamiento del Bubble Sort se puede resumir en los siguientes pasos:
### Primero. Comienza comparando el primer elemento con el segundo. Si el primer elemento es mayor que el segundo, los intercambia. Luego, compara el segundo elemento con el tercero, y así sucesivamente, hasta llegar al final de la lista.
### Segundo. Este proceso se repite para cada elemento de la lista, recorriendo la lista múltiples veces hasta que ningún intercambio adicional sea necesario.
### Tercero. El algoritmo continúa pasada tras pasada hasta que la lista esté completamente ordenada.
### Para ilustrar cómo funciona el Bubble Sort, consideremos el siguiente ejemplo conceptual con la lista de números [34, 7, 23, 32, 5]: Primero comparamos 34 y 7. Como 34 es mayor que 7, los intercambiamos: [7, 34, 23, 32, 5]. Luego comparamos 34 y 23. No se requiere intercambio. Despues comparamos 34 y 32. No se requiere intercambio.Por ultimo, comparamos 34 y 5. Intercambiamos: [7, 23, 32, 5, 34].
### Después de la primera pasada, el elemento más grande (34) está en su posición final. Repetimos este proceso para los elementos restantes hasta que la lista esté completamente ordenada. En este ejemplo, se requerirían varias pasadas adicionales para ordenar completamente la lista.