##----RANDOM JOKE TELLER (PYTHON EDITION)----##
##----MODULE IMPORTS----##

import random
import sys

jokes = [
    "Why do Java developers wear glasses? Because they don't see sharp!",
    "How many Python programmers does it take to screw in a light bulb? None. They prefer a light framework.",
    "Why did the C++ code break up with the Java code? It had too many issues.",
    "How does a computer catch a cold? It starts with a bit of Windows!",
    "Why did the programmer quit his job? He didn't get arrays.",
    "What's a programmer's favorite hangout place? Foo Bar.",
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the JavaScript developer go broke? Because he kept using 'var' for everything.",
    "Why was the HTML element so frustrated? It had too many parents.",
    "How do you comfort a JavaScript bug? You console it, then it logs its feelings!"
]

##----VARIABLES----##

user_input1 = input("wanna hear a joke? y/n")

randomjoke = random.choice(jokes)
noanswer = "Okay, No joke then!"

yes = "y"
no = "n"
##----FIRST JOKE----##

if user_input1 == yes:
  print(randomjoke)
elif user_input1 == no:
  print(noanswer)
  sys.exit()
##----SECOND JOKE----##
user_input2 = input("wanna hear another joke? y/n")

if user_input2 == yes:
  print(randomjoke)
elif user_input2 == no:
  print(noanswer)
  sys.exit()
