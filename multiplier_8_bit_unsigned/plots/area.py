import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [709.6, 637.8, 542.5, 395.6, 239.3, 110.8]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('Area in µm²')

# Aggiunta di un titolo al grafico
plt.title("Andamento dell'area occupata - moltiplicatore senza segno a 8-bit")

# Visualizzazione del grafico
plt.show()
