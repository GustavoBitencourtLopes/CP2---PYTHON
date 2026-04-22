def valor_hora_extra(salario, horas_extras):
    valor_hora_extra = (salario / 100 * 1.5) * horas_extras

    return valor_hora_extra    


def desconto_falta(faltas,salario):
    desconto_falta = (salario / 100 * 2) * faltas

    return desconto_falta

def calcular_bonus(cargo, consulta_bonus):
    if consulta_bonus.lower() == "sim":
        if cargo == "gerente":
            bonus = 1000
        
        elif cargo == "analista":
            bonus = 500

        elif cargo == "assistente":
            bonus = 300

        elif cargo == "estagiario":
            bonus = 100    

        else:
            bonus = 0

    else:
        bonus = 0

    return bonus         

def salario_bruto(salario, calcular_bonus, valor_hora_extra):
    salario_bruto = salario + valor_hora_extra + calcular_bonus
    return salario_bruto

def total_acrescimos(consulta_bonus, valor_hora_extra):
    total_acrescimos = consulta_bonus + valor_hora_extra
    return total_acrescimos

def salario_final(salario_bruto,desconto_falta):
    salario_final = salario_bruto - desconto_falta
    return salario_final


nome = input('Digite o seu nome ')
cargo = input('Digite seu cargo (Gerente, Analista, Assistente, Estagiário) ').lower()
salario = float(input('Digite seu salário '))
horas_extras = float(input('Digite quantas horas extras você trabalhou ' ))
faltas = int(input('Digite quantas faltas você teve ' ))
consulta_bonus = input('Recebeu bônus ? (Sim ou Não) ' )

valor_extra = valor_hora_extra(salario, horas_extras)
desconto = desconto_falta(faltas,salario)
bonus = calcular_bonus(cargo, consulta_bonus)
bruto = salario_bruto(salario, bonus, valor_extra)
acrescimos = total_acrescimos(bonus, valor_extra)
final = salario_final(bruto, desconto)

print("\n--- RESUMO DO SALÁRIO ---")
print(f'Salário bruto: R$ {bruto:.2f}')
print(f'Total de acréscimos (horas extras + bônus): R$ {acrescimos:.2f}')
print(f'Total de descontos (faltas): R$ {desconto:.2f}')
print(f'Salário final: R$ {final:.2f}')