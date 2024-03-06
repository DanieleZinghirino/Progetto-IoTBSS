import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [3203.0, 2992.3, 2404.2, 1284.9, 642.0, 244.0]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('Area in µm²')

# Aggiunta di un titolo al grafico
plt.title("Andamento dell'area occupata - moltiplicatore senza segno a 16-bit")

# Visualizzazione del grafico
plt.show()
