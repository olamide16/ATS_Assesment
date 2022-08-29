import csv
from email import header
from http.client import NETWORK_AUTHENTICATION_REQUIRED
import string



#-----------occurence of each word -------------------
d = dict()
    # line_word = []
with open("poem.txt", 'r', encoding="utf8") as file:
        var = file.readlines()
        # print(var)
        
        for line in var:
            line = line.strip()
            # line = line.lower()
            line = line.translate(line.maketrans("", "", string.punctuation))
            words = line.split(" ")
            
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
        for key in list(d.keys()):
            pass
            # print(key," ",d[key])

            
#----------line number-------------------
list_file = []
with open('poem.txt', 'r') as file:
    for line in file:
        line_strip = line.strip()
        line_split = line.split()
        list_file.append(line_split) 
# print(list_file[0])
list_file2 =list_file[0] + list_file[1] + list_file[2] + list_file[3] + list_file[4]+ list_file[5] + list_file[6] + list_file[7] +list_file[8] + list_file[9] +list_file[10] +list_file[11] + list_file[12] + list_file[13]
# print(list_file2)
# we have gotten the list of each element in the text file
filename = open('poem.txt')
dic = {}
for line in filename:
    newline = line.replace('\n', ' ')
    if newline == ' ':
        continue
    newline2 = newline
    split_line = newline2.split()
    
    for word in split_line:
        count = 0
        for word2 in split_line:
            if word2 == word:
                if word2 in dic:
                    temp = dic[word]
                    temp.append(count)
                    dic[word] = temp
                else:
                    temp = []
                    temp.append(count)
                    dic[word] = temp
            count += 1
for word in list_file2:
    # print('{:12} {}'.format(word, ", ".join(map(str, dic[word]))))
    pass

#---------vowel and consonant-------------
first_letter = []
for x in list_file2:
    # x[0].lower()
    first_letter.append(x[0])
# print(first_letter)
# dic = {}
vowel_list = []

for i in list_file2:
    for j in list_file2:
        # print(i)
        i = i.translate(str.maketrans("", "", string.punctuation))
    
    list_vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

    if (i[0] in list_vowel):
        # print("vowel")
        vowel_list.append('v')
    
    else:
        vowel_list.append('c')
print 
    
list_file2   
new_output = list(d.values())
second_new_output = list(dic.values())
     
header = ['word', 'occurence','line_number','vowel/consonant']

with open("Test.csv", 'w', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows([list_file2, new_output, second_new_output,])

# print(new_output)
# print(second_new_output)
