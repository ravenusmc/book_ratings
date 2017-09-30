#This file will handle all the data manipulation of the CSV file 

#Importing all required files
import numpy as np
import pandas as pd 

class Books():

    def __init__(self):
        self.__data = pd.read_csv('books.csv')

    #This method will get the rating for a book and then return it. 
    def book_rating(self, title):
        #Gettting the row of data for the title that the user entered.
        info = self.__data[self.__data.original_title == title]
        #Pulling the rating out of the row of data
        rating = info.iloc[0][12]
        #returning the data
        return rating

    #This method will get the books with the highest ratings
    def high_rating(self):
        #Here I am getting the books with the highest ratings. 
        high_rating = self.__data[self.__data.average_rating >= 4.7]
        #Getting just the book titles.
        rating = high_rating.iloc[0][10]
        #Setting up a counter
        count = 0
        #This list will hold the books
        book_list = []
        while count < len(high_rating):
            book = high_rating.iloc[count][10]
            book_list.append(book)
            count += 1
        return book_list

    #This method will get the books with the lowest ratings
    def low_ratings(self):
        #Here getting the books with low ratings
        low_rating = self.__data[self.__data.average_rating <= 2.8]
        #Getting just the book titles.
        low_rating = low_rating
        print()


#Problem: data is gettting messed up when coming in through JSON

#The Catcher in the Rye
#The Fault in Our Stars

book = Books()
# rating = book.book_rating('The Girl on the Train')
# print('Rating:', rating)
book.low_ratings()

# scrap code 

# print(info.iloc[0][12])
#rating = info.average_rating
#I now need to get the exact rating
# rating = rating.reset_index().values[0][1] 
# print(rating)
