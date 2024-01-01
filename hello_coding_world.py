from datetime import date

today = date.today()

message = "Hello programing world"
greeting = "Have a succesful programming year"

print(message + ' ' + '\n' + greeting + ' ' + today.strftime("%Y"))
