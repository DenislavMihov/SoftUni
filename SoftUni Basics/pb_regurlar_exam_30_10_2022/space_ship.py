width_of_ship = float(input())
lenght_of_ship = float(input())
height_of_ship = float(input())
average_height_astro = float(input())

volume_of_rocket = width_of_ship * lenght_of_ship * height_of_ship
volume_of_room = (average_height_astro + 0.40) * 2 * 2

space_for = int(volume_of_rocket / volume_of_room)

if space_for < 3:
    print("The spacecraft is too small.")
elif space_for <= 10:
    print(f"The spacecraft holds {space_for} astronauts.")
else:
    print(f"The spacecraft is too big.")
