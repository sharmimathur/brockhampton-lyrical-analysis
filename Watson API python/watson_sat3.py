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
        entities=EntitiesOptions(emotion=True, sentiment=True,limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True),
        emotion=EmotionOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
