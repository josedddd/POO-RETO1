# POO-RETO1
Este es el reto 1:
En este read-me colocare como pense la solucion de cada punto, igual cada codigo esta documentado
***
# Primer punto: 
Pensé en hacer simplemente un if y dependiendo del operador (el string), hacer tal operación (suma, resta multiplicacion, division), pero como nunca había utilizado match-case, quería utilizarlo.
***
# Segundo punto: 
Con este punto lo importante es como recorrer la palabra al revez. Para esto pensé que con un for, pero con en rango decreciente, comenzando en el último carácter de la palabra (usando el length de la palabra - 1), puedo recorrer la palabra al revés, y luego es simplemente comparar ambas. Lo anterior lo hago usando listas y list comprehension
***
# Tercer punto: 
Un número primo es un número que solo es divisible por sí mismo y por 1. Entonces, mi idea fue usar el operador divisor resto y guardar todos los restos como una lista. Por lo tanto, si en la lista algún resto da 0, significa que el número no es primo. Para eso uso la función all(), que devuelve True si todos los elementos en un iterable son True, y en Python, 0 es False y los demás números son True, así que esa función es perfecta para esto.
***
# Cuarto punto: 
Con este punto pensé en un for, que comenzara en el segundo elemento de la lista de números y que fuera sumando ese número con el anterior y pusiera esto en una lista nueva, y luego ver cuál suma es la mayor con la función max().
***
# Quinto punto
Con este punto use dos for aninados, uno para que recorriera cada palabra en la lista, y el otro para que comparara la longitud de esa palabra con la longitud de las otras palabras en la lista. Tambien creo otra lista nueva y uso .append para añadir las palabras que tengan las misma longitud. 
