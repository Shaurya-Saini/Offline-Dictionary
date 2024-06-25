# Offline-Dictionary

This project is a offline digital dictionary application developed using Python. Tkinter and ttkbootstrap libraries are used for the simple graphical user interface (GUI) of the application. The dictionary stores data about the word in an SQLite database, including the meaning and type. Upon searching the dictionary shows upto 3 different defination for the given word at almost instant speed. 

The data base for the project was made using webscraping of the wordnik website and using the list of words provided by nltk library in python. Also asynsio and aiohttp libraries were used to send concurrent requests to the website for improving the speed. Word were differntiated based on the first letters as in a real dictionary to improve the querying speed of the main program. All the code for the same is in the backend.py file.

The main file where the dictionary functions is the Dictionary.py file. Tkinter, ttkbootstrap and sqlite3 libraries were used to make the simple GUI and the querying of the databases based on the word respectively.
