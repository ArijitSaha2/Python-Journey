# WAP to fill a letter template given below with name and date.
letter = '''
       Dear <|Name|>,
       You are Selected!
       <|Date|>
       '''
print(letter.replace('<|Name|>','Harry').replace('<|Date|>','25/4/2025'))#This method is called Chaining

# letter = letter.replace('<|Date|>','25/4/2025')
