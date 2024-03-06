import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [0, 0.017, 0.18, 0.66, 2.41, 8.21]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('WCE in percentuale')

# Aggiunta di un titolo al grafico
plt.title("Andamento del WCE - moltiplicatore senza segno a 8-bit")

# Visualizzazione del grafico
plt.show()
