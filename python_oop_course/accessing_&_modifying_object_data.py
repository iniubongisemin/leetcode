class User:
    def __init__(self, name, email, password):
        self.username = name
        self.__email = email
        self.password = password

    def say_hi_to_user(self, user): 
        print(f"Sending a message to {user.username}: Hi {user.username} it's {self.username}")

    def get_email(self): # Don't do this!!!!
        return self._email
    
    def clean_email(self):
        return self.__email.lower().strip()
    


user_one = User("Inie", "eugeneinie@gmail.com", "1234")
user_two = User("python_bot", " Robot@yahoo.com", "1CU14CU")

user_two.say_hi_to_user(user_one)

# MODIFYING ATTRIBUTES OF A CLASS 
# user_one._email = "iceley007@gmail.com"
# print(user_one._email)
# print(user_one.get_email())

# print(user_two._email)
# print(user_two.clean_email())

# MAKING ATTRIBUTES PRIVATE (Use _ to prefix the attribute definition) - Not strict
# print(user_two._email)
# MAKING ATTRIBUTES TRULY PRIVATE (Use __ double underscore)
print(user_one.__email)

