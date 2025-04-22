#Punto 4
def maxsum(list_num: list):
    consecutive_sum = [list_num[i]+list_num[i-1] for i in range(1,len(list_num))] #Sumo un numero de la lista con el anterior, por eso se comienza con indice 1 
    return print(max(consecutive_sum)) #Se usa la funcion max para obtener el mayor de los resultados 
