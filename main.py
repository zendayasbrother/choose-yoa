name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("you are on a dirt road as a 20 year old, it has come to an end and you can either go left or right. Which way would you go? ").lower()

if answer == "left": 
  answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around or swim to swim across: ")

if answer == "swim":
 answer = input("You're now in the forest and you've been walking for five minutes. You reach a Y junction. The left path has a continuing path that has this mysterious ball of light  at the end of it and the right path is the start of a hilly path to what you hope is a campsite. Type left or right to continue: ")


elif answer == "walk":
    print("You walked for many miles and ran out of water. You lost.")

if answer == "right": 
   answer = input("You see an abandoned dirt bike on your walk. It looks fairly new and functional. Would you take it to get to the campsite quicker or would you not risk potentially stealing. Type bike or safe to continue: ")
if answer == "bike":
  answer = input("You have now reached the quater point. You're about to take a break after no food for four hours. But suddenly, you hear the loudest growl from some direction. Do you panic and quickly restart the dirt bike or do you assume it's harmless and continue eating your cereal bar? Type restart or harmless to continue: ")
if answer == "restart":
  answer = input("You're escaping the growl and you see a speed limit sign with a 20 on it. Are you going to speed to not risk hearing the growl, or go below 20 for the rest of the bike ride? Type over or under to continue:")
  
if answer == "harmless":
  answer = input("You encounter a bear. Not exactly adult or baby. Are you going to pet it and give it some food, or just ignore the bear? Type pet or ignore to continue: ")
 

elif answer == "safe":
  answer = input("You can't see the other campsite in your direction on your map. Suddenly you see some teenage bikers come your way. Are you going to ask the teens for help or figure this out on your own until you can't? Type teens or independence to continue: ")
  

else:
   print("Not a valid option. You lose")