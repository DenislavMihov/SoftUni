bottles_of_soap = int(input())

detergent = bottles_of_soap * 750
counter = 0
command = input()
washed_dishes = 0
washed_pots = 0

while command != "End":

    dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        detergent -= (dishes * 15)
        washed_pots += dishes

    else:
        detergent -= (dishes * 5)
        washed_dishes += dishes

    if detergent < 0:
        break

    command = input()

if detergent < 0:
        print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")

else:
    print("Detergent was enough!")
    print(f"{washed_dishes} dishes and {washed_pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")

