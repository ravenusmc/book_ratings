#This file will handle all the data manipulation of the CSV file 

#Importing all required files
import numpy as np
import pandas as pd 

class Books():

    def __init__(self):
        self.__data = pd.read_csv('books.csv')

    #This method will get the rating for a book and then return it. 
    def book_rating(self, title):
        print('Title:', title)
        #Gettting the row of data for the title that the user entered.
        info = self.__data[self.__data.original_title == title]
        print(info)
        # rating = info.iloc[0][12]
        rating = 0
        return rating

#Problem: data is gettting messed up when coming in through JSON

#The Catcher in the Rye
#The Fault in Our Stars

# book = Books()
# rating = book.book_rating('The Kite Runner')
# print('Rating:', rating)


# scrap code 

# print(info.iloc[0][12])
#rating = info.average_rating
#I now need to get the exact rating
# rating = rating.reset_index().values[0][1] 
# print(rating)
