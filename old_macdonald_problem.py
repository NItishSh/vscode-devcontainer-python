def old_macdonald(name):
    # first_letter = name[0]
    # inbetween = name[1:3]
    # fourth_letter = name[3]
    # rest = name[4:]
    # return first_letter.upper()+inbetween+fourth_letter.upper()+rest

    first_half=name[:3]
    second_half=name[3:]
    return first_half.capitalize() + second_half.capitalize()

print("macdonald --> {}".format(old_macdonald('macdonald')))
print("nitish --> {}".format(old_macdonald('nitish')))