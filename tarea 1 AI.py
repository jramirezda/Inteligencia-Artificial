# %% [markdown]
# <img src="logo completo.png" width="1200" height="400">

# %% [markdown]
# Soy estudiante de la carrera de estadística. He visto las asignaturas de programación en lenguajes estadísticos, bases de datos, sistemas de información y computación estadística, entre otros conocimientos.
# 
# 
# # Funcion Vec

# %% [markdown]
# La función vec en álgebra matricial es una función que toma una matriz $m \times n$ de tal forma que nos devuelve un vector de columna de longitud $(m \times n) \times 1$, donde vamos a denotar por $A$ a la matriz y $A_{j}$ a los $m$ vectores columna que la componen y la función vec se vería de la siguiente forma:
# 
# $vec(A)=[A_{1};A_{2};\ldots;A_{m}]$
# 
# Donde $[A_{1};A_{2};\ldots;A_{m}]$ hace referencia a la concatenación vertical de vectores.

# %% [markdown]
# Para usar la función $vec$ en python podemos usar la siguiente función en python usando la libreria numpy:

# %%
import numpy as np

def vec(matriz):
    vector = matriz.flatten().reshape(-1,1)
    return vector

# %%
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = vec(matriz)
print(vector)


