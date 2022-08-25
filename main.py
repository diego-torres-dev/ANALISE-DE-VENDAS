# Lista com os meses do ano
meses = ["jan", "fev", "mar", "abr", "mai", "jun",
         "jul", "ago", "set", "out", "nov", "dez"]


# Lista com as vendas do 1º semestre do ano
vendas1sem = [20000, 25000, 30000, 10000, 12000, 24000]

# Lista com as vendas do 2º semestre do ano
vendas2sem = [31000, 20000, 23000, 22500, 13200, 34000]

# Concatena as duas listas
vendas_ano = vendas1sem + vendas2sem

# Vendas do melhor mes
vendas_melhor_mes = max(vendas_ano)

# Vendas do pior mês
vendas_pior_mes = min(vendas_ano)

# Total de vendas do ano
total = sum(vendas_ano)

# Índice do melhor mês
i = vendas_ano.index(vendas_melhor_mes)

# Índice do pior mês
j = vendas_ano.index(vendas_pior_mes)

# Percentual das vendas do melhor mês
vendas_melhor_mes_percentual = vendas_melhor_mes / total

# Exibição de resultados
print(
    f"O melhor mês foi {meses[i]}, com {vendas_melhor_mes} unidades vendidas.")
print(f"O pior mês foi {meses[j]}, com {vendas_pior_mes} unidades vendidas.")
print(f"O total de vendas do ano foi de {total} unidades.")
print("O melhor mês representou {:.2%} das vendas do ano.".format(
    vendas_melhor_mes_percentual))
