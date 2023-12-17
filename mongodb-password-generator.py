import string
import random 

# Store all characters in lists 
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)
exclusion = [':','/','?','#','[',']','@']  # special characters need to be excluded
filtered_punctuation = list(set(punctuation).difference(exclusion))

# Generate password based on the combination of alphanumeric and special characters.
characters = lowercase + uppercase + digits + filtered_punctuation
password = ''.join(random.choice(characters) for i in range(16))
print("Random password is:", password)