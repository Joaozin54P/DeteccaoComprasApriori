# Sistema de Detecção de Compras Fora do Normal com ideia do Apriori

print("=" * 60)
print("SISTEMA DE DETECÇÃO DE COMPRAS SUSPEITAS")
print("=" * 60)

nome = input("Digite seu nome: ")

# Limites por categoria
limite_passagens = 5
limite_mercado = 10
limite_salgados = 120

# Padrões frequentes inspirados no algoritmo Apriori
padroes_apriori = {
    "passagens": ["Primeira Classe", "Classe Executiva"],
    "mercado": ["M&M", "Sucrilhos", "Coca-Cola"],
    "salgados": ["Coxinha", "Pastel", "Refrigerante"]
}

while True:
    print(f"\nBem-vindo(a), {nome}!")
    print("\nO que deseja comprar?")
    print("1 - Passagens de avião")
    print("2 - Itens de mercado")
    print("3 - Salgados")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # PASSAGENS
    if opcao == "1":
        categoria = "passagens"

        print("\n===== PASSAGENS DISPONÍVEIS =====")
        print("1 - Classe Econômica ........ R$ 800,00")
        print("2 - Classe Executiva ........ R$ 2.500,00")
        print("3 - Primeira Classe ......... R$ 5.000,00")

        escolha = input("\nEscolha uma passagem: ")
        quantidade = int(input("Digite a quantidade de passagens: "))

        if escolha == "1":
            produto = "Classe Econômica"
            preco = 800
        elif escolha == "2":
            produto = "Classe Executiva"
            preco = 2500
        elif escolha == "3":
            produto = "Primeira Classe"
            preco = 5000
        else:
            print("Opção inválida!")
            continue

        limite = limite_passagens

    # MERCADO
    elif opcao == "2":
        categoria = "mercado"

        print("\n===== ITENS DE MERCADO =====")
        print("1 - M&M ............... R$ 12,00")
        print("2 - Sucrilhos ......... R$ 18,00")
        print("3 - Nutella ........... R$ 35,00")
        print("4 - Coca-Cola ......... R$ 10,00")
        print("5 - Doritos ........... R$ 14,00")

        escolha = input("\nEscolha um item: ")
        quantidade = int(input("Digite a quantidade: "))

        if escolha == "1":
            produto = "M&M"
            preco = 12
        elif escolha == "2":
            produto = "Sucrilhos"
            preco = 18
        elif escolha == "3":
            produto = "Nutella"
            preco = 35
        elif escolha == "4":
            produto = "Coca-Cola"
            preco = 10
        elif escolha == "5":
            produto = "Doritos"
            preco = 14
        else:
            print("Opção inválida!")
            continue

        limite = limite_mercado

    # SALGADOS
    elif opcao == "3":
        categoria = "salgados"

        print("\n===== SALGADOS DISPONÍVEIS =====")
        print("1 - Coxinha ........... R$ 8,00")
        print("2 - Pastel ............ R$ 10,00")
        print("3 - Esfiha ............ R$ 7,00")
        print("4 - Enroladinho ....... R$ 6,00")
        print("5 - Refrigerante ...... R$ 9,00")

        escolha = input("\nEscolha um salgado/item: ")
        quantidade = int(input("Digite a quantidade: "))

        if escolha == "1":
            produto = "Coxinha"
            preco = 8
        elif escolha == "2":
            produto = "Pastel"
            preco = 10
        elif escolha == "3":
            produto = "Esfiha"
            preco = 7
        elif escolha == "4":
            produto = "Enroladinho"
            preco = 6
        elif escolha == "5":
            produto = "Refrigerante"
            preco = 9
        else:
            print("Opção inválida!")
            continue

        limite = limite_salgados

    elif opcao == "4":
        print(f"\nSistema encerrado. Obrigado, {nome}!")
        break

    else:
        print("\nOpção inválida!")
        continue

    total = quantidade * preco

    # Análise Apriori
    if produto in padroes_apriori[categoria]:
        padrao = "Produto dentro dos padrões frequentes de compra."
    else:
        padrao = "Produto fora dos padrões mais frequentes de compra."

    print("\n" + "=" * 60)
    print("RESUMO DA COMPRA")
    print("=" * 60)
    print(f"Cliente: {nome}")
    print(f"Categoria: {categoria}")
    print(f"Produto escolhido: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário: R$ {preco:.2f}")
    print(f"Valor total: R$ {total:.2f}")

    print("\nANÁLISE APRIORI:")
    print(padrao)

    print("\nANÁLISE DE QUANTIDADE:")
    if quantidade > limite:
        print("🚨 ALERTA!")
        print("Compra fora do normal detectada.")
        print(f"Limite permitido para essa categoria: {limite}")
        print("Compra encaminhada para análise.")
    else:
        print("✅ Compra dentro do limite permitido.")

    print("=" * 60)