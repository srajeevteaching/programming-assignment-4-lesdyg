import random

deck = []
deck2 =[0]*52
num=0

#function to start game
def start_game():

    for i in ["Spades","Clubs","Diamonds","Hearts"]:
            for x in range(2,15):
                if x == 11:
                    deck.append( "Jack of " + i)
                elif x == 12:
                    deck.append( "Queen of " + i)
                elif x == 13:
                    deck.append( "King of " + i)
                elif x == 14:
                    deck.append( "Ace of " + i)
                else:
                    deck.append( str(x) + " of " + i)
def shuffle(d):
    i=0
    second_array = [100]*52
    while i < len(d):
        x= random.randint(0,51)
        if second_array[x] == 100:
            second_array[x] = d[i]
            i=i+1
    return second_array


def convert(): #use to convert the strings into ints for counting
    for i in range(len(deck)):
        num=deck[i].find(" ")
        if deck[i][:num] == "Jack":
            deck2[i]= 10
        elif deck[i][:num] == "Queen":
            deck2[i]= 10
        elif deck[i][:num] == "King":
            deck2[i]= 10
        elif deck[i][:num] == "Ace":
            deck2[i]= 11
        else:
            deck2[i] = int(deck[i][:num])

def house(i,c,househand,housecount):
    ace=0
    for b in range(2):
        if deck2[b+2] == 11:
            ace+=1
    while(housecount<=c and housecount != 21):
        househand.append(deck[i])
        if deck2[i] == 11:
            ace+=1
        housecount += (deck2[i])
        i+=1
        if housecount >21:
            housecount =bust(housecount,ace)
            ace=ace -1
    if housecount >21:
        print("You Win, The House lost")
        print("the house had" , househand)

    else:
        print("you lost")
        print("the house had" , househand)
    return True
#bust function
def bust(c,a):
    for i in range(a):
        while c>21:
            c = c-10
    return c
#function play
def play():
    i=4
    y=0
    ace=0
    monkey=False
    convert()
    # print(deck2)
    count= deck2[0]+deck2[1]
    hand= [deck[0],deck[1]]
    housecount = deck2[2] + deck2[3]
    househand = [deck[2], deck[3]]
    print("The house has: " + deck[3])
    while y<2:
        if deck2[y]==11:
            ace=ace+1
        y+=1
    print("your hand is", hand )
    while monkey is False:
        while(count<21):
            x=input("would you like to hit or stay?")
            if x == "hit":
                hand.append(deck[i])#Adds Card name to string list, which we show to the user
                count += (deck2[i])# Adds Card value to the count list which keeps track of users card values
                if deck2[i] == 11:# Keeps Track of aces so in case the users busts, they can change their ACE to a 1
                    ace = ace + 1
                i+=1
                # print("hitloop "+str(count))
                print("your hand is ", hand)
            elif x == "stay":
                monkey =house(i,count,househand,housecount)
                break
            else:
                print("invalid, please type hit or stay")
        if count >21: #checks for aces in hand before calling the users bust
            count = bust(count,ace)
            ace=ace -1
            # print("countloop1 " + str(count))
            if count >21:
                # print("countloop2" + str(count))
                print("you lost")
                monkey=True
        elif count == 21:
            print("you win")
            monkey=True
#To implement choosing if ace is 1 or not implement bust() method
# if count > 21 call bust() and if a value in Hand is 11 change the value to 11
# run game
start_game()
deck=shuffle(deck)
play()















