x = float(input())
y = float(input())
h = float(input())

# Steni
stranichna_stena = x * y
prozorec = 1.5*1.5
dve_stranichni_steni = (2 * stranichna_stena) - (2 * prozorec)

zadna_stena = x * x
vhod =  1.2*2
predna_i_zadna_steni =  (2*zadna_stena) - vhod

obshta_plosht_steni = dve_stranichni_steni + predna_i_zadna_steni


green_paint = obshta_plosht_steni / 3.4

# Pokriv

dva_pravougalnika_na_pokriva = 2 * (x * y)
dvata_triugalnika = 2 * (x * h / 2)

obshta_plosht_pokriv = dva_pravougalnika_na_pokriva + dvata_triugalnika

red_paint = obshta_plosht_pokriv / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
