def master_yoda(text):
    word_list=text.split()
    reverse_worl_list=word_list[::-1]
    return ' '.join(reverse_worl_list)

print("I am home --> {}".format(master_yoda('I am home')))
print("We are ready --> {}".format(master_yoda('We are ready')))