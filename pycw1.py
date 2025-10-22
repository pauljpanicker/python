heading= "*****receipt*****\n"
book1="Python Basics"
price=450
book2= "Data Science Intro"
price2=600
line1=f"{price} {book1} \n"
line2=f"{price2} {book2} \n "
total=price+price2
final_l=heading + line1  + line2 + str(total)+ "\n thank you"
print(final_l.upper())
