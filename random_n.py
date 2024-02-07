#script para crear archivo con números random 
# creado con la inteligencia artificial chat gpt 
#pregunta: Crea un archivo de texto con 3000 números aleatorios enteros entre 0 y 10000.

import random
def generate_random_numbers(random_n, count):
    with open(random_n, 'w') as file:
        for _ in range(count):
            file.write(str(random.randint(0, 10000)) + '\n')

generate_random_numbers('random_numbers.txt', 3000)
