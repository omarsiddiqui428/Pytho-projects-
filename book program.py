#Global variables

import json
#did a lot of testing and adjusting, but don't necessarily know why some things worked.Some errors, I put my code into chat gpt so it could explain the errors to me, is that okay?

#Functions

def load_books():
   with open('data.json', 'r') as file: #go through this
       data = json.load(file)

def book_exists(title): #check if title of book in json file
    with open('data.json', 'r') as file:
        data = json.load(file) #can replace with the load function
    if title in data: #COME BACK does this have to parse? #Check the keys since they are the titles. Why not data.keys()
        print("This book is in the JSON file") #return True?
    else:
        print("This book is not in the JSON file") #return False?

def save_books(data): #why do I have to pass in data here?
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

#Having issues with this one
def update_quantity(title, quantity): #Updates the quantity of a specific book.COME BACK, what are the inputs here? what is books doing?
    data = json.load(file)
    if title in data:
        data[title]['quantity'] = quantity  # COME BACK, I don't think I selected the thing I wanted to select to change
        save_books(data)
    else:
        print("The title you entered is not in the JSON file")

def add_book(info,books): #COME BACK, go through this in class
    load_books()
    print(data)

def update_book(title,field_to_update,update_value):
    load_books()
    if title in data:
        data[title][field_to_update] = update_value
    save_books(data)
    else:
        print("This title is not in the JSON file") #how do I integrate the book_exists function here?

def get_book(title):
    load_books()
    details = data[str(title)]
    print(details)

def display_all_books(): #Displays all books along with their details
    with open('data.json', 'r') as file:  # go through this
        data = json.load(file)  #why does this not woek when I replace with load_books()
        print(data)

#def remove_book(title,books): #removes a book from the database
def remove_book(title):
    if title in data:
        data.pop(title) #for stuff like this, can I just look up?
    else:
        print("This book is not in the JSON file")

#Additional functions
def quantity(title):
    load_books()
    if title in data:
        current_quantity = data[title]["quantity"]
        print("The current quantity of the book " + title + " is " current_quantity)

def borrow(title):
    #check if book exists in JSON here
    load_books()
    data[title]["quantity"] = data[title]["quantity"] - 1
    quantity(title)

def return(title):
    # check if book exists in JSON here
    load_books()
    data[title]["quantity"] = data[title]["quantity"] + 1
    quantity(title)

def add_rating(title,rating) #will have to rate out of 5 stars
#Have a number of ratings variable
#Have a rating total variable
#have an average rating variable
    #step 1: open json
    #step 2: access rating total and add this rating to the rating total
    #step 3: access number of ratings variable and add 1
    #Steps 4: access average rating variable and modify it to be the new rating total % new number of ratings
    #step 5: write this data back to the JSON file



    else:
        print("This book is not in the JSON file")

if __name__ == "__main__":
    main()



