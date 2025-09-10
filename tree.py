import time
print("You are on your morning walk when you see a starving monkey on the side of the road. It looks slightly violent and ravenous.")
time.sleep(1.5)
choice = input("1: Feed the monkey the banana in your pocket\n2: Pretend to ignore the monkey")
if choice == "1":
    print("The monkey was so hungry that it accidentally bites your finger.")
    time.sleep(1.5)
    choice = input("1: Forgive the monkey and take it in as your own\n2: Get angry at the monkey and run away")
    if choice == "1":
        print("You and the monkey grow close over the next couple months and become best friends. However, you start to notice the monkey is slightly foaming at the mouth.")
        time.sleep(1.5)
        choice = input("1: Take the monkey to the vet and spend all of your money\n2: Procrastinate on taking the monkey to the vet and use your money on groceries")
        if choice == "1":
            print("The monkey had rabies but it was too late to save it and it died shortly later. However, you got a rabies vaccine and lived a long and prosperous life.\nTHE END")
        elif choice == "2": 
            print("You speed away at 76 MPH, but since you suck at driving, you crash into a ditch and die.\nTHE END")
            print("Both you and the monkey die from rabies because you are lazy. However, because you helped the monkey in its time of need, you have such good karma that you are reborn as the prince of Saudi Araabia.\nTHE END")    
    elif choice == "2":
        print("The monkey starts chasing after you because it thinks you have more food in your pockets.")
        time.sleep(1.5)
        choice = input("1: Throw nuts and seeds at the monkey\n2: Hop in your car and drive away as fast as you can")
        if choice == "1":
            print("The monkey is not satisfied and it eats you alive.\nTHE END")
        elif choice == "2":
            print("You speed away at 76 MPH, but since you suck at driving, you crash into a ditch and die.\nTHE END")
elif choice == "2":
    print("The monkey is very sad and dejected and it dies all alone :(\nA couple days after you came across the monkey, you notice that the lights in your apartment start flickering every so often.")
    time.sleep(1.5)
    choice = input("1: Use all your money to call an electrician to get the lights fixed\n2: Use your Ouija board to determine if there is a ghost haunting you")
    if choice ==  "1":
        print("The electrician cannot find any problems in your apartment and you just wasted all your money. You got evicted the next week for not paying your bills.")
        time.sleep(1.5)
        choice = input("1: Ask your mom to stay at her house even though she kind of hates you\n2: Find an abandoned building to squat at")
        if choice == "1":
            print("You continue living with the guilt of the dead monkey. You eventually die from laziness because you never get a job and you eat chicken nuggets for every meal.\nTHE END")
        elif choice == "2":
            print("You die from hypothermia because the building has no insulation. Your last thoughts are full of regret for ignoring the poor starving monkey.\nTHE END")
    elif choice == "2":
        print("You ask the Ouija board if there is a spirit present. The board responds with 'BANANA.'")
        time.sleep(1.5)
        choice = input("1: Apologize to the monkey for ignoring it\n2: Scream and run away to stay at your mom's house for the night")
        if choice == "1":
            print("The monkey ghost is vengeful. The overhead chandelier falls down and you are crushed to death.\nTHE END")
        elif choice == "2":
            print("The monkey ghost locks your doors before you can escape. It starts throwing bananas at you so hard that you die from your injuries.\nTHE END")