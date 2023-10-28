def inverse_word_in_same_orderr(sentence):
    if sentence == "":
        return None
    words = sentence.split(" ")

    for i in words:
        sentence = sentence.replace(i, i[::-1])
    return sentence


print(inverse_word_in_same_orderr("the boy ran"))
