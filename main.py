x = 3 + 4

x = 3 * 20

x = 12 / 4

x = 8 + 2

x = 8 + 2 * 10

x = (8 + 2) * 10

# rounds and drop the decimal
x = 18 // 4

# modulus
x = 18 % 4

# ** means calculate the powers
x = 2 ** 3

# print(x)

# varieble
tuna = 5
bacon = 18
# print(20+tuna)
# print(bacon/ tuna )

# String needs to be in quotes "" or single quotes ''
# mix and match single quotes

# 'She said, "what part of the cow is the meatloaf from?" '
# 'I don\'t think she is 18'
# use backslash '\' escape character

# print("Hey now brown cow")

# print('C:\Bucky\Desktop\nudePics')
# r"" raw string formating
# print(r'C:\Bucky\Desktop\nudePics')
#
# firstName = "Bucky "
# print(firstName + "Roberts")
#
# firstName = "McLovin "
# print(firstName + "Roberts")
#
# # string multiplication
# print(firstName * 5 + "Roberts")
# computer starts counting from 0
# user = "Tuna McFish"
# print(user[0])
# print(user[5])
# # negative indexing
# print(user[-1])
# print(user[-3])
# # slice out string
# print(user[2:7])
# # start at the beginning
# print(user[:7])
# # finish at the end
# print(user[2:])
# # Whole entire thing
# print(user[:])
# # length of a string len("sdfasdflkjhwe")
# print(len("sdfasdflkjhwe"))
# print(len(user))

# python lists
# players = [29, 58, 66, 71, 87]
# print(players[2])
#
# players[2] = 68
# print(players)
#
# new_players = players + [90, 91, 98]
# print(new_players)
# players.append(120)
# print(players)
# # slicing a list in python similar to slicing a string
# print(players[:2])
# # changing multiple values at once in a list
# players[:2] = [0, 0]
# print(players)
# # slicing a list and removing items
# players[:2] = []
# print(players)
# # entire list empty
# players[:] = []

# pycharm is bucky's favorite ide and he has the professional edition
# project is where all the files are stored
# many files it may have
# .py is the extension

# print("this works")
# cool program begins
# cardboard is not allowed to be thrown away I guess
# lets learn if statement
# age = 13
# if age < 21:
#     print('No beer for you!')
# elif

# name = "Tommy D"
# if name == "Bucky":
#     print("Hey there Bucky")
# elif name == "Lucy":
#     print("What up Lucedawg")
# elif name == "Sammy":
#     print("What up Slammy")
# else:
#     print("Please sign up for the site!")

# for loop bucky
# foods = ['bacon', 'tune', 'ham', 'sausages', 'beef']
# # you can also slice the list for looping through
# for f in foods[:2]:
#     print(f)
#     print(len(f))

# for x in range(10):
#     print(x)
# range(start, end - 1, increment)
# for x in range(5, 40, 5):
#     print(x)

# buttcrack = 5
#
# while buttcrack < 10:
#     print(buttcrack)
#     buttcrack += 1

# break and continue
# ok this program finds a magic number
# single line comments
'''
multi line comment
'''


# print number and string in the same line
# print(9, " Bucky")
# magicNumber = 26
#
# for n in range(101):
#     if n is magicNumber:
#         print(n, " is the magic number!")
#         break
#     else:
#         print(n)
# for i in range(1, 101):
#     if i%4 == 0:
#         print(i)
#
# # Continue
# numbersTaken = [2, 5, 12, 13, 17]
#
# print("Here are the numbers that are still available")
#
# for n in range(1, 20):
#     if n in numbersTaken:
#         continue
#     print(n)
#

# Functions

# divide the program into manageable chunks
# we can use it over and over again.
# def beef():
#     print("Dayum,functions are cool!")
#
#
# def bitcoin_to_usd(btc):
#     amount = btc * 527
#     print(amount)
#
#
# beef()
# bitcoin_to_usd(3.85)
# bitcoin_to_usd(1)
# bitcoin_to_usd(13)
# def allowed_dating_age(my_age):
#     girls_age = my_age/2 + 7
#     return girls_age
#
#
# buckys_limit = allowed_dating_age(27)
# creepy_joe_limit = allowed_dating_age(49)
# print("Bucky can date girls",buckys_limit," or older")
# print("Creepy joe can date girls",creepy_joe_limit," or older")
# for x in range (51):
#     print(allowed_dating_age(x), "is the age limit for age",x)
#
# def get_gender(sex = "Unknown"):
#     if sex is 'm':
#         sex = "Male"
#     elif sex is 'f':
#         sex = 'Female'
#     print(sex)
#
#
# get_gender("m")
# get_gender("f")
# get_gender()

#
# def corn():
#     a = 7823
#
#     print(a)
#
#
# def fudge():
#     print(a)
#
#
# corn()
# fudge()

# def dumb_sentence(name="Bucky", action="ate", item = 'tuna'):
#     print(name, action, item)
#
# dumb_sentence()
# dumb_sentence('Sally', 'farts','gently')
# dumb_sentence(item="awesome")
# dumb_sentence(item="awesome", action="is")
# def add_numbers(*args):
#     total = 0
#     for a in args:
#         total += a
#     print(total)
#
# # function with flexible arguments
# add_numbers(3)
# add_numbers(3, 32)
# add_numbers(3,43,5453, 354234, 463463)
# how to create a function with any amount of arguments
# def add_numbers(*args):
#     total = 0
#     for a in args:
#         total += a
#     print(total)
#
# add_numbers(3)
# add_numbers(3, 32)

#
# # Unpacking list
# def health_calculator(age, apples_ate, cigs_smoked):
#     answer = (100-age) + (apples_ate *3.5) - (cigs_smoked*2)
#     print(answer)
#
#
# buckys_data = [27, 20, 0]
#
# health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
# # Unpack arguments
# health_calculator(*buckys_data)

# sets collection of items but cant have duplicate
# groceries = {'serial', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'}
# print(groceries)
# if 'milk' in groceries:
#     print("You already have milk hoss!")
# else:
#     print("oh yea, you need mik!")

# python Dictionaries - keys and values
# classmates = {'Tony': 'cool but smells', 'Emma':'She sits behind me', 'Lucy': 'asks too many questions'}
# # print(classmates)
# # print(classmates['Emma'])
#
# for k, v in classmates.items():
#     print(k +" "+ v)

# modules function included in another file
# import tuna
# import random
#
# tuna.fish()
# print(random.randrange(0,5))
#
# import random
# import urllib.request
#
# def download_web_image(url):
#     name = random.randrange(1,1000)
#     full_name = str(name) + ".jpg"
#     urllib.request.urlretrieve(url, full_name)
#
#
# download_web_image("https://plus.unsplash.com/premium_photo-1666900440561-94dcb6865554?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
#
# fw = open('sample.txt', 'w')
# fw.write('Writing some stuff in my text file\n')
# fw.write('I like bacon \n')
# fw.close()
#
# fr = open('sample.txt', 'r')
# text = fr.read()
# print(text)
# fr.close()
# from urllib import request
# import random
# def download_web_image(url):
#     name = random.randrange(1, 1000)
#     full_name = str(name) + ".jpg"
#     request.urlretrieve(url, full_name, )
#
# download_web_image("https://plus.unsplash.com/premium_photo-1666900440561-94dcb6865554?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
# fw = open("sample1.txt", "w")
# fw.write('writing some stuff in my text fiile\n')
# fw.write('I like bacon\n')
# fw.close()
#
# fr = open('sample1.txt', 'r')
# text = fr.read()
# print(text)
# fr.close()
# The goog csv project
# from urllib import request
# goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1686523687&period2=1718146087&interval=1d&events=history&includeAdjustedClose=true'
#
# def download_stock_data(csv_url):
#     response = request.urlopen(csv_url)
#     csv = response.read()
#     csv_str = str(csv)
#     lines = csv_str.split('\\n')
#     dest_url = r'goog.csv'
#     fx = open(dest_url, "w")
#     for line in lines:
#         fx.write(line + "\n")
#     fx.close()
#
# download_stock_data(goog_url)

# The web crawler

import requests
from bs4 import BeautifulSoup

# url = https://evaly.com.bd/search?categoryName=Frozen%20Meat%2CT-Shirts%2CWatches%20For%20Men%2CCasual&page=1
# # make core spider
# def trade_spider(max_pages):
#     page = 1
#     while page < max_pages:
#         url = 'https://en.wikipedia.org/wiki/English_Wikipedia'
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, 'html.parser')
#         for link in soup.findAll('a', {'class': 'mw-redirect'}):
#             href = 'https://en.wikipedia.org/wiki/English_Wikipedia'+link.get('href')
#             print(href)
#
#         page += 1
#
# trade_spider(1)
#
#
# import requests
# from bs4 import BeautifulSoup
#
# def trade_spider(max_pages):
#     page = 1
#     while page < max_pages:
#         url = 'https://en.wikipedia.org/wiki/English_Wikipedia'
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, 'html.parser')
#         for link in soup.findAll('a', {'class': 'mw-redirect'}):
#             href = 'https://en.wikipedia.org' + link.get('href')
#             print(href)
#         page += 1
#
# trade_spider(1)


# import requests
# from bs4 import BeautifulSoup
#
# def trade_spider(max_pages):
#     page = 1
#     while page <= max_pages:
#         url = "https://evaly.com.bd/search?categoryName=Frozen%20Meat%2CT-Shirts%2CWatches%20For%20Men%2CCasual&page="+ str(page)
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#         for link in soup.find_all('a', {'class': ''}):
#             href = link.get('href')
#             title = link.string
#             print(href)
#             print(title)
#         page +=1
#
# trade_spider(1)

# import requests
# from bs4 import BeautifulSoup
#
# def trade_spider(max_pages)
#     page = 1
#     while page <=max_pages:
#         url = "https://google.com"
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text)
#         for link in soup.find_all('a', {"a", {'class': 'item name'}}):
#             href = 'https://'


import requests
from bs4 import BeautifulSoup

#
# def trade_spider(max_page):
#     page = 1
#     while page <= max_page:
#         url = 'https://google.com'
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#         for link in soup.find_all('a', ):
#             href = link.get('href')
#             title = link.string
#             print(title)
#             print(href)
#
#         page = page + 1
#
#
#
# trade_spider(1)



# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, "html.parser")
#     for item_name in soup.find_all('div', {'class': 'gLFyf'}):
#         print(item_name.string)

n, m = map(int, input().split())
a = 0
b = 0
count = 0
for a in range(0, max(n, m)+1):
    for b in range(0, max(n, m)+1):
        if a**2 + b == n and a + b**2 == m:
            count += 1

print(count)





