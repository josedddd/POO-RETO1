# POO-RETO1
Este es el reto 1:
En este read-me colocare como pense la solucion de cada punto, igual cada codigo esta documentado
***
Primer punto:
Es simplemente un if y dependiendo del operador (el string) hace tal operacion, pero como nunca habia utilizado match case, queria utilizarlo
***

Segundo punto:
Con este punto, hago que la palabra se convierta en una lista de caracteres, y pense que con un for pero en rango decreciente (comenzando en el utimo caracter de la lista) puedo recorer la palabra al revez, y luego puedo comparar ambas listas. 

***
Tercer punto:
Un numero primo, es un numero que solo es divisible por si mismo y por 1, entonces mi idea fue usar el operador divisor resto, y guardar todos los restos como una lista. Entonces si en la lista algun resto da 0, significa que el numero no es primo. Para eso uso la funcion all, esta devuelve True si todos los elementos en un iterable son True, y en python 0 es false y los demas numeros son True, asi que esa funcion es perfecta para esto. 

***
