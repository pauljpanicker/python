import re
try:
 book_title=input("enter the book name:")
 year=input("enter the year:")
 if not re.match(r'^a-zA-Z/s+$',book_title):
   raise ValueError("invalid input")
 if not re.match(r'^(19|20)\d{2}$',year):
   raise ValueError("invalid input")
except ValueError as e:
   print("Error:",e)
else:
 print("Data is saved")
finally:
 print("thank you")