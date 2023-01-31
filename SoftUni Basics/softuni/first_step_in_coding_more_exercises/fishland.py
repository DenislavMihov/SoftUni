skumria_na_kilo = float(input())
caca_na_kilo = float(input())
kilograma_palamud = float(input())
kilograma_safrid = float(input())
kilograma_midi = int(input())

price_per_kilo_palamud = skumria_na_kilo * 1.6
price_per_kilo_safrid = caca_na_kilo * 1.8
MIDI = 7.50
cost_of_palamud = kilograma_palamud * price_per_kilo_palamud
cost_of_safrid = kilograma_safrid * price_per_kilo_safrid
cost_of_midi = kilograma_midi * MIDI

cost_total = cost_of_palamud + cost_of_safrid + cost_of_midi
print(f"{cost_total:.2f}")
