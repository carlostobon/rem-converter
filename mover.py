name = input("Give me a path: ")

with open(name, 'r') as file:
    lines = file.readlines()
    for num, line in enumerate(lines):
        if line.rfind("/*") > 0: continue
        for word in line.split():
            if word.rfind('rem') > 0:
                initial_word = word
                add_semi = False
                if word.rfind(';') > 0:
                    add_semi = True

                word = word.replace('rem', '').replace(';', '')
                word = float(word) * 16.0

                if add_semi:
                    word = str(word) + 'px' + ';'
                else:
                    word = str(word) + 'px'

                line = line.replace(initial_word, word)
                lines[num] = line
    css = open(name + ".fixed", "w")
    css.writelines(lines)













