import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions

authenticator = IAMAuthenticator('8O9EMgIsxfs9-tsACK_-FTZSQey4_69U2WdjirOgzjbT')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

#natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    text='''
    i got pipe dreams of crack rocks and stripper poles
    of fucking centerfolds
    so i got secrets only me and all my niggas know
    of kicking in the doors
    i’ll send a bitch to get ya, so don’t play fucking stupid
    i know you got the product
    'cause i could smell the money, i could taste the weed
    give me somethin' or a body, only way i’ll leave
    i love to watch 'em squirm, i love when bitches bleed
    if she’s sucking on the barrel, you can’t hear her scream
    so kiss the fucking carpet, this aggravated larson
    and then i’m out the door, it’s monsters in your home
    black gloves, mask on, muzzle plated chrome

    who done called the cops on my niggas?
    who done called the cops on my niggas?
    that’s the first one to go, the first shot i blow
    who done called the cops on my niggas?
    who done called the cops on my niggas?

    shotta, shotta
    who be that, the number one shotta?
    put a missile on you when i'm on your blocka
    it no be thing, no be issue when i'm off it, off it, i'm off it
    i got the magazine for the pistol
    for any politician talkin' shit, givin' issue
    another black man in the street, it's official
    we riding out the spirit, we go another pistol
    huh, fuck—another cracker
    cop comin' on my block for the answers
    huh, i no got time for your question
    huh, this pon' mi mommy and mi bredren

    i hate the way i think, i hate the way it looms
    i hate the way the things i say incinerate a room
    i know i’m tryna change, but it’ll never work
    just end up more broken down than when i started
    and that concrete feels the hardest every time i seem to touch it
    started thinking i ain’t meant for life; but that’s too deep
    falling up into the ceiling while i’m drowning
    in the creek of my emotions trying harder to be open
    talking 'bout release dates, i’m trying to make it to tomorrow
    internal honesty could be the hardest pill to swallow
    so i need two shots of everything that’s on the fuckin' menu
    i’m dancing with myself, setting fire to the venue, motherfucker

    who done called the cops on my niggas?
    who done called the cops on my niggas?
    that’s the first one to go, the first shot i blow
    who done called the cops on my niggas?
    who done called the cops on my niggas?

    fuck you!
    i’ll break your neck so you can watch your back
    fuck you!
    i’ll break your neck so you can watch your back
    i’ll break your neck so you can watch your back
    fuck you!
    i’ll break your neck so you can watch your back
    fuck you

    my old friend fucked my girlfriend, i should’ve shot him
    pray to god about him, man, i hit the lotto
    yeah, my bitch got badder, shit, my ass got badder
    and i forgave them bitches, so now it’s off to millions
    i been fucking sinning, hit the forehead
    chest, left, right, i’m grinning, asses on the ceiling
    and i got mirror feelings, for all you lil' demons
    yeah, you see the chain, 'fore all y'all changed on me
    rearranged on me, suck a dick about it
    i hope you get offended, and this ain’t clean shit
    this is pissing off the yacht with my bitch on me
    wearin' mink on me, sippin' cris’ on ya
    bet ya life on it, i came to fight for it

    came in, raided all y'all pockets
    and your bitch came in and rubbed up on me
    i’m burning rubber, i pulled up on ya

    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect

    rock the boat like a one-eyed pirate
    rick james, i get glitter on my eyelids
    2 a.m., 85 on the highway
    whole world get a little misguided
    where the spotlight? put me in the spotlight
    trust no one that put you in the wrong light
    high scream when i hit her with the long pipe
    mmm, ice cream when i hit her with the sweet thang
    do my thing, no, i do not do speaking
    get my shot, point it out like ruth, man
    i'ma win a bitch and i got a mood swing
    i'm the realest, bitch, now i got a mood swing
    i got bipolar confidence
    wake up like "shit" then i feel like the shit
    so i guess i'm the shit
    yeah, guess i'm the shit

    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect

    grab life by the horns when i whip the lambo
    black on red like i whip the sambo
    clip's so long it'll make you mambo
    watch you tango, dutty wine
    she grind on my dick like a hundred times
    shawty love me long when i grip her sides
    and slip inside like a slip 'n slide
    my electric eel do electric slide but—
    i just wanna feel on the booty
    all on me, all on me, all on me
    make it slow clap like rudy!
    all on me, all on me, all on me
    i just wanna feel on your booty
    grab the camcorder, we can make it a movie
    bring a friend with you if you like how i do it
    gold chain swingin' and she like how i shoot it

    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect

    damn, damn, i'm frosty
    blood diamond, i'm flossing
    navy camo, i'm drowning
    but you don't see what it cost me
    turmoil like the saudi's, hand-me-downs never fit me
    party never fit me, punani never fit me
    damn, time-travelin', honda-swervin', that's so merlyn
    that's so merlyn, that's so merlyn, that's so merlyn
    damn, time-travelin', honda-swervin', book learnin'
    that's so merlyn, that's so merlyn, that's so merlyn

    swan dive down the 405
    land at the bottom of el toro high
    with the precision of a cut from a zorro knife
    the boy spit like he made out of 409
    so that's clean, bitch
    you can't play with my team, bitch
    we rock pink now on wednesdays
    green looks good with your envy
    mix with white 'cause you salty but this stainless
    i'm like platinum and it's painless
    i just skip on the beat like i'm pee-wee herman
    hands up for all my sermons
    my wheel's turnin', now i'm more efficient than ever
    i feel like ratatouille when i'm whipping that cheddar
    you see, you better find your thickest of sweaters
    'cause this ice might fuck around and change your whole life
    'cause we about to take flight

    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect
    (keep a gold chain) keep a gold chain on my neck
    fly as a jet, boy, better treat me with respect

    keep a gold chain (fly, fly as a jet)
    i keep a gold chain (fly, fly as a jet)
    keep a gold chain (i said i keep a, gold chain)
    keep a gold chain (i keep a gold chain)
    keep a gold chain (i said i keep a)
    (i said i keep a gold chain, a gold chain)
    keep a gold chain
    (i said i keep a, i keep a)
    keep a gold chain (fly, fly as a jet)

    i might go interstellar
    i feel like matthew mcconaughey
    i don't care for what they gotta say
    tony perkis how i drop the weight
    jason bourne with the headshot
    jason statham with the whip game
    liam neeson with the rescue
    i go gunnar with the leather face
    bruce campbell with the chains
    tobin bell with the saw
    anthony hopkins, i'm eatin' 'em raw
    they don't know who we are
    molly shannon i'm a superstar
    ride or die like it's seabiscuit
    tryna stack like tobey
    john wick, i don't leave a witness
    chris paul, i'm assistin'
    ameer go blake griffin
    give me forty-eight minutes
    we go '04 pistons
    catch a fade like robert horry
    only time to get the spotlight
    deray how i'm top flight
    go obama when i drop mics

    i'm the black tom hanks
    you can call me nigga banks
    secret agent cody banks
    quarter pound of the dank
    on the scale and it stank
    put my mama in a range
    i just bought a new wraith
    nic cage with the face off
    john travolta when i take off
    brad pitt, start a fight club
    turn the trap into the nightclub
    i'm like prince with the white doves
    paint a picture with the white dust
    lionel richie with the white bitch
    try to tell it to her nicely but she never wanna listen
    beat the pussy to submission
    tom cruise on a mission
    pull a r&b singer, bring her back to south central
    i shine just like a popstar, mj my initial
    kobe bryant with the spin moves
    if these niggas got issues
    h-town with beyoncé, turn her to my prom date
    kingpin like jay-z, dance moves like jt

    heath ledger with some dreads
    i just gave my nigga head
    standing on my two legs
    fuck what that nigga done said
    bruh, i don't fuck with no white boys
    'less the nigga shawn mendes
    i been off and i been dead
    bad as hell, i don't bench press
    high school they ain't fuck with me
    now the critics don't fuck with me
    my own fam ain't fuck with me
    but viceland did fuck with me
    i'm the only popstar with no money
    can't drive, so i'm still running
    uber takin' all my show money
    but that's okay, i got more money
    not enough to get my teeth fixed
    so my boyfriend in the street, bitch
    in the moonlight, i get seasick
    did ya see all the art that we did?
    did all that shit in a weekend
    we was up all late tweakin', yeah
    ice cube on a friday, chris tucker on a friday
    michael cera on a friday, jonah hill on a friday
    rockin' leo's blood diamonds
    sucked off on the highway
    police right behind me like a nigga stole his oj
    okay, i don't play, got the same last name as o.j.

    in the city i'm a menace, i give ceo's the business
    marathons i gotta finish, foreign whip is speaking yiddish
    lately, i been feeling vicious, why y'all crying like some infants?
    you don't wanna be a witness?
    then you better mind your fucking business
    all these crumbs on my denim, we the only dogs spitting venom
    been some years i tried to tell them
    but they wanted me to be the villain
    they just wanted me to lose, ones i loved would make me choose
    had to cut the ones i thought i'd take to the top
    just so i could make a move
    dropped out of college, smoking the same campus
    tell me 'bout limits
    last year i was suicidal, took those thoughts and tried to kill it
    used to avoid, used to being paranoid, huffin' with my boys
    pack it up, i shake the world like asteroids
    give me love before you try to give me noise, i destroy

    i feel just like zayn, i feel just like harry
    i cop it and i flip it, have it sittin' on pirellis
    me and all my niggas, southside one direction
    tens and tens and tens and tens, got lens that make direction
    flow to my location, lowkey i'm in cali
    just avoiding my probation, fuck your jurisdiction
    fuck the federales, sold out by my father
    he gon' feel the karma when i get the, get the commas, nigga
    i don't have, i don't have no fear, nigga
    buy the ounce, sellin' ounces over here, nigga
    i don't lie, i just bought a whole grill
    arguing with my bitch, my whip sit twenty-six, nigga

    i got some demons on me, they been feeding on me
    when i sold prescriptions, and my pill addiction
    fuck the damn detectives, momma called the reverend
    i know she praying for me, but i'm in the shadows
    hella drugs and ammo, kicking doors, my mo
    i got some bad habits, i do some shit i shouldn't
    my life is on a scale, i know there's angels on me
    all my dead homies, i know they waiting on me
    selling dope from out ya house, i know you praying for me
    i know you used to trust me, i miss the chicken nuggets
    and the kisses from her, damn i miss you momma

    trouble keep following me
    trouble keep following me, oh yeah
    the shadow keep following me
    the shadow been following me, oh-wee, oh-wee, oh-wee
    trouble keep following me
    trouble keep following me, oh yeah
    the shadow keep following me
    the shadow been following me, oh-wee, oh-wee, oh-wee
    trouble keep following me

    i look like a somali pirate (don't say that!)
    failed middle school and college (don't say that!)
    daddy say i'm an asshole (don't say that!)
    dick complexion of a backwoods (eww, don't say that)
    she text me, dry as the sahara (oh wow!)
    after she get in that casa merlyn (straight up!)
    i was in that mouth like flouride
    that pussy tight as a hair tie (ah, ooh ooh)
    scrunchie, i'm so horny baby, bitch your house, pussy baby
    when i get the munchies i steal, i don't share roaches baby
    bum with the good haircut
    bum with a good haircut, mattress and magic dick

    ohh-ohh-ohh, i feel like master p
    i ain't no slave, ain't lettin no one try to master me
    i'm getting tested, tested, but nobody passing me
    ain't sugar coating shit don't need them extra calories
    it's a machine, that's why we work inside the factory
    put 'em up for me, display it like it's a gallery
    don't need your salary, gold on me like it's alchemy
    giving niggas the battery when they witness the mastery
    ohhh, don't say that, don't talk to me, we don't play that
    they got chalk for me, i make outlines like it's pottery
    i got a squad full of fucking oddities
    i got squash, apricots and broccoli
    we turn weird shit to a commodity
    i'm on a odyssey for real quality
    it's like ohhh

    nigga talk shit, i'll single you out
    if you've got a problem we can figure it out
    i'm from h-town, but the gold in my mouth
    southside niggas put a hole in your house
    a hole in your spouse
    better think twice 'fore you open your mouth
    it's getting real close to the first of the month
    niggas hit licks, for the gas and the blunt
    send 'em to the doc, gotta open them up
    niggas load guns in the back of the truck
    niggas hate money til they laced with gold
    gotta get a gun for your hateful foes
    flex too hard and your casket close
    you don't want your momma come
    and get you from the morgue
    tall white t, blood on the floor
    ohhh, don't say that

    get money, big bands, simple bands
    big money, big bands, simple bands
    get money, big bands, simple bands
    big money, big bands, simple bands
    get money, big bands, simple bands
    big money, big bands, simple bands
    get money, big bands, simple bands
    big money, big bands, simple bands
    rollin' in my truck (uh-huh), gotta keep it tucked (uh-huh)
    cause whitey wanna fuck with some niggas like us
    confederate flag (uh-huh), neighbors call me "fag" (uh-huh)
    gotta keep it low, i keep that thang up in my bag
    whose society is this? who delayed my first kiss?
    who command my scholarship
    and kick us out our neighborhood?
    play our music, make 'em rich, play our music, make amends
    box us in like plantains, free all of my africans
    there go that danger boy, danger boy!
    nigga, i slay, nigga, i waste them, them, waste them
    oh-hoooo!
    there go that danger boy, danger boy!
    oh-hoooo!
    niggas kill you for a dollar, listen to 'em holler
    big blood ballers with a crown on my corner
    crack and marijuana, slab around the corner
    sitting low on elbows, syrup on the dashboard
    get money, big bands, simple bands
    big money, big bands, simple bands
    get money, big bands, simple bands
    big money, big bands, simple bands
    get money, big bands, simple bands
    big money, big bands, simple bands
    get money, big bands, simple bands
    big money, big bands, simple bands
    i got a dream i'm willing to die for
    i got a team i'll commit a crime for
    got some dead homies i ain't get to cry for
    'cause i'm working for my freedom, while the world cry war
    cry wolf when the shepherd finds a way to strike gold
    'cause the stocks gon' crash and the dollar gon' fold
    you don't know that the poor eat the rich when there's no profit
    they gave you the floor but you brought up the wrong topic
    so it's
    me against the world
    me against the world
    me against the world
    me against the world

    tuggin' on my pinky ring, smelling like chrysanthemum
    i just want that, i just want that bump, bump in my trunk
    blowing skunk, getting crunk with my baby, oh, what's up?
    bump, bump in my trunk, bump, bump in my trunkwe gon' ride, ride, ride down to mexico
    you can see the bad man, i'll come to new york
    you can't catch him though
    you can see the bad man, i'll come to new york
    you can't catch him though
    we gon' ride white lines all the way to mexico
    merlyn, merlyn!and when this ends
    at least i'll have a reason to live
    and when this ends
    at least i'll have a reason to live (ahh!)i've been trappin' out my momma house
    dope boy money keep the water and the lights on
    spray it, like it's lysol
    your bitch don't like the dark so we fuckin' with the lights on
    i fuck her with my chains on, you the one i changed on
    i just won the ghetto lottery, i guess i'm hood-rich
    chillin' at the gallo, smokin' blacks with my hood bitch
    you ain't what you could be, come get on this dope dick
    i sell it by the gram, now tell me who you fuck withand when this ends
    at least i'll have a reason to live
    and when this ends
    at least i'll have a reason to live (ahh!)watch me, watch me, watch me, watch me, watch me operate
    i ain't here to talk now, nigga, we ain't gonna conversate
    this modern terrorism, you can't moderate
    i've been fiendin' time to put these demons on display
    'cause they don't understand, i don't give a damn
    smoke some shit straight outta alice in wonderland
    brockhampton the clan, bitch, i ain't your man
    like they're stacking just to crumble like an avalanche
    this is how it stand, this is how it is
    bitch, i ain't your friend, i ain't havin' kids
    'cause i know that if i'm gon' bring him in the world
    my little spawn of satan just might take off with your fucking girlbump, bump in my trunk, bump, bump, bump, bump
    bump, bump in my trunk, bump, bump in my trunk
    bump, bump in my trunk, bump, bump, bump, bump
    bump, bump in my trunk, bump, bump in my trunkand when this ends
    at least i'll have a reason to live
    and when this ends
    at least i'll have a reason to live
    and when this ends
    at least i'll have a reason to live
    and when this ends
    at least i'll have a reason to live

    i ain't the same nigga that i once was
    i lost my fucking mind and then i fell in love
    i did a bunch of drugs because i couldn't sleep
    i lost a couple months, i chipped my fucking teeth
    and there's a couple women and they know some things
    about lies that i done told and shit that i done said
    and niggas that i robbed, so i'm real paranoid
    i have voices in my headhi, my name is merlyn, i just applied for food stamps
    i just moved to california, with my boy band
    dropped out of a good school, hippies in my commune
    i left 'fore the rent was due
    used to want a briefcase and a short commute
    used to wanna sell coke and whip an audi coupe
    crazy, if i did that, wouldn't be talking to you
    walking through the pitfalls of a college student
    crazy how you get them letters and that make you feel accepted
    til you walking 'round the campus and you the only african
    nobody with passion, just cats that take direction well
    take acid trips to find themselves, well...i gotta get better at being me (being who i am)
    i gotta get better at everything (being who i am)
    i just want a friend that i can hang out with (being who i am)
    someone i can sit around, lay on my couch with (being who i am)ever since i moved out, i've been broke
    ever since i grew up, i've been ugly
    ooh, i need get me some dollar, dollar, dollar bills y'all
    ever since i left my momma house
    i've been mad as hell at the world
    sometimes you don't gotta rhyme when you feel it
    sometimes i barely ever feel a fucking thing
    sometimes i wish that my fucking phone would fucking ring
    and go off, and wake a nigga up
    i'm used to being sad and i'm used to being down
    i'm used to being used, i miss my boy being aroundi gotta get better at being me (being who i am)
    i gotta get better at everything (being who i am)
    i just want a friend that i can hang out with (being who i am)
    someone i can sit around, lay on my couch with (being who i am)dropping all i got on this one day
    i just wanna be somebody someday
    dropping all i got on this one way
    i just wanna be somebody someday
    dropping all i got on this one day
    i just wanna be somebody someday
    dropping all i got on this one way
    i just wanna be somebody somedai gotta get better at being me (being who i am)
    i gotta get better at everything (being who i am)
    i just want a friend that i can hang out with (being who i am)
    someone i can sit around, lay on my couch with (being who i ami'm trying to look for motivation of smaller things
    but baby steps to my atonement when i foster dreams
    i've been told i'm too transparent with my thoughts sometimes
    so i wrote songs until they pass and i can fall in line
    i fell apart the moment that you thought you found yourself
    'cause i knew at that point, i couldn't be in the equation anymore
    but moving on with open, broken hearts
    will show you everything you need to see about yourself to start moving forward
    so many things i wanna say that i'm not sure need to be known
    but everybody swears they fucking know me
    so why, don't i lay every card i'm holding on the table?
    at that point i wonder what they'd show me
    i almost lost my father, still surreal for me to think about
    considering how many of my friends have lost theirs
    i never know if what i'm saying is the right thing
    if not, i'm ready more than ever for the crosshairs
    it's all fair when it's not you
    some people have angels, what if only shadows follow you?
    and all the ghosts inside that seem to hollow you
    the branches of the weeping willow start to swallow you
    and then you realize you're exactly where you're supposed to be
    the horizon clears, you wipe the tears
    and all the skeletons are ready for your story

    tell me what you're waiting for
    i just wanna love you
    tell me what you're waiting for
    i just wanna hold you
    tell me what you're waiting for, huh
    i just wanna love you
    just wanna hold you, never would lie to you
    tell me what you're waiting for, huh
    what you waiting forit feels like i can see the past in your eyes
    i know the future has been passing you by
    these other niggas, they just passing your time
    they don't know how to ride the tidal waves
    that crash in your thighs
    but i got the dream, and if you believe
    then i can take you somewhere that is pristine
    i'm keeping it clean, my title is mean
    they boxin' us in but we broke out the seams
    don't make me a fiend, i know what i want
    i'm working to get everything that i need
    but i got a plan for you
    i'm taking a stand for you, i care for yowhat's your motive with me, baby?
    'cause i don't trust nobody lately
    i twist and turn, moving just like a serpent
    new times are coming just like a virgin
    get you all outta my head, 'cause lately i'm better off dead
    i say this all out of respect, sometimes, i want nothing with you
    wearing your love like medallions
    'cause i know thousand men want ya, wants the menages
    fucking, riding shotgun, slap your buns
    melting, fading, under stars and the sun
    85, 90, gon' bust out the gun
    know they sent me from the neck of the woods
    change my name, state so they never coultell me what you're waiting for
    i just wanna love you
    tell me what you're waiting for
    i just wanna hold you
    tell me what you're waiting for, hun
    i just wanna love you
    just wanna hold you, never would lie to you
    tell me what you're waiting for, hun
    what you waiting fori need a friend (i need a friend)
    and you need a home (you need a home)
    i love when you come (i love when you coming)
    i still feel alone
    you make it warm in my bed, butterflies in my head
    sunrise, let it set
    but you don't love me like you say you do
    white lies hold the hidden truth
    you keep leaving when i need you most
    it's true what they say about
    love had and love lost, here you are and now you're gone
    i'm left alone in the same bed, i wake up in a cold sweaplease don't make me wait long
    i just wanna be your main one
    your main, your main one, mm-mm
    see, i don't want nobody, but you. mm-mm
    see, i don't want nobody, but you-u-u, mm-mm
    i spent the day by my lonesome
    who do you call when there's no one?
    no one ever did what you did for me and did to me
    my bed is cold and indented where you used to sleep
    tell me what you're waiting for, shit
    tell me what i'm here fotell me what you're waiting for
    i just wanna love you
    tell me what you're waiting for
    i just wanna hold you
    tell me what you're waiting for, huh
    i just wanna love you
    just wanna hold you, never would lie to you
    tell me what you're waiting for, huh
    what you waiting f

    these niggas take me for granted, what would hap' if i vanish?
    bet a hunnid they'd panic, my shooters only speak spanish
    keep my heart with my dogs, keep my car in the yard
    i can't drive it nowhere so i'll let you niggas take off
    seen the shit that they drop, that shit not instantly hot
    i give that instant re-bop, that replay value go off
    that make my value go up, i keep that bow in my cup
    my niggas rolling, got that going with a thousand to bust
    that nigga kevin can't rap, he too sappy with his shit
    he don't rep me with his shit, he on that teenage bullshit
    and he 'bout 20 and shit? when he let go of that shit?
    he'll prolly be a little colder, y'all agree with me? shit
    that nigga need to act his age, he ain't acting like a grown up
    ain't that boy from texas? he ain't acting like a soldier
    knew that boy in high school, man, that nigga wasn't awkward
    and i know his mama, man, that nigga just a liar

    cash don't last, my friends will ride with me
    keep 'em in my bag, we robbed a limousine
    when the guns go pow, won't bother us again
    i don't wanna do it but they keep on pushing me

    cash don't mean shit, shit
    cried my last tears, bitch
    cashed my last check, check
    cash don't mean shit, shit
    cash don't mean shit, shit
    cried my last tears, bitch
    cashed my last check, check
    cash don't mean shit, shit

    call me king of the niggas, i need a crown made of thorns
    god said, "let there be light" on the day i was born
    step off the ship with the slaves, then i go hit the stage
    i just left in a whip, all i need is a chain
    i don't trust no niggas and i don't trust no bitch
    'cause people talk too much, i bought a black fo'-fifth
    and a brand new clip, that's my new best friend
    'cause i'm a brand new nigga, in a brand new crib
    i ain't sellin' no more, but got my hand in the zip
    whitey gave me the check, i ain't ask for the fame
    i used to deal with the grams 'til they put the cam on my face
    now i'm evading the law, i'm on a high-speed chase
    i'm in a big-ass truck, i tell 'em, "get out the way"
    i gotta couple of warrants, so i'm leaving my state
    now i'm in cali today, with the sun on my face
    i got a bag of the gas, and a blunt i can face

    how i'm gon' move at your pace? i'm busy settin' the tone
    you think we runnin' together? i'm in a lane of my own
    don't got no friends in this game, it's me and my brothers alone
    they thinkin' that we competing, that shit depletin' my bones
    i don't need all that energy, they just fuck up my chakras
    i put my heart in a locker, they love me when i'm a martyr
    they hate me when i'm myself, i can't barter with that
    you watch us charter these tracks, it's sticking like tartar and plaque
    i need a parlour of plaques, need lobsters and helicopters
    i need peace for my niggas, need darker skin for all my doctors
    i like to speak like a scholar, like to think like a nigga
    in this world i can't wander, no honor behind the trigger
    i could get shot in my back and they'd tell the world that i fought 'em
    "we ain't taught 'em nothin' new, but somehow they been gettin' smarter"
    that's what they sayin' in private, speaking from that entitlement
    we still workin' for titles and makin' tidal environments

    cash don't last, my friends will ride with me
    keep 'em in my bag, we robbed a limousine
    when the guns go pow, won't bother us again
    i don't wanna do it but they keep on pushing me
    cash don't last, my friends will ride with me
    keep 'em in my bag, we robbed a limousine
    when the guns go pow, won't bother us again
    i don't wanna do it but they keep on pushing me

    fuck, put ya ante up, riding in the limousine
    i'm stuck on some bud i hit, under concrete canopy
    fuck all this energy, you just wanna bring me down
    fuck all your energy, you just wanna bring me down
    fuck, put the windows up, blowin' past the exit now
    up like a money shot, swerve into the sunset
    me and all my boys jet, swerving like a doughnut
    off, off, off, off, swerving like a doughnut

    nigga, what?
    pull up, pull up, pull up, pull up, pull up if you want to
    nigga, what?
    pull up, pull up, pull up, pull up, pull up if you want to
    nigga, what?
    pull up, pull up, pull up, pull up, pull up if you want to
    nigga, what? y-yo

    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down
    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down

    hi, i live a wonderful life
    should've died twice, wonder who on my side
    life always better keepin' two on the side
    need no music when my niggas arrive
    we be in van nuys, black van with some white guys
    keep your hand out, waiting for the appropriate time
    to ask a question like
    "could you perform at my best friend's birthday party?
    with your friends and go crazy, just bring the shotty
    bring the loud one with the blonde hair."
    making out with zayn in a lawn chair
    they kicked me out but i belong here
    hear these songs nigga, see this long hair, see these videos
    direct these hoes with no budgets though
    how the fuck did i land a fucking tv show?
    met all my friends through kanye west and i ain't met him yet

    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down

    just shaved down to the baby face
    clothes on me, guess it's holiday
    fried, no sides at the restaurant
    my sleep schedule like the power here, it's never on
    feeling like the past year a whole escapade (uh-oh)
    four cars, need a motherfucking escalade
    pack it up like a clown car (honk, honk)
    bet you know my name from here to hong kong, bet i get along
    make some commas, karma, watch 'em sing along
    ayy, err, err, butter knife like dancing on a knuckle
    in the thunder car, rocked up in the lumma
    incidental, i be better by the summer
    i be better by the winter, i be hoppin' in the rental
    maybe tesla for all my missus sitting in the volvo
    damn, shoot 'em down like, hmmm, sorry, do it all here

    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down
    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down

    i'm moonwalking on the sun hot
    i used to live where the guns popped
    made some records then we moved out
    turned rap into the new pop
    bandana, i'm the new pac
    i been blowing up, i can't stop
    they need my niggas in the white house
    i do business with the white folks
    bring that money back to black folks
    flip it, stimulate the cash flow
    economic, but i speak ebonics
    l.a. turned me to an asshole
    i been shopping down on melrose
    still a nigga but i'm livin' different
    i been looking at the bigger picture
    so i don't hear 'em when they talking to me

    i just want a friend to fall in love with
    maybe someone i can binge drugs with
    living like a prince but i'm dove-less
    playin' my emotions, you a dumb bitch
    everybody talking on some gun shit
    they don't even know where to bust it
    cry nigga, gotta fuckin' kick back
    gotta leave those soft niggas at the kickback
    splittin' all my problems like a kit-kat
    i finessed the night that we slipped up
    i could let you know where i'm next at
    tell my baby girl where the brakes at
    you know i got number one pick stats
    catch me on the field, it's a mismatch
    more like an eclipse, she couldn't miss that
    putting my ideas where my chips at

    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down
    la-di-da-di-da-di-da, do i trust 'em? probably not
    i think that y'all prolly fraud, i think that my brain is fried
    la-di-da-di-da-di-da, do not turn my volume down
    do not bring your friends around, only few i'm holding down

    la-di-da-di-da-di-da (la-di-da, la-di-da)
    do-walla, do-walla-walla, do-walla
    la-di-da-di-da-di-da (la-di-da, la-di-da)
    do-walla, do-walla-walla, do-walla
    la-di-da-di-da-di-da (la-di-da, la-di-da)
    do-walla, do-walla-walla, do-walla

    i done been in trouble 'bout as long as i remember
    my momma tried to help me but i hardly ever listened
    so she sent me to them white schools, i learned that i was different
    they told me i'm a nigga, well, now i know i am
    i got my finger on the trigger, i'm a project baby
    a free lunch felon, and i'm hungry every minute
    empty stomach, weed smoke can't fill it
    if you don't listen to me, i set fire to the building
    need to listen to the children and the weapons they concealing
    hear the voices of a million when i sell my first million
    i am bound to go diamond, ain't no luck or surprises
    i am tanning on an island
    i can feel the pressure but i see my new horizons
    me and all my niggas getting stars down on sunset boulevard
    but niggas from the southside with xan bars and gun play
    niggas on that "someday..."
    if you shooting for the stars, you only headed one way

    i could be here all day. you're gonna tell me what i need to know. you're gonna tell me! are you gonna tell me? c'mon, spit it out...
    me ilamo roberto, y este es el camino al éxito.

    fucking commas up from the outside
    from the outside, from the outside
    fu-fucking dollars up from the outside
    from the outside, from the outside
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?

    my daddy taught me how to sell dope
    turn grams into elbows
    light it up when the l rolled
    black mask, used to kick doors
    wasn't no bullets in the guns though
    niggas still never argued
    raid the house like the task force
    me and my niggas like drug dogs
    find the dope then we take off
    fuck my girl with my chain on
    then she tatted my name on it
    yellowstone, i was raised on it
    actavis in my baby bottle
    baby stroller was an impala
    niggas like to talk down on me
    when i see 'em, i don't hear about it

    fucking commas up from the outside
    from the outside, from the outside
    fu-fucking dollars up from the outside
    from the outside, from the outside
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?

    (merlyn! merlyn!)
    never would've met my friends if not for satellites
    yeah, i'll cuff her even if she do not suck me right (suck me, suck me!)
    always planned to be a rapper when i failed at life
    luckily professor failed me at the proper time (yee! yee!)
    shh-shh, shh, i say "please" all the time, bitch
    shh-shh, shh, i like white collar crime, bitch
    shh-shh, shh, money digital broke and
    shh-shh, shh, ghana prince in your messages

    i know you hate me for leavin'
    then let's go crazy together
    when i tell ya all the things that i'm thinking
    just so that we could get better
    but you wanna put my heart on the stretcher
    i don't got insurance for this pressure
    wanna find the benefits, i can't measure
    trying not to run out on my temper
    i can see the ash and the ember
    that was made from emotional texture
    i don't know why i took this endeavor
    don't identify with oppressors
    don't identify with surrender
    all of my old friends fair-weather
    gotta treat my heart like a treasure
    'cause all i know is no one else will

    fucking commas up from the outside
    from the outside, from the outside
    fu-fucking dollars up from the outside
    from the outside, from the outside
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?

    you do not know me, don't speak of my homies, you are a phony
    quit pinnin' shit on me, you gon' bring out the old me
    you don't wanna know what i wanna do when y'all talk down on my name
    i don't wanna see you in the street 'cause i might catch a case
    people smile when they face to face (woo, woo, woo!)
    then turn their back and switch up words you say (ah, ah, ah!)
    running to the papers everyday (woo, woo, woo!)
    i'm running to the paper anyway (ah, ah, ah!)

    fucking commas up from the outside
    from the outside, from the outside
    fu-fucking dollars up from the outside
    from the outside, from the outside
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?
    they been talkin' down on me (huh) what ya say?

    too many things i'd rather do different
    woke up in a cold sweat (uh!)
    my emotions creepin'
    three o'clock on the weekend, might as well sleep in
    stay down for the count when
    she hit me with the "what-ifs?"
    and the "what-whens?" and the "what-thens?"
    wonder where my life went, living in the moment
    i been thinking 'bout my time spent, are the bills paid?
    is it make or break? will i find a way?
    have my feelings changed? will i be okay? i don’t know
    but what i do know is, life don't make sense
    if you can't pay rent, so i place my bet
    what got you shook on this saturday?
    i take my l and i hold my place
    i split my l and i go away
    you left a spell on my saturday
    what got you shook on this saturday?
    i take my l and i hold my place
    i split my l and i go away (yah)
    you left a spell on my saturday

    i got cracks in my phone screen
    the past fuck with my psyche
    smoke weed and get high, please
    went to school in the woodlands
    and that made niggas wanna fight me
    so i don't take threats lightly
    tell them niggas, "come and find me"
    gotta say it in my eye view
    new house off itunes
    new money, my perfume
    big smile, in a good mood
    i been running out of issues
    i ain't trippin' when the rent due
    i ain't runnin' with a pistol
    i ain't locked in the system
    taking care of my kinfolk

    taking a book out the page of the greats
    i'm only human and i make mistakes
    chisel my flows so they can't liberate
    talking the time as the pendulum sways
    i gotta face what i didn't create
    just 'cause i can't relate, i don't debate
    i educate, illuminate
    or we can't duplicate, no more moving the plates
    second chances feeling overrated
    unappreciated, so i bossed up
    missed the time when we could share space
    but it'll all be straight the day we cross up
    nothing better than some time with you
    because it's time i never wanna toss up
    lose myself inside of you, you find yourself in me
    i don't wanna be cautious

    what got you shook on this saturday?
    i take my l and i hold my place
    i split my l and i go away
    you left a spell on my saturday
    what got you shook on this saturday?
    i take my l and i hold my place
    i split my l and i go away (yah)
    you left a spell on my saturday

    what got you shook?
    what got you shook?
    what got you shook?
    what got you shook?

    i felt awesome when you walked in
    you caught me doin' something
    that i should've never been caught with
    i played the forest, my far trip
    i tripped and i fell, still think i'm living in austin
    remember when i was trippin' off some wack shit
    when i thought the automatic had an answer?
    when i was jammin' out beyonce like sampha
    and you broke up with me 'cause i'm a cancer?
    our relationship was toxic, cancer
    i fell in love with a dancer in atlanta
    i'm lying, i ain't a drake-ass nigga
    i'm more like troye sivan
    with a whole lotta mela-nahn
    sendin' bombs to your lawn
    grew up on rockafella, so i'ma get a chain
    and sing every song in the vain of your name
    and this'll...

    be there when they call me up
    save me wishin' for you, i'm missing you too
    miss the way we talk, miss the way we stop
    miss the way we talk, ooh
    be there when they call me up
    save me wishin' for you, i'm missing you too
    miss the way we talk, miss the way we stop
    miss the way we talk, ooh

    why you look like that? (he looks crazy as fuck)
    he look crazy as hell
    but he dress well (oh my god)
    why his face look puff?
    why he look like that? (you look like a)
    why your hair like that? (like a chipmunk or something)
    why your teeth like that? (or like a prairie dog)
    why your cheeks like that?

    i got this shitty moustache, and a new haircut
    short but tall enough to ride every ride so it's fair enough
    teeth crooked but my breath fresh just like the evergreens
    my attitude is bit like, a psys- fuck!
    you mean a psychopath
    i bet the marble feel good on your bare foot
    i'm in the backyard hiding out like i'm bigfoot
    and i won't cater to you
    yeah i am not carrabba's, and i ain't taking orders
    here for the loot, and to inspire some of you
    to do what you do despite all the "fuck you's"
    'cause they shit on your shit, stab you right in the back
    'til you're shittin' on the toilet with grammys in your lap

    niggas talk a lot of shit, in a safe place
    aiming with they keyboard, they shootin' uppercase
    i'm booking tour dates, money in the suitcase
    commander and the chief like, barack hussein
    same nigga, two names, i am onto new things
    flying out of houston, lemme say a few things
    i don't give a fuck about you or your screen name
    i'ma be a star even if i say the same things
    'cause them same things keep me on the wavelengths
    i dropped another verse, so you gon' have to pay me
    glock with no safety, seen niggas on the pavement
    over gang affiliations, guns with extensions
    seeing niggas get anxious, all these internet gangstas
    i'm running outta patience, nigga, stick to your day shift
    and watch what you're saying, and please keep praying
    'cause niggas talk big 'til that price on their head
    i feel the voices always drown out all the noise in the room
    they don't employ you for your purpose, they just need a platoon
    another number in a line ready to march into tombs
    i ain't the one to assume, i put the coon in tycoon
    we colonizing the moon, i see you look to the sky
    and start to wish it was you, sometimes i wish i was me
    sometimes i'm watching my life
    i'm dissociated from what eats my heart up at night
    sleep on a cloud of my strife
    i ain't afraid of the heights, they all afraid to appall
    i'm just afraid of excitement being a trip to the mall
    i need a summer to fall, i need a winter to spring
    got all these seasons within me, building a story to sing
    don't need a dollar to dream, i need a billion in facts
    i need a trillion in wealth, y'all niggas need to relax
    i wanna build up the culture, they wanna dream in the trap
    i took the zoom off my lens and i saw the world in my lap
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the bag, all my niggas in the bag
    i'm not tryna be like you, when i grow, money in the bag
    keep the sand in the

    i spit my heart out, lookin' out for my best interests
    he gave me good head, peepin' out while the windows tinted
    i speak in tongues and i arrive without a damn mention
    it's kinda sick and i was born in 1996 and
    1999 the only year that i remember
    i slip through the cracks without havin' a damn temper
    i bleach my hair because these bitches all about they bitchin'
    i say shit when i rap and y'all niggas barely listen
    i do the most for the culture, nigga, by just existing
    delete my tweets 'cause i'm ashamed of being a fuckin' simpson
    i told my mom i was gay; why the fuck she ain't listen?
    i signed a pub deal and her opinion fuckin' disappearin'
    i'm payin' bills for my sister and tryna fund her business
    is it homophobic to only hook up with straight niggas?
    you know like closet niggas, masc-type?
    why don't you take that mask off?
    that's the thought i had last night
    "why you always rap about bein' gay?"
    'cause not enough niggas rap and be gay
    where i come from, niggas get called "faggot" and killed
    so i'ma get head from a nigga right here
    and they can come and cut my head off, and
    and my legs off, and
    and i'ma still be a boss 'til my head gone, yeah
    break the wheel, pack the steel, hold my niggas down
    twistin' on that syrup ‘til i hear crackin’ sounds
    break the wheel, pack the steel, hold my niggas down
    twistin' on that syrup ‘til i hear crackin’ sounds
    break, break, break the steel, hold my niggas down
    twistin' on that syrup ‘til i hear crack, crack, crack
    break the wheel, pack the steel, hold my niggas down
    twistin' on that syrup ‘til i hear crack
    i don't trust nobody 'cause they don't deserve it
    niggas run in your house, they know you doin' dirty
    (go 'head, now)
    i got my hand on an ounce, and i got money servin'
    i just bought me a fifth and now i'm speedin', swervin'
    (go 'head, now)
    i took an eighth of them shrooms and now i'm hearin' voices
    i took like two of them pills, i can't remember nothing
    (go 'head, now)
    i ain't under control, i'm losin' motor function
    i need an intervention, i need an exorcism
    i need a therapist, paranoia and drug addiction
    it's very scary, my momma don't even recognize me
    i'm goin' crazy, don't need nobody to say they love me
    my acts of desperation, i'm on an empty stomach
    so fuck the consequences, i ain't runnin' from them
    feelin' like a goner, put my life in locker
    hotbox in the hummer
    hot bars in the summer (merlyn, merlyn!)
    if i had the option, i would do it all again
    if i had the option, i would do it all again
    i just wanna feel like i did the right program
    i just want to appeal to my dad and my cousins (again)
    when i cop that feel, i do not think 'bout diplomas
    love is knowin' that you didn’t do it by your lonesome
    so i forgive my mommy, daddy, auntie, and my uncles
    for guilt-tripping feelings whenever they call my number
    they see men dream, they see men fallin'
    but when i dream, i'm smashing on atlanta
    both pessimistic, drug addicted, caught in our feelings
    we spit venom then stare at the ceiling, wondering, "why?"
    my mom's no alcoholic, she just wanna drown her sorrows
    love her to death and soon enough i'll give back all i borrowed
    both so submissive, take turns dominating, the light has been faded
    this hate-fueled love, we don't fake it, no givin', just takin'
    i took some steps to be a bigger person
    i should've thrown ya off the highway to cars swerving
    ain't no burden, ain't no sermon, ain't no motherfuckin' plaque
    i hate these hospitals and police and the smell of death, all that
    i hate these shady folk, that want a lady like
    but don't treat lady right, but they be sayin' like ("just the tip!")
    and yeah you mad 'cause she ain't fuck, mad 'cause she ain't suck
    beat your ass before you got time to say "why not?"
    here to catch ya slip up, wish you could just rewind
    timing all fucked up, thought you had just lucked up
    where the respect? is your ass human?
    i look you in your eyes, say, "fuck you, are you fuckin' stupid?"
    respect my mother, 'spect my sister, 'spect these women, boy
    i get my 9-9, i don't own one, hit the store to blow your brains off
    better hope my aim off, better hope the range off
    better hope my tame off before i blow your brains off, boy
    uh, no hands with the stunts
    jump off the roof like i do what i want
    all of my life in my past wanna haunt
    and my sight of the future beginning to taunt my ambition
    man on the moon, i'm marooned, i ain't trippin', i'm on a mission
    every time that i speak they ain't skippin'
    turned my inspiration to a vision, that's a given, no slippin'

    my male role models drug dealers and thugs
    my father learned how to solve problems with guns
    and when i grew up i learned what racism was
    and what teaching it does, and like my teachers would say
    "little black boys have a place in the world
    like hanging from trees, or dead in the street"
    like i seen on tv
    all them boys they killed, they looked just like me
    not like brandon or chandler, but malik and kareem
    i was born with a target, and it stuck to my skin
    and i learned in social studies, i was one of them men
    who were locked in the chains, but not locked in the pen
    but i'm bigger than that, i'm the beginning and end
    i'm the sun and the moon
    i'm the light and the dark, i am life in the tomb
    i'm the pharaoh and slave, gentrifying my spirit
    it's like a knife in the womb, refuse to act like a parrot
    or to dance like a monkey, see your stance is apparent
    that's why i'm here for the money, don't care to cater to merit
    y'all fetishizing my spirit, i see your culture’s dependent
    on what you didn’t inherit, won't let my world be attempted
    i'm staying distant
    who gonna be the reason why i get high?
    who gonna be the reason why i turn over?
    who gonna be the gunner that i don't trust?
    who gonna be the gunner that get they ass whooped?
    who gonna be the reason why i get high?
    who gonna be the reason why i turn over?
    who gonna be the gunner that i don't trust?
    who gonna be the gunner that get they ass whooped?
    who gonna be the reason why i get high? (bloodsucka!)
    who gonna be the reason why i turn over? (bloodsucka!)
    who gonna be the gunner that i don't trust? (bloodsucka!)
    who gonna be the gunner that get they ass whooped? (bloodsucka!)
    who gonna be the reason why i get high? (bloodsucka!)
    who gonna be the reason why i turn over? (bloodsucka!)
    who gonna be the gunner that i don't trust? (bloodsucka!)
    who gonna be the gunner that get they ass whooped? (bloodsucka!)

    bum, bum, beat 'em, i would never wanna be 'em
    if i catch 'em slipping, they gon' have to meet the eagle
    bum, bum, beat 'em, treat these niggas how i see 'em
    i don't need you either, send you right back where i seen ya
    bum, bum, beat 'em, i would never wanna be 'em
    if i catch 'em slipping, they gon' have to meet the eagle
    bum, bum, beat 'em, treat these niggas how i see 'em
    i don't need you either, send you right back where i seen ya
    in the game, in the game, in the game, in the game (bloodsucka!)
    in the game, in the game, in the game, in the game (bloodsucka!)
    running thangs, running, run, running, run, running thangs (bloodsucka!)
    running thangs, running, run, running, run, running thangs
    in the game, in the game, in the game, in the, in the
    in the game, in the game, in the game, running thangs
    running thangs, running, run, running, run, running, run
    running thangs, running, run, running, run, running thangs

    stripped down to my skin and my bones
    i love huskies but i feel like a wolf (howl!)
    in a pack but i feel all alone
    i'm scatterbrained man, better offer the clon'
    in tejas apartments with racists doin' weird shit
    like, this'll make the biopic (haha!)
    rile 'em up, hit zaxby's, get the wing and tings (yum!)
    real quick bills still stacking to the ceiling (uh-oh...)
    whatchu mean, it ain't working? (what?)
    whatchu mean, you ain't finding yourself? (oh, i am, i'm trying)
    whatchu mean, you ain't got no cash? (i got a little bit...)
    whatchu mean? whatchu mean?
    shouldn't your pockets be big just like a fat chick? (uh-huh!)
    shouldn't your mama be done paying the house off? (i guess?)
    shouldn't you have a real big-ass ego? (no?)
    shouldn't these girls be flockin' just like seagulls? (eh...)

    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit
    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit

    the original lick-splickety, higher than yosemite
    breaking the mold mentally, master with no limiting
    making 'em say "ugh!", they worshipping our force viciously
    watching the floor tip in your temple of authenticity
    often they say i’m off it, i offer my crossed empathy
    they forgot what we on, i’ll remind 'em with hostility
    hot-diggity damn, everyone running scams
    gotta cover your clams and take another glance
    running a clinic, no scans, ain't no one claimin' yo mans
    it's all pertaining to plan, call me the architect
    lap you in a ufo, i haven't started yet
    still gotta figure out exactly where to park it at
    moses with the pen, each line an ocean i can part it at
    but that's too deep

    don't call me stupid, that ain't the way my name pronounced
    don't call me cupid, i got too many hoes right now
    poolside in houston
    tryna see if beyoncé will take me for adoption
    broke-ass rich suburbs
    a civilian shot in 3rd ward, we just by the fountain
    this is merlyn wood, man
    everywhere i go is the woodlands
    i need a honey butter, vodka in a sprite can
    when i'm in the whataburger, all the kids know who i am
    i need a honeybutter, puttin' lean in my sprite can

    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit
    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit

    i got a record but i'm clean as they come
    i'm godzilla, when they see me, they run
    on 37th, used to run from the bloods
    the undercovers gotta duck when they come
    i moved out and in a couple of months
    i'ma be a pop star, they call me a thug
    i used to write raps on the back of the bus
    now i'm in the front seat shifting the gears

    it's funny how things can change
    three hundred dollars to my name, led to hollywood
    i was living off ramen and change
    five hundred dollars on these dinners, never have to pay
    growing up my teachers told me
    "you better get them grades up if you wanna finish high school
    and after high school, you better get a degree
    'cause it's a dog-eat-dog world, you could live in the street"
    flashback, i had my walkman in the minivan
    listening to nsync, saw my name on the cd
    bleach blond tips, wanted to be jt
    wanted to do big things, had to fulfill a dream
    one might say i was doomed from the get-go
    but those same people assume, 'cause they'll never know
    what it's like to be called to what's not set in stone
    i am one with the ebb and flow, that's all i know

    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit
    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit
    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit
    twistin' me up like licorice
    think i need someone who can handle it
    ice on my boys and my wrist is fixed
    i don't need nobody tryna give me shit

    i don't know why i wanna fuck with you
    but all i know is that i really fuck with you
    really wish you didn't like to fuck with me
    wish you took that energy and trusted me
    i get so exhausted when you fuss with me
    'cause all that time could be spent in love with me
    i know i need it and you deserve it
    you like to size me up to see if it's all worth it
    i don't know where it is now, but i'm searchin'
    i think you want what i don't ever want: be perfect
    'cause i ain't perfect, i just wanna be good to you
    i would take my heart right out the hood for you
    wanna do the things i know i should for you
    standing by myself until i stood for you
    if i knew this love, i woulda looked for you
    but i'm glad you found me, i'm glad you found me

    [chorus: kevin abstract]
    callin', callin', callin', callin', trip, fall
    callin', callin', callin', callin', trip
    callin', callin', callin', callin', trip, fall
    callin', callin', callin', callin', trip
    callin', callin', callin', callin', trip, fall
    callin', callin', callin', callin', trip
    what you gonna do when you older?
    what you gonna do when you grow?

    split the diamond with us, fuck taking the bus
    i want a whip to call my own and a home to call my own
    all 14-15 of my niggas
    to figure, ooh, that's a step-back
    ooh, my nigga, that's a step-back
    if i had to choose, i would not choose you
    if i had to stop, i would turn around and choose glue
    if i had to hit the breaks, i'ma stop right
    if i had to choose, i'ma not choose you
    if i had to turn around, i'ma turn into some glue
    if i had to hit the brakes, i'ma stop right here, yeah

    callin', callin', callin', callin', trip, fall
    callin', callin, callin', callin', trip
    callin', callin', callin', callin', trip, fall
    callin', callin', callin', callin', trip
    callin', callin', callin', callin', trip, fall
    callin', callin', callin', callin', trip
    what you gonna do when you older?
    what you gonna do when you grow?

    you're all i love, washing off my hands
    you're all i love, washing off my hands
    you're all i love, washing off my hands

    don't waste your mind
    i'll be the one to settle
    to do what i am
    to say what i am
    don't waste your mind
    i'll be the one to settle
    to do what i am
    to say what i am

    callin', callin', callin', callin', trip, fall (you're all i love)
    callin', callin', callin', callin', trip (washing off my hands)
    callin', callin', callin', callin', trip, fall (you're all i love)
    callin', callin', callin', callin', trip (washing off my hands)
    callin', callin', callin', callin', trip, fall (you're all i love)
    callin', callin', callin', callin', trip (washing off my hands)
    what you gonna do when you older?
    what you gonna do when you grow?

    yeah!
    yeah, yeah, yeah!

    all i do is work and play (ay-yah-woo-woo!)
    tryna' find a place to stay (ay-yah-woo-woo!)
    tryna' find some food today (ay-yah-woo-woo!)
    this shit is real hard okay? (okay)
    take that, homie got the lysol spray, ain’t it? (ain't it?)
    you don't wanna see all my bad days, ain't it? (ain't it?)
    you don't wanna see what i got to say, ain't it?
    you don't wanna see my boys, man, they ain't friendly

    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down

    it ain't my birthday yet and i'm acting like a bitch
    screaming "motherfuck your set" like i'm 2pac
    ain't got no ice on me yet, still feeling how i dress
    so it's dickies and i got these hoes from walmart
    it ain't my birthday yet and i'm acting like a bitch
    screaming "motherfuck your set" like i'm 2pac
    ain't got no ice on me yet, still feeling how i dress
    so much dickies and i got these hoes from walmart

    i just saw my p.o. (what up, nigga?)
    he like me, though (he like me, though)
    clean money, tryna stay up out the streets, though
    7 days a week though, (all day!) it's that heat, though
    my daddy called me, said he seen my last video
    looking at a younger me, coulda had a heatstroke
    in the middle of the summer with my negros
    cool cuts and snow cones, smoking to the ozone
    smokin' 'til it's all gone, smoking 'til my folks come home

    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down
    trip a lot, sinned a lot, send em' all down

    runnin' outta time again
    runnin' outta time again
    runnin' outta time again, mmm
    ay-yeahh, ay-yeahh
    ooh, ooh, oo-ooh, ooh


    what are the rules for breakfast today?
    what are the words i'm forbidden to say?
    i need to let my hair down and grow it like a real ass bitch
    a real ass bitch, bitch
    what are the rules for breakfast today? (grow it like a real-)
    what are the words i'm forbidden to say? (grow it like a real-)
    i need to let my hair down and grow it like a real ass bitch (grow it like a real-)
    a real ass bitch, bitch (grow it like a real-)

    i've been beat up my whole life
    i've been shot down, kicked out twice
    ain't no stoppin' me tonight
    i'ma get all the things i like
    i've been beat up my whole life
    i've been shot down, kicked out twice
    ain't no stoppin' me tonight
    i'ma get all the things i like

    my niggas takin' over
    brockhampton, call your momma
    my niggas goin' platinum
    break necks, send you to the doctor
    best boy band since one direction
    makin' niggas itch like a skin infection, mm
    did me wrong like a perfect stepson, mm
    been a wrong, you can change the song, hun

    [verse 3: matt champion]
    who got me riled up?
    who the lame ass bitch wanna talk 'bout us?
    ooh, who got me riled up?
    who the lame ass bitch wanna talk 'bout us?
    ooh, come get it from me, uh
    come get it from me, uh
    come get it from me, uh, uh, uh
    come get it from me

    break necks, i'm the chiropractor
    come on down, you know i gotcha
    real shit, feelin' saturated
    realign the spine, fuck the haters
    break necks, i'm the chiropractor
    come on down, you know i gotcha
    real shit, feelin' saturated
    realign the spine, fuck the haters

    when you see me in the street, they say, "willy, willy!"
    but you won't see me in the street, i'm like a hillbilly
    i was sad 'cause nobody wanna suck my willy
    now i'm sad, everybody wanna suck my willy
    when you see me in the street, they say, "willy, willy!"
    but you won't see me in the street, i'm like a hillbilly
    i was sad 'cause nobody wanna suck my willy
    now i'm sad, everybody wanna suck my willy

    they be like, "what the fuck is you on?" when we hit the room
    move til' these niggas throw me in the tomb
    hear the sounds of the pharaoh when we spin the tunes
    everything feel right now you in the womb
    wanna motivate you in the afternoon
    top shelf money, that's my new perfume
    twist it up, light the end and inhale the fumes
    i'm the one that's zoom if you just assume

    i've been beat up my whole life
    i've been shot down, kicked out twice
    ain't no stoppin' me tonight
    i'ma get all the things i like
    i've been beat up my whole life
    i've been shot down, kicked out twice
    ain't no stoppin' me tonight
    i'ma get all the things i like

    pretty sure i'm maniacal, but what do i know?
    i don't know, all i know is what i see through my monocle
    that and the telescope, keep one lens on the money flow
    the other's gold and complemental trusty, well, well
    i'm rolling down hills in a suit through the mud
    throw my dress shoes in a fire with the woods
    sit back and relax with the fumes of everything i hate in the world
    play mozart, smoke my cigar on
    my estate, keep the cars parked on the front lawn
    neighbors hate, place duct tape underneath their tires
    and i wait

    sun sets to blood moon horizons
    left brain and right brain divided
    set frames and watch plays inside them
    in the mountains now's where you'll find him
    i smell a breeze in the morning
    i feel your presence, it's warming
    i paid attention to warnings
    but we were too caught up in transforming

    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to
    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to
    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to
    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to

    lucky days, i'm burnin' the four-sil
    your boy is dusty like brush up a fossil
    hear that shit urk like the noise of a possum
    bitch, i'm a king, i was born in the castle
    built like a boxer, i'm ready to tussle
    fuck on my baby, i'm ready to bust one
    come fuck with me and my dogs
    hate on my ass like in-laws, uh
    that boy stay light like a cheerleader, um
    she want me filled like a two litre, um
    eat it all day, watch it ricochet off
    then i skrrt off on that michelin, aw
    they don't got nothing on me 'til i pop
    they don't got nothing on me, call the cops
    i hit that run like a heisman boy, run it back
    look at that boy, hit that running back

    shout out to south central, san marcos
    i got addicted to soft shell tacos
    right after panties and ramen noodles
    now i see how i'm gon' make a shooter
    stamina, stamina!
    i used to be holding the camera
    head through the glass, throw your window up
    start praying to me like my handle cortana
    we like wu-tang but i feel like santana
    sweet talkin' just like she hannah montana
    head was clean, tony fantano
    made her my wife-a
    she can't eat 'cause she's so bella
    confused erection
    bad hoes, no name, brand slave, brainless

    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to
    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to
    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to
    ghetto in here flash it, ooh, them boys stay nasty
    floating like aladdin, them the ones you talkin' to

    when i imagine myself on acid
    i take steps backwards and find those to lap itself
    even dance and pounce around
    my silent thoughts who had the crown
    don't-don't-don't-don't let life pass yourself
    when i imagine myself on acid
    i take steps backwards and find those to lap itself
    even dance and pounce around
    my silent thoughts who had the crown
    don't-don't-don't-don't let life pass yourself

    i could've got a job at mcdonald's, but i like curly fries
    that's a metaphor for my life, and i like taller guys
    could've got a deal if i wanted, but i like owning shit
    and i like making shit, and i like selling it

    could've peaked when i was in high school, but i had bigger plans
    could've took the time out to find you, but you ain't understand
    you don't gotta leave for them to define you, cause what could you demand?
    when everybody out to define you without a circumstance

    anybody got harry styles' phone number?
    okay, i called him and they said i got the wrong number
    i was tryna be pac when i was younger, dreaming of better days
    i don't see my mom no more, remind me of bad weather days

    if you got a problem with me, try some other guy
    i let you know i'm a dog, i eat the cat alive
    but really, though, i'm alone, 'cause i don't stick around
    and yes, i know it's my fault, so put your finger down

    i would keep this shit pent up if it weren't for my mom
    if it weren't for dijon, yeah, i don't like to lie
    guess it sounds out the month
    should've opened up my mouth more, show 'em what my fist for
    let 'em get a fistful, caught up in the lust, man
    bred from the legs of straight killers on best end
    black eyes, bloody sheets, damn, where yo' feet stand?
    we should get a new plan, maybe some more fans

    i love it when the people go wild for me
    i love it when the people go wild for me
    i love it when the people go wild for me
    keep it wild for me, wild, wild, homie
    i love it when the people go wild for me
    i love it when the people go wild for me
    i love it when the people go wild for me
    keep it wild for me, wild, wild, homie

    baby, i been trippin' off 'em, tie me up and send 'em off
    and i been on a mission for it, i just want my own apartment
    i just want a space with my old best friend
    lock me in your cellular, won't elevate again
    baby, i been trippin' off 'em, tie me up and send 'em off
    and i been on a mission for it, i just want my own apartment
    i just want a space with my old best friend
    lock me in your cellular, won't elevate again

    i'm a shithead son, and i'm bad at growing up
    i'm a shithead son, and i'm bad at growing up
    my life ain't been the same since my dog died
    since my girl left
    i quit drinking and drugging and still can't get ahead
    been at a loss for words
    it seems i'm destined to fall apart when i'm depressed
    it's all a test, scream at god from my bedside
    i glue my hands together, life's got me hog-tied
    there's no applause in the game of life, i just bought a car
    and a new house, here's the cost to prove it
    i spin a little wheel when i'm feelin' moody
    and that's like all the time, try not to mind the clock
    because my heart is ticking, i smoke a pack a day and
    i wish i didn't, having some trouble quittin'
    i have a couple vices, we had that show on viceland
    i was hardly in it, most the time i'm hidden
    anxious, impatient and always wanting something different
    i hate the way i'm feeling, i'm sick of chasing feelings

    baby, i been trippin' off 'em, tie me up and send 'em off
    and i been on a mission for it, i just want my own apartment
    i just want a space with my old best friend
    lock me in your cellular, won't elevate again
    baby, i been trippin' off 'em, tie me up and send 'em off
    and i been on a mission for it, i just want my own apartment
    i just want a space with my old best friend
    lock me in your cellular, won't elevate again

    i grew up all alone, my mom and dad fighting
    i moved around a lot, i did a lot of fighting
    i met my friend ian, i seen a lot of cyphers
    i did a lot of writing

    watch my uncles duck indictments
    i'm used to ramen noodles, victims of mental illness
    products of neighborhoods with broken souls and wounded spirits
    don't judge me by appearance (i moved to california)
    started getting paid (nigga, you broke) shit's already boring

    dash into the money like a hyphen, fuck a pipe dream, man
    had this shit when i was in my diapers
    burnin' through my diapers, hot shit
    it was hot shit, back when niggas looking for the loch ness

    stuck 'round dip spittin' assholes, make they mamas bashful
    got holes in my pockets so my shoes full of cash though
    cigar, fidel castro, car full of castrol
    see the sunset when i backstroke, can't swim but i could act though

    i was playing rock paper scissors with imaginary friends
    imagine having no friends, ayy
    i was playing rock paper scissors with imaginary friends, ayy
    imagine having no friends, man
    i was playing rock paper scissors with imaginary friends
    imagine having no friends, man... ayy
    imagine having no friends, man

    me la pasé mejor que nunca aquí, a pesar de que cometí algunos errores
    pólvora y accidentes
    la navidad nunca es el mejor momento para mí
    ¡ah dios, cómo extraño a mi familia!
    a veces salgo y me fijo en los aviones que sobrevuelan mi casa
    enciendo un cigarillo y miro al suelo
    manteniendo mi cabeza baja por los próximos días
    con mis zapatos atados
    pero bueno
    casi terminamos muchachos, casi terminamos

    merlyn, hopping out the vehicle, i feel like batman
    hanging with directors, 'bout that action
    so please don't stick and move in my direction
    all i got to lose is my erection

    i'm a black man with a deadly weapon
    (what drug reference, huh?)
    i'm a real dog, we all go to heaven
    but i been tripping on the steps and i don't think i'll make it
    i'm in this big house, still i'm suffocating

    carnival, my heart like a supreme phantom
    going hundred speed, blowin' steam, i throw a tantrum
    judging by my face, my eyes slit like a python
    i think she might hate me for a lifetime, ay, ay
    daddy cracking red drum, blueprint for the pipeline
    going out the weather, leave my name, i'm goin' offline
    i just want my shit to fit, tailored just like tiffany
    oh, they say i'm perfect, on my back, oh, man, they killing me

    boys wanna play with my cell phone
    but i don't want nobody to see what's in it
    boys wanna play with my cell phone
    but i don't want nobody to see what's in it
    boys wanna play with my cell phone
    (wha-wha, aqua, for my)
    but i don't want nobody to see what's in it
    (wha-wha, aqua, for my)
    boys wanna play with my cell phone
    (wha-wha, aqua, for my)
    but i don't want nobody to see what's in it
    (wha-wha, aqua, for my)

    white burner, black burner, i do not discriminate
    i am on a pilgrimage so don't try to insinuate
    building up an instrument to aim it at the human race
    let it off in hopes that all the pain and stress disintegrates
    i think you intolerant, when you do the most it's moderate
    i come with that gas that'll make you think i had a doctorate
    what we do provocative, i ain't no apologist
    don't step to professionals if you still move like novices

    america's favorite, i do my best and they hate it
    it's like i'm stuck in the matrix and i'm stuck losin' patience
    while they stuck on they day shift, i hate my boyfriend's fragrance
    i'm a faggot, i say it, i scream that shit like i mean it
    yeah, i'm ugly and genius
    i went from nothing to sleeping on jon's couch
    to makin' people bounce at every show that's sold out
    you know who i'm talkin' 'bout, with ghouls all in my dirty mouth
    boys be on that silly shit so billy 'bout to air 'em out

    boys wanna play with my cell phone
    but i don't want nobody to see what's in it
    boys wanna play with my cell phone
    but i don't want nobody to see what's in it
    boys wanna play with my cell phone
    (wha-wha, aqua, for my)
    but i don't want nobody to see what's in it
    (wha-wha, aqua, for my)
    boys wanna play with my cell phone
    (wha-wha, aqua, for my)
    but i don't want nobody to see what's in it
    (wha-wha, aqua, for my)

    who got the feelin'? tell me why i cry when i feel it
    tell me why, tell me why
    who got the feelin'? tell me why i cry when i feel it
    tell me why, tell me why (why?)

    phone ringin', never outgoin', homebody
    never outgoin', put my doubts on when these walls up
    tearing at the black tie, finish addin' notches to my belt loop
    they say help you, i can't help you
    why i can't speak out? is wideout, wideout
    keep it deep inside my mind, it's off-kilter, off-kilter
    i turn memory to fantasy, for that better pleasure, fuck
    time machine gonna make it better, maybe better for ya
    i can't make this up, i can't take it back
    feel like a monster, feel like a deadhead zombie
    feelings you don't want me, i ain't givin' up, you should set it off
    tell me “time's up,” let the water run, let my body run

    who got the feelin'? tell me why i cry when i feel it
    tell me why, tell me why
    who got the feelin'? tell me why i cry when i feel it
    tell me why, tell me why (why?)

    said she wanna get high off a nigga
    i wanna die durin' sex or religion
    god and pussy only know my intentions
    waking on the tour bus then i'm swimmin'
    you'd be hurtin' if you trust me but you isn't
    honestly, that's probably the right decision
    pick up, listen, if you wanna get rich
    no sleep, how real bad man wake up

    i found false hope in all kinda places
    hotel rooms and temporary feelings
    i put my clothes on and try to check out
    i try to hide from the sun, let it set now
    don't let god see me, i got a lot of demons
    and i've been sleepin' with 'em
    and now i'm tangled in the sheets and sinkin' deeper with 'em
    i'm going deeper in it, find me drownin' in it

    they said “do you make mistakes or do you make a change
    or do you draw the line for when it's better days?”
    you taste the wind for when it's cold enough to kill our flame
    i wonder who's to blame
    they ask me “do you make mistakes or do you make a change
    or do you draw the line for when it's better days?”
    we taste the wind for when it's cold enough to kill our flame
    i wonder who's to blame

    who got the feelin'? tell me why i cry when i feel it
    tell me why, tell me why
    who got the feelin'? tell me why i cry when i feel it
    tell me why, tell me why (why?)

    everything i have (is a mirror)
    and everywhere i stand (isn't solid ground)
    people don't make sense (to me anymore)
    i'm hiding out, again, tryna figure it out
    i'm tryna figure it out
    i'm tryna figure it out, yeah
    i'm tryna figure it out
    i forgot my passport for sure, all for a pretty sky
    i forgot my passport for sure, all for a pretty sky
    i forgot my passport for sure, all for a pretty sky
    i forgot my passport for sure, all for a pretty sky

    everything you wear, i'll be the one to care
    softly, you braid your hair, all the angels stare, yeah
    tell me why, tell me why (why?)

    i used to work for people
    i made a couple hundred dollars, wasn't worth it even
    i'm worth a hundred thousand
    not dollars but diamonds, i am mud out the bayou
    rip a page out the bible, come and crucify me
    i'm a long way from home and this ain't yellowstone
    i trade a white bitch for catfish and yellow bones
    this from the catacombs, this for the broken homes
    from the south side of cities where my granny home
    i moved to california, i bring a grammy home
    i call up bill collectors, "leave my fucking family 'lone"
    we left the corner store on the way to caviar
    the coupe is mustard colored, what the fuck is grey poupon?

    young k.a., never quit your day job, uh
    i bring the love to work, i need the day off, uh
    i need the [censored], this hard work should pay off, uh
    the lights stay off until my mind is made up, uh
    a young zuckerberg, i wake up and make stuff, uh
    these niggas copy us, they really need to pay us, uh
    i'm from the city where your neighbors fight back
    you talking shit, we bring that work right to your lap
    i love my niggas like white people love rap
    we make the shit you'll probably never say on track again

    walked through doors all my life, just to close them
    tore down walls all my life, here's to the other side
    a whole new life
    (feeling the brand new feeling, feeling the brand new feeling)
    a whole new life
    (feeling the brand new feeling, feeling the brand new feeling)
    a whole new life
    (new feeling, brand new feeling, brand new feeling)
    a whole new life
    (new feeling, brand new feeling, brand new)
    (brand new, brand new)

    (a whole new life)
    back when i was hustling, ain't get no love from them (uh)
    (a whole new life)
    i paid my own bills and came up with the illest shit (uh)
    (a whole new life)
    i was tryna find a way to get my family out of it (uh)
    (a whole new life)
    spent my days in basements tryna write a motherfuckin' hit
    nowadays he's stumbling, they show such love to him
    i shut it down to every show, we set the precedent
    i'm just tryna show these niggas, life is on some other shit
    keep your head high, smile when the trouble rumblin'

    i don't do what they say, it's unorthodox
    like bears sharing porridge inside with goldilocks
    like ozzy with no sharon, he just called his parents
    so fuck what i'm doing and fuck these damn critics
    you should think for yourself, that shit is cancerous
    get my head rubbed by fingers of fuckin' hand models
    middle finger, fuck the hair up at all our concerts
    maybe if i cared less, i'd wear a hair net
    but now my eyes, ten million by twenty five
    dropped out of lone star, booked flight from lone star
    was working a couple jobs and quit, became a star, uh

    put the bag in the cup, add it up, add it up
    put my friends in the truck, add it up, add it up
    if you think you know me now, that's enough, that's enough
    if you think you know me now, that's enough, that's enough
    put the bag in the cup, add it up, add it up
    put my friends in the truck, add it up, add it up
    if you think you know me now, that's enough, that's enough
    if you think you know me now, that's enough, that's enough

    do you see what you contribute to my consciousness?
    voices feelin' so ominous
    i can't place a pen for you, they mark it out as anonymous
    i would shift the whole continent
    if it helped you 'round with some confidence
    thinkin' bout all the consequence
    gotta try to break, was monotonous

    how could i be better?
    i paid the price in full, just to clear the record
    rewound just to fast forward
    on the eight-track i stole from my grandmama

    catastrophic, where the stoppin'?
    man, i wish i had a rocket
    wish i ain't feel microscopic
    wish my thoughts was telepathic
    but instead i'm always rapping
    love rappin' like it's my girlfriend
    every tour is like a catfish
    just kidding, i love you assholes

    put the bag in the cup, add it up, add it up
    put my friends in the truck, add it up, add it up
    if you think you know me now, that's enough, that's enough
    if you think you know me now, that's enough, that's enough

    it's hard to air out in deep water
    you keep calling, i ignore it
    cleared my conscience in absurd ways
    i do the things you hate, i'm changing every day

    i just wanna know, know (i just wanna know where the party at)
    i just wanna know, know (24/7 thinkin' 'bout you)
    i just wanna know, know (i just wanna know when we leavin', boo)
    i just wanna know, know (24/7 thinkin' 'bout you)
    i just wanna know, know (i just wanna know where the party at)
    i just wanna know, know (24/7 thinkin' 'bout you)
    i just wanna know, know (i just wanna know when we leavin', boo)
    i just wanna know, know (24/7 thinkin' 'bout you)

    put the bag in the cup, add it up, add it up
    put my friends in the truck, add it up, add it up
    if you think you know me now, that's enough, that's enough
    if you think you know me now, that's enough, that's enough
    put the bag in the cup, add it up, add it up
    put my friends in the truck, add it up, add it up
    if you think you know me now, that's enough, that's enough
    if you think you know me now, that's enough, that's enough

    no quiero beber agua hoy
    no quiero caminar por el vecindario y ver cuán perfecto es el mundo
    no quiero hablar con nadie
    solo quiero pararme enfrente de mi casa y ver como se hunde en mis llamas
    ojalá pudiera pedirle a mis amigos que se salgan afuera
    ojalá pudiera haberlos salvado, uno por uno
    pero todo se ha ido
    me pregunto a menudamente si yo seré el proximo
    summer, lo siento

    drink of the apple pie with it, yeah, yeah, yeah
    i don't got no chains in my denim, yeah, yeah, yeah
    i don't listen what the blogs tell me, yeah, yeah, yeah
    i know niggas got their own agenda, yeah, yeah, yeah

    i've got [censored] but you would never know
    i like to hide them, so much i lose myself
    that's why i'm pure to some, a psychopath to others
    and grew up in counseling, flipping off my counselors
    they gave me mood stabilizers but when i came off 'em, i was violent
    took the drugs that i wanted which didn't help with the voices
    they just grew louder and louder
    like all the people who'd just chatter and chatter
    i juggle all my personalities

    estoy tan harto y cansado, no puedo seguir haciendo esto
    ojalá pudiera rendirme pero tengo que seguir siendo fuerte para mi familia y mis amigos

    i found myself getting better by the fucking minute
    'member when my momma always had to save the minutes
    got some d's, dropped out, wanted to be russell simmons
    gotta keep workin', my head on innervisions
    where the kitchen at? keep the lyrics written
    raid my cell and dope, askin' for forgiveness
    i just ran into somebody sellin' lemonade
    kiss your kids tonight before them bitches run away

    get your man, get your man all up off me
    think again, want a hundred bands around me
    in december, i don't care what they call me

    this for all my broke niggas, this for all them jokes, nigga
    that you niggas made when i was still livin' at home, nigga
    did it on my own, nigga, grew up and i bossed out
    grew up and i bossed out, grew up and i bossed out

    i see you peekin’ through bushes
    and tryna get secret ingredients from us
    i know that you do it 'cause you see us boomin'
    like c4 when you hit that detonator
    lucky-lucky on the elevator
    eat my dust, baby, i’ll see ya later
    i could always call your bluff
    you already said enough
    take a risk, bitch
    still sittin' on your ass, waitin' for a handout
    giving nothin', put your hands down
    "ooh, yeah, this for the culture!"
    "ooh, yeah, this important!"
    fuck off with that slang shit
    fuck off with that networking
    keep ya mouth where the money at

    yellow lights on my dashboard
    red flags in the rearview
    i know i'm the one that made you upset
    but all i wanna do is see you
    you know that lately i don't think straight
    but i don't really know what i'm doing now
    'cause everybody got me fucked up
    i'm struggling while on the move now
    yellow lights on my dashboard
    red flags in the rearview
    i know i'm the one that made you upset
    but all i wanna do is heal you
    you know that lately i don't think straight
    but lately i don't know what to do now
    'cause everybody got me fucked up
    i'm struggling while on the move now

    get your man, get your man all up off me
    think again, want a hundred bands around me
    in december, i don't care what they call me
    get your man, get your man all up off me
    think again, want a hundred bands around me
    in december, i don't care what they call me
    get your man, get your man all up off me
    think again, want a hundred bands around me
    in december, i don't care what they call me
    get your man, get your man all up off me
    think again, want a hundred bands around me
    in december, i don't care what they call me


    barely got control of it, must've got a hold of it
    threw me to the ground and left a scar right on my nigga-lips
    i look in my closet when i think about the past life
    never good in my wallet, tryna see if i got my cash right
    fuck a flight, they ain't never wanna treat my bag right
    fuck a job, they ain't never treat my mom and dad right

    i hate them quiet suburbs, i hate those picket fences
    i hate the separation, first thing they called me: "nigga"
    i fight, i got suspended, my teachers saw me hit him
    so they ain't listen to me, and from that moment on
    i would learn that i was different
    i would grow to see the difference
    second guessing my decisions, black bodies come up missing

    i feel like all my days are coming to a blend
    i feel like all my days are coming to a blend

    i would walk through the halls at my own pace
    every lunch, i would flow, having no place
    all the books in my bag 'til my bones ache
    wonder how the world would be if i had no face
    if i had no heart, if i had no skin
    and i was just thoughts, reminiscing
    the things i always brushed off
    had my father try to tell me i was just soft
    and when i look at the things that i've been through
    and the things i survived, and at what cost?
    all the love in my life that i just lost
    all this shit persevere to the pole vault
    in the lies of the law, i'm a problem
    in the eyes of the blogs, i'm a paycheck
    in the eyes of the world, i'm a icon
    in the eyes of my own, i ain't start yet
    in the eyes of the law, i'm a problem
    in the eyes of the blogs, i'm a paycheck
    in the eyes of the world, i'm a icon
    in the eyes that i own, i ain't start yet, i ain't start yet

    power, african power!
    power, african power!
    power, african power!

    i feel like all my days are coming to a blend
    i feel like all my days are coming to a blend
    uh, i feel like all my days are coming to a blend
    i feel like all my days are coming to a blend

    i need it all downtown, nigga
    put it back where you fuckin' found it though
    i need it all down (my nigga)
    keep 'em right there, oh, you found 'em though
    i want a shirt that make my body feel all sexy
    i want a chain that make my body feel all hefty
    i want my head to fall off when i walk out the door
    i want the rain to fall down and i'm askin' for more

    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head
    (ride slow, ride slow, slow)
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head (woo, slow)
    (ride slow, ride slow, slow)
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head (woo, slow)

    i want a love that make me feel like i ain't breakin' ya heart
    i wanna know what made you stay
    when it was wrong from the start
    i need to know where you went lookin'
    where you went through the chart
    i need this fear of being everybody else to depart
    i got a lot on my mind, not enough hours to shed
    not enough trust to believe, not enough feelin' to care
    i'm feeling numb to the world so i've been ignoring instead
    i'm seeing through what i wanted, to recognize who is there, yeah

    throw me in the fire, baby, i'll survive
    coming top down by the seaside
    ay-yi-yi-yi-yah
    ay-yi-yi-yi-yah
    see the road sign on the 45
    only you and me by the borderline (ooo)
    ay-yi-yi-yi-yah (ooo-ooo)
    ay-yi-yi-yi-yah, let it go

    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head
    (ride slow, ride slow, slow)
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head (woo, slow)
    (ride slow, ride slow, slow)
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head (woo, slow)

    and i will show you off for everything i own
    i know it's not what you're used to
    see they could tear me down, take everything i made
    i'll still be here next to you

    throw me in the fire, baby, i'll survive
    coming top down by the seaside
    ay-yi-yi-yi-yah
    ay-yi-yi-yi-yah
    see the wrong side of the 45
    only you and me by the borderline (ooo)
    ay-yi-yi-yi-yah (ooo-ooo)
    ay-yi-yi-yi-yah, let it go

    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head
    (ride slow, ride slow, slow)
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head (woo, slow)
    (ride slow, ride slow, slow)
    ridin' on the roof with a dollar sign attached to my
    head, head, head, head, head, head, head, head (woo, slow)

    i spent like a year and a half on the greyhound bus
    on the way to see this girl
    take a flight back just to keep my job
    used to fly standby, late to the airport
    where the buddy pass? stuck in the traffic
    whole lotta hours, real long distance
    but i've grown since then
    learned to be on my own since then
    marble floor in my brand new crib
    this the life that i wanted still
    got a hole and it burn my chest
    mash the chip that's still in my shoulder
    ain't a day that i still been sober
    these the things that i'm tripping over

    y'all motherfuckers made three albums
    still talking about the same shit
    the one gay, the one selling drugs
    the one that's tryna act like lil wayne
    what the fuck is this shit man?
    y'all better turn this shit off when y'all get in the whip
    when y'all enter my whip, y'all better not play this shit
    'cause this can go right the fuck off

    now them boys hooked on heroin
    parents always asking like, "where y'all get it from?"
    rehab poppin' like when amy had the single out
    single out the reasons how i quit before i fell down
    i used to pick ameer up
    talk about what's got us fucked up
    we vent 'til the sun up, ay
    hopefully get our funds up, ay
    and if i didn't know y'all
    maybe i would have a desk job
    ticking 'til i off myself...

    used to drive around for some hours (oh-oh)
    used to get paid by the hour (oh-oh)
    now i'm just pickin up my check (oh-oh)
    now i'm just pickin up a sweat (yeah)
    used to drive around for some hours (oh-oh)
    circle round the block for some hours (oh-oh)
    now i'm just pickin up my check (oh-oh)
    now i'm just pickin up a sweat (yeah)

    be there any minute, i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby

    i spent like a year and a half feeling sorry for myself
    'cause i thought love ain't make sense anymore
    if i drank, you would probably see a fifth on the floor
    and a hole in the door, rest a few more
    scared of the past i’ve been tryna avoid
    from before i was born
    running from the shoes that my grandfathers wore
    tryna pick a better battle i saw on the wharf
    feel the sun in my pores but i still got clouds in my head, now
    rain for a little bit, stay for a little bit
    moved along with my head, down
    that's what momma taught me and i never let them fuck me
    when they handed me a dead king's crown
    told 'em think of what you doing before i'm the one you're choosing
    i just wanna be a human when i share myself
    hear the things i'm saying and i scare myself, goddamn

    be there any minute, i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby
    be there any minute (ooh), i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby
    be there any minute, i'll be on it, in it baby
    be there any minute (ooh), i'll be on it, in it, baby
    be there any minute, i'll be on it, in it, baby

    padre celestial
    soy tu humilde servidor
    te presento mi necesidad de esperanza
    hay momentos en que me siento impotente
    hay momentos en que me siento débil
    rezo por esperanza
    necesito esperanza para un futuro mejor
    necesito esperanza para una vida mejor
    necesito esperanza para amor y amabilidad
    algunos dicen que el cielo se hace más oscuro justo antes de la luz
    rezo que esto sea cierto
    ya que todo parece oscuro
    necesito tu luz, señor, en cada sentido
    rezo para ser llenado con tu luz de cabeza a pies
    para disfrutar de tu gloria y saber que todo está bien en el mundo
    como has planeado, y como quieres que sea
    ayúdame a caminar en tu luz, y vivir mi vida en fe y gloria
    en tu nombre rezo
    amén

    evanie, did you lie to him since you were seventeen?
    how's he holding up?
    evanie, do you cling to him like you would onto me?
    bet he needs you more than i
    evanie, did you hide your neck to save him from his sleep?
    i know how that feels
    evanie, every chance you take you make me want to flee
    can't you see?

    you should move on
    i swear you'll be fine
    whenever you want
    i'll be your ride
    and when you're alone, and his love is gone
    maybe you'll see that your company was the worst
    thing for him, your sin


    little old me, i thought my world was progressive
    'cause my president was black, twenty-five lighters on the dresser
    i had guilt trip on my back and a bulletproof vest
    inside my uncle john's toyota was a walking crayola–
    (gimme that mic, nigga)
    i got a hard time, i gotta watch myself
    the way i move through a room full of suits
    ain't no, ain't no constitution, i hate uniforms (ha, ha, ha!)
    i hate handcuffs, i can't stand up (shut up, nigga!)
    they throw me in the crowd and tell me "boy, i'd lose that smile"
    but see i got it from my dad and that's the reason why we had
    i raise my black fist, i got big lips
    i'm strong as samson, they cut my fucking locks
    i lose my fucking strength, fuck

    i'm running out of zips
    my life been feeling tense, i won't be on the fence
    i put my phone on airplane mode cause i'm on autopilot
    i need a lot of patience, i need a lot of silence

    i hope this holy water burn me 'cause i ain't worth this life
    i ain't worth the light of day, but for some i light the way
    nude along the banister, kitchen smell of lavender
    swimming in my wranglers, i am another caliber

    ooh, yeah
    soon, soon
    no, no, no, no, no, no

''',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
