import os
import json
import re
path_input = 'data'
path_hindi = 'hindi'
path_english = 'english'
files = os.listdir(path_input)
for file_name in files:
    with open(path_input+'/'+file_name) as file_read:
        data = file_read.read()
        data = re.sub('[0-9]',' ', data)
        data_list=data.replace('\n',' ').replace('/',' ').replace('.',' ').replace('(',' ').replace(')',' ').replace('?',' ').replace('-',' ').replace(',',' ').split(' ') 
        data_list = [ word for word in data_list if len(word)<20 ]    
    with open(path_hindi+'/'+file_name, 'w') as hindi_file:
        hindi_file.writelines("%s\n" % word for word in data_list)

    command = 'python3 runTransliteration.py '+path_hindi+'/'+file_name+' '+file_name
    os.system(command)
word_dict = {}
for file_name in files:
    hindi = [line.strip('\n').strip(')').strip('(').strip('।') for line in open(path_hindi+'/'+file_name, 'r')]    
    english = [line.strip('\n') for line in open(path_english+'/'+file_name, 'r')]
    word_dict.update(dict(zip(english, hindi))) 

with open('data.json', 'w', encoding='utf-8') as final:
    json.dump(word_dict, final, ensure_ascii=False, indent=4)

        