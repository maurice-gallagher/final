import time
START = 1
QUIT = 2
def main():
    choice = 0
    while choice != QUIT:
        display_start_menu()
        try:
            choice = int(input('Enter your selection: '))
        except ValueError:
            time.sleep(1)
            print("Narrator: C'mon we haven't even started the damn game yet!")
            time.sleep(3)
            print("Narrator: Please just make a valid selection.")
        if choice == QUIT:
            time.sleep(1)
            print('Quitting game...')
            exit()
        if choice == START:
            return level_1()

def display_start_menu():
    print('1)START')
    print('2)QUIT')

print('Narrator: Hello?')
time.sleep(2)
print('Narrator: Hey, you...')
time.sleep(2)
print('Narrator: Wake up we have stuff to do.')
time.sleep(2)
print("Narrator: Hurry up, you don't wanna die again do you?")
time.sleep(2)
print("Narrator: I'm tired of always having to bring you back to life.")
time.sleep(2)
print("Narrator: Anyway, I'm your narrator, follow me.")
time.sleep(2)

def level_1():
    print("_________________________________________________________________________________")
    print("Narrator: Okay user, I haven't cared to learn your name, and I still don't.")
    time.sleep(3)
    print("Narrator: I mean, it's not like you will survive this game, it's IMPOSSIBLE!")
    time.sleep(3)
    print("Narrator: Okay, so, um I forgot what we were doing...")
    time.sleep(3)
    print("Narrator: Oh yeah! We are tutoring you with english right?")
    time.sleep(4)
    print("Narrator: No need for the silent treatment... I get it let's just get to the game.")
    time.sleep(3)
    print("Narrator: So, you are walking through the woods and see three pathways.")
    time.sleep(3)
    print("Narrator: Um, yeah three pathways.")
    time.sleep(3)
    print("Narrator: One on the right one in the middle and one on the left.")
    time.sleep(3)
    print("Narrator: Which one does...")
    time.sleep(3)
    print("Narrator: Uh...")
    time.sleep(2)
    print("Narrator: I guess I have to learn your name.")
    time.sleep(3)
    print("Narrator: What is your name?")
    time.sleep(2)
    input("Enter name: ")
    time.sleep(2)
    print("Narrator: Okay Jonny make a decision.")
    print("┌-----------┐")
    print("| 1) Right  |")
    print("| 2) Middle |")
    print("| 3) Left   |")
    print("└-----------┘")
    time.sleep(2)
   
    try:
        right_middle_left = int(input("Hurry up and enter your choice: "))
   
    except ValueError:
        print('')
        print("Narrator: Ugh I knew you were stupid but I didnt think it was THIS bad.")
        time.sleep(3)
        print("Narrator: Make a valid selection you idiot.")
        time.sleep(3)
        print("Narrator: You know what?")
        time.sleep(3)
        print("Narrator: Go back to the beginning of level one and listen to me talk again.")
        time.sleep(3)
        return level_1_dead()
   
    if right_middle_left == 1:
        print("_________________________________________________________________________________")
        print("Narrator: You walk down the path and hear a noise.")
        time.sleep(3)
        print("Narrator: It turns out to be a big bear and it mauls you to death.")
        time.sleep(3)
        print("Narrator: I knew it wouldn't be long until you died.")
        time.sleep(3)
        print("Narrator: Okay well back to the start of level one.")
        time.sleep(3)
        return level_1_dead()
    
    if right_middle_left == 2:
        print("_________________________________________________________________________________")
        print("You make your way down the middle path and...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("BOOM!!!")
        time.sleep(2)
        print("*A landmine that the narrator promises he did not place ")
        print("blew up at your feet causing your flesh to rip from your ")
        print("bones and killed you almost instantly.*")
        time.sleep(8)
        print("Narrator: That wasn't my mine I promise.")
        time.sleep(3)
        print("Narrator: We can just go back to the start of level one okay?")
        time.sleep(3)
        print("Narrator: No hard feelings right?")
        time.sleep(2)
        return level_1_dead()
        
    if right_middle_left == 3:
        print("_________________________________________________________________________________")
        print("Narrator: So you picked the path to the left.")
        time.sleep(3)
        print("Narrator: And nothing bad happens.")
        time.sleep(3)
        print("Narrator: Have you heard of beginners luck?")
        time.sleep(3)
        print("Narrator: You won't make it through the next level alive though!")
        time.sleep(2)
        return level_2()
        
def level_1_dead():
    print("_________________________________________________________________________________")
    time.sleep(1)
    print("Narrator: Okay now that we are here again let's actually do something right.")
    time.sleep(3)
    print("Narrator: So, three paths in the woods blah blah blah...")
    time.sleep(3)
    print("Narrator: Pick one.")
    print("┌-----------┐")
    print("| 1) Right  |")
    print("| 2) Middle |")
    print("| 3) Left   |")
    print("└-----------┘")
    
    try:
        right_middle_left_dead = int(input("which one does Andrew choose: "))
    except ValueError:
        print("Narrator: What are you doing Jake can you just follow simple directions or is that too hard for you?")
        time.sleep(3)
        print("Narrator: Time to start over.")
        return level_1_dead()
        
    if right_middle_left_dead == 1:
        print("_________________________________________________________________________________")
        print("Narrator: You walk down the path and hear a noise.")
        time.sleep(3)
        print("Narrator: It turns out to be a big bear and it mauls you to death.")
        time.sleep(3)
        print("Narrator: I knew it wouldn't be long until you died.")
        time.sleep(3)
        print("Narrator: Okay well back to the start of level one.")
        time.sleep(3)
        return level_1_dead()
    
    if right_middle_left_dead == 2:
        print("_________________________________________________________________________________")
        print("You make your way down the middle path and...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("BOOM!!!")
        time.sleep(2)
        print("*A landmine that the narrator promises he did not place ")
        print("blew up at your feet causing your flesh to rip from your ")
        print("bones and killed you almost instantly.*")
        time.sleep(8)
        print("Narrator: That wasen't my mine I promise.")
        time.sleep(3)
        print("Narrator: We can just go back to the start of level one okay?")
        time.sleep(3)
        print("Narrator: No hard feelings right?")
        time.sleep(2)
        return level_1_dead()
    
    if right_middle_left_dead == 3:
        print("_________________________________________________________________________________")
        print("Narrator: It took you long enough you might as well give up now.")
        time.sleep(3)
        print("Narrator: So you picked the path to the left.")
        time.sleep(3)
        print("Narrator: And nothing bad happens.")
        time.sleep(3)
        print("Narrator: You won't make it through the next level alive though!")
        time.sleep(2)
        return level_2()
        
    
    try:
        right_middle_left_error = int(input("Hurry up and enter your choice: "))
    
    except ValueError:
        print('')
        print("Narrator: Ugh I knew you were stupid but I didnt think it was THIS bad.")
        time.sleep(3)
        print("Narrator: Make a valid selection you idiot.")
        time.sleep(3)
        print("Narrator: You know what?")
        time.sleep(3)
        print("Narrator: Go back to the beginning of level one and listen to me talk again.")
        time.sleep(2)
        return level_1_dead()

def level_2():
    print("_________________________________________________________________________________")
    print("Narrator: Okay level two, here we are.")
    time.sleep(3)
    print("Narrator: You reach the end of the path and see an old lady.")
    time.sleep(3)
    print("Narrator: She looks very thirsty and sad.")
    time.sleep(3)
    print("Narrator: I don't expect someone like you to help her.")
    time.sleep(3)
    print("Narrator: I mean you really probably aren't a good person.")
    time.sleep(3)
    print("Narrator: You haven't even said a word to me this whole time!")
    time.sleep(4)
    print("Narrator: Anyway, back to this old lady.")
    time.sleep(3)
    print("Narrator: you have 2 options.")
    time.sleep(2)
    print("┌-------------------------------------------------------┐")
    print("| 1) Help her and give her water like a good person     |")
    print("| 2) Walk away like the terrible person I knew you were |")
    print("└-------------------------------------------------------┘")
    
    try:
        old_lady = int(input("which one does Nicholas choose: "))
    except ValueError:
        print("Narrator: What are you doing Fredrick can you just follow simple directions or is that too hard for you?")
        time.sleep(3)
        print("Narrator: Time to start over.")
        return level_2_dead()
    if old_lady == 1:
        print("_________________________________________________________________________________")
        time.sleep(2)
        print("Old lady: Thank you young human.")
        time.sleep(3)
        print("Old lady: Now I am strong enough to transform.")
        time.sleep(3)
        print("Narrator: Well that was a stupid idea.")
        time.sleep(3)
        print("Narrator: When have I ever lead you the right way or been nice?")
        time.sleep(3)
        print("Narrator: Any smart person would have known to not pick my way.")
        time.sleep(3)
        print("Narrator: You deserve this.")
        time.sleep(3)
        print("*The old lady suddenly transforms into a big squid,")
        print(" grabs you with her tenticles, and forces you into her beak* ")
        time.sleep(3)
        print("Narrator: Hopefully you know not to trust me now.")
        return level_2_dead()
    
    if old_lady == 2:
        print("_________________________________________________________________________________")   
        print("Narrator: You are a terrible person, I knew this was the real you.")
        time.sleep(4)
        print("Narrator: But that was a good choice don't talk to strangers.")
        time.sleep(3)
        print("Narrator: You move on to level 3 with the sounds of a dying old woman behind you.")
        time.sleep(4.5)
        return level_3()

def level_2_dead():
    print("_________________________________________________________________________________")
    time.sleep(2)
    print("Narrator: Okay now I have no hope for you.")
    time.sleep(3)
    print("Narrator: Let's just get this over with.")
    time.sleep(3)
    print("Narrator: Help the old lady or no?")
    time.sleep(2)
    print("┌-------------------------------------------------------┐")
    print("| 1) Help her and give her water like a good person     |")
    print("| 2) Walk away like the terrible person I knew you were |")
    print("└-------------------------------------------------------┘")

    try:
        old_lady_dead = int(input("which one does Nash choose: "))
    except ValueError:
        print("Narrator: What are you doing Gregory can you just follow simple directions or is that too hard for you?")
        time.sleep(3)
        print("Narrator: Time to start over.")
        return level_2_dead()
    
    if old_lady_dead == 1:
        print("_________________________________________________________________________________")
        time.sleep(2)
        print("Old lady: Thank you young human.")
        time.sleep(3)
        print("Old lady: Now I am strong enough to transform.")
        time.sleep(3)
        print("Narrator: Well that was a stupid idea.")
        time.sleep(3)
        print("Narrator: When have I ever lead you the right way or been nice?")
        time.sleep(3)
        print("Narrator: Any smart person would have known to not pick my way.")
        time.sleep(3)
        print("Narrator: You deserve this.")
        time.sleep(3)
        print("*The old lady suddenly transforms into a big squid,")
        print(" grabs you with her tenticles, and forces you into her beak* ")
        time.sleep(3)
        print("Narrator: Hopefully you know not to trust me now.")
        return level_2_dead()
    
    if old_lady_dead == 2:
        print("_________________________________________________________________________________")
        time.sleep(2)
        print("Narrator: Okay well it isn't even like you were playing the game anymore.")
        time.sleep(3)
        print("Narrator: You just had to pick the other option.")
        time.sleep(3)
        print("Narrator: Anyway...")
        time.sleep(2)
        print("Narrator: You are a terrible person, I knew this was the real you.")
        time.sleep(4)
        print("Narrator: But that was a good choice don't talk to strangers.")
        time.sleep(3)
        print("Narrator: You move on to level 3 with the sounds of a dying old woman behind you.")
        time.sleep(4.5)
        return level_3()
        
def level_3():
    print("_________________________________________________________________________________")
    print("Narrator: SO...")
    time.sleep(3)
    print("Narrator: You walk into town and see two adjacent buildings.")
    time.sleep(3)
    print("Narrator: One is an arcade and one is a library.")
    time.sleep(3)
    print("Narrator: if I were you I would pick the arcade it sounds like a lot more fun.")
    time.sleep(3)
    print("Narrator: But that's just me...")
    time.sleep(3)
    print("Narrator: So, which one do you choose?")
    time.sleep(3)
    print("┌--------------------------------------┐")
    print("|1) Go to the Library                  |")
    print("|2) Go to the super fun looking arcade |")
    print("└--------------------------------------┘")  
    
    try:
        town = int(input("which one does Nash choose: "))
    except ValueError:
        print("Narrator: What are you doing mason can you just follow simple directions or is that too hard for you?")
        time.sleep(3)
        print("Narrator: Time to start over.")
        return level_3_dead()
    
    if town == 1:
        time.sleep(2)
        print("Narrator: Oh... Okay I guess the boring Library...")
        time.sleep(3)
        print("Narrator: Okay here we go.")
        return library()
    if town == 2:
        time.sleep(1)
        print("Narrator: YES!!")
        time.sleep(1)
        print("Narrator: THE ARCADE IS MY FAVORITE!!")
        time.sleep(3)
        print("Narrator: Okay, sorry about that...")
        time.sleep(3)
        print("Narrator: We make our way to the arcade.")
        return arcade()

def library():
    print("_________________________________________________________________________________")
    print("Narrator: You walk into the really boring library and sit in a chair.")
    time.sleep(3)
    print("Narrator: It is completely silent in the library.")
    time.sleep(3)
    print("Narrator: No one else in here can hear me because they aren't insane like you.")
    time.sleep(3)
    print("Narrator: Out of nowhere your phone starts ringing at top volume.")
    time.sleep(3)
    print("Narrator: You fiddle with your tightly buttoned pocket.")
    time.sleep(3)
    print("Narrator: The librarian becomes furious and glares at you.")
    time.sleep(3)
    print("Narrator: As you continue to fiddle with your pocket the librarian calls security.")
    time.sleep(3)
    print("Librarian: SECURITY THROW THAT HUMAN OUT OF HERE!!!")
    time.sleep(3)
    print("Narrator: You see a very large man walking towards you and you freeze in fear.")
    time.sleep(3)
    print("Narrator: He grabs you and throws you out of the doors onto your head.")
    time.sleep(3)
    print("Narrator: You bleed out on the pavement.")
    time.sleep(3)
    print("Narrator: I told you to go to the arcade, you should have listened to me")
    time.sleep(3.5)
    print("Narrator: Okay back to town we go!")
    return level_3_dead()

def arcade():
    print("_________________________________________________________________________________")
    print("Narrator: WE WALK INTO THE ARCADE AND START PLAYING A FUN GAME!!!")
    time.sleep(1)
    print("Narrator: IT'S CALLED ASMUND AND IT IS MY FAVORITE GAME!")
    time.sleep(1)
    print("Narrator: I AM TALKING SO FAST BECAUSE I AM EXCITED!")
    time.sleep(1)
    print("Narrator: LET'S JUST SIT AND PLAY THIS GAME FOREVER")
    time.sleep(3)
    print("*You and the narrator become best of friends over the great game Asmund.")
    print("You share laughs and tears together and sit in the arcade playing the ")
    print("game for eternity.*")
    time.sleep(10)
    print("┌--------------------------------------┐")
    print("|              DON'T DIE               |")
    print("└--------------------------------------┘")
    exit()

def level_3_dead():
    print("_________________________________________________________________________________")
    print("Narrator: Okay so since you died can we go to the arcade????")
    time.sleep(3)
    print("Narrator: PLEEEEAAASSSEEE????")
    time.sleep(3)
    print("┌-------┐")
    print("|1) yes |")
    print("|2) yes |")
    print("└-------┘")
    
    try:
        town_dead_choice = int(input("which one does Nash choose: "))
    except ValueError:
        print("Narrator: What are you doing Josh can you just follow simple directions or is that too hard for you?")
        time.sleep(3)
        print("Narrator: Time to start over.")
        return level_3_dead()
    if town_dead_choice == 1:
        print("Narrator: YES!")
        time.sleep(2)
        return arcade()
    if town_dead_choice == 2:
        print("Narrator: YES!")
        time.sleep(2)
        return arcade()
        
main()