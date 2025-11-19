# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Mirassol.

brasileirao_2025 = (
    "Atlético Mineiro",
    "Bahia",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Grêmio",
    "Internacional",
    "Juventude",
    "Mirassol",
    "Palmeiras",
    "Red Bull Bragantino",
    "Santos",
    "São Paulo",
    "Sport",
    "Vasco da Gama",
    "Vitória"
)

print(brasileirao_2025)
print(f'Os 5 primeiros são {brasileirao_2025[0:5]}')
print(f'Os 4 últimos são {brasileirao_2025[-4:]}')
print(f'Times em ordem alfabética {sorted(brasileirao_2025)}')
print(f'O Mirassol esta na{brasileirao_2025.index("Mirassol") + 1} posição')
