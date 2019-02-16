import csv
import docx2txt
import shutil
from translate.translate import Translator
import os

# set chrome path
chrome_path = '/usr/bin/google-chrome %s'

# set directory
directory = "/home/satq/Documents/new_site/doce"

# set list of title tags
tag_list = ("T: ", "Title:", "Tytuł:")

# set file list
file_list = []

# set title list
title_list = []

# set translator languages
translator = Translator(to_lang='en', from_lang='pl')

# set title list
translated_title_list = []

try:
    os.stat(directory + '/used')
except:
    os.mkdir(directory + '/used')

# set csv file

myFile = open('spis.csv', 'w')
with myFile:
    myFields = ['title', 'translation', 'file']
    writer = csv.DictWriter(myFile, fieldnames=myFields)
    writer.writeheader()
myFile.close()

# browse files
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".docx"):
        file_list.append(filename)
        my_text = docx2txt.process(directory + "/" + file)
        my_text_XXX = my_text.replace('\n', 'XXX')  # todo split on \n
        my_text_split = my_text_XXX.split('XXX')

        # check for title add to title_list and translate_title_list
        for line in my_text_split:
            if line.startswith(tag_list):
                start_char = line.find(':') + 2
                title_list.append(line[start_char:])  # check if all starts at 7th todo
                # TRANSLATIONS LIMIT todo
                translation = translator.translate((line[start_char:]))
                translated_title_list.append(translation)  # .split(" ")
        # move done file -> used todo
        shutil.move(directory + "/" + file, directory + "/used/" + file)




    else:
        pass

    f = open("spis.txt", "a+")
    f.write(title_list[-1] + "\n")
    f.write(file_list[-1] + "\n\n")
    f.close()

    myFile = open('spis.csv', 'a+')
    with myFile:
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writerow({'title': title_list[-1], 'translation': translated_title_list[-1], 'file': file_list[-1]})
