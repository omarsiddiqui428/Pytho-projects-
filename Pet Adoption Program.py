# List to hold pet preferences
pet_preferences = []


# List of available pets

pets_dict = {
    "dog": 3,
    "cat": 1,
    "fish": 2,
    "bird": 2,
    "hamster": 1
}

# Start the infinite loop
while True:
   # Get user input
   pet_type = input("Which type of pet are you interested in adopting? (or type 'done' to finish): ")
   pet_type = pet_type.lower()
   if pet_type == "done":
       break
   elif pet_type in pets_dict.keys():
       if pets_dict[pet_type] == 0:
           print("Sorry, we don't have any more " + str(pet_type) + "s")
       else:
           pets_dict[pet_type] = pets_dict[pet_type] - 1
           pet_preferences.append(pet_type)
   else:
       print("Sorry, we don't have that type of pet. Try another one!")

   # Your code here


# Print the filtered pet preferences
print("You're interested in adopting:", pet_preferences)