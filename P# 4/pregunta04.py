# Importar las bibliotecas necesarias
import multiprocessing

# NOMBRE: VICTOR GABRIEL CAPIA ALI
# CI: 4762494 LP
# PREGUNTA 4
# Con multiprocesing genera la siguiente serie 2, 2, 5, 4, 10, 6, 17,… (10000 posiciones sin restricción de procesador).

def calcular_valor(posicion):
    if posicion % 2 == 1:
        # Números impares
        return (posicion // 2 + 1) * (posicion // 2 + 1) + 1
    else:
        # Números pares
        return (posicion // 2) * 2

if __name__ == '__main__':
    num_posiciones = 10000
    
    # Creamos un grupo de procesos
    pool = multiprocessing.Pool()

    # Generamos la serie en paralelo
    serie = pool.map(calcular_valor, range(1, num_posiciones + 1))

    # Cerramos el grupo de procesos
    pool.close()
    pool.join()

    print(serie)