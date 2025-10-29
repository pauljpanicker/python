from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year
    def account_age(self):
        current_yr=2025
        return current_yr-self.account_year
    @abstractmethod
    def get_role(self):
     pass

class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"hi this is admin:{self.name},account age:{self.account_age()}"
class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"hi this is guest:{self.name},account age:{self.account_age()}"

admin_user=Admin("Paul",2024)
guest_user=Guest("sith",2023)

print("role:",admin_user.get_role())
print("admin account age:",admin_user.account_age())
print(admin_user)

print("role:",guest_user.get_role())
print("guest account age:",guest_user.account_age())
print(guest_user)