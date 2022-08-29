from itertools import count
from posixpath import split
from re import A
import string


# def index2():

#     word_list = ["of", "many", "lots", "words"]
#     infile = ["lots of words","many many work words","how come this picture lots work","poem poem more words that rhyme"]
#     dct = {}
    # deleted line
    # for line in infile:
    #     newLine = line.replace('\n', ' ') # shouldn't do anything, because I have no newlines
    #     if newLine == ' ':
    #         continue
        # deleted line
        # newLine2 = newLine # ignoring punctuation
        # split_line = newLine2.split()
        # for word in word_list:
            # count = 0 # you might want to start at 1 instead, if you're going for 'word number'
            # important note: you need to have 'word2', not 'word' here, and on the next line
            # for word2 in split_line: # changed to looping through data
                # if word2 == word:
                    # if word2 in dct:
                        # temp = dct[word]
                        # temp.append(count)
                        # dct[word] = temp
                    # else:
                        # temp = []
                        # temp.append(count)
                        # dct[word] = temp
                # count += 1
    # for word in word_list:
        # print('{:12} {}'.format(word, ", ".join(map(str, dct[word])))) # edited output so it's comma separated list without a trailing comma

# index2()
# count = 0
  
# Opens a file in read mode
# f = open("poem.txt", "r", encoding="utf8")
  
# Gets each line till end
# for line in f:
#     Splits into words
#     word = line.split(" ")
#     Counts each words
#     count += len(word)
  
# print("Total Number of Words: " + str(count))
# f.close()

# with open("poem.txt", 'r', encoding="utf8") as file:
#     content = file.read()
#     for line in file:
#         for word in line.split():
#             word = word.translate(line.maketrans("", "", string.punctuation))
#             for punct in word.translate(line.maketrans("", "", string.punctuation)): 
#                     print(punct)
#                     pass
#             print(word)
    # print(content)

# def word_search(key):
#     with open('poem.txt', 'r', encoding='utf8') as file:
#         lines = file.readlines()
#     for number, line in enumerate(lines, 1):
#         if key in line:
#             pass
            # print(f'{key} is on line {number}')
# word_search('1')


# def index2():
#     d = dict()
#     with open('poem.txt','r',encoding='utf8') as file:
#         var = file.readlines()
#         for line in var:
#             line = line.strip()
#             line = line.lower()
#             line = line.translate(line.maketrans("", "", string.punctuation))
#             words = line.split(" ")
#             for word in words:
#                 # if word in d:
#                 #     d[word] = d[word]
#                 for number, line in enumerate(var,1):
#                     if key in line:
                         
#                         print(key, " ",d[key])
#             # print(line)
# index2()

#--------vowel and consonant--------
# with open('poem.txt','r',encoding='utf8') as file:
#     word_list = [word for line in file for word in line.split()]
#     word_list = word_list.translate(word_list.maketrans("", "", string.punctuation))
#     print(word_list)
    
    
# dict = {}
# couter = 0
# with open('poem.txt', 'r', encoding='utf8') as file:
#     for line in file:
#         (key,value) = line.split()
#         dict[int(key)] = value
#     print('\ntext file to dictionary=\n',dict)

# dict = {}
# with open('poem.txt','r',encoding='utf8')as file:
#     for k,l in enumerate(file):
#         for word in l.split(" "):
#             if word in file:
#                 if word in dict.keys():
#                     dict[word].append(k)
#                 else:
#                     dict[word] = [k]
# print (dict)

# with open('poem.txt','r',encoding='utf8') as file:
#     for k,v in enumerate(file):
#         pass
# print(k + 1)

# with open ('poem.txt', 'r') as f:
#     list_txt = []
#     for line in f:
#         strip_line = line.strip()
#         list_line = strip_line.split()
    # print(list_line)
        # print(list_line)
        # m = list_txt.append(list_txt)
    # print(list_line)
    
# a_dict = {}
# a_file= open('poem.txt')
# for line in a_file:
#     key,value = line.split()
    
#     a_dict[key] = value
# print(a_dict)

# dic = []
# with open('poem.txt', 'r',encoding='utf8') as f:
#     file_name = f.readlines()
#     for line in f:
#         line = line.split()
               
# print(line)
# d = {}
# with open('poem.txt') as f:
#     for line in f:
#         (key,val) = line.split()
#         d[int(key)] = val
# print(d)

# with open('poem.txt') as myFile:
#     for num,line in enumerate(myFile,1):
#         print
# filename = 'poem.txt'
# d = {}
# with open(filename,encoding='utf8') as f:
#     for line in f:
#         line = line.strip()
#         alist = line.split(',')
#         d[alist[0]] = alist[1]
# print(d) 
# def index1():
#     d = dict()
#     # line_word = []
#     with open("poem.txt", 'r', encoding="utf8") as file:
#         var = file.readlines()
#         # print(var)
        
#         for line in var:
#             line = line.strip()
#             line = line.lower()
#             line = line.translate(line.maketrans("", "", string.punctuation))
#             words = line.split(" ")
            
#             for word in words:
#                 if word in d:
#                     print(word)
# index1()
# row  = []
# filename = open('poem.txt', 'r')
# for line in filename.readlines():
#     row.append(line)
#     for i in line.split(","):
#         pass
#         # row[-1].append(i)
#     # print(row)
# print(row[0])

# with open('poem.txt') as file:
#     listfile = []
#     for line in file:
#         listfile.append(line.strip())
#     print(listfile)
# with open('poem.txt','r') as f:
#     list_word = [line.strip() for line in f]
#     print(list_word)
# crimefile = open('poem.txt', 'r')
# yourResult = [line.split(',') for line in crimefile.readlines()]
# print(yourResult)
# text_file = open("poem.txt", "r")
# lines = text_file.readlines()
# print (lines)
# print (len(lines))
# text_file.close()
# my_file = open('poem.txt','r')
# content = my_file.read()
# content_list = content.strip()
# content_list = content.translate(line.maketrans("", "", string.punctuation))
# content_list = content.lower()
# content_list = content.split(",")
# my_file.close()
# print(content_list)


# def firstLetterOfEachWord():
#     list_file2 
#     firstLetter = [x[0] for x in list_file2]
#     firstLetter = x[0].lower()
    # return firstLetter
# answer = firstLetterOfEachWord()
# print(answer)
# for x in list_file2:
#     list_first_num =x[0]
#     list_first_num = list_first_num.lower()
#     print(list(list_first_num))
    # print(list_first_num)
    # print (list(x[0]))

        
    
        # print(i)
