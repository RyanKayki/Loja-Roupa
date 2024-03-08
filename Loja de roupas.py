import os

def juros_comp(juros, capital, tempo):
    taxa = juros / 100
    montante = capital * (1 + taxa) ** tempo
    return montante

while True:
    os.system('cls')  

    print("Bem vindo")
    print("(1 - dinheiro, débito ou PIX - desconto de 10%")
    print("(2 - pagamentos parcelados no cartão de crédito - 1% de juros para mês")
    print("(3 - pagamentos no carnê - 2% de juros ao mês.")

    forma = int(input("Agora, insira a forma de pagamento: "))
    valor_compra = float(input("Por favor, insira o valor a ser pago: "))
    

    if forma == 1:
        desconto = 0.10
        valor_desconto = valor_compra * desconto
        valor_final = valor_compra - valor_desconto
    elif forma == 2:
        parcelas = int(input("Agora, insira o numero de parcelas que deseja (max=12): "))
        valorparcela = juros_comp(1,valor_compra,parcelas)
        juros = valorparcela / parcelas
    elif forma == 3:
        parcelas = int(input("Agora, insira o numero de parcelas que deseja (max=12): "))
        valorparcela = juros_comp(2,valor_compra,1)
        juros = valorparcela / 1

    print("\n--- Informações de Pagamento ---")
    print(f"Valor da Compra: R$ {valor_compra:.2f}")
    if forma == 1:
        print(f"Desconto: R$ {valor_desconto:.2f}")
    elif forma == 2 or forma == 3:
        print(f"Juros: R$ {juros:.2f}")
    print(f"Valor a ser pago: R$ {valorparcela:.2f}")

    again = input("\nDeseja fazer outro cálculo? (s/n): ")
    if again.upper() != 'S':
        break
