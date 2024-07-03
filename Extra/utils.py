def removepunc(text):
    punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    analyzed_Text = ""
    for char in text:
        if char not in punctuations:
            analyzed_Text = analyzed_Text + char
    return analyzed_Text


def capfirst(text):
    analyzed_Text = ""
    for char in text:
        analyzed_Text = analyzed_Text + char.upper()
    return analyzed_Text


def newlineremover(text):
    analyzed_Text = ""
    for char in text:
        if not char == "\n":
            analyzed_Text = analyzed_Text + char.upper()
    return analyzed_Text


def spaceremover(text):
    analyzed_Text = ""
    for index, char in enumerate(text):
        if not (text[index] == " " and text[index+1] == " "):
            analyzed_Text = analyzed_Text + char           
    return analyzed_Text


def charcount(text):
    punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    space = " "
    newline = "\n"
    charcount = 0
    for char in text:
        if not (char in punctuations or char == space or char == newline):
            charcount = charcount + 1
    return charcount



if __name__ == "__main__":
    django_Text1 = "My name is Rakib.';.';.';';"
    analyzed_Text = removepunc(django_Text1)
    print(analyzed_Text)

    django_Text2 = "My name is Rakib."
    analyzed_Text = capfirst(django_Text2)
    print(analyzed_Text)

    django_Text3 = "My \nname \nis \nRakib."
    analyzed_Text = newlineremover(django_Text3)
    print(analyzed_Text)

    django_Text4 = "My  name  is  Rakib."
    analyzed_Text = spaceremover(django_Text4)
    print(analyzed_Text)

    django_Text5 = "My name is Rakib."
    analyzed_Text = charcount(django_Text5)
    print(analyzed_Text)

