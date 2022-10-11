from operator import index


times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')

print(f"Lista de times do Brasileirão (2018): {times}")

print(f"\nOs 5 primeiros são: {times[:5]}")

print(f"\nOs 4 últimos são: {times[-4:]}")

print(f"\nTimes em ordem alfabética: {sorted(times)}")

print(f"\nO Chapecoense está na {times.index('Chapecoense') + 1}° posição")