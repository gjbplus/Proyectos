# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

message_leap = "Leap year."
message_not_leap = "Not leap year."

# not is div by 4
if year % 4 != 0:
    print(message_not_leap)
# is div by 4
elif year % 4 == 0:
    # not is div by 100
    if year % 100 != 0:
        print(message_leap)
    else:
        # is div by 4
        # not is div by 100
        # is div by 400
        if year % 400 == 0:
            print(message_leap)
        else:
            print(message_not_leap)
