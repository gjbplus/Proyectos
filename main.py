
year = int(input("Which year do you want to check? "))

message_leap = "Leap year."
message_not_leap = "Not leap year."

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(message_leap)
    else:
      print(message_not_leap)
  else:
    print(message_leap)
else:
  print(message_not_leap)

