machine_id = "DM-2"


# Utilisation de la fonction zfill qui remplit les zéros à gauche
part_two = machine_id[-1].zfill(3)
print(part_two)

# Utilisation de :3 qui permet de prendre les 3 premiers caractères
part_one = machine_id[:3]
print(part_one)

# Concaténation des deux parties
new_id = part_one + part_two
print(new_id)

# Erreur car la variable answer est un entier, seules les strings peuvent être indexées
answer = "42"
print(answer[0])
voldemort = "Tom Marvolo Riddle"
print(voldemort[:3])

framework = "django"
print(framework.upper())

book = "Da Vinci Code"
print(book[-4:].lower())

date = "2025-04-23"
print(date.split("-"))

number = "7"
print(number.zfill(3))
