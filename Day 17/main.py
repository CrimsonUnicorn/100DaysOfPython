# class User:
#   pass
  
# user_1 = User()
# user_1.id = "001"
# user_1.username = "aman"

# user_2 = User()
# print(user_1.username)

class User:
  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0  #default value
    self.following = 0
  def follow(self, user):
    user.followers +=1
    self. following +=1

user_1 = User("001", "Aman")
print(user_1.id)

# user_2 = User()        give error as we parameter for it to work as we initialized in class
# user_2.id = "002"

user_2= User("002", "aman")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)