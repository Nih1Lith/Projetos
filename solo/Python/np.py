import numpy as np
notas = np.array([4.7, 6.5, 3.2, 6.7, 7, 9])
for i in notas:
    if(i > 5):
        print("Aprovado", i)
    else:
        print("Recuperação", i)