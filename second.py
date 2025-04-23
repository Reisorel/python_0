its_easy_as = [1,2,3,4,5]
title = [4, "mariages", "et", 1, "enterrement"]

LOTR_movies = ["La communauté de l'anneau", "Les deux tours", "Le retour du roi"]
movies = ["Titanic", "Django Unchained", ["Star Wars 1", "Star Wars 2", "Star Wars 3"], "Harry Potter", LOTR_movies]
print(movies)


groceries = ["tomatoes", "carrots", "bananas"]
groceries.reverse()
print(groceries)

# fonction len renvoie la longueur d'une liste
my_list = [1, 2, 3, 4, 5]
print(len(my_list))


#Récupérer le premier élément d'une liste
famous_guitarists = ["Jimi Hendrix", "Eric Clapton", "Jimmy Page", "Chuck Berry", "B.B. King"]
first_guitarist = famous_guitarists[0]
print(first_guitarist)
second_and_third_guitarist = famous_guitarists[1:3]
print(second_and_third_guitarist)
last_guitarist = famous_guitarists[-1]
print(last_guitarist)
every_guitarist_but_first = famous_guitarists[1:]
print(every_guitarist_but_first)


famous_surfers = ["Kelly Slater", "Mick Fanning", "John John Florence", "Gabriel Medina"]
double_famous_surfers = famous_surfers + famous_surfers
print(double_famous_surfers)

# new_surfer_list = famous_surfers + 1
# print(new_surfer_list)

# Extend "pousse les murs" de la liste tandis que append "rajoute un élément"
famous_surfers.extend(["Mikey February", "Owen Wright"])
print(famous_surfers)

#les listes sont mutables
#les strings sont immutables
famous_skaters = ["Tony Hawk", "Rodney Mullen", "Nyjah Huston"]

famous_skaters[1]= "Bob Burnquist"
print(famous_skaters)
famous_skaters.sort(reverse=True)
famous_skaters.reverse()
