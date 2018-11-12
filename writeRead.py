

filename = 'text.txt'



#read the entire file & replace a word

with open(filename) as file_object:
    contents = file_object.read()
    b = contents.replace('sucks','is great')
    print(b)
    
    
#read line by line & strip blank lines
        
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
#making a list of lines from a file
        
filename = 'text.txt'

with open(filename) as file_object:
    lines = file_object.readlines() #store as a list
for line in line:
    print(line.rstrip())
    
    
#writing to an empty file
    
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("""
    I'm lookin' like I'm gonna get it, you probably don't get it
    I come in your house with a microphone
    Lookin' like I'm about to set up a show in your kitchen
    I'm outta my mind but I feel like I'm in it
    If I never make it, don't make any difference
    I'm still gonna kill it
    You know what the deal is
    Ain't never no chillin' when I'm in the buildin'
    NF is a monster, I am a villain
    My music is sick, and you don't know what ill is
    You better get back, I don't write any filler
    I write what I feel and I'm feelin' a million
    So you better shh, be quiet, you hear it?
    I'm 'bout to lose it
    I'm on a whole different level of music
    Don't treat me like I don't have no clue how to do this
    You better rethink what you're thinkin' and move it
    Now picture me writin' when I was a kid tryna make it in music
    I'm thinkin' it's crazy
    I spent all my money on studio time, tryna get on my music so people could play it
    I'ma keep it one hundred, my music was terrible
    Learned to get better, the more that I made it
    Go back to my Moments album
    Most of you people, you probably don't know what I'm sayin', hold up!
    What you're witnessin' now, don't try to figure me out
    I grab on that microphone, jawin' the crowd
    They was laughin' at me, who they laughin' at now, huh?
    I laugh at myself, some people they lookin' like, wow
    The moment you told me that you was a rapper, I couldn't believe it
    You believe it now?
    Step in the booth and I murder it
    You never heard of a rapper that kill it like I do
    I sleep on the couch in the studio, stay up 'til 3 in the morning
    And write 'till I get more
    The moment I wake up I feel like I don't even sleep
    And I'm ready to put out my record
    Well, thank you for buyin' it!
    Maybe you burned it!
    But either way, I'm gonna wreck it!
    I look at the industry, look what it did to me
    You'll never make it if you never grind
    You put a whole lot of money into it, you better be ready to give it your time
    I look at the past few years of my life and I promise you I have been given it mine
    Try to keep up with this
    I'm not a puppet, no string on my back, I'm one of a kind
    Music is changing, no way to tame this
    I am an artist, look what I painted
    Hang up the caution tape, I'm dangerous
    Does anyone know where my brain is?
    Rappers are comfortable knowing they're famous
    But I really don't care what your name is
    And I really don't care if I'm nameless
    Y'all just drivin' around, I know where my lane is
    Cocky?
    Nah, I'm competitive?
    This is a job for me, it's adrenaline
    Don't try to box me in, I am Mayweather
    I come in the ring, my punches are way better
    I never drink but I live in these bars
    The moment you blink is the moment you lost
    Say you a king, who put you in charge?
    Don't care what you think, I'll break in your car
    Climb on the top of it, sound the alarm
    And wake up the neighborhood, rap in your yard
    And the carry the speakers on both of my arms
    'Til you keep sleepin' on me, I'm at large
    Enough with the jokes, I ain't jokin'
    You come in a session with me Imma show you what dope is
    And when I say dope I ain't talkin' 'bout smoke
    And I'm talkin' 'bout music that has an emotion
    I look at this mic, it's part of my family
    Take it away, I'm comin' to find you
    I've been through a lot in my life
    And it's hard to get people to listen when no one's behind you
    And then Capitol came in the picture and gave me a shot
    And look at it now
    I look at the team I'm dealin' with, these people ain't playin' around
    Lookin' back, I gotta laugh
    I was in a whole different place a year ago
    I look at the math, I look at the map
    And thank you God, I swear it's a miracle
    And I'm sorry, but I gotta leave
    But man, this track was beautiful
    The least I can do if I murder a beat is take the time to go his funeral
    - Intro by NF
    """)

    
filename = 'guest.txt'

with open(filename,'w') as file_object:
    
    guest = input("please enter your name: ")
    
    file_object.write(guest)
    
    

filename = 'guest_list.txt'

with open(filename,'w') as file_object:

    i = 0

    while i < 10:
    
        guest = input("please enter your name: ")
        adjusted = guest + "\n"
        file_object.write(adjusted)
        
        i+=1
        


    