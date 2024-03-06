import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [0,75,97.72,98.37,98.99,99.16]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('Probabilità di errore in percentuale')

# Aggiunta di un titolo al grafico
plt.title("Andamento della probabilità di errore - moltiplicatore senza segno a 8-bit")

# Visualizzazione del grafico
plt.show()
