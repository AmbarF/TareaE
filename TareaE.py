import numpy as np
import matplotlib.pyplot as plt

def generar_num (distibucion="uniforme", tipo="continuo", n=10):
  if distribucion =="uniforme":
    if tipo =="discreto":
       return np.random.randint (1,10, size=n)
    else:
      return np.random.uniform (0,1, size=n)
  elif distribucion == "exponencial":
      return np.random.exponential (scale=1, size=n)

k= [2,10,25]
distribucion="uniforme"
tipo="continuo"

plt.figure(figsize=(10,6))
for n in k:
  suma_val= np.sum([generar_num(distribucion,tipo, n) for _ in range(10000)], axis=1)
  plt.hist(suma_val, bins=30, alpha=0.7, label=f"n{n}", color='purple', edgecolor='black')

plt.xlabel("Suma de valores")
plt.ylabel("Frecuencia")
plt.title("Histograma")
plt.legend()
plt.show()
