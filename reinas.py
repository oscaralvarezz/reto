# numero de reinas (backtracking)
n = 6
contador = 0 # el contador controlará si encontramos una solucion
columna = [False]*n
'''las diagonales ayudan para saber si las reinas
comparten diagonales y por ende se amenazan'''
diagonal_derecha = [False]*(n*2)
diagonal_izquierda = [False]*(n*2)

solucion = []


def backtrack(y,n,contador):
    if (y==n):
        return contador + 1

    for x in range(n):
        global columna
        global diagonal_derecha
        global diagonal_izquierda

        if(columna[x] or diagonal_izquierda[x+y] or diagonal_derecha[x-y+n-1]):
            continue
         #colocamos a la reina
        columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = True
        solucion.append((x,y))

        contador = backtrack(y+1,n,contador) # la enviamos la fila siguiente

        #ya encontró una solución, si quitamos esto encuentraría todas
        if contador!=0:
            return contador

        columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = False
        solucion.pop(-1)
    return contador
    #en el paso anterior quitamos la reina para probar otras posibles opciones.

solucion_encontrada = backtrack(0,n,contador) #modifcamos la solucion para entregarla según especificaciones
solucion_problema = [ pos[1] for pos in sorted(solucion, key=lambda x: x[0])]

print(solucion_problema)
