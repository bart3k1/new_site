import docx2txt
import os
import webbrowser
# from googletrans import Translator
from py_translator import Translator

# set chrome path
chrome_path = '/usr/bin/google-chrome %s'

# set directory
directory = "/home/satq/Documents/Pythony/new_site/doce"

# set list of title tags
tag_list = ("T: ", "Title:", "Tytuł:")

# set title list
title_list = []

# browse files
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".docx"):
        # print(os.path.join(directory, filename))

        # read .docx files
        my_text = docx2txt.process(directory + "/" + file)
        my_text_XXX = my_text.replace('\n', 'XXX')
        my_text_split = my_text_XXX.split('XXX')

        # check for title
        for line in my_text_split:
            if line.startswith(tag_list):
                title_list.append(line)
        continue
    else:
        continue

print(title_list)

# translate - webpage

# for i in title_list:
#     j = i.replace(" ", "%20")
#     print(j)
#     webbrowser.get(chrome_path).open("https://translate.google.pl/#view=home&op=translate&sl=auto&tl=en&text=" + j)

# translate googletrans/py_translator
# translator = Translator()
#
# translated = translator.translate("dupa", dest='en')
# print(translated.text)

# s = Translator().translate('Hello my friend', dest='es').text
# print(s)

# for i in title_list:
#     translated = translator.translate("dupa")
#     print(i)
#     print(translated.text)
