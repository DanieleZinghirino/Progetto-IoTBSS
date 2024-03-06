#MOLTIPLICATORE 8-BIT SENZA SEGNO CON APPROSSIMAZIONE 3
import pyximport; pyximport.install()
import mul8u_197B

#   Definizione del numero di operandi
op_len = 2**8
mult_len = op_len * op_len

#   Definizione ed inizializzazione delle variabili per calcolare le metriche
wce = e = e_sq = e_count = e_rel = wce_rel = diff_rel = 0

#   Loop per eseguire tutte le moltiplicazioni
for i in range(0,op_len):
    for j in range(0,op_len):
        #   Calcolo dell'errore assoluto tra il risultato della moltiplicazione approssimata
        #   e il risultato della moltiplicazione esatta tra i due numeri i e j
        diff = abs(mul8u_197B.mul(i,j) - (i*j))

        #   Verifica se i e j sono entrambi maggiori di zero per evitare divisioni per zero
        if i > 0 and j > 0:
            #   Calcolo dell'errore relativo, normalizzato rispetto alla moltiplicazione esatta
            diff_rel = abs(mul8u_197B.mul(i,j) - (i*j))/(i*j)

        #   Aggiornamento del massimo errore assoluto    
        if diff > wce: 
            wce = diff

        #   Aggiornamento del massimo errore relativo
        if diff_rel > wce_rel: 
            wce_rel = diff_rel

        #   Aggiornamento del numero di errori
        if diff != 0: 
            e_count += 1

        #   Aggiornamento delle somme cumulative per calcolare le medie (assoluta, quadratica e relativa)
        e += diff
        e_sq += diff * diff
        e_rel += diff_rel

#   Visualizzazione a schermo dei valori delle metriche in percentuale
print('mean_absolute_error (MAE) = ', e*100/(mult_len * e_count))
print('worst-case error (WCE) = ', wce * 100/mult_len)
print('mean_squared_error (MSE) = ', e_sq /mult_len)
print('mean_relative_error (MRE) = ', e_rel * 100/mult_len)
print('error_probability (EP) = ', e_count * 100/mult_len)