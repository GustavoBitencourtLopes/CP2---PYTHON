def pode_aprovar(idade, renda, valor):
    if idade < 18:
        return False, "Menor de 18 anos"
    if valor > renda * 20:
        return False, "Valor acima de 20x a renda"
    return True, ""


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))
valor = float(input("Digite o valor do empréstimo: "))
parcelas = int(input("Digite o número de parcelas (3 a 24): "))

aprovado, motivo = pode_aprovar(idade, renda, valor)

if not aprovado:
    print(f"Status: Negado - {motivo}")
else:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)
    
    print("Status: Aprovado")
    print(f"Nome: {nome}")
    print(f"Valor financiado: {valor:.2f}")
    print(f"Taxa de juros aplicada: {taxa*100:.0f}%")
    print(f"Valor da parcela: {parcela:.2f}")
    print(f"Valor total pago: {total:.2f}")
    print(f"Total de juros: {juros:.2f}")