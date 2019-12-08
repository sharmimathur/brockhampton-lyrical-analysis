import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions

authenticator = IAMAuthenticator('8O9EMgIsxfs9-tsACK_-FTZSQey4_69U2WdjirOgzjbT')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

#natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    text='''
    i don't know where i'm goin'
    if  i gotta take the high road, i'm rollin'

    i  ain't tryna get like all up in your head again, montana, 'lanta
    maybe i should just go mosey my ass over to your house
    bewildered by the sight of you up on the couch, so cozy
    lowly  lit lights, rosy cheeks, oh, you so cozy with somebody else
    get  nervous, my stomach churnin', burnin'
    i'm beat, ready to knock some teeth out of his ass
    late  night corner, we pass
    lick that swisher, get red
    used to skip rocks 'round that bend
    we don't go there no more
    we  don't see sun no more
    baby wanna raid the whole apartment like the fbi
    takin' everything, from pots and pans to fans to goldeneye
    everything 'cept the dog
    everything in the drawers
    used to be so perfect, but it's never gettin' solved

    i'm sure i'll find it
    no one help me when my eyes go red
    i'm sure i'll find it
    no one help me when my, no one help when my
    i'm sure i'll find it
    no one help me when my eyes go red
    i'm sure i'll find it
    no one help me when my, no one help when my

    do i matter? i'm ecstatic, i'm depressed
    more like god's special mess, never had no halo
    trippy, i can barely hike it out of bed
    time bomb under it, persuading you to hop in
    mmm, options, runnin' out of options
    mmm, options, used to have options
    mmm, options, runnin' out of options
    mmm, options, used to have options

    i don't know where i'm goin'
    if i gotta take the high road, i'm rollin'
    i don't know where i'm goin'
    if i gotta take the high road, i'm rollin'

    i'm sure i'll find it
    no one help me when my eyes go red
    i'm sure i'll find it
    no one help me when my, no one help when my
    i'm sure i'll find it
    no one help me when my eyes go red
    i'm sure i'll find it
    no one help me when my, no one help when my

    used to fight all my night terrors, now i smoke through the dreams
    depression put me into places where i'm stuck in the seams
    they sealed my mouth and said the only way to breathe is to scream
    pop the stitches from society and fall to my knees
    the machines weavin' our fate are gettin' harder to please
    but i believe to an extreme
    (that we all can find a way)
    to anybody listenin' that's in between
    (that we all can find a way)

    went to church for the hell of it, stumbled in drunk as shit
    been goin' through it again
    been talkin' to myself, wonderin' who i am
    been thinkin' i am better than him
    in times like these, i just need to believe it's all part of a plan
    lost a part of me, but i am still here

    wash it out of all of me to feel the fire (maybe i'll be gone for a minute)
    but you know, you know that's a lie (no one help me when my eyes go)
    wash it out of all of me to feel the fire (maybe i'll be gone for a minute)
    but you know, you know that's a lie (no one help me when my eyes go)

    i'm sure i'll find it
    no one help me when my eyes go red
    i'm sure i'll find it
    no one help me when my, no one help me when my
    i'm sure i'll find it
    no one help me when my eyes go red
    i'm sure i'll find it
    no one help me when my, no one help me when my

    spendin' all my nights alone, waitin' for you to call me
    you're the only one i want by my side when i fall asleep
    tell me what i'm waitin' for, tell me what i'm waitin' for
    i know it's hard but we need each other
    know it's hard but we need each other

    i move mountains on my own, don't need nobody help
    changed your mind when i changed my life, better start believin' in myself
    and we all out lookin' for, lookin' for god so we never see it in ourself
    shit, divine intervention move in stealth
    it's hard to tell what the prayer compelled
    you can find me dancin' in between the raindrops
    tryna find a way to make the pain stop
    overtime, on the graveyard
    got a nigga feeling brainwashed
    my instability's trademark
    copy-written in all my decisions
    this is not supposed to be a way of livin'
    turned my temple down into a prison, shit

    spendin' all my nights alone, waitin' for you to call me
    you're the only one i want by my side when i fall asleep
    tell me what i'm waitin' for, tell me what i'm waitin' for
    i know it's hard but we need each other
    know it's hard but we need each other

    yeah, back on vincent with the braces on
    used to slide out the back without the neighbors knowin'
    pose for the picture with the pearly whites
    dead lens zoomin' in, catchin' all my strikes
    used to trade jordan for some molly
    and she gave me all i need for the night, forties suffice
    morally alright, but i need some advice
    and i know that i'm actin' foolish
    chris would pick me up around noon-ish
    half a blunt, yeah, we coolin'
    twist it up, puttin' on outkast
    hunnid, texas heat, and yeah, we cruisin'

    but when i love you right, i love you right
    all by yourself
    but i'll make it bright, baby, i want you to know
    i'ma be there for you, i'ma make you see that
    i want you, i want you

    spendin' all my nights alone, waitin' for you to call me
    you're the only one i want by my side when i fall asleep
    tell me what i'm waitin' for, tell me what i'm waitin' for
    i know it's hard but we need each other
    know it's hard but we need each other

    back and forth
    i'll take that if that's all you askin' for
    with my legs up on the dashboard
    only thing in my pocket is my passport, pa-passport
    back and forth
    i'll take that if that's all you askin' for
    with my legs up on the dashboard
    only thing in my pocket is my passport, pa-passport
    back and forth
    i'll take that if that's all you askin' for
    with my legs up on the dashboard
    only thing in my pocket is my passport, pa-passport

    so, do you love me, love me, love me?
    do you love me, love me, love me?
    do you love me, love me, love me?
    do you love me, love me? oh
    do you love me, love me, love me?
    do you love me, love me, love me?
    do you love me, love me, love me?
    do you love me, love me? oh

    jabari, me paddy

    everybody  ask me how i deal with my depression
    man  look, man, i don't got the answer to your question
    if i did, you would probably never hear from me again
    that's a promise, not a threat and it ain't no half-steppin' (hey)
    can't  let it compromise the pace i'm settin' (hey)
    grandma  told me don't forget to count my blessings (woo)
    breakin' up botanicals to ease my stressin'
    was  the one that you needed but you weren't expectin'
    game need refreshin' (hey), what you been suggestin'? (hey)
    wrote a new constitution, we don't need amendin' (hey)
    i go johnnie cochran when i'm raisin' my defenses (yeah)
    man,  i feel like michael keaton when a nigga start ascendin' (hey)
    never second-guessin' (hey), had to do a lot of restin' (hey)
    like i played for popovich, tryna fine our new direction (woo)
    listen, i ain't for the shelvin', what you niggas tellin'?
    my team been rebellin' from wherever you were headin', goddam

    man, this shit bump like a belly when it's pregnant (mhm)
    bonafide big brr lookin' like a yeti (mhm)
    swift feet cheetah, that's a real big kitty
    who made y'all judges? that's a real ass feeling
    i don't like the sly ones, forget 'em and i dead 'em (yeah)
    always off the shit like a constipated reverend (alright)
    y'all don't like to shit talk, dumb pun, all fun
    but i make your bitch crack a giggle with the next one (oh)
    goofy ass boy, look like elmer fudd's cousin (sheesh)
    heavy-ass feet, bet pluto heard you comin' (shit)
    actin' like regina, you a lil' bit dramatic (george)
    i been in the cockpit, i been in the cabin (right)
    take the ego out, just revolve around the planet (right)
    damn, i'm like kirby, man, i don't take damage
    oh, so hot, so, sst, get branded
    i'm just havin' fun, cops hit me, goddamn it

    trauma got me fucked up, my mama got me fucked up
    my lil' nigga locked up, it's like hakuna matata
    never liked sci-fi, empathetic wifi
    keep it in the back room, hidin' with my dry eye
    put it in the vacuum, i got love for my label
    fifteen million on the table, none of my niggas is stable
    need a personal connection, i just wanna feel you, baby
    bein' sober made me realize how poorly i been behavin', uh

    my bitch, she so pretty, pretty (mmh)
    i get cash like really, really
    tell the dj, man, he ain't slick
    'cause he ain't playin' hits, he silly, silly (mmh)
    my bitch is so pretty, pretty (mmh)
    i get cash like really, really (get it)
    tell the dj, man, he ain't slick
    'cause he ain't playin' hits, he silly, silly (boy, bye)

    ring in their ears like a bark
    always feel left in the dark
    trauma the price for the patience
    character shift like an arc
    move like my shit stay in park
    don't feel the love or respect
    grip like a hand on my neck
    this is the year, place your bets
    boy, bye

    ooh, ooh, beautiful and bashful
    ooh (mmm), ooh, ooh (mmm)
    i'm beautiful and bashful
    boy, bye
    goddamn (sheesh)
    boy, bye
    boy, bye
    goddamn
    i'm beautiful and bashful

    immersed myself in discontent
    hopin' you can only repent these things
    it smells like ginger

    what you mean, i ain't green like timothy?
    dead leaves in the breeze‚ sweep your chimneys
    see the boy try me‚ now the boy deceased
    they put the blame on me‚ but hey, it wasn't me (boom, boom‚ boom)
    like god can't judge me, but only god can see
    i ain't bein' judged, no one judgin' me
    i walk on water‚ pain and torture what i bring to these
    and there's a war in my head, just like the middle east
    and i'm the flurry, vision blurry, see soliloquies
    i didn't get the memo, didn't cc me
    only cc me when i'm doin' burglaries
    and if it weren't on tv you wouldn't have ever seen

    fuck god, i'm a dog backwards
    backwards, i don't smoke backwoods
    what you sayin'? why you prayin' for forgiveness?
    when you wanna get money, get them riches
    like what you sayin'? why you prayin' for forgiveness?
    whole lot of shit and some bitches, like
    (mmm, mmm, ha, yeah, fuck it, yeah, yeah)

    break the law, break the law
    break the law, break the law
    break the law, break the law
    break the law, break the law

    i'm the same one you seen in the classroom, ayy
    we was chillin' in the stall makin' crowds move‚ ayy
    young k still posted in the a like a brave
    no chain ya boys got would make my neck fuckin' bang
    hangin' on your speaker‚ bangin' on your speaker‚ baby (ayy)
    need to find a reason to make you believe me, baby (ayy, ayy)
    young nola‚ playstation controlla (ayy, ayy)
    send 'em just to get 'em, i hit 'em when it is over (ayy)
    roll over‚ yo soldier, no coaster
    i told ya i'm back whenever the storm is over
    send it back if them boys wanna feel the clover
    no closure, never reply to faux orders
    my nigga so sculptured, such a short quota (ayy, ayy)
    police pull up on me, boy, i kept that cold shoulder (ayy, ayy)
    cup runneth over for a hunnid orders (ayy, ayy)
    all i got is pennies, still want me to fuckin' flow, bruh (ayy)

    there is no love in the ghetto
    money got it where i just can't let go
    there is no love in the ghetto
    money got it where i just can't let go
    ooh-oh-ooh, oh, oh

    how you do that right there, boo, i'm bamboozled, yeah
    legs go up behind the head like leopard ambushin', huh
    give her space, big ol' drop, call it grand canyon, huh
    she bust back, blow a fuse out the damn cannon
    circus, olé, okay (yeah), roly (woah)
    poly, slide that (uh), pole, yeah, (hm) low blow (ooh)
    not seen like a dodo (no), i skip fall, stay snow globe (ayy)
    stuck inside the corridor (ayy), make me go so loco (ayy)
    major league, i'm sheen (uh), call me wild thing (uh)
    she got strings all up the neck just like a violin (ah)
    i crave that chada-ching, when that venom sting (hey)
    eyes turn redder than a motherfuckin' cherry stem

    run up a check, ayy, uh (run up a check)
    hit 'til i miss, ayy, uh (hit 'til i miss)
    and then keep on hittin'
    my niggas ain't quittin', they way too legit, ayy, uh (they way too legit)
    don't get on my list, ayy, uh (don't get on my list)
    i'm from the abyss, ayy, uh (i'm from the abyss)
    you sayin' you real
    but i watch how you act and i can't be convinced, uh
    smokin' 'em out like a habit
    you know we could make it tragic (ayy)
    money had never made a nigga (ayy)
    we holdin' all our money in the mattress (ayy)
    fire rapid like a savage (ayy)
    taste is way above your palate (ayy)
    no, i ain't for burying the hatchet (ayy)
    take a break to pick apart the balance of this madness

    uh
    you got big boy money like you ready for war
    you be talkin' like you really gon' run that though
    you be runnin' like the snot drainin' in from your nose
    that's that ice cream, sugar, that cocaine throat
    and this shit gon' bounce like my shin off your dome
    and you know these boys deep, we ain't fittin' in the door
    and my dogs, they bark, michael vick on fours
    boy, this shit long gone, why you hit my phone? (whoa!)

    see how full it is, homie
    see how real it is
    hell no

    murder man, murder man
    someone better hold me before this shit gets ugly
    murder man, murder man
    someone better–
    murder man, murder man
    someone better–
    murder man, man
    someone hold me b–, b–, shit gets ug–
    murder man, murder man
    someone better hold me before this shit gets ugly

    hallelujah, holy lion‚ word to judas
    how i'm supposed to‚ (hey) trust what you say is the truest? (right)
    haile selassie‚ (uh) insha'allah if i gotta (woo)
    spin my words around as if you wanted a mandala for nirvana
    singin' a sonata towards our karma
    did a rain dance, bringin' commas from tacoma to oaxaca
    i got spirits in my heart that make my mind move like it's water
    flow into the moment and avoid the melodrama
    gotta breathe for a second
    can't believe anybody still testin'
    my whole team is a force to be reckoned with
    operatin' like specialists
    one to the two to the who are you?
    sendin' out projections with prejudice
    my attention to detail is in scale with classic impressionists
    so the lesson is that prerequisites are irrelevant to my standards (right)
    it's a deficit in your settlement, you better learn to mind all your manners (right)
    my whole troop been goin' bananas
    try and step inside of our jungle (right)
    you can try to take all your chances
    we won't help your ass if you stumble‚ nigga (right)

    hidin' at my partner house
    couple bands'll send 'em out
    'stead of feelin' trippy, dawg
    you need to help your city out
    hidin' at my partner house
    couple bands'll send 'em out
    'stead of feelin' trippy, dawg
    you need to help your city out

    couple...
    couple...
    couple...
    couple bands'll‚ couple bands'll—
    couple...
    couple...
    couple bands'll send 'em out
    couple bands'll, couple bands'll—

    watch your back, (ayy) don't leave your door cracked (yeah, yeah)
    slither through your space and watch it all collapse (yeah)
    watch your back, (what?) don't leave your door cracked (woohoo)
    slither through your space and watch it all collapse (if you, if you, if you, if you, hey)

    if you want a feature, we can figure it out
    want a color for your album? we can figure it out
    how you not invite the boys who colored your rollout
    then you copy-paste hard work from the bh house?
    i always got somethin' to say when you take food from my mouth
    i begged my mommy for money until the day it ran out
    they say, "we helped you when and when, now you should figure it out"
    figure it out

    hidin' at my partner house
    couple bands'll send 'em out
    'stead of feelin' trippy, dawg
    you need to help your city out
    hidin' at my partner house
    couple bands'll send 'em out
    'stead of feelin' trippy, dawg
    you need to help your city out

    couple...
    couple...
    couple...
    couple bands'll, couple bands'll—
    couple...
    couple...
    couple bands'll send 'em out
    couple bands'll, couple bands'll—

    waste your breath, watch the tone though
    take you to the dojo
    roll up my doja, sticky fingers
    at the door, bruh, jehovah, you ho bitch
    witness sadistic shit, will come again
    next time i take my belt off, spank you
    bad kid, bad seed, not me, got beef
    i leave body, blackout from rage
    childproof my pockets, don't need the options
    romanticizing what i do if i ain't stop me
    can be off me, tread lightly

    break the law, break the law
    break the law, break the law
    break the law, break the law
    break the law

    i'm tired of making a fool out of me and you
    is there anything that i can do that'll save us, baby?
    is there anybody lovin' lies and robbin' shotties
    45's and still alive, and no drunk drivin'
    that's how they killed my brother
    (walking with jesus)
    you know, you know better, better, better, better, better
    better, better, better, better, better, better, better, bet on it
    better bet on it, better bet on it, hey
    (walking with jesus)
    you know, you know better
    better, better, better, bet, bet on it
    bet on it, ayy, ayy, yeah
    ayy, yeah
    i wanna sing, i wanna
    i wanna sing, ooh
    (just tell 'em, tell 'em that)
    ah, cool
    (walking with jesus christ)
    (walking with the lord)

    i pray i find you at the bottom of the hill
    i  pray i make it outta texas
    i  pray my a/c come back on
    my mom was stuck outside her job
    my sister just asked for a lexus
    can  jesus send me a message?
    what's  the point of havin' a best friend if you end up losin' him?
    world don't view my text messages
    world  don't view my text messages
    don't view my bad side
    only get on the 'gram to show you motherfuckers the best side
    who am i? who am i? who am i?
    why  i hide? huh
    fourth grade, mary j. blige all i like
    i made a mill' off a lie and a lie so i write another lie
    rca‚ that note wasn't 'bout y'all
    no lies‚ it was about how me and my brothers been traumatized
    and i must keep creatin' truths and hooks to get up outta this hell for myself
    seashells

    dearly departed
    look what you've started
    i've been so heartless
    i try‚ i try, i try
    why?
    why?
    why?
    try

    big dog, i feel like i don't got anybody on my side no more
    highs to lows‚ truth be told
    it's hard to ignore, hard to endure
    where's my stamina in this life?
    make sure my family tight
    more rubies on my neck and they catch me at night
    lookin' immaculate, no one in sight
    standards are high‚ expectations are low
    wake up sweatin' at night, mind in a flight
    i don't get scared no more when i'm standin' on the mountaintop
    i'm afraid of people dyin'
    rest in peace wako, ray, rita
    wish you could've took me to japan
    back ten years, holdin' my hand, felt like a hundred grand
    wish them letters didn't fade, love will never do the same
    out the window screamin' your name, bless it
    mama on track, my dad got my back
    my sister graduated, now she racin'
    love her through the days and whiskey in my hand
    bloody colored trinkets wrapped around my wrist
    lookin' magnificent, man
    no stoppin' me, no boggin' me down
    i know myself, me and the obstacles now
    i done shit on myself too much to not know how to move properly now
    on the property now, money gets foul
    keep your wits about you
    they stretch the truth longer than the nile
    eyes full of evil, mouth full of vile
    they tracin' your smile
    stay alert, big dog
    only one life is offered to you
    (only one life is offered to you)

    how many sides to a story can there be when you saw it with your own eyes?
    i got all my thoughts out on records y'all won't ever hear
    tried to give it time
    find that truth trickles down, hits the fan
    freezes over like a dagger to the spine
    when somebody that you know throws you in the fire
    how do you survive?
    i kicked down the door inside a home i didn't own just to save a friend's life
    little did i know, the one who pulled the strings was once on my side
    i had just moved to texas, tried to make it right
    i do not feel obliged to dismiss the truth because of how i feel about our time
    if i knew what you would do to someone you owe money to, you wouldn't get a dime
    watch for where you land, sorry 'bout your plans
    that was all a scam, you won't understand
    pass the weight off to your friends and never face the truth
    because you never learned how to be a man
    and it's not my fault, and it's not my problem anymore
    that's just where you stand
    that's just who you are
    that's your cross to bear
    you could talk to god
    i don't wanna hear, motherfucker

    out on the deck like i'm wildin' for respect
    it's a three-peat, see-see
    bitch, you in the d-league
    boy, you fucked up
    can't come around here, this shit is gated
    we made it, happy belated, i see the rage hit

    it's better if i try not to talk about the shit that's always on my mind
    money on my mind (that's right), couple hunnids at a time
    try to fuck me blind, duckin' down, hear me whine (ooh)
    we outside now (that's right), milk carton in the back
    we don't like to fuck around with them niggas in the back
    pullin' triggers in the 'lac (that's right)
    may the praise stay bad
    ayy, dad, hercules want his fuckin' waves back, stay strapped (ooh, i like that, that's right)
    dancin' like a bad bitch, love on top my mattress
    hope the good lord catch this, i ain't tellin' backwards
    lie just like an actor, hollywood is batshit
    mama in the south still, gold all in my mouth still
    rappin' 'bout dick still, and i lease a house still
    move my nigga out, still need my nephew out here
    god gave me a good deal
    miss my little niggas down low like a big wheel
    bitch, i wanna hit still
    this shit for my partna 'nem, devil keep on robbin' them
    express and feel myself, like i'm fuckin' dennis rodman (that's right)

    like i'm dennis rodman
    diamond dentures for my partna 'dem (that's right)
    golden rubbers from my pocket, friend
    ain't no answer, that's my partna 'dem (that's right)
    she so bad, i let her touch my butt (yeah)
    merlyn, what the fuck?

    line 'em-line 'em-line 'em up, you know that i'm shootin' (that's right)
    it ain't no one business who or what we doin’ (that's right)
    hit this gas, they break the glass and keep it movin’
    to you basic bitches i know i'm a nuisance

    sugar, yeah, gimme some
    gimme dome, i'ma smoke some
    y'all ain't want the smoke, been smokin'
    garden gnome shrooms, y'all, who is y'all?
    this what it mean to ball?
    okay, chateau marmont, shangri-la
    valet park it, drive a shit whip
    but i ain't broke, bitch
    write my own shit, hit my own switch
    watched the clock tick, never ran and hid
    tell it like it is
    dead on the nail, call me hammerhead
    texas 'til i'm dead
    bbq and cornbread, like 'em corn fed
    here we go again, hit 'em one mo' 'gain
    screwed up from the woodlands
    number six, been through hell, think i'm heaven-sent
    ask the preacher man, said i need jesus, like i ain't know
    guess i found him, i am blessed, man
    rake in dividends, let the money stack, see you copycats
    i ain't trippin', but copy that
    it's a wrap, keep my distance
    where's waldo, but we winnin'
    me and my dogs ain't finished (that's right)
    the real know, what's a billfold?
    you can't fold, i stay grinnin'
    no peekin'

    go ahead and try harder
    you ain't gotta ask to put up with nobody
    you oughta be ashamed of yourselves
    get on your damn knees
    and pray sometimes with your muhfuckin' ass
    you oughta be ashamed of yourselves
    get yo' muhfuckin' ass on out there
    that's all you gon' be, a muhfucker
    you oughta be ashamed of yourselves

    [outro: matt champion]
    s-s-send 'em out the door
    they ain't knockin' no more
    send 'em-send 'em out the door
    they ain't knockin' no more
    send 'em-send 'em out the door
    they ain't knockin' no more
    they ain't knockin' no more
    they ain't-they ain't knockin' no more
    s-s-s-s-send 'em out the door
    they ain't knockin' no more
    send 'em-send 'em out the door
    they ain't knockin' no more
    send 'em-send 'em out the door
    they ain't knockin' no more
    they-they-they ain't knockin' no more
    they ain't-they ain't knockin' no more
    (that's right)

    know you got your own shit, and all of it together
    and  you know you got your own space right here forever, baby
    you  know you got your own, know you got your own
    know you got your own, know you, know you got your own
    know you got your own shit, and all of it together (my own session)
    and  you know you got your own space right here forever, baby (and my own blessing)
    know  you got your own, know you got your own
    know you got your own, know you, know you got your own
    know  you got your own shit, and all of it together (my own session)
    and you know you got your own space right here forever, babe (and my own blessing)
    know you got your own, know you got your own
    i know you got your own, i know you got your own

    ayy,  stay sound when you not around
    mood is always better whenever you not around
    fuckin' up the weather and you fuckin' up my town
    fuckin' up a sweater and i'm fuckin' up a gown
    look at how i'm shinin' though
    look at how i'm smilin' though
    look at how i'm smilin'
    look at how i'm wildin', and i'm still broke, uh
    you still think i'm a joke, uh, i still think i'm a joke, uh
    i still think it ain't gon' work out
    nigga that shit is broke, broke, broke, broke

    tell me, goddamn, what god made me for?
    i don't even love no more
    i don't even trust no more
    i don't need to clutch no more
    some things outside of my control
    i need some space, i need to grow
    so i go, plague my soul
    say i won't
    i never tried to let you go so deep, deep, deep, deep

    know you got your own shit, and all of it together (my own session)
    and you know you got your own space right here forever, baby (and my own blessing)
    know you got your own, know you got your own
    know you got your own, know you, know you got your own
    know you got your own shit, and all of it together (my own session)
    and you know you got your own space right here forever, baby (and my own blessing)
    you know you got your own, know you got your own
    i know you got your own know you got your own

    but i couldn't lie, you swear and you cry
    your teeth rotting while they fall onto mine
    pouring bleach on the white, won't bring them to life
    pliers twist to the right, pull out your mind
    but i couldn't lie, you swear and you cry
    your teeth rotting while they fall onto mine
    pouring bleach on the white, won't bring them to life
    pliers twist to the right, pull out your mind

    i don't wanna take this ride
    i don't wanna take this ride
    pouring bleach on the white, pouring bleach on the white, white, white
    i don't wanna take this ride
    pouring bleach on the white, pouring bleach on the white, white, white
    i don't wanna take this ride
    pouring bleach on the white, pouring bleach on the white, white, white
    pull out your mind

    oh, oh
    oh-oh, oh-oh
    oh, oh
    oh, oh

    i still remember writin' words down
    tryna get them all out of my mouth
    big boy, you a big boy now
    big boy, you a big boy now
    don't pout 'round me
    don't cry around me
    don't laugh 'round me
    you ain't shinin' like me
    you ain't shinin' like me
    you ain't shinin' like my cousin
    you ain't shinin' like me
    you ain't shinin' like my cousin

    if i had another
    i'm a bad motherfucker
    got love for my mother
    the city that protect me
    i don't fuck with y'all like i used to though
    but you could come around for the houston baby, oh

    i still remember writin' words down
    tryna get them all out of my mouth
    big boy, you a big boy now
    big boy, you a big boy now
    don't pout 'round me
    don't cry around me
    don't laugh 'round me
    you ain't shinin' like me
    you ain't shinin' like me
    you ain't shinin' like my cousin
    you ain't shinin' like me
    you ain't shinin' like my cousin

    who the hell am i?
    who the hell are you?
    don't waste my time, i got shit to do
    been in love with you, don't know what to do
    still searchin' for the truth, every which way
    mental foreplay, bound by cuffs to you
    do it my way, like everything i do
    take my breath away
    don't let me fade away
    may die before i wake
    not the type to play
    i take, and take, and take
    never want a change
    always wanna change
    used to count my change
    everybody changed
    memories of the days
    i was young at heart
    matters of the heart
    rearrange, reactions in my brain
    redefine my pain
    been wishin' i could change
    hard to change my ways
    trained a certain way
    afraid of my own fate
    just another phase

    lost cause and a lost child
    lost my way tryna change for the wrong crowd
    i'm weak and i'll say it proud
    built me up, pull me down, let's air it out
    patch me up, and stitch it
    make me better
    just patch me up, and stitch it
    make me better (make me better)

    what a day, what a day
    i just had a dream that you took it all away (ayy)
    blow smoke in the face
    i just hope your lil' bro grow to be great (ayy)
    what a day, what a day
    i just had a dream where you took it all away (ayy)
    blow smoke in the face
    one in the clip, and one in the chamber (yeah)
    we was riding in the dark, you were putting your legs up (legs up)
    girl, i don't know, maybe i should just stay shut (stay shut)
    did i ruin your life baby, even from day one? (uh-uh)
    if it was another life, maybe you could still save us (ooh-ooh)

    i still remember writin' words down
    tryna get them all out of my mouth
    big boy, you a big boy now
    big boy, you a big boy now
    don't pout 'round me
    don't cry around me
    don't laugh 'round me
    you ain't shinin' like me
    you ain't shinin' like me
    you ain't shinin' like my cousin
    you ain't shinin' like me
    you ain't shinin' like my cousinwhat i gotta do?
    keep it real with you
    stuck inside my truth
    spendin' all my loot
    diamond on my tooth
    r.i.p. my brother luk
    when i spit, let it hit, hit a double u
    couple rainbows, my lil' halo
    think it's j-lo, bro don't say so
    homie don't play, no
    takin' my day slow
    takin' my ray, throw
    talkin' to angels
    speedin' a pave' though
    changin' a page though
    lookin' like ace, talkin' 'bout spade, you are afraid though
    spendin' my queso
    all on some fake clothes
    when i change, never say, this is my blaze throat
    south central
    all my homies know
    if i could go, i would just wait though

    anyways, gotta go, disregard what i say
    grain of salt, sprinkle some over the shoulder, ayy
    lucky strike, filterless, don't push me, 'kay?
    sensitive, abrasive, stab you in the face
    keep a blade, heaven sakes, had to raise the stakes
    dracula, in a cave, a bit lonely, mane
    grab a stake, have a cape, it don't work no more
    fly away, different ways, hit the liquor store
    better days, follow me like the saddest song
    grab a case, hideaway, fill my loads with bleach
    couple stains ain't a game, they both hauntin' me
    lot to say, people hate, wearin' blindfolds
    now where did i go? where do we go?
    how do we grow? how should i know?
    feel responsible, intolerable, displaced (uh-huh), insane

    piss 'em off, piss 'em off, piss 'em off
    shit, i better set it off
    i just made a deposit, cdg in my closets
    fuel ain't really made of fossils
    dirt on me, i'm finna blossom
    spying on your ho from a spacex rocket
    she wanna know why my wrist so rocky
    flash splash on me, photocopy
    my weed, my weed at the party
    shoot me a sheriff for trayvon martin
    king, ali, and bobby marley
    dirt on me, i'm finna blossom
    dirt on me, i'm finna blossom
    you know

    i wish you'd love me for life
    love me for life, love me for life, wish you would lie
    i wish you'd love me for life
    love me for life, love me for life, i will
    love, love me for, yeah
    love me, love me for life
    love, love me for life
    love, love me for life
    love, love me for
    love, love me for life
    love, love you for
    love you for

    my fuckin' power rangers couldn't protect me from that lapd kick door
    motel, pig-pork
    swim through the living room, straight to the bedroom, lookin' for bricked dope
    my papa looked at my mama, lookin' at that closet like
    "there that shit go"
    two keys and a thumper, 10k with the mustard
    a whole family and no buster, this don't add up
    my padre facin' them three strikes
    and my mama just smacked the pipe
    crack smoke got crash tight, this shit still bad, 'cause
    the boys peeped a brillo pad and some glass tucked
    and it's lookin' like my parents was up in here runnin' all through that stash dumb
    but the fact, crack different than coke
    plus the smoke wasn't close enough to choke me
    lowered scrutiny so mom could kick big facts for bruh
    the truth is we held the bag for this kid we took in
    tryna part with his old ways, maybe we all mistook him
    'cause i knew something was fucked up when he said
    "don't open or look in this here satchel that i'll be back for in just a couple of minutes"
    then hella hours later, like do i cook dinner now or later?
    worried about cold food for a cold fool
    motherfucker put my family in danger
    i blame myself, pardon my anger
    i never looked inside his stuff so he never really needed to hide his stuff
    when you showed me what was really inside this stuff
    i never had a clue
    now i know as police, you gotta do what you gotta do
    but this my family, all i got is us, my nigga
    my own mother just shot at us, my nigga
    this is why we here
    and i don't fuck with niggas i don't know
    but i had a heart to help this kid in danger, tears in anger
    gemini gettin' violently
    police silence don't help anxiety
    my daddy's priors tame all of his wildin'
    all of these pilots, not one of them flyin'
    y'all planning on trying?
    this flight is diving, nose tucked
    po-po stuck, play your part
    all this commotion and neighbors listenin' like, "oh fuck"
    shit finna spark
    all this emotion, need a decision made with some heart
    'cause ours is broken, they tryna lock the third notch on my pop's choker
    this shit ain't kosher
    moms is oh for if cps get sent them pages
    i ain't gon' see my parents for ages
    all this erosion, no more protection
    shit don't feel safe
    what graduation? what degrees?
    what dissertation? what imagination?
    imagine my whole world taken away from me
    all over some bass and misconstrued melodies
    my heart racin', clutchin' my red ranger, pacin'
    i can barely breathe
    and mister policeman, told policeman, we got what we need
    just let 'em be

    thank god for my bitches still sticking with me
    thank god, when i talk, i know you listen to me
    thank god that i'm built for the distance
    thank god for me, thank god for me
    thank god for my bitches still sticking with me
    thank god, when i talk, i know you listen to me
    thank god that i'm built for the distance
    thank god for me, thank god for me

    and if you're hurting, love yourself with my heart
    and if you're hurting, love yourself with my heart

    [chorus: ryan beatty]
    thank god for my bitches still sticking with me
    thank god, when i talk, i know you listen to me
    thank god that i'm built for the distance
    thank god for me, thank god for me
    thank god for my bitches still sticking with me
    thank god, when i talk, i know you listen to me
    thank god that i'm built for the distance
    thank god for me, thank god for me

    thank god for me, thank god for me
    thank god for me
    thank god for me, thank god for me
    thank god for me
    oh, oh
    (nobody)


''',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True,limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True),
        emotion=EmotionOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
