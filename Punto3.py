#Punto 3
def prime(list_num: list):  
       for num in list_num:  #Recorro la lista de numeros 
              remainders = [num % i for i in range(2, num)] #Con list comprehension, divido ese numero por todos los numeros enteros comenzando en dos
              if all(remainders):  #Si todos los restos son diferentes de cero, el numero es primo y lo imprimo
                     print(f"{num}")

