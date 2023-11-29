class User:
    def __init__(self, first_name, last_name, email, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        for attribute, value in self.__dict__.items():
            print(value) 
        # print(self.first_name)
        # print(self.last_name)
        # print(self.email)
        # print(self.age)
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points -= amount


catron = User("catron", "gainey", "cg@gmail.com", 100)
# catron.enroll()
catron.display_info()
# print(catron.is_rewards_member, catron.gold_card_points)
# catron.spend_points(50)
# print(catron.gold_card_points)