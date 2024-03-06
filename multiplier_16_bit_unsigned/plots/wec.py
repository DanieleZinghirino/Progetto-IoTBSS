import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [0, 0.0000027, 0.00042, 0.058, 0.063, 7.03]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('WCE in percentuale')

# Aggiunta di un titolo al grafico
plt.title("Andamento del WCE - moltiplicatore senza segno a 16-bit")

# Visualizzazione del grafico
plt.show()
