# Codificador y decodificador para el codigo de bloques lineal sistemático (n,k) con n=6 y k=3
import numpy as np

matriz_P  = [[1, 0, 1], [1, 1, 1], [1, 1, 0]]
n = 6
k = 3

def codificador_k(bits_originales, matriz_P):
    matriz_G = np.concatenate((np.identity(np.shape(matriz_P)[1]),
                               np.transpose(matriz_P)), axis=1)
    return np.matmul(bits_originales, matriz_G) % 2
    
def decodificador_k(bits_recibidos, matriz_P, logs):
    matriz_H = np.concatenate((matriz_P, np.identity(np.shape(matriz_P)[1])), axis=1)
    matriz_HT = np.transpose(matriz_H)
    syndrome = np.matmul(bits_recibidos, matriz_HT) % 2

    bits_recibidos = np.array(bits_recibidos, dtype=int)

    # Encontrar el vector de error
    error = np.zeros(np.shape(matriz_HT)[0], dtype=int)
    for i in range(np.shape(matriz_HT)[0]):
        if np.array_equal(syndrome, matriz_HT[i]):
            error[i] = 1
            logs.append("Error en la posicion: "+str(i))

    if np.sum(error) != 0:
        logs.append("Palabra antes de la corrección: "+np.array2string(bits_recibidos))

    # Corregir el vector recibido
    bits_recibidos = (bits_recibidos + error) % 2

    if np.sum(error) != 0:
        logs.append("Palabra despues de la corrección: "+np.array2string(bits_recibidos))

    # Eliminar los bits de paridad
    return bits_recibidos[:np.shape(matriz_P)[1]]


def codificar_palabra(palabra, ruido = True):
    global matriz_P, k
    # Separar la palabra en bloques de k bits
    bloques = []
    for i in range(0, len(palabra), k):
        bloques.append(palabra[i:i+k])
    
    # Codificar cada bloque
    bloques_codificados = []
    for bloque in bloques:
        bloques_codificados.append(codificador_k(bloque, matriz_P))

    if ruido:
        # Numero de bits a cambiar aleatoriamente, maximo 10% de los bits
        num_bits = np.random.randint(0, round(len(palabra) * 0.1))

        for _ in range(num_bits):
            # Introducir ruido en un bit aleatorio
            i = np.random.randint(0, len(bloques_codificados))
            j = np.random.randint(0, len(bloques_codificados[i]))
            bloques_codificados[i][j] = (bloques_codificados[i][j] + 1) % 2
    
    # Concatenar los bloques codificados
    return np.concatenate(bloques_codificados)

def decodificar_palabra(palabra):
    global matriz_P, n
    logs = []

    # Separar la palabra en bloques de n bits
    bloques = []

    for i in range(0, len(palabra), n):
        bloques.append(palabra[i:i+n])
    
    # Decodificar cada bloque
    bloques_decodificados = []

    for bloque in bloques:
        bloques_decodificados.append(decodificador_k(bloque, matriz_P, logs))

    # Concatenar los bloques decodificados
    return np.concatenate(bloques_decodificados), logs



