def text_analyzer(*texte):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if len(texte) > 1:
        print("ERROR")
        quit()
    elif len(texte) == 0:
        texte = str(input("What is the text to analyse?"))
    else:
        texte = str(texte[0])
    print("The text contains ", len(texte) ," characters:\n\n")
    print("- " , sum(1 for letter in texte if letter.isupper()) , " upper letters\n\n")
    print("- " , sum(1 for letter in texte if letter.islower()) , " lower letters\n\n")
    print("- " , sum(1 for letter in texte if letter in punct), " punctuation marks\n\n")
    print("- " , sum(1 for letter in texte if letter.isspace()) , " spaces")
