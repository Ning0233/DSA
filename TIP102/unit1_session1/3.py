def tiggerfy(word):
    new_word = word
    new_word = new_word.replace('t', '')
    new_word = new_word.replace('T', '')
    new_word = new_word.replace('i', '')
    new_word = new_word.replace('I', '')
    new_word = new_word.replace('gg', '')
    new_word = new_word.replace('Gg', '')
    new_word = new_word.replace('GG', '')
    new_word = new_word.replace('gG', '')
    new_word = new_word.replace('er', '')
    new_word = new_word.replace('Er', '')
    new_word = new_word.replace('eR', '')
    new_word = new_word.replace('ER', '')
    return new_word


if __name__ == "__main__": 
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))
