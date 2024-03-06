import matplotlib.pyplot as plt

# Dati 
x = list(range(0, 6))
y = [0.391, 0.370, 0.302, 0.206, 0.104, 0.034]  

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di etichette agli assi
plt.xlabel('Approssimazione')
plt.ylabel('Potenza in mW')

# Aggiunta di un titolo al grafico
plt.title("Andamento del consumo di potenza - moltiplicatore senza segno a 8-bit")

# Visualizzazione del grafico
plt.show()
