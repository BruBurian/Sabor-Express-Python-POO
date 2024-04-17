from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Papaspizza', 'Pizzaria')
restaurante_mexicano= Restaurante('La Cucaracha', 'Mexicana')
restaurante_sushi = Restaurante('SushiBar', 'Japônes')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()

Restaurante.listar_restaurantes()
