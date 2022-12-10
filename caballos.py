# hacemos el mapa de posibles pasos empezando por cada número
NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
    # el 5 no tiene camino. 
}
def neighbors(position):
    # devuelve cada número y a donde puede llegar
    return NEIGHBORS_MAP[position]

def yield_sequences(starting_position, num_hops, sequence=None):
    if sequence is None:
        # se inicia la secuencia
        sequence = [starting_position]
        # cuando la función recursiva llega a numero de pasos = 0 devuelve la secuencia acumulada
   
    if num_hops == 0:
        yield sequence
        #return hace que salga definitivamente
        return

    '''para la posición en la que inicia devuelve los números a  los que puede llegar y para cada número se ejecuta  de nuevo
     la función recursiva. Para saber a cuáles puede llegar es necesario disminuir el número de pasos para terminar la función
     y cada número al que es posible llegar'''
    for neighbor in neighbors(starting_position):
        yield from yield_sequences(
            neighbor, num_hops - 1, sequence + [neighbor])


def count_sequences(num_hops):
    num_sequences = 0
    '''para cada posible numero de inicio se busca cuantos movimientos
     son posibles de realizar.'''
     
    '''finalmente se cuentan los movimientos por número'''
    for posible_start_number in [1,2,3,4,5,6,7,8,9,0]:
        for sequence in yield_sequences(posible_start_number, num_hops):
            num_sequences += 1
    return num_sequences


#completamos la tabla
for n_hop in [1,2,3,5,8,10,15,18,21,23,32]:
    pos_val = count_sequences(num_hops=n_hop)
    print('Número de movimientos: {} --> posibilidades válidas: {}'.format(n_hop, pos_val))
    
