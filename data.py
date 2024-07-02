import csv
import random
from datetime import datetime, timedelta

# Função para gerar dados aleatórios de vendas da padaria
def generate_data(num_rows):
    # Lista de produtos fictícios
    produtos = [
        "Pão Francês", "Bolo de Chocolate", "Croissant", "Pão de Queijo", 
        "Pão Integral", "Baguete", "Torta de Frango", "Rosquinha", "Suco", 
        "Pão de Mel", "Bolo Mole", "Salgado", "Pão na Chapa", 
        "Café Filtrado 150 ml", "Café Pingado 150 ml", "Café Espresso 50 ml"
    ]

    # Lista de modos de pagamento
    modos_pagamento = ["pix", "credito", "debito"]

    # Definir horário de abertura e fechamento da padaria
    hora_abertura = 8
    hora_fechamento = 17

    # Data inicial e final para geração de timestamps
    d1 = datetime.strptime('2024-01-08', '%Y-%m-%d')
    d2 = datetime.strptime('2024-06-25', '%Y-%m-%d')

    # Abrir arquivo CSV para escrita
    with open('dados_padaria.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escrever cabeçalho
        writer.writerow(['id_vendas', 'data', 'produto', 'quantidade', 'modo_pagamento'])

        for i in range(1, num_rows + 1):
            # Gerar data e horário aleatório dentro do horário de funcionamento
            random_date = d1 + (d2 - d1) * random.random()
            timestamp = datetime.combine(random_date.date(), datetime.min.time()) + timedelta(hours=random.randint(hora_abertura, hora_fechamento - 1), minutes=random.randint(0, 59))

            # Selecionar produto aleatoriamente
            produto = random.choice(produtos)

            # Gerar quantidade aleatória
            quantidade = random.randint(1, 5)

            # Selecionar modo de pagamento aleatoriamente
            modo_pagamento = random.choice(modos_pagamento)

            # Escrever linha no CSV
            writer.writerow([i, timestamp.strftime('%d-%m-%Y %H:%M:%S'), produto, quantidade, modo_pagamento])

            if i % 10000 == 0:
                print(f'Gerados {i} de {num_rows} registros.')

    print(f'Arquivo CSV gerado com sucesso: dados_padaria.csv')

# Chamar função para gerar 220.000 linhas
generate_data(220000)
