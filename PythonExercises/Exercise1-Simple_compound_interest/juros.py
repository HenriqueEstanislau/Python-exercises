print("--------------------------------")
print("Programa para o calculo de juros")
print("--------------------------------")

def imprimirMensagem():
    print(" - Digite (1) para calcular juros simples")
    print(" - Digite (2) para calcular juros compostos")
    print(" - Digite (0) para sair do programa")

imprimirMensagem()
resp = int(input(">>> "))

while resp != 0:
    if resp == 1:
        print("\nJuros simples\n")
        capital = float(input("Digite o capital: "))
        taxaJuros = float(input("Digite a taxa de juros em meses: "))
        tempo = int(input("Digite o tempo em meses: "))
        taxaJuros /= 100 
        montante = capital*(1+taxaJuros*tempo)
        juros = montante - capital
        print(f'\nO rendimento no final do periodo será R$ {montante:.2f}')
        print(f'Juros final: R$ {juros:.2f}')
        print("\n")
        imprimirMensagem()
        resp = int(input(">>> "))
        
    elif resp == 2:
        print("Juros compostos\n")
        capital = float(input("Digite o capital: "))
        taxaJuros = float(input("Digite a taxa de juros em meses: "))
        tempo = int(input("Digite o tempo em meses: "))
        taxaJuros /= 100 
        montante = capital*(1+taxaJuros)**tempo
        juros = montante - capital
        print(f'\nO rendimento no final do periodo será R$ {montante:.2f}')
        print(f'Juros final: R$ {juros:.2f}')
        
        print("\n")
        imprimirMensagem()
        resp = int(input(">>> "))
    else:
        print("\nResposta inválida\n")
        imprimirMensagem()
        resp = int(input(">>> "))
print("\nFIM DO PROGRAMA")
