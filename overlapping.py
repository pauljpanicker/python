class Account:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance

    def __add__(self, other):
        total=self._balance+other._balance
        return Account(self._name,total)

    def display(self):
        print("name:",self._name)
        print("balance:",self._balance)

class Savings(Account):
    def __init__(self,_name,_balance):
        super().__init__(_name,_balance)
        #why not self.interest
        self.interest=self.calculate()


        # self.interest=_balance*5

    def calculate(self):
        interest=self._balance*0.05
        return interest
    def display(self):
        print("name:",self._name)
        print("balance:",self._balance)
        print("interest:",self.interest)



class Current(Account):
    def __init__(self,_name,_balance):
        super().__init__(_name,_balance)
        self.new_interest=self._balance*0.02
    def display(self):
        print("name:", self._name)
        print("balance:", self._balance)
        print("interest:", self.new_interest)



x=Savings("Ravi",10000)
y=Current("Anjali",15000)
z=x+y

print(">>>Old interest<<<")
x.display()
print("<<<new interest>>>")
y.display()
print("TOTAL BALANCE")
z.display()
