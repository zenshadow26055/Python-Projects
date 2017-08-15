def begin_story():
	user_response = 0
	print("You are a villager on a small island. As you walk down a beach, you notice a fairly large object that resembles a space shuttle. You walk closer and see that it contains a strange being that you have never seen before. The being looks injured. What do you do?")
	user_response = int(input("1. You investigate the object and the being inside of it. \n2. You call the police. \n3. You run away."))
	decision1(user_response)
	
def decision1(user_response):
	#print("This would be the story continuing after the user's first response")
	if user_response == 1:
		print("You get close to the lifeform and see that it has shards of glass in its arm and it is unconsious. What do you do next?")
		user_response = int(input("1. Pull out the shards of glass. \n2. Nudge the alien. \n3. Leave the spaceship."))
		decision2_1(user_response)
	elif user_response == 2:
		print("Your phone does not work. Try again.")
	#	user_response = int(input("1.option one\n2.option two\n3.option three"))
		#decision2_2(user_response)
	elif user_response == 3:
		print("You activate some kind of motion sensor on the ship which sends a laser beam in your direction and kills you.")
	#	user_response = int(input("1.option one\n2.option two\n3.option three"))
		#decision2_3(user_response)
	
def decision2_1(user_response):
#	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("The alien wakes up shocked and in pain. It uses the little strength it has to grab its death ray and kill you.")
		#user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("You awaken the alien and it looks around. It speaks to you gently in a language that is not from Earth. What do you do?")
		user_response = int(input("1. Try to use sign language to explain the situation. \n2. Back away and try to leave the spaceship. \n3. Try to speak to it in English."))
		decision2_2(user_response)
	elif user_response == 3:
		print("You try to leave, but accidentally activate a security protocol that initiates a self destruct sequence and you explode.")
		#user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision2_2(user_response):
#	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("The alien sees this as a threat and shoots you with a laser.")
#		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("You try to leave, but accidentally activate a security protocol that initiates a self destruct sequence and you explode.")
		#user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("The alien does not understand you, but shows a face of realization, pulls out a device, and turns it on. He turns a knob on the device in the direction of an image of what looks like a human profile. Suddenly, he speaks to you and the device translates his speech into English. He asks you to help him pull out any shards of glass in his skin and treat his injuries. What do you do?")
		user_response = int(input("1. Tend to his injuries. \n2. Ask if he has any first aid items or anything that can help. \n3. Rush home to grab a first aid kit."))  
		decision2_3(user_response)
  
    
def decision2_3(user_response):
#	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("The alien became infected because you did not take any precautions or clean your hands.")
#		user_response = int(input("1.option one\n2.option two\n3.option three"))
#		decision3_1(user_response)
	elif user_response == 2:
		print("The alien provies you with materials similar to antibacterial spray and bandages. You treat his wounds and he thanks you.")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_2(user_response)
	elif user_response == 3:
		print("You took too long and the alien died from loss of blood.")
	#	user_response = int(input("1.option one\n2.option two\n3.option three"))
		#decision3_3(user_response)
		
def decision3_1(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)

def decision3_2(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)
    
def decision3_3(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)
	
#This runs the game
user_name = input("Enter your name")
begin_story()
