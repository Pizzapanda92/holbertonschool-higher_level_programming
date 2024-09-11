#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5]
# Devrait imprimer "12345" suivi d'un saut de ligne, puis retourner 5
print(safe_print_list_integers(my_list, 10))

my_list = [1, 2, 3, 4, 5]
# Devrait imprimer "12" suivi d'un saut de ligne, puis retourner 2
print(safe_print_list_integers(my_list, 2))

my_list = ["Hello", "World"]
print(safe_print_list_integers(my_list, 2))
