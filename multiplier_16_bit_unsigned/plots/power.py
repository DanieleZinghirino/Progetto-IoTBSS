import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [2.202, 2.106, 1.648, 0.791, 0.401, 0.101]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('Potenza in mW')

# Aggiunta di un titolo al grafico
plt.title("Andamento del consumo di potenza - moltiplicatore senza segno a 16-bit")

# Visualizzazione del grafico
plt.show()
