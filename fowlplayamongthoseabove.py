#fowlplayamongthoseabove.py
#a Python program creating a text-based adventure game based off of the DnD campaign: Fowl Play Among Those Above

#import items from tkinter
from tkinter import *
from tkinter.ttk import *
from pygame import mixer
start_sound= 'mixkit-medieval-show-fanfare-announcement-226.wav'
gameover_sound= 'mixkit-player-losing-or-failing-2042.wav'
select_sound= 'mixkit-extra-bonus-in-a-video-game-2045.wav'


root= Tk() #making tkinter window

photo = PhotoImage(file = r"Fowl Play Among Us-2-1.png") #Creating a photoimage object to use image

Button(root, image= photo).pack(side = TOP) # image set on button

root.after(8000, root.destroy) #after 4 seconds, the title screen will disappear
mixer.init()
mixer.music.load(start_sound) #epic start up music
mixer.music.set_volume(2.5)
mixer.music.play(loops=0)
mainloop()

from termcolor import colored


def start():
    print()
    print("Why are your memories so foggy?")
    print("Who are you...? Where are you?")
    print("You cannot even recall your name...")
    print()
    print(colored("You are currently standing in the void. Or. Uh. Hovering. I guess.", "blue", attrs= ['bold']))
    print(colored("You can stay in this endless void, if you so choose.", "blue", attrs= ['bold']))
    print()
    print("Stay in the void?\n(yes or no)")
    voidansw= input().lower() #user input will be lowercase
    if 'y' in voidansw:
        void_room()
    elif 'n' in voidansw:
        proceed()
    else:
        #if the player typed something else  
        game_over("I said yes or no, meaning yes or no")

def selection_sound(): #sound that plays when user makes a choice that doesn't lead to a game over
    mixer.init()
    mixer.music.load(select_sound) 
    mixer.music.set_volume(2.5)
    mixer.music.play(loops=0)



def void_room():
    print()
    print(colored("Oh. So you wanted to stay here.", "blue", attrs= ['bold']))
    print(colored("That's cool, I guess...", "blue", attrs= ['bold']))
    print(colored("...", "blue", attrs= ['bold']))
    print(colored("Well, there's really nothing left here, so I guess I'm going to give you a game over.", "blue", attrs= ['bold']))
    game_over("You wanted to stay in the void")
def proceed():
    selection_sound()
    print()
    print(colored("So you wish to leave this void.", "blue", attrs= ['bold']))
    print(colored("Excellent.", "blue", attrs= ['bold']))
    print(colored("In order to leave, there's a simple term you must follow.", "blue", attrs= ['bold']))
    print (colored("You must join a group of...adventurers of sorts.", "blue", attrs= ['bold']))
    print()
    print ("Will you agree to these terms?\n(yes or no)")
    adventureansw= input().lower()
    if 'y' in adventureansw:
        warp_room()
    elif 'n' in adventureansw:
        stuck_in_void()
    else:
        game_over ("What part of yes or no do you not understand?")
def stuck_in_void():
    print()
    print (colored("Oh?", "blue", attrs= ['bold']))
    print (colored("So you don't agree to my terms?", "blue", attrs= ['bold']))
    print (colored("Very well. Have fun in the eternal nothingness", "blue", attrs= ['bold']))
    game_over ("You didn't agree to the terms.")
def warp_room():
    selection_sound()
    print()
    print (colored("Great.", "blue", attrs= ['bold']))
    print (colored("You should be on your way then.", "blue", attrs= ['bold']))
    print (colored("Are you all ready to go?","blue", attrs= ['bold']))
    print ("(yes or no)")
    leaveansw= input().lower()
    if 'y' in leaveansw:
        selection_sound()
        print()
        print(colored("Great. Do not disappoint me", "blue", attrs= ['bold']))
        outside_of_dungeon()
    elif 'n' in leaveansw:
        selection_sound()
        print()
        print (colored("That sucks because I'm ready for you to leave. Get out of my realm and do not disappoint me.", "blue", attrs= ['bold']))
        outside_of_dungeon()
    else:
        selection_sound()
        print()
        print (colored("I don't know what the heck you're talking about, it was a yes or no answer", "blue", attrs= ['bold']))
        print (colored("Whatever, just get out of here. You're lucky I'm not giving you a game over", "blue", attrs= ['bold']))
        outside_of_dungeon()
def outside_of_dungeon():
    print()
    print ("You are standing in what appears to be a heavily wooded area.") 
    print ("In a distance, you can make out the sounds of a few different voices.")
    print()
    print ("Will you approach the sounds?\n(yes or no)")
    soundansw= input().lower()
    if 'y' in soundansw:
        approach()
    elif 'n' in soundansw:
        stay()
    else:
        game_over("These instructions are so simple to follow, why do you fail me so?")
def stay():
    selection_sound()
    print()
    print("You decide to stay put, hidden in the thicket.")
    print("You're able to make out a little bit of the conversation from the voices...")
    print(colored("???: 'Tell me why we're doing this?'", "magenta"))
    print(colored("???: 'Because we said we would.'", "green"))
    print(colored("???: 'Yeah, we said. That doesn't mean we actually have to.'", "magenta"))
    print(colored("???: 'Quack'", "yellow", attrs= ['bold']))
    print(colored("???: 'We can't just lie to a God, Rue.'", "red"))
    print(colored("???: 'Says who?'", "magenta"))
    print("Weren't you supposed to join a group of adventurers?")
    print("That is what you promised that...weird voice thing in that void place")
    print("These, what you assume to be people, must be the group of adventurers that voice refrenced")
    print()
    print("Will you approach the adventurers?\n(yes or no)")
    adventureansw= input().lower()
    if 'y' in adventureansw:
        approach()
    elif 'n' in adventureansw:
        wolfdeath()
    else:
        game_over("Booooo. That's me booing you off stage since you can't follow instructions.")
def wolfdeath():
    print()
    print("You decide to stay in the thicket, however...")
    print("Soon enough, you hear the sounds of rustling behind you. As if a creature was appraoching.")
    print("Before you have enough time to do anything, you feel something jump at you from behind!")
    print("You loose your balance and fall to the ground!")
    print("Oh no! A giant wolf is on top of you, it's sharp teeth is all you can see!")
    print("The creature sinks its jaws into your skin without hesitation.")
    game_over("Those sharp teeth are the last thing you ever saw again.")
def approach():
    selection_sound()
    print("You walk toward the sounds and come across a group of 5")
    print("Two appear to be human. Two appear to be elves. And one appears to be...")
    print("Uh...you don't know...are those fangs?")
    print("One of the elves seem to have a duck with green hair sitting on her shoulder.")
    print("The other seems to have antlers.")
    print("As you step closer, you step on a twig, causing all eyes of the group to land on you")
    print("The elf with the duck opens her mouth to speak, but before she can...")
    print("A massive wolf jumps out from the thicket! It's growling, and doesn't look happy")
    print()
    print("What do you do? (1 or 2)")
    print("1= Throw the large stick by your feet at the wolf")
    print("2= Let the others handle it")
    wolfansw= input()
    if wolfansw == "1":
        stick()
    elif wolfansw == "2":
        stand()
    else:
        game_over("I said 1 or 2. Not 1 or 2 or whatever you just typed.")
def stand():
    selection_sound()
    print()
    print("You, somewhat awkwardly, just stand there. The others got this, right?")
    print("The fanged member of the party was quick to lunge at the wolf.")
    print("Yeah, you were right! They got this.")
    print(colored("Elf w/ Antlers: 'Gale, WAIT!'", "green"))
    print("Oh, looks like that elf didn't want that wolf to get hurt.")
    print("Before, who you assume to be Gale, could reach the wolf...")
    print("The creature suddenly began barreling toward...you!")
    print()
    print("Quick! What're you going to do?! (1 or 2)")
    print("1= Throw the stick by your feet at the wolf")
    print("2= RUN!")
    anotherwolfansw= input()
    if anotherwolfansw == "1":
        stick()
    elif anotherwolfansw == "2":
        rundeath()
    else:
        game_over("Go stand in the corner and think about why you can't correctly type 1 or 2")
def rundeath():
    print()
    print("You turn on your heel and run from the massive beast, letting out a shriek as you do so")
    print("Sure, you can run fast...but the beast can run faster!")
    print("Within moments, the massive wolf is on top of you!")
    print("Before anything can be done, the massive teeth of the wolf is sinking into your skin.")
    print("As you feel your life draining from your body, you can make out a voice...")
    print(colored("Gale: 'I don't think we can save them...so can I have their blood?'", "cyan"))
    print(colored("???: 'Gale, can you stop talking for at least five minutes?'", "magenta"))
    game_over("You're dead and Gale is probably going to drink your blood.")
def stick():
    selection_sound()
    print()
    print("You reach down and pick up the stick from the ground")
    print("You feel sort of strange...it was hard to find words to describe the feeling.")
    print("You look down at your hand and notices vines are emitting from the stick...")
    print("Woah! And wrapping around yourself.")
    print("Before you can even question what was going on, the wolf suddenly jumps at you!")
    print("You point the stick at the wolf, letting out a shriek as you anticipate pain...")
    print("...But the pain of being ripped to shreds never comes.")
    print("Vines from the ground sprouted out and wrapped around the creatures limbs!")
    print("The wolf is now restrained to the forest floor.")
    print("Uh...did YOU do that?")
    print(colored("Elf w/ Duck: 'Did any of you do that, or...?'", "yellow"))
    print()
    print("Will you say anything? (1 or 2)")
    print("1= Say nothing")
    print("2= Speak up")
    speakingansw= input()
    if speakingansw == "1":
        silence()
    if speakingansw == "2":
        speak()
def speak():
    selection_sound()
    print()
    print("You take a breath, before opening your mouth")
    print(colored("You: 'I think it could have been because of this?'", "blue"))
    print("You hold up the stick, that still is interwined to your hand by vines.")
    print("Come to think of it...could you even get this stick off?")
    print(colored("Female Human: 'Oh, no. It was me. I did it.'", "magenta"))
    print(colored("Male Human: 'Really?'", "red"))
    print(colored("Female Human: 'No, I just thought it would be funny if I said I did.'", "magenta"))
    print(colored("Elf w/ Duck: '...Anyways.'", "yellow"))
    print("The elf turns to face you, a friendly aura surrounds her. You feel at ease.")
    print(colored("Poloma: 'My name is Poloma! That's a cool stick. What's your name?'", "yellow"))
    print("Your name...you still can't remember. Why can't you remember?")
    print("The confusion on your face must have been clear. Poloma offered you a smile")
    print(colored("Poloma: 'That's okay! Sometimes Rue forgets her name when she drinks too much.'", "yellow"))
    print(colored("Female Human whose probably Rue: 'No I don't-'", "magenta"))
    print(colored("Poloma: 'I'll just introduce you to everyone. So that's Rue!'", "yellow"))
    print("Poloma then points over to the elf, still knelt down by the wolf")
    print(colored("Poloma: 'Wyn.'", "yellow"))
    print(colored("Wyn: 'Hello...'", "green"))
    print("Then, she points to the human male")
    print(colored("Poloma: 'Anton.'", "yellow"))
    print(colored("Anton: 'Nice to meet you. I hope you're not hurt or anything.'", "red"))
    print("Then, toward the fanged...uh, creature")
    print(colored("Poloma: 'Gale.'", "yellow"))
    print(colored("Gale: 'That's me.'", "cyan"))
    print("She then points to herself again")
    print(colored("Poloma: 'Poloma!'", "yellow"))
    print(colored("Anton: 'Poloma, you said yourself twice.'", "red"))
    print(colored("Poloma: 'Shhh. Anyways, we're about to go in that cave.'", "yellow"))
    print("Poloma points toward the inside of the cave.")
    print("You sense a sort of danger coming from inside.")
    print(colored("Poloma: 'We promised a God named Canner we'd get something for him in there.'", "yellow"))
    print(colored("Poloma: 'Do you wanna come with us? We'll share the reward with you!'", "yellow"))
    print("That thing in the void...it did say you had to join a group of aventurers.")
    print("It must be these people. What would happen if you disobeyed that voice?")
    print(colored("Poloma: 'Sooo, are you in?'", "yellow"))
    print("Will you join them? \n(yes or no)")
    joinansw= input().lower()
    if 'y' in joinansw:
        user_joins()
    elif 'n' in joinansw:
        user_nojoin()
    else:
        game_over("You had one job: choose y or n. Foolish mortal.")

def silence():
    selection_sound()
    print()
    print(colored("Female Human: 'Me. It was me.'", "magenta"))
    print(colored("Male Human: 'I didn't know you knew a spell like that...'", "red"))
    print(colored("Female Human: 'That's cause I don't.'", "magenta"))
    print(colored("Male Human: 'Huh??'", "red"))
    print(colored("Female Human: 'I thought it'd be funny to lie about it.'", "magenta"))
    print("You notice the elf with the duck is looking at you.")
    print(colored("Elf w/ Duck: 'Was it you? That stick looks kinda magical.'", "yellow"))
    print("You glance down at the stick, the vines are still wrapped around your hand.")
    print("Maybe this stick was magical. Or something like that, anyways.")
    print(colored("Elf w/ Duck: '...Anyways.'", "yellow"))
    print("The elf turns to face you, a friendly aura surrounds her. You feel at ease.")
    print(colored("Poloma: 'My name is Poloma! What's your name?'", "yellow"))
    print("Your name...you still can't remember. Why can't you remember?")
    print("The confusion on your face must have been clear. Poloma offered you a smile")
    print(colored("Poloma: 'That's okay! Sometimes Rue forgets her name when she drinks too much.'", "yellow"))
    print(colored("Female Human whose probably Rue: 'No I don't-'", "magenta"))
    print(colored("Poloma: 'I'll just introduce you to everyone. So that's Rue!'", "yellow"))
    print("Poloma then points over to the elf, still knelt down by the wolf")
    print(colored("Poloma: 'Wyn.'", "yellow"))
    print(colored("Wyn: 'Hello...'", "green"))
    print("Then, she points to the human male")
    print(colored("Poloma: 'Anton.'", "yellow"))
    print(colored("Anton: 'Nice to meet you. I hope you're not hurt or anything.'", "red"))
    print("Then, toward the fanged...uh, creature")
    print(colored("Poloma: 'Gale.'", "yellow"))
    print(colored("Gale: 'That's me.'", "cyan"))
    print("She then points to herself again")
    print(colored("Poloma: 'Poloma!'", "yellow"))
    print(colored("Anton: 'Poloma, you said yourself twice.'", "red"))
    print(colored("Poloma: 'Shhh. Anyways, we're about to go in that cave.'", "yellow"))
    print("Poloma points toward the inside of the cave.")
    print("You sense a sort of danger coming from inside.")
    print(colored("Poloma: 'We promised a God named Canner we'd get something for him in there.'", "yellow"))
    print(colored("Poloma: 'Do you wanna come with us? We'll share the reward with you!'", "yellow"))
    print("That thing in the void...it did say you had to join a group of aventurers.")
    print("It must be these people. What would happen if you disobeyed that voice?")
    print(colored("Poloma: 'Sooo, are you in?'", "yellow"))
    print("Will you join them? \n(yes or no)")    
    joinansw= input().lower()
    if 'y' in joinansw:
        user_joins()
    elif 'n' in joinansw:
        user_nojoin()
    else:
        game_over("Tonight I'm making cookies and you get NONE.")
    


def user_nojoin():
    print()
    print("You shake your head. Go in a spooky cave with these random people? No thanks.")
    print("Poloma visibly seemed a little disappointed...but...")
    print(colored("Poloma: 'It's okay. I understand. I'm a little scared to go in there too.'", "yellow"))
    print("...but she seemed understanding")
    print("Rue appeared to drag Wyn away from the restrained wolf, uttering a 'he'll be fine' as she did so")
    print("Poloma offered you one last smile and a wave")
    print("Then, the group made their way into the cave.")
    print()
    print(colored("It would appear as though you did not join the group of adventurers.", "blue", attrs= ['bold']))
    print()
    print("That voice...it sounded like the one from the void.")
    print()
    print(colored("Just who do you think you are?", "blue", attrs= ['bold']))
    print()
    print("The vines wrapped around your arm seem to tighten.")
    print("Before you know it, a force throws the stick in your hand onto the ground")
    print("The vine wrapped around your arm yanks you down. The stick sinks into the dirt.")
    print("Soon enough, you begin to sink into the dirt.")
    print("As you're dragged into the earth, you think back to the mysterious voice...")
    print("Maybe this wouldn't be happening if you hadn't disobeyed it.")
    game_over("You should've obeyed the terms you agreed to.")



def user_joins():
    selection_sound()
    print()
    print("Poloma's face seems to light up. She seems...excited?")
    print(colored("Poloma: 'Wow! I didn't think you'd actually join us.'", "yellow"))
    print("Rue wandered over to Wyn, who was still by the wolf.")
    print(colored("Rue: 'Wyn, he'll be fine.'", "magenta"))
    print(colored("Wyn: 'He's a she.'", "green"))
    print(colored("Rue: 'My bad.'", "magenta"))
    print("With that, Rue grabbed Wyn and began to pull him away from the creature.")
    print(colored("Anton: 'We only have until sundown to get this done, so we need to hurry.'", "red"))
    print("Until sundown? To do what?")
    print(colored("Anton: 'We promised a God we'd get back something stolen from him.'", "red"))
    print(colored("Poloma: 'His name is Canner and he's gonna turn us into ducks if we're late.'", "yellow"))
    print(colored("Duck on Poloma's shoulder: 'Quack.'", "yellow", attrs= ['bold']))
    print(colored("Poloma: 'Oh, yeah! This is my duck, his name is Henry.'", "yellow"))
    print("Ducks were...an oddly specific thing to be turned into. You decide not to question it.")
    print("One by one, the group filed into the cave.")
    print("As you step inside, you feel a chill run down your spine. This place is spooky.")
    print("The group is mostly quiet as you all venture deeper into the cave. However...")
    print("Soon enough, the passage way splits into two, leaving the group with a choice.")
    print(colored("Rue: 'Well this is a problem.'", "magenta"))
    print(colored("Gale: 'I say we go left.'", "cyan"))
    print(colored("Rue: 'No way. Let's go right.'", "magenta"))
    print(colored("Henry: 'Quack.'", "yellow", attrs= ['bold']))
    print(colored("Poloma: 'Henry's looking left, so we both say left.'", "yellow"))
    print(colored("Rue: 'Wait, why does Henry get a vote?'", "magenta"))
    print(colored("Poloma: 'Don't discriminate against Henry just cause he's a duck, Rue.'", "yellow"))
    print(colored("Anton: 'I...guess we should go right?'", "red"))
    print(colored("Wyn: 'I vote right, too.'", "green"))
    print("All eyes land on you...oh no...")
    print("That was three and three! You're left as the tie breaker!")
    print()
    print("Which way do you want to go? (1 or 2)")
    print("1= Left")
    print("2= Right")
    directionansw= input()
    if directionansw== "1":
        print()
        print(colored("You: 'Let's head left.'", "blue"))
        print(colored("Rue: 'I'm taking your disagreement personally.'", "magenta"))
        left_path()
    elif directionansw== "2":
        print()
        print(colored("You: 'Let's head right.'", "blue"))
        right_path()
    else:
        game_over("It was a simple question, bro")



def right_path():
    selection_sound()
    print()
    print("The party begins to wander down the right path.")
    print("It's pretty dark, you can't see too far ahead of yourself, which is unsettling.")
    print("After a few minutes of walking, you and the party stumble across...")
    print("A small wooden table! There's a mysterious vial. It has a label on it that reads 'drink me'.")
    print("You realize that behind the table is a stone wall- clearly a dead end.")
    print(colored("Rue: 'Uh. I knew this was the wrong way, I was just testing the rest of you.'", "magenta"))
    print(colored("Poloma: 'Really?'", "yellow"))
    print(colored("Rue: 'Yes. You all fail.'", "magenta"))
    print("Anton shoots Rue a look, much like one a disapproving father would give.")
    print(colored("Wyn: 'Anyways...we should probably leave that there. It could be poison.'", "green"))
    print(colored("Poloma: 'Or it could taste really good.'", "yellow"))
    print(colored("Rue: 'Or it could give us super powers or something...'", "magenta"))
    print(colored("Anton: 'Poloma. Rue. Absolutely not.'", "red"))
    print(colored("Gale: 'Who cares? Let's just start heading in the right direction.'", "cyan"))
    print("That vial seems appealing to you...")
    print("It's almost as if a little voice is whispering to you. Begging you to drink it.")
    print("What's the worst that can happen, anyways?")
    print()
    print("Are you going to drink the mysterious liquid?\n(yes or no)")
    vialansw= input().lower()
    if 'y' in vialansw:
        print()
        print("Ah! You can't take it!")
        print("You just NEED to drink it!")
        print("It'll probably be fine!")
        print("Without saying anything, you step forward and grab the vial.")
        print(colored("Anton: 'Hey, what're you doing? You don't know what's in there.'", "red"))
        print(colored("Wyn: 'Yeah, don't drink that!'", "green"))
        print(colored("Gale: 'Idiot.'", "cyan"))
        print("Their voices seem so far away...your body seemed to be moving on it's own.")
        print("You unscrew the top of the vial.")
        print("You press the rim of the glass to your lips.")
        print("You tilt it back and allow the liquid to spill into your mouth.")
        print("And, you drink it.")
        print("...")
        print("Oh, hey. You were right. It was fine.")
        print("...")
        print("Suddenly, an agonizing pain burns throughout your body.")
        print("You crumble to the ground. Your vision blurring.")
        print("Members of the party crouch down in front of you, but you can't tell who is who.")
        print("Come to think of it, your vision is blurring...")
        print("All of their voices are meshing together...")
        print("Maybe...you shouldn't have drank whatever was in that vial.")
        game_over("Anton and Wyn tried to warn you.")
    if 'n' in vialansw:
        selection_sound()
        print()
        print("The substance in that vial seems so tempting to drink.")
        print("You don't get why. You want to drink it, but...")
        print("No. What kind of crazy person would drink a mysterious liquid found in a cave?!")
        print(colored("Anton: 'We're on a time limit. We need to get moving.'", "red"))
        print(colored("Wyn: 'Yeah, you're right. Let's take the other path.'", "green"))
        print("You and the party walk back to where you started.")
        print("Looks like there's no choice but to take the left path.")
        left_path()
    else:
        game_over("You had ONE job.")




def left_path():
    selection_sound()
    print()
    print("The party begins to wander down the left path.")
    print("As you walk, you can't help but to notice that the air feels a bit colder.")
    print("The path seems to continue forever.")
    print("After about five minutes of walking, Wyn suddenly stops cold in his tracks.")
    print(colored("Poloma: 'Wyn?'", "yellow"))
    print(colored("Wyn: 'We're not the only one's here.'", "green"))
    print(colored("Anton: 'What do you mean by that?'", "red"))
    print(colored("Wyn: 'I mean we're not alone. It's too dark to see, but we aren't alone.'", "green"))
    print(colored("Rue: 'Leave it to me.'", "magenta"))
    print("Rue presses her thumbs together. A thin sheet of flames shoots from her fingertips.'")
    print("You're able to make out the dark ceiling. It's...moving?")
    print("Hold on, it's not moving. The entire ceiling is covered with bats!")
    print("With the sudden burst of light and heat, they seem to become aggravated.")
    print("Some of them begin to swoop down toward you and the party. They don't seem friendly.")
    print()
    print("What're you going to do?! (1 or 2)")
    print("1 = RUN FOR YOUR LIFE!!!")
    print("2= Stand your ground with the party")
    batansw= input()
    if batansw== "1":
        print()
        print("Screw this! You didn't sign up to deal with blood-thirsty bats!")
        print("You turn on your heel and make a run for it, however...")
        print("Out of nowhere, a root grows out of the ground and wraps around your leg.")
        print("You struggle, but you're pulled to the ground!")
        print("Before you can get up, the bats began to swarm you. You can't see anything!")
        print("They all frantically bite at you, as if they're starving and you're a meal")
        game_over("Turns out you are their meal. Those bats are the last thing you ever see again.")
    elif batansw=="2":
        selection_sound()
        print()
        print("You aren't going to let a few bats scare you off!")
        print("You duck as a bat swoops toward you.")
        print("Before your very eyes, you watch as all of the bats swarm together.")
        print(colored("Rue: 'Screw this! There's too many of them and we have a deadline! Let's just go!'", "magenta"))
        print(colored("Anton: 'We can't! They're blocking the way! If you force your way through...'", "red"))
        print(colored("Poloma: 'They'll eat you up like this! Nom nom nom!'", "yellow"))
        print(colored("Gale: 'Okay, so we have to fight!'", "cyan"))
        print(colored("Rue: 'No way, really? I had no idea.'", "magenta"))
        print(colored("Wyn: 'Those...aren't bats.'", "green"))
        print("Everyone looks toward Wyn in confusion. They're not bats??")
        print(colored("Wyn: 'Those aren't animals. I don't know what they are, but...'", "green"))
        print("Before Wyn could finish, roots burst from the ground! What the heck?!")
        print("The roots wrap around the legs of everyone...but you.")
        print("All of the members of the party are dragged to the ground.")
        print("Roots begin to grow over their bodies. They're trapped!")
        print("And just in time, the bats only seem to get angrier and angrier.")
        print("They all fly to each other, forming a big ball of blood-thirsty bats.")
        print("You're the only one not bound by the roots. It looks like it's up to you!")
        print("Will you fight to protect the party?\n(yes or no)")
        fightansw= input().lower()
        if 'y' in fightansw:
            bat_fight()
        if 'n' in fightansw:
            print("There's no way you're risking your life for these strangers!")
            print("You glance at the party, before turning on your heel and making a run for it.")
            print("The party yells out to you as you run, but you ignore them.")
            print("After a bit of running, you find yourself outside of the cave.")
            print("You lean against the entrance as you try to catch your breath.")
            print("As you stand there, a familiar voice rings out to you...")
            print()
            print(colored("You were supposed to join them. Not betray them.", "blue", attrs= ['bold']))
            print()
            print("Roots suddenly erupt from the ground.")
            print()
            print(colored("I don't grant life and powers to cowards.", "blue", attrs= ['bold']))
            print()
            print("Before you can breathe, the roots drag you into the dirt.")
            game_over("Maybe you shouldn't have betrayed the party.")

    else:
        game_over("I'm telling mom you don't know how to choose 1 or 2")

def bat_fight():
    selection_sound()
    print()
    print("You're going to fight and protect the party!")
    print("Despite the fear running through your veins, you'll protect them!")
    print("To the very end!")
    print()
    print("You are now engaged in combat.")
    print("What would you like to do? (1,2,3,4, or 5)")
    print("1= Point your stick at the bats.")
    print("2= Punch the bats.")
    print("3= Spit at the bats.")
    print("4= Kneel down and pray for your life.")
    print("5= Screw this. RUN!")
    round1= input()
    if round1 == "1":
        selection_sound()
        print()
        print("You point your stick at the bunch of bats")
        print("Roots erupt from the ground! They slash at the bats!")
        print("Looks like it hurt...")
        bat_attack1()
    
    elif round1== "2":
        selection_sound()
        print()
        print("You let out a yell as you rush up to the bats.")
        print("You ball up your fist and swing at the flying creatures!")
        print("Looks like it did a bit of damage.")
        bat_attack1()
    
    elif round1== "3":
        selection_sound()
        print()
        print("You gather up a decent amount of spit in your mouth.")
        print("Then, you fire away! You spit at the bats.(Congrats?)")
        print("It seems to do...something, anyways.")
        bat_attack1()
 
    elif round1== "4":
        selection_sound()
        print()
        print("You kneel down and close your eyes.")
        print("You don't exactly know who you're praying to.")
        print("You wish for help. You think back to the voice from the void...")
        print("Suddenly, roots rip out of the ground, thrashing wildly at the bats!")
        print("They appear to be weakened from that. Cool!")
        bat_attack1()

    elif round1== "5":
        print()
        print("You turn on your heel and run...")
        print("When suddenly, a root comes out of the ground!")
        print("It wraps around your leg and drags you to the ground!")
        print("The bats swarm you! Oh no!")
        game_over("You tried to run, but now you're dead.")

def bat_attack1():
    print()
    print("The hoard of bats fly closer toward you.")
    print("A few fly in front of your face, you can't see anything but dark wings!")
    

    
    








#play again and game over copied from https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3
def play_again(): #prompt the player to play again
    print("\nPlay again? (yes or no)")
    answ= input().lower()
    if 'y' in answ:
        selection_sound()
        start() #start over if player says yes
    elif 'n' in answ:
        exit() #exit out of game if player says no
    else:
        exit("I'll take that as a no")


def game_over(reason): #gameover screen
    mixer.init()
    mixer.music.load(gameover_sound) #sound that plays when user gets a game over
    mixer.music.set_volume(2.5)
    mixer.music.play(loops=0)
    print ("\n" + reason) #reason is dialogue written with game over function 
    print ("GAME OVER")
    play_again() 

        




if __name__ == "__main__":
    start()