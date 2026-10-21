import numpy as np 

califas=np.array([60,70,90])
print(" ----------------------- Ej: 1 Imprimir califas ----------------------- ")
print(califas) # Imprime la lista de califas
print(type(califas)) # Muestra el timpo de arreglo
print(" ----------------------- Ej: 0 Dimensiones de un Array ----------------------- ")
califas=np.array(60)
print(califas)
print("Dimension :", califas.ndim)  
print(" ----------------------- Ej: 1 Dimensión de un Array ----------------------- ")
califas=np.array([60,70,90])
print(califas)
print("Dimension :", califas.ndim) 
print(" ----------------------- Ej: 2 Dimensiones de un Array ----------------------- ")
califas=np.array([
    [60,70,90],
    [50,80,98]
    ]) # Un arreglo de 2 dimensiones es como una tabla en excel
print(califas)
print("Dimension :", califas.ndim) 