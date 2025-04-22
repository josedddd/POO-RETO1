#Punto 5
def equal(list_word: list):
    list_equal_length = []
    # Recorro la lista de palabras
    for i in range(0,len(list_word)):
        for j in range(i+1,len(list_word)):
        # Compruebo si las palabras tienen la misma longitud
            if len(list_word[i])==len(list_word[j]):
                # Si aún no están en la lista, las agrego
                if list_word[i] not in  list_equal_length:
                    list_equal_length.append(list_word[i])
                if list_word[j] not in list_equal_length:
                    list_equal_length.append(list_word[j])
    return print(list_equal_length)
