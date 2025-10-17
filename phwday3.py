is_logged_in = True
is_subscribed = False
user_credits = 100
max_credits = 200
min_credits = 50
credits_valid = user_credits <= min_credits
print("credits_valid=",credits_valid)

bonus_credits = is_subcribed = True or user_credits > min_credits
print("bonus_credits=",bonus_credits)

user_credits +=50
user_credits -=20
user_credits *=2
user_credits %=150
print("final_user_credits=",user_credits)
power_result=math.sqrt(user_credits)
print("power_result",power_result)
full_acces = is_logged_in and is_subcribed
print("full_acces",full_acces)
is_true_login=  is_logged_in is True
print("is_true_login",is_true_login)
access_result = is_logged_in or is_subscribed and False
print("access_result",access_result)