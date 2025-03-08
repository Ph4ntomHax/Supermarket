print()

print(f'{" LOJAS GUANABARA ":=^40}')
compra = float(input("Qual o valor das compras: "))

print()

print("Escolha a forma de pagamento: ")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista no cartão")
print("[ 3 ] em até 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
forma = int(input("Opção de pagamento: "))

print()

if forma == 1:
    valor = compra * 0.1
    print(f"O valor final será de {(compra - valor):.2f}R$")

elif forma == 2:
    valor = compra * 0.05
    print(f"O valor final será de {(compra - valor):.2f}R$")

elif forma == 3:
    parcelas = compra / 2
    print(f"O valor final será 2 parcelas de {(compra / 2):.2f}R$")

elif forma == 4:
    parcelas = int(input("Quantidade de parcelas: "))
    if parcelas <= 2:
        print("Volte e selecione a opção 3!")
        exit()
    else:
        valorfim = (compra / parcelas) * 1.20
        total = compra * 1.20
        print(f"O valor final das {parcelas} parcelas será {valorfim:.2f}R$")
        print(f"O preço total será de {total:.2f}R$ devido a juros")

print()

confirmar = int(input("Caso queira confirmar digite 0 caso contrario digite enter: "))

print()

if confirmar == 0:
    while True:
        senha = int(input("Digite a senha do cartão: "))
        if senha > 999 and senha < 10000:
            print()
            print("Compra finalizada, Obrigado pela preferencia")
            print()
            break
        else:
            print("Tente novamente!")
            print()
else:
    exit()