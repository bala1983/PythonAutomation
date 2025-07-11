while True:
    word_h = input("Введіть слово з літерою h:")
    search_criteria = 0
    for h in word_h:
        print(h)
        if h.lower() == "h":
            search_criteria += 1
            break
    if search_criteria != 0:
        break