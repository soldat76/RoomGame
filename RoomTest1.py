## RoomTest1.py
##
## This program serves as a test for future iterations of text-based adventure.
##
## Aster Fan
##
## June 2017

print("\nYou wake up in a room. There is a DOOR in the room.") # Introductory statement.

x = 1 # First part starts here.
while x == 1:
    userDecision = input("\nWhat will you do?: ")
    userDecision = userDecision.lower()
    if "go to door" in userDecision or "unlock door" in userDecision or "open door" in userDecision:
        print("\n\n\nThe door is locked. There seems to be a KEY on the ground.")
        x = 2
        break
    elif "door" in userDecision:
        print("\n\n\nWhat do I do with the door?")
        print("\nThere is an unopened DOOR in the room.")
    else:
        print("\n\n\nI don't understand...")
        print("\nThere is a DOOR in the room.")
        
while x == 2:
    userDecision = input("\nWhat will you do?: ")
    userDecision = userDecision.lower()
    if "pick up key" in userDecision or "get key" in userDecision:
        print("\n\n\nYou pick up the key on the ground.")
        x = 3
        break
    elif "key" in userDecision:
        print("\n\n\nWhat should I do to the key?")
        print("\nThere is a key on the ground.")
    else:
        print("\nI don't understand...")
        print("\n\n\nThe door is locked. There seems to be a KEY on the ground.")


print("\nYou have the key now. It might just fit inside the DOOR.")
while x == 3:
    userDecision = input("\nWhat will you do now?: ")
    userDecision = userDecision.lower()
    if "unlock door" in userDecision or "open door" in userDecision:
        print("\nYou unlock the door and step outside the room. End of game.")
        break
    else:
        print("\n\n\nI don't understand...")
        print("\nYou have the key to the DOOR now.")
