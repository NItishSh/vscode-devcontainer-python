def animal_crackers(text):
    wordlist = text.lower().split()
    if wordlist[0][0] == wordlist[1][0]:
        return True
    else:
        return False

print("Levelheaded Llama --> {}".format(animal_crackers("Levelheaded Llama")))
print("Crazy Kangaroo --> {}".format(animal_crackers("Crazy Kangaroo")))
print("Crazy cat --> {}".format(animal_crackers("Crazy cat")))