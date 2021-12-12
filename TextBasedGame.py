#Dwaine Brannon
#Stan Wars

#A Function to show instructions
def show_instructions():
    #Print a main menu and the commands
    print('Welcome to Stan Wars.')
    print("The goal is to cancel your fav popstar arch nemesis by finding items you find throughout the rooms in their home")
    print("They have been subtweeting ur fav all day long, what r u gonna do about it bestie?")
    print('Find the items 6 to get them cancelled before THEY cancel YOU')
    print('To navigate between rooms, enter: Go (Direction on compass)')
    print('If you find an item in a room, type get(item name)')
    print('Good luck bestie.')

#player status function
def show_status(current_room, player_inventory, room_item):
    print('You are in:', current_room)
    print('Inventory:',player_inventory)
    print('This room contains item:', room_item)
#Get item function
def get_item(item):
    player_inventory.append(item)


#main gameplay function
def main():
    rooms = {
        'Foyer': {'South': 'Kitchen', 'East': 'Bathroom'},
        'Bathroom': {'West': 'Foyer', 'South': 'Dining Room', 'item':'Vaccine Balls'},
        'Dining Room': {'West': 'Kitchen', 'South':'TV Room', 'item':'Homophobic Tweets'},
        'Kitchen':{'North':'Foyer', 'East':'Dining Room', 'South':'Great Hall', 'West': 'Awards Room', 'item':'Mesh Mask'},
        'Awards Room':{'East':'Kitchen','item':'Tax Returns'},
        'TV Room': {'North':'Dining Room', 'South' : 'Great Hall','item':'Rumors'},
        'Great Hall':{'North':'Kitchen','West':'Luxury Bedroom', 'item':'YourFavIsProblematic Tumblr Post'},
        'Luxury Bedroom':{'item':'Boss'}

    }
    #Give instrucitons
    show_instructions()
    directions=['Go South', 'Go North', 'Go East', 'Go West']
    items = ['Get Vaccine Balls', 'Get Homophobic Tweets', 'Get Mesh Mask', 'Get Tax Returns', 'Get Rumors','Get YourFavIsProblematic Tumblr Post', 'Boss']

    player_inventory_count = 0
    current_room = 'Foyer'
    player_action = ''
    player_inventory = []
    room_item = ''
    while True:
        show_status(current_room, player_inventory,room_item)
        if room_item == 'Boss':
            if player_inventory_count != 6:
                print('Oh no...they found you. ur cancelled. Game over bestie')
                break
            if player_inventory_count == 6:
                print('YOU DID IT QUEEN. YOU BEAT THE BOSS. NOW THEY GONNA GET CANCELLED')
                break
        if room_item != 'Boss':
            player_action = input('What do you want to do? \n') #Action input
            if player_action in directions:
                player_action = player_action.split()[1]
                if player_action in rooms[current_room]: #If the player inputs a direction
                     current_room = rooms[current_room][player_action] #Update current room
                     if current_room != 'Foyer':
                        room_item = rooms[current_room]['item']#from function, it should show us the room item
                     elif current_room == 'Foyer':
                        room_item = None
                else:
                    print("Invalid Command") #invalid direction
            elif player_action in items:
                room_item = rooms[current_room]['item']
                player_inventory.append(room_item)
                player_inventory_count += 1
            else:
                    print('Chile...that aint in here..')



main()