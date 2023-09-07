def trim(phrase, size):
    if(size < len(phrase)):
        if(size <= 3):
            return phrase[0 : size] + "..."
        return phrase[0: size - 3] + "..."

    return phrase


# print(trim("He", 1))
# print(trim("Code Wars is pretty rad", 50))
print(trim("Creating kata is fun", 14))

