class Tomate:
    def __init__(self, color, sabor):# tomate recebe cor e sabor e nao tem metodos
        self.color = color
        self.sabor = sabor
def salva_lista_tomate(lista:list):

    with open('tomates.txt', 'w') as file:
        for tomate in lista:
            file.write(f'Color: {tomate.color}, Sabor: {tomate.sabor}\n')

def carrega_lista_tomate():
    with open('tomates.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(', ')
        color = data[0].split(': ')[1]
        sabor = data[1].split(': ')[1]
        tomate = Tomate(color, sabor)
        list_tomate.append(tomate)

    for tomate in list_tomate:
        print(f'Color: {tomate.color}, Sabor: {tomate.sabor}')


tomate1 = Tomate('verde', 'dulce')
tomate2 = Tomate('rojo', 'agrio')
list_tomate = [tomate1, tomate2]

salva_lista_tomate(list_tomate)