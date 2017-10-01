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
        #This dictionary will hold the books
        book_list = {}
        while count < len(high_rating):
            book = high_rating.iloc[count][10]
            author = high_rating.iloc[count][7]
            book_list[book] = author
            count += 1
        return book_list

    #This method will get the books with the lowest ratings
    def low_ratings(self):
        #Here getting the books with low ratings
        low_rating = self.__data[self.__data.average_rating <= 2.8]
        #Setting up a counter
        count = 0
        #This dictionary will hold the books
        low_list = {}
        #while loop to go through the books that have low ratings
        while count < len(low_rating):
            #Here I get the book with the lowest rating 
            book = low_rating.iloc[count][10]
            author = low_rating.iloc[count][7]
            low_list[book] = author
            #Place that book into the list
            # low_list.append(book)
            #Increment the count by one
            count += 1
        return low_list



