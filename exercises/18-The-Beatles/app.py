def sing():
    my_str = ""

    for i in range (1, 12):
        if i == 5:
            my_str += 'whisper words of wisdom, '
        elif i == 11:
            my_str += 'there will be an answer, let it be'
        else:
            my_str += 'let it be, '
    return my_str

print(sing())
