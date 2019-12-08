import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions

authenticator = IAMAuthenticator('{api key}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

#natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    text='''
    I got pipe dreams of crack rocks and stripper poles
    Of fucking centerfolds
    So I got secrets only me and all my niggas know
    Of kicking in the doors
    I’ll send a bitch to get ya, so don’t play fucking stupid
    I know you got the product
    'Cause I could smell the money, I could taste the weed
    Give me somethin' or a body, only way I’ll leave
    I love to watch 'em squirm, I love when bitches bleed
    If she’s sucking on the barrel, you can’t hear her scream
    So kiss the fucking carpet, this aggravated larson
    And then I’m out the door, it’s monsters in your home
    Black gloves, mask on, muzzle plated chrome

    Who done called the cops on my niggas?
    Who done called the cops on my niggas?
    That’s the first one to go, the first shot I blow
    Who done called the cops on my niggas?
    Who done called the cops on my niggas?

    Shotta, shotta
    Who be that, the number one shotta?
    Put a missile on you when I'm on your blocka
    It no be thing, no be issue when I'm off it, off it, I'm off it
    I got the magazine for the pistol
    For any politician talkin' shit, givin' issue
    Another black man in the street, it's official
    We riding out the spirit, we go another pistol
    Huh, fuck—another cracker
    Cop comin' on my block for the answers
    Huh, I no got time for your question
    Huh, this pon' mi mommy and mi bredren

    I hate the way I think, I hate the way it looms
    I hate the way the things I say incinerate a room
    I know I’m tryna change, but it’ll never work
    Just end up more broken down than when I started
    And that concrete feels the hardest every time I seem to touch it
    Started thinking I ain’t meant for life; but that’s too deep
    Falling up into the ceiling while I’m drowning
    In the creek of my emotions trying harder to be open
    Talking 'bout release dates, I’m trying to make it to tomorrow
    Internal honesty could be the hardest pill to swallow
    So I need two shots of everything that’s on the fuckin' menu
    I’m dancing with myself, setting fire to the venue, motherfucker

    Who done called the cops on my niggas?
    Who done called the cops on my niggas?
    That’s the first one to go, the first shot I blow
    Who done called the cops on my niggas?
    Who done called the cops on my niggas?

    Fuck you!
    I’ll break your neck so you can watch your back
    Fuck you!
    I’ll break your neck so you can watch your back
    I’ll break your neck so you can watch your back
    Fuck you!
    I’ll break your neck so you can watch your back
    Fuck you

    My old friend fucked my girlfriend, I should’ve shot him
    Pray to God about him, man, I hit the Lotto
    Yeah, my bitch got badder, shit, my ass got badder
    And I forgave them bitches, so now it’s off to millions
    I been fucking sinning, hit the forehead
    Chest, left, right, I’m grinning, asses on the ceiling
    And I got mirror feelings, for all you lil' demons
    Yeah, you see the chain, 'fore all y'all changed on me
    Rearranged on me, suck a dick about it
    I hope you get offended, and this ain’t clean shit
    This is pissing off the yacht with my bitch on me
    Wearin' mink on me, sippin' Cris’ on ya
    Bet ya life on it, I came to fight for it

    Came in, raided all y'all pockets
    And your bitch came in and rubbed up on me
    I’m burning rubber, I pulled up on ya

    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect

    Rock the boat like a one-eyed pirate
    Rick James, I get glitter on my eyelids
    2 A.M., 85 on the highway
    Whole world get a little misguided
    Where the spotlight? Put me in the spotlight
    Trust no one that put you in the wrong light
    High scream when I hit her with the long pipe
    Mmm, ice cream when I hit her with the sweet thang
    Do my thing, no, I do not do speaking
    Get my shot, point it out like Ruth, man
    I'ma win a bitch and I got a mood swing
    I'm the realest, bitch, now I got a mood swing
    I got bipolar confidence
    Wake up like "shit" then I feel like the shit
    So I guess I'm the shit
    Yeah, guess I'm the shit

    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect

    Grab life by the horns when I whip the Lambo
    Black on red like I whip the sambo
    Clip's so long it'll make you mambo
    Watch you tango, dutty wine
    She grind on my dick like a hundred times
    Shawty love me long when I grip her sides
    And slip inside like a Slip 'N Slide
    My electric eel do electric slide but—
    I just wanna feel on the booty
    All on me, all on me, all on me
    Make it slow clap like Rudy!
    All on me, all on me, all on me
    I just wanna feel on your booty
    Grab the camcorder, we can make it a movie
    Bring a friend with you if you like how I do it
    Gold chain swingin' and she like how I shoot it

    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect

    Damn, damn, I'm frosty
    Blood diamond, I'm flossing
    Navy camo, I'm drowning
    But you don't see what it cost me
    Turmoil like the Saudi's, hand-me-downs never fit me
    Party never fit me, punani never fit me
    Damn, time-travelin', Honda-swervin', that's so Merlyn
    That's so Merlyn, that's so Merlyn, that's so Merlyn
    Damn, time-travelin', Honda-swervin', book learnin'
    That's so Merlyn, that's so Merlyn, that's so Merlyn

    Swan dive down the 405
    Land at the bottom of El Toro High
    With the precision of a cut from a Zorro knife
    The boy spit like he made out of 409
    So that's clean, bitch
    You can't play with my team, bitch
    We rock pink now on Wednesdays
    Green looks good with your envy
    Mix with white 'cause you salty but this stainless
    I'm like platinum and it's painless
    I just skip on the beat like I'm Pee-Wee Herman
    Hands up for all my sermons
    My wheel's turnin', now I'm more efficient than ever
    I feel like Ratatouille when I'm whipping that cheddar
    You see, you better find your thickest of sweaters
    'Cause this ice might fuck around and change your whole life
    'Cause we about to take flight

    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect
    (Keep a gold chain) Keep a gold chain on my neck
    Fly as a jet, boy, better treat me with respect

    Keep a gold chain (fly, fly as a jet)
    I keep a gold chain (fly, fly as a jet)
    Keep a gold chain (I said I keep a, gold chain)
    Keep a gold chain (I keep a gold chain)
    Keep a gold chain (I said I keep a)
    (I said I keep a gold chain, a gold chain)
    Keep a gold chain
    (I said I keep a, I keep a)
    Keep a gold chain (fly, fly as a jet)

    I might go Interstellar
    I feel like Matthew McConaughey
    I don't care for what they gotta say
    Tony Perkis how I drop the weight
    Jason Bourne with the headshot
    Jason Statham with the whip game
    Liam Neeson with the rescue
    I go Gunnar with the leather face
    Bruce Campbell with the chains
    Tobin Bell with the saw
    Anthony Hopkins, I'm eatin' 'em raw
    They don't know who we are
    Molly Shannon I'm a superstar
    Ride or die like it's Seabiscuit
    Tryna stack like Tobey
    John Wick, I don't leave a witness
    Chris Paul, I'm assistin'
    Ameer go Blake Griffin
    Give me forty-eight minutes
    We go '04 Pistons
    Catch a fade like Robert Horry
    Only time to get the spotlight
    Deray how I'm top flight
    Go Obama when I drop mics

    I'm the black Tom Hanks
    You can call me Nigga Banks
    Secret Agent Cody Banks
    Quarter pound of the dank
    On the scale and it stank
    Put my mama in a Range
    I just bought a new Wraith
    Nic Cage with the face off
    John Travolta when I take off
    Brad Pitt, start a fight club
    Turn the trap into the nightclub
    I'm like Prince with the white doves
    Paint a picture with the white dust
    Lionel Richie with the white bitch
    Try to tell it to her nicely but she never wanna listen
    Beat the pussy to submission
    Tom Cruise on a mission
    Pull a R&B singer, bring her back to South Central
    I shine just like a popstar, MJ my initial
    Kobe Bryant with the spin moves
    If these niggas got issues
    H-Town with Beyoncé, turn her to my prom date
    Kingpin like JAY-Z, dance moves like JT

    Heath Ledger with some dreads
    I just gave my nigga head
    Standing on my two legs
    Fuck what that nigga done said
    Bruh, I don't fuck with no white boys
    'less the nigga Shawn Mendes
    I been off and I been dead
    Bad as hell, I don't bench press
    High school they ain't fuck with me
    Now the critics don't fuck with me
    My own fam ain't fuck with me
    But Viceland did fuck with me
    I'm the only popstar with no money
    Can't drive, so I'm still running
    Uber takin' all my show money
    But that's okay, I got more money
    Not enough to get my teeth fixed
    So my boyfriend in the street, bitch
    In the moonlight, I get seasick
    Did ya see all the art that we did?
    Did all that shit in a weekend
    We was up all late tweakin', yeah
    Ice Cube on a Friday, Chris Tucker on a Friday
    Michael Cera on a Friday, Jonah Hill on a Friday
    Rockin' Leo's blood diamonds
    Sucked off on the highway
    Police right behind me like a nigga stole his OJ
    Okay, I don't play, got the same last name as O.J.

    In the city I'm a menace, I give CEO's the business
    Marathons I gotta finish, foreign whip is speaking Yiddish
    Lately, I been feeling vicious, why y'all crying like some infants?
    You don't wanna be a witness?
    Then you better mind your fucking business
    All these crumbs on my denim, we the only dogs spitting venom
    Been some years I tried to tell them
    But they wanted me to be the villain
    They just wanted me to lose, ones I loved would make me choose
    Had to cut the ones I thought I'd take to the top
    Just so I could make a move
    Dropped out of college, smoking the same campus
    Tell me 'bout limits
    Last year I was suicidal, took those thoughts and tried to kill it
    Used to avoid, used to being paranoid, huffin' with my boys
    Pack it up, I shake the world like asteroids
    Give me love before you try to give me noise, I destroy

    I feel just like Zayn, I feel just like Harry
    I cop it and I flip it, have it sittin' on pirellis
    Me and all my niggas, Southside One Direction
    Tens and tens and tens and tens, got lens that make direction
    Flow to my location, lowkey I'm in Cali
    Just avoiding my probation, fuck your jurisdiction
    Fuck the Federales, sold out by my father
    He gon' feel the karma when I get the, get the commas, nigga
    I don't have, I don't have no fear, nigga
    Buy the ounce, sellin' ounces over here, nigga
    I don't lie, I just bought a whole grill
    Arguing with my bitch, my whip sit twenty-six, nigga

    I got some demons on me, they been feeding on me
    When I sold prescriptions, and my pill addiction
    Fuck the damn detectives, momma called the Reverend
    I know she praying for me, but I'm in the shadows
    Hella drugs and ammo, kicking doors, my MO
    I got some bad habits, I do some shit I shouldn't
    My life is on a scale, I know there's angels on me
    All my dead homies, I know they waiting on me
    Selling dope from out ya house, I know you praying for me
    I know you used to trust me, I miss the chicken nuggets
    And the kisses from her, damn I miss you momma

    Trouble keep following me
    Trouble keep following me, oh yeah
    The shadow keep following me
    The shadow been following me, oh-wee, oh-wee, oh-wee
    Trouble keep following me
    Trouble keep following me, oh yeah
    The shadow keep following me
    The shadow been following me, oh-wee, oh-wee, oh-wee
    Trouble keep following me

    I look like a Somali pirate (don't say that!)
    Failed middle school and college (don't say that!)
    Daddy say I'm an asshole (don't say that!)
    Dick complexion of a Backwoods (eww, don't say that)
    She text me, dry as the Sahara (oh wow!)
    After she get in that casa Merlyn (straight up!)
    I was in that mouth like flouride
    That pussy tight as a hair tie (ah, ooh ooh)
    Scrunchie, I'm so horny baby, bitch your house, pussy baby
    When I get the munchies I steal, I don't share roaches baby
    Bum with the good haircut
    Bum with a good haircut, mattress and magic dick

    Ohh-ohh-ohh, I feel like Master P
    I ain't no slave, ain't lettin no one try to master me
    I'm getting tested, tested, but nobody passing me
    Ain't sugar coating shit don't need them extra calories
    It's a machine, that's why we work inside the factory
    Put 'em up for me, display it like it's a gallery
    Don't need your salary, gold on me like it's alchemy
    Giving niggas the battery when they witness the mastery
    Ohhh, don't say that, don't talk to me, we don't play that
    They got chalk for me, I make outlines like it's pottery
    I got a squad full of fucking oddities
    I got squash, apricots and broccoli
    We turn weird shit to a commodity
    I'm on a odyssey for real quality
    It's like ohhh

    Nigga talk shit, I'll single you out
    If you've got a problem we can figure it out
    I'm from H-Town, but the gold in my mouth
    Southside niggas put a hole in your house
    A hole in your spouse
    Better think twice 'fore you open your mouth
    It's getting real close to the first of the month
    Niggas hit licks, for the gas and the blunt
    Send 'em to the doc, gotta open them up
    Niggas load guns in the back of the truck
    Niggas hate money til they laced with gold
    Gotta get a gun for your hateful foes
    Flex too hard and your casket close
    You don't want your momma come
    And get you from the morgue
    Tall white T, blood on the floor
    Ohhh, don't say that

    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Rollin' in my truck (Uh-huh), gotta keep it tucked (Uh-huh)
    Cause whitey wanna fuck with some niggas like us
    Confederate flag (Uh-huh), neighbors call me "fag" (Uh-huh)
    Gotta keep it low, I keep that thang up in my bag
    Whose society is this? Who delayed my first kiss?
    Who command my scholarship
    And kick us out our neighborhood?
    Play our music, make 'em rich, play our music, make amends
    Box us in like plantains, free all of my Africans
    There go that danger boy, danger boy!
    Nigga, I slay, nigga, I waste them, them, waste them
    Oh-hoooo!
    There go that danger boy, danger boy!
    Oh-hoooo!
    Niggas kill you for a dollar, listen to 'em holler
    Big blood ballers with a crown on my corner
    Crack and marijuana, slab around the corner
    Sitting low on elbows, syrup on the dashboard
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    Get money, big bands, simple bands
    Big money, big bands, simple bands
    I got a dream I'm willing to die for
    I got a team I'll commit a crime for
    Got some dead homies I ain't get to cry for
    'Cause I'm working for my freedom, while the world cry war
    Cry wolf when the shepherd finds a way to strike gold
    'Cause the stocks gon' crash and the dollar gon' fold
    You don't know that the poor eat the rich when there's no profit
    They gave you the floor but you brought up the wrong topic
    So it's
    Me against the world
    Me against the world
    Me against the world
    Me against the world

    Tuggin' on my pinky ring, smelling like chrysanthemum
    I just want that, I just want that bump, bump in my trunk
    Blowing skunk, getting crunk with my baby, oh, what's up?
    Bump, bump in my trunk, bump, bump in my trunkWe gon' ride, ride, ride down to Mexico
    You can see the bad man, I'll come to New York
    You can't catch him though
    You can see the bad man, I'll come to New York
    You can't catch him though
    We gon' ride white lines all the way to Mexico
    Merlyn, Merlyn!And when this ends
    At least I'll have a reason to live
    And when this ends
    At least I'll have a reason to live (Ahh!)I've been trappin' out my momma house
    Dope boy money keep the water and the lights on
    Spray it, like it's Lysol
    Your bitch don't like the dark so we fuckin' with the lights on
    I fuck her with my chains on, you the one I changed on
    I just won the ghetto lottery, I guess I'm hood-rich
    Chillin' at the gallo, smokin' Blacks with my hood bitch
    You ain't what you could be, come get on this dope dick
    I sell it by the gram, now tell me who you fuck withAnd when this ends
    At least I'll have a reason to live
    And when this ends
    At least I'll have a reason to live (Ahh!)Watch me, watch me, watch me, watch me, watch me operate
    I ain't here to talk now, nigga, we ain't gonna conversate
    This modern terrorism, you can't moderate
    I've been fiendin' time to put these demons on display
    'Cause they don't understand, I don't give a damn
    Smoke some shit straight outta Alice in Wonderland
    BROCKHAMPTON the clan, bitch, I ain't your man
    Like they're stacking just to crumble like an avalanche
    This is how it stand, this is how it is
    Bitch, I ain't your friend, I ain't havin' kids
    'Cause I know that if I'm gon' bring him in the world
    My little spawn of Satan just might take off with your fucking girlBump, bump in my trunk, bump, bump, bump, bump
    Bump, bump in my trunk, bump, bump in my trunk
    Bump, bump in my trunk, bump, bump, bump, bump
    Bump, bump in my trunk, bump, bump in my trunkAnd when this ends
    At least I'll have a reason to live
    And when this ends
    At least I'll have a reason to live
    And when this ends
    At least I'll have a reason to live
    And when this ends
    At least I'll have a reason to live

    I ain't the same nigga that I once was
    I lost my fucking mind and then I fell in love
    I did a bunch of drugs because I couldn't sleep
    I lost a couple months, I chipped my fucking teeth
    And there's a couple women and they know some things
    About lies that I done told and shit that I done said
    And niggas that I robbed, so I'm real paranoid
    I have voices in my headHi, my name is Merlyn, I just applied for food stamps
    I just moved to California, with my boy band
    Dropped out of a good school, hippies in my commune
    I left 'fore the rent was due
    Used to want a briefcase and a short commute
    Used to wanna sell coke and whip an Audi coupe
    Crazy, if I did that, wouldn't be talking to you
    Walking through the pitfalls of a college student
    Crazy how you get them letters and that make you feel accepted
    Til you walking 'round the campus and you the only African
    Nobody with passion, just cats that take direction well
    Take acid trips to find themselves, well...I gotta get better at being me (Being who I am)
    I gotta get better at everything (Being who I am)
    I just want a friend that I can hang out with (Being who I am)
    Someone I can sit around, lay on my couch with (Being who I am)Ever since I moved out, I've been broke
    Ever since I grew up, I've been ugly
    Ooh, I need get me some dollar, dollar, dollar bills y'all
    Ever since I left my momma house
    I've been mad as hell at the world
    Sometimes you don't gotta rhyme when you feel it
    Sometimes I barely ever feel a fucking thing
    Sometimes I wish that my fucking phone would fucking ring
    And go off, and wake a nigga up
    I'm used to being sad and I'm used to being down
    I'm used to being used, I miss my boy being aroundI gotta get better at being me (Being who I am)
    I gotta get better at everything (Being who I am)
    I just want a friend that I can hang out with (Being who I am)
    Someone I can sit around, lay on my couch with (Being who I am)Dropping all I got on this one day
    I just wanna be somebody someday
    Dropping all I got on this one way
    I just wanna be somebody someday
    Dropping all I got on this one day
    I just wanna be somebody someday
    Dropping all I got on this one way
    I just wanna be somebody somedaI gotta get better at being me (Being who I am)
    I gotta get better at everything (Being who I am)
    I just want a friend that I can hang out with (Being who I am)
    Someone I can sit around, lay on my couch with (Being who I amI'm trying to look for motivation of smaller things
    But baby steps to my atonement when I foster dreams
    I've been told I'm too transparent with my thoughts sometimes
    So I wrote songs until they pass and I can fall in line
    I fell apart the moment that you thought you found yourself
    'Cause I knew at that point, I couldn't be in the equation anymore
    But moving on with open, broken hearts
    Will show you everything you need to see about yourself to start moving forward
    So many things I wanna say that I'm not sure need to be known
    But everybody swears they fucking know me
    So why, don't I lay every card I'm holding on the table?
    At that point I wonder what they'd show me
    I almost lost my father, still surreal for me to think about
    Considering how many of my friends have lost theirs
    I never know if what I'm saying is the right thing
    If not, I'm ready more than ever for the crosshairs
    It's all fair when it's not you
    Some people have angels, what if only shadows follow you?
    And all the ghosts inside that seem to hollow you
    The branches of the weeping willow start to swallow you
    And then you realize you're exactly where you're supposed to be
    The horizon clears, you wipe the tears
    And all the skeletons are ready for your story

    Tell me what you're waiting for
    I just wanna love you
    Tell me what you're waiting for
    I just wanna hold you
    Tell me what you're waiting for, huh
    I just wanna love you
    Just wanna hold you, never would lie to you
    Tell me what you're waiting for, huh
    What you waiting for

    It feels like I can see the past in your eyes
    I know the future has been passing you by
    These other niggas, they just passing your time
    They don't know how to ride the tidal waves
    That crash in your thighs
    But I got the dream, and if you believe
    Then I can take you somewhere that is pristine
    I'm keeping it clean, my title is mean
    They boxin' us in but we broke out the seams
    Don't make me a fiend, I know what I want
    I'm working to get everything that I need
    But I got a plan for you
    I'm taking a stand for you, I care for yoWhat's your motive with me, baby?
    'Cause I don't trust nobody lately
    I twist and turn, moving just like a serpent
    New times are coming just like a virgin
    Get you all outta my head, 'cause lately I'm better off dead
    I say this all out of respect, sometimes, I want nothing with you
    Wearing your love like medallions
    'Cause I know thousand men want ya, wants the menages
    Fucking, riding shotgun, slap your buns
    Melting, fading, under stars and the sun
    85, 90, gon' bust out the gun
    Know they sent me from the neck of the woods
    Change my name, state so they never coulTell me what you're waiting for
    I just wanna love you
    Tell me what you're waiting for
    I just wanna hold you
    Tell me what you're waiting for, hun
    I just wanna love you
    Just wanna hold you, never would lie to you
    Tell me what you're waiting for, hun
    What you waiting forI need a friend (I need a friend)
    And you need a home (you need a home)
    I love when you come (I love when you coming)
    I still feel alone
    You make it warm in my bed, butterflies in my head
    Sunrise, let it set
    But you don't love me like you say you do
    White lies hold the hidden truth
    You keep leaving when I need you most
    It's true what they say about
    Love had and love lost, here you are and now you're gone
    I'm left alone in the same bed, I wake up in a cold sweaPlease don't make me wait long
    I just wanna be your main one
    Your main, your main one, mm-mm
    See, I don't want nobody, but you. mm-mm
    See, I don't want nobody, but you-u-u, mm-mm
    I spent the day by my lonesome
    Who do you call when there's no one?
    No one ever did what you did for me and did to me
    My bed is cold and indented where you used to sleep
    Tell me what you're waiting for, shit
    Tell me what I'm here foTell me what you're waiting for
    I just wanna love you
    Tell me what you're waiting for
    I just wanna hold you
    Tell me what you're waiting for, huh
    I just wanna love you
    Just wanna hold you, never would lie to you
    Tell me what you're waiting for, huh
    What you waiting f
''',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True,limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True),
        emotion=EmotionOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
