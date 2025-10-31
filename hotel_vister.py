import re
try:
    name=input("Enter the name")
    feedback=input("feedback")
    if not name.strip() or not feedback.strip():
        raise ValueError("please enter the input")
except ValueError as a:
    print("error:",a)
else:
    print(f"thank for your feedback{name}")
finally:
    print("VIST AGAIN")