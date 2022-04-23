def gen_board(size, initial_val=None):
    return[[initial_val for x in range(size)] for y in range(size)]


chickens = [
    {"name": 'Henry', "sex": 'rooster'},
    {"name": 'lady Grey', "sex": 'Hen'}
]

hens = [bird["name"] for bird in chickens if bird["sex"]=='Hen' ]
