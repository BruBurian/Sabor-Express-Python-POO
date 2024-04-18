from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('Papaspizza', 'Pizzaria')
restaurante_pizza.receber_avaliacao('Bruno', 10)
restaurante_pizza.receber_avaliacao('Athena', 8)
restaurante_mexicano= Restaurante('La Cucaracha', 'Mexicana')
restaurante_sushi = Restaurante('SushiBar', 'Japônes')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
