#Punto 1
# Por cada operacion se hace con un match y un case, y se asigna el resultado la correspondiente operacion
def operations(num1: float, num2: float, op: str): 
    match op:
        case "+":               #Caso de la suma
            result = num1+num2  
        case "-":               #Caso de la resta
            result = num1-num2
        case "*":               #Caso de la multiplicacion
            result = num1*num2
        case "/":               #Caso de la division
            result = num1/num2
    return print(result) 


    
    
