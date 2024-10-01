#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file(
    "my_first_file.txt", "jfjfhfhfbvhvbhvbufbhubdhfdiuddfk kkjfv jf\n")
print(nb_characters)
