import random
choice_list = ['Rock','Paper','Scissor']
user1 = str(raw_input("enter first user1 name: "))
user2 = str(raw_input("enter second user1 name: "))
while(1):
    user1_choice = str(raw_input("enter " + user1 + " choice among Rock,Paper,Scissor"))
    user2_choice = str(raw_input("enter " + user2 + " choice among Rock,Paper,Scissor"))
    if user1_choice == user2_choice:
        print("its a tie")
    if user1_choice == 'Rock' and user2_choice == 'Paper':
        print(user2 + " won,congrats and " + user1 + " loose")
    if user1_choice == 'Rock' and user2_choice == 'Scissor':
        print(user1 + " won,congrats and " + user2 + " loose")
    if user1_choice == 'Paper' and user2_choice == 'Scissor':
        print(user2 + " won,congrats and " + user1 + " loose")
    if user1_choice == 'Paper' and user2_choice == 'Rock':
        print(user1 + " won,congrats and " + user2 + " loose")
    if user1_choice == 'Scissor' and user2_choice == 'Rock':
        print(user2 + " won,congrats and " + user1 + " loose")
    if user1_choice == 'Scissor' and user2_choice == 'Paper':
        print(user1 + " won,congrats and " + user2 + " loose")
    if (user1_choice != 'Scissor' and user1_choice != 'Rock' and user1_choice != 'Paper') or (user2_choice != 'Scissor' and user2_choice != 'Rock' and user2_choice != 'Paper'):
        print("Invalid input")
    qut = str(raw_input("do you want to continue: Y/N"))
    if qut != 'Y' and qut != 'y':
        break
