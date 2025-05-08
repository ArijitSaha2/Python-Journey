# String is a data type in python.

# String is a sequence of characters enclosed in quotes.

# We can primarily write a string in these three ways.

# a = 'harry'      # Single quoted string         
# b = "harry"      # Double quoted string  
# c =  '''harry''' # Triple quoted string



                                        #Index
# name = "Harry" => Length = 5      # H  a  r  r  y 
                                    # 0  1  2  3  4 <--- Postive Slicing
                                    #-5 -4 -3 -2 -1 <--- Negative Slicing

name = 'harry'
# nameshort = len(name) # len Helps us display the length of a string
#Positive Slicing:
nameshort = name[0:3] # start from index 0 all the way till 3 exclduding 
print(nameshort)

character1 = name[1] # Displays character number 1 if used print()
print(character1)
 
