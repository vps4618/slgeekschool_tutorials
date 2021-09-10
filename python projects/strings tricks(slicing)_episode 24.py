#first example

text = "SL Geek School"
       #0123456789

first_word=text[:2]
print(first_word)

second_word=text[3:7]
print(second_word)

last_word=text[8:]
print(last_word)

last_word1=text[8:-2]
print(last_word1)

#second example

text1="Vishwa Praveen"
      #0123456789
first_word1=text1[0:6:2]#3rd one stands for space between letters
print(first_word1)

#third example

text2 = "SL Geek School"
       #0123456789

first_word2=text2[::-1]#reversing sentence
print(first_word2)
