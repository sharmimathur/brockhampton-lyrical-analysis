import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions

authenticator = IAMAuthenticator('8O9EMgIsxfs9-tsACK_-FTZSQey4_69U2WdjirOgzjbT')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

#natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(limit_text_characters=100000,
    text='''
    perfectly fine, that's fine!

    said nigga brother, nigga brother, what you living for?
    is you gon' finish what you started? what you quitting for?
    they told me god gave me a mission
    but i'm missing the supplies to complete it
    i ain't the one you should read in, i'm used to being defeated
    so nigga, brother who you standing with?
    i'm independent 'cause these parties never planned for this
    brother nigga with a brain, unintentionally swerving in every lane
    the feeling's never the same, you chase what you couldn't gain
    i'm so accustomed to flames, i couldn't tell you what's fire
    situation is dire, hear them calls from the choir
    the disposition acquired from my position on earth
    it's telling me "decapitate everything for what it's worth!"
    when i die, these words gon' need separate caskets and a hearse
    i don't rhyme, i freeze time and let these hands just do the work
    i'm in tandem with my curse, going manic since my birth
    see the canvas as a planet i'm commanding with my nerves, ah

    tell 'em boys, don't run from us
    i been down too long, cousin
    i been down too long, brother
    tell the world, i ain't scared of nothing
    tell the world, i ain't scared of jumping
    tell my boy i want a crib in london
    tell the world to stop tripping, i'll
    build a different house with some different functions
    tell 'em boys, don't run from us
    i been down too long, cousin
    i been down too long, brother
    tell the world, i ain't scared of nothing
    tell the world, i ain't scared of jumping
    tell my boy, i want a crib in london
    tell the world to stop tripping, i'll
    build a different house with some different functions

    try to treat man like baby
    feel the teeth sink in like rabies
    boy, you know you don't look fly
    them gold chains turn your neck green, bye
    ah ah-ah, ah, ah-ah-ah ah
    ah ah-ah, ah, ah-ah-ah ah

    nothin' different now (woo!) all around now (woo!)
    who you keep around now? that's a big reflection
    don't like how they talkin' to me, why they walkin' to me?
    wear your shit upon your sleeve, stop projectin' on me
    sense is your surround sound, what's your take on me?
    kill the ego now, what that make of me?
    angle widescreen, couple sips of tanqueray
    i'ma throw a couple punches, i'ma do it anyway
    chin up little son, i slide in like the macarena
    lose time, pen it, style spiced on, jalapeño
    supersonic, move through tunnel, two-wheel cycle, slightly
    silence crowd better than 9 millimeter with extended suppressor
    bustin' out the function, highly comfortable
    got this martine on my body, man, my sweat lethal
    sweet kisses like the candy out the carnival
    i'ma call my own shots, hit the audible

    impending death is the only sign of life
    i'm throwing hail marys 'til i die
    throw it up, all i have is peace of mind, throwin' up
    have my wings clipped, i don't need them shits
    learn to fly again
    fast track to last place, i swear
    i've never been up top but i'm up here somewhere
    out here, nobody can tell me shit
    shit, never mind what i did back then
    you should take a look at yourself instead
    maybe you can find yourself, love yourself
    here's to health and here's to wealth, all together now

    hoo! voodoo man
    momma took me to the church and i sang a hymn
    co-colonized chris-ti-an
    now i'm losing my reli-gi-on
    god damn, so narcissistic this millennium
    fuck you and the bubble that you livin' in
    i don't go to church, but i'm so spiritual
    pulled my life out of dirt, that's a miracle
    if jesus was a pop star, would he break the bank?
    all these diamonds in my face, i'm shining like the day
    i'm living in my prime, man, what can i say?
    if the service is an hour, i'm an hour late

    i gotta get that bag
    it's a thug life, it's a thug life
    i gotta get that bag (run, sha-na-na-na-na-sha-ah)
    it's a thug life (la-da-da-da)
    it's a thug life (it's a, oh-uh-oh)


    try to treat man like baby
    feel the teeth sink in like rabies
    boy you know you don't look fly
    dem gold chains turn your neck green, bye


    it's different reconciling with skeletons i ain't know i possessed
    i sought perfection out in ways i no longer accept
    i understand what i neglect in times when i obsess
    i'm learning to confess, this fate is harder to digest
    the biggest threat i'm up against is who i face in my reflection
    depression still an uninvited guest i'm always accepting
    can't help but meet the feeling with a familiar embrace
    when i know that it'll kill me if i give into my brain
    i see the shadows inside, they ten feet tall with no eyes
    they put my head in the water and it's so beautiful under
    the sun reflecting off the corals, colors i can't describe
    to make the darkness divine

    she said, "baby boy, why you looking grimy as shit?"
    i'll make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    trade in thatoose they put around us for a cuban link
    so my ancestors can see me shining, tell me what you think
    i remember the illusions that they tried to move to me
    that pollution still ain't stunt my evolution
    what you choosing?
    no chip on my shoulder, hunnid leagues under the sea (hoo!)
    we live life like cheetah power up like hummer diesel
    golden chain for niece and nephew
    pessimistic, i do not hang 'round them boys
    metaphysics, need another dimension i can enjoy
    she said, "baby boy, why you looking grimy as shit?"
    i'll make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    baby boy, why you looking grimy as shit?
    i'll make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    reporting for the operation
    i learned that the beauty is in the creation
    i added my detail for decoration
    so baby boy, what's the occasion?
    you dressed like you 'bout to take over a nation
    avoiding social litigation
    when that admiration turns into abrasion
    y'all can find another station
    otherwise, stay tuned, evolution coming soon
    rolling deeper than a dune
    howling at the moon, i'll be back in june
    told my baby i'd be back in november
    did some beatles shit to kick off this september
    crazy 'cause in 2010, i had some old friends
    that thought i'd be another—[censored]
    go fucking figure
    if i pull up out the tool, riding still up on the roof
    seems like only legends do
    (check this, hot lookin' babes!)
    bitch, and that's the fucking move
    (i feel you, when she said—)
    she said, "baby boy, why you lookin' grimy as shit?"
    i make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    baby boy, why you lookin' grimy as shit?
    i make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, lookgood riddance, goodbye, out of sight, out of mind
    cutthroat every time, this time i get what's mine
    where the hell is your back bone?
    ducking me like whac-a-mole
    looking like an inflatable at a car show; a spectacle
    lick my finger, bet i found the wind
    i follow that shit wherever it blows
    you hung yourself, that's not my fault
    i just supplied the rope, ugh!
    most thoughts, i don't think twice, make decisions i'll die by
    never asked for the drama, but i'll turn it into dollars
    dollars, dollars, dollars"do you think about me?"
    ohh, ohh

    something about him
    his car ain't nice and flashy (yeah, yeah)
    there’s something about him
    yeah, his attitude, it's like magic (yeah, yeah)
    there's something about him
    i know i got to have it
    and oh, oh, oh, oh, oh, oh, ohi really like how you do all the things that you do
    i really like how you say all the things that you say (i love him!)
    i really like how you do all the things you could do
    i really like all the things that you really could say, ayy
    i really like how you move when you’re out by yourself
    i really like all your crew and you can take 'em to hell
    boy, don't you know i fucking got you? right, rightthere's something about him
    his car ain't nice and flashy (yeah, yeah)
    there's something about him
    yeah, his attitude is like magic (yeah, yeah)
    there's something about him
    i know i got to have it
    and oh, oh, oh, oh, oh, oh, ohi love him, i love him
    something about him

    there's not a soul in herepull to your house and dump like the trash man
    all up in your grill, but i'm not a fan
    merlyn, i do no hat trick, just show me where the cash at
    then show me where the hash at, fuck that
    show me where the cash at
    (there's not a soul in here)
    i would rather be on acid, rather make investments
    they'll come out of that debt, we'll come out of those bedsheets
    i'm like the irs, pull up to your address
    i was trying my best to seizure, but pull it like keisha
    (there's not a soul in here)
    johnny dang gon' ice my diamonds, up out that freezer
    i used to be broke, i don't got amnesia
    i used to deal with both, now it's black victims
    she know not to call collect if she go to prison
    (there's not a soul in here)pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure where you niggas at (show out)
    "where the cash at?" used to ask that (ayy, clip, ho out, throw down, ho out, know 'bout, throw down, hold out)
    "where the cash at?" used to ask that
    (there's not a soul in here—)
    pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure where you niggas at (show out)
    "where the cash at?" used to ask that
    (ayy, clip, ho out, throw down, ho out)
    (now 'bout, throw down, hold out)
    "where the cash at?" used to ask thatat night i bring them out, i was sleeping upside-down
    keep you up, i come around, they stay right up on my tip
    send me a pic whenever you slip, hoping this outflow my scales
    full throttle whenever i blaze, fifty mil', put it under my wheel (there's not a soul in here—)
    human, i see through your eyes
    until my ccc wide open to my skin
    they can see they run, they feel like they been kicking ddr
    bustin' out the bar, human of the tour
    they grip three types of the gas, miss the days i can't get back (there's not a soul in here—)pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure where you niggas at? (show out)
    "where the cash at?" used to ask that (ayy, clip, ho out, throw down, ho out, know 'bout, throw down, hold out)
    "where the cash at?" used to ask that
    (there's not a soul in here—)
    pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure, where you niggas at (show out)
    "where the cash at?" used to ask that (ayy, clip, ho out)
    "where the cash at?" used to ask that

    they split my world into pieces, i ain't heard from my nieces
    i been feeling defeated, like i'm the worst in the boyband
    i ain't sleep in some weekends, tryna headline both weekends
    lead my niggas, y'all sheepin', i keep the world in my hands
    i know accounts should be deleted
    i know some niggas should stop hitting my phone
    whenever they needing money or favors done
    'cause i'm still worried 'bout when ashlan finna put the razor down
    so i don't really give a fuck about what story they done spun
    and i ain't done (no, no)
    yeah (tell something)
    and i ain't done, you heard me?
    i ain't done (yeah, i'm screaming oh, oh, oh, oh-oh)
    i really miss the old days before the cosigns
    i really miss them cold days before the road signs
    i really miss when i ain't know which way i was supposed to head
    and i was pressed because my shawty gave me cold signs
    i was writing poems 'bout her dawg in study hall
    and she was mad 'cause i never wanna show her off (scared)
    and every time she took her bra off my dick would get soft
    i thought i had a problem, kept my head inside a pillow screami don't wanna waste no more time
    i'm ready to go
    i put my life on standby
    i can leave you alon'cause we're born with a dollar sign attached to our temple
    life is a dish served cold most times
    and all my life i've taken handfuls
    force-fed by the hand that feeds us
    but not all hands created equal
    i stand by, waiting for something good to come
    in due time, the skies will split for the sun to smilmy mother called me today
    she said she thought she felt my energy a country away
    i apologized for not calling enough due to weight
    but couldn't tell you if i kept it in my head to decay
    i asked her "why this world love echoing hate?"
    she said "don't let those who don't know you start dictating your fate"
    i think the hardest part of love could be rebuilding the breaks
    conditioned to omit them until our foundation will shake
    it's no debate
    the road to peace is filled with snakes, you gotta keep your cool
    and recognize the wolves that wanna try and leave you wool
    don't let 'em treat you like a window, you know you're a jewel
    this world is cruel and not as simple as they teach in schools
    sometimes you gotta step away and check your own intentions
    and analyze if what they do can compromise your vision
    if people trust you, they don't need to question your decisions
    you never needed them if they make you another villaipressure
    "they tried to take the bike. and they took my friend's bike and then my friend was gonna get it back but then he didn't get it back and then we had to go to the police station. and then, um, then some (pressure) random stranger brought back his bike. we just, you know, and we didn't tell our mums so we got in trouble (pressure makes me—) because they found out like a day later."
    do you want to start the game againpressure makes me lash back, wish i could get past that
    i can't take a step back, makes me wish you'd pass that
    pressure makes me lash back, wish i could get past that
    i can't take a step back, makes me wish you'd pass that
    take it all or leave it
    pressure makes, pressure makes, pressu—
    wish i could, wish i could, wish i—
    i can't take, i can't take, i can't—
    makes me wish, makes me wish, makes me—
    pressure makes, pressure makes, pressu—
    wish i could, wish i could, wish i—
    i can't take, i can't take, i can't—
    makes me wish, makes me wish, makes mesipping on my pain, smoking by my pain
    ingesting my pain, i just wanna play
    sipping on my pain, smoking by my pain
    ingesting my pain, i just wanna play
    take it all or leave it
    sipping on my (sipping on my), smoking by my (smoking by my)
    ingesting my (ingesting my), i just wanna (i just wanna)
    sipping on my (sipping on my), smoking on my (smoking by my)
    ingesting my (ingesting my), i just wanna (i just wanna)

    "i'm sammy jo, and my favorite colors are, um, black and red.let me find my way out of this bitch (uh)
    find myself high in the distance (uh)
    find me up, lying in this ditch (uh)
    with a wrist and some diamonds a-mixin' (woo)
    if i can't find the time to get my heart out (uh)
    would you stomp 'em out when we slow the world down? (uh)
    would you hold it down for me when my heart pound? (uh)
    ain't no telling, no telling, so call the coroner
    let me find my way out of this bitch (uh)
    find myself high in the distance (uh)
    find me up, lying in this ditch (uh)
    with a wrist and some diamonds a-mixin' (woo)
    if i can't find the time to get my heart out (uh)
    would you stomp 'em out when we slow the world down? (uh)
    would you hold it down for me when my heart pound? (uh)
    ain't no telling, no telling, so call the coroneayy, i'ma just bounce with that
    in fact, i bought a whole damn house with that
    ayy, hand me where the ounces at
    tell me where the damn these ounces at
    ayy, tell me where the ounces at
    tell me where the ounces, ounces at
    ayy, tell me where the ounces at
    tell me where the ounces, ounces ait's getting hot, you best just—
    woo! simmer down, simmer down, simmer down, simmer down
    the effects can't touch this
    woo! simmer down, simmer down, simmer down, simmer down
    stand up, stand down, bitch
    woo! simmer down, simmer down, simmer down, simmer down
    wait, wait, waii'm alive, i'm alive, the bags in my ride, i, i
    i ain't ever been the one that's scared of you
    baby, you can come and get it
    i'm alive, i'm alive, the bags in my ride, i, i
    baby, when the karma gets you
    maybe you can run away within my bag in the vault, moving on, move along
    ain't my fault, moved too fast, life had skidded to a halt
    got back on the road and made it to the start
    disregard the emotional discharge
    can't forget the mission put into my heart
    i ain't playing games with you to play your part
    standing up with pride behind my battle scarmoney walk and money talk, but money no make comfortable
    big ass house and big ass car don't add up when you die alone
    i want wife, nice life highlights with some little clones
    i want bliss, no strife
    rewind, don't slice around my aura with the better lies
    i want a better life, bend around the corner
    one deep, eyes shut really know the place
    but you don't know me, i don't correlate
    straight from manipulation, wouldn't wanna infiltrate my brothers
    still wanna get me high, eyes low off that methadone
    always throwing curve, like a reaper scythe
    gnawing on my wood like a termite
    entering my world like a parasite
    (parasite, parasite, parasite, parasitepraise god, hallelujah! (god, god) i'm still depressed (damn, damn)
    at war with my conscience, paranoid, can't find that shit
    woo, praise god, hallelujah! (god, god) i'm still depressed (damn, damn)
    at war with my conscience, paranoid, i can'tlet me find my way out of this bitch
    "i'm sammy jo, and my favorite colors are, um, black and red." (damn)
    (uh) with a wrist and some diamonds a-mixin'
    (ooh da-aa, da, da, da, da)
    if i can't find the time to get my heart out (uh)
    would you stomp 'em out when we slow the world down? (damn)
    would you hold it down for me when my heart pound? (uh)
    ain't no telling, no telling, so call the coronesittin' on your porch, across parking lots and you
    light it up, better dodge the cops
    and i'll never get sick of playing with your locks
    i, i miss you lots, i, i miss you lots, i, i
    sittin' on your porch, across parking lots
    that's all i got for you
    and i'll never get sick of playing with your locks, i, i
    that's all i got for you
    sittin' on your porch, across parking lots and you
    that's all i got for you
    miss you lots, i, i miss you lots, i, i
    that's all i got for you
    sittin' on your porch, across parking lots
    that's all i got for you
    and i'll never get sick of playing with your locks
    i, i miss you lots, i, i miss you lots
    i, i miss you lots, i, i miss you lots, i, i
    that's all i got for you

    "amazing how back then fame was more important than the business, like—"
    "yeah, you know, that's what i was explaining to somebody. i said i didn't mind gettin' jerked because i was like, i just want my record on the radio, i just wanna shoot videos"
    "...and get it popping"
    "i just wanna get popping. look, i don't care—take my publishing, i don't know what that is anyway, you know what i'm saying? like just take my shit so i can have a video and songs on the radio, i'll figure it out later"
    "that's crazy, man"
    "and then the next album, i'll start and i'm like, damn, these checks ain't like the checks i'm used to niggas seeing. i'm not being able to get four or five cars or jewelry or things i wanted to get, so i'm like let me figure out what's the loophole in this shit. why i'm not winning"
    "but isn't it crazy that it makes you question what kind of friends you had back then? because they weren't telling you how the business was running and they were just—"
    "see, that goes to show, maybe they wasn't never really my friends..."

    i can barely rap, i can barely dance
    i can barely laugh, i can barely hang
    i want a male stripper to do a belly dance
    for me and my boyfriend, that's entertainment
    and i'm drunk as fuck, my niggas tuxed up
    i need a reason to get my bucks up
    i need a reason to care about society
    they need a good enough reason just to hire me
    but honestly, you see my mom can't walk
    and her lungs don't work like they used to
    i feel like it's my fault 'cause of music
    i be saying shit that's just fucking rude and untrue, and
    but truthfully, the words had damage, and it's cruel to me
    but even more cruel to be
    dissing you in front of niggas that pay to hear sometimes i be wondering, why i been tripping off it
    i should probably spend my time
    writing rhymes in the dentist's office
    that's killing two birds in one stone
    when i was younger, way before i was grown
    i wanted a deal with death row or rhymesayers
    i'm saving my time for mics later
    i might save it, depending on the shit that y'all write later
    i hate writers, i hate tweets, i hate journalists
    they hate truth, they hate peace
    they want my niggas to burn with flicking on the face of my wrist watch
    watch the time stop just to speed up, watch life unfold
    and between the tick-tocks, speeding down the one-way
    fuck these signs, fuck these lights, put my life on the line
    when it feel right, i'm fine, no, i'm not lyin', don't ask me
    i'll pay the fine, i'll pay the toll, just hope i don't crash it
    but hey, if i do, it will be a blaze of glory
    engulfed by the manifestation of death behind me
    all my life i've felt inadequate
    and through the years i've dealt with
    tragedy after tragedy, god, send a message
    send a messenger my way
    never claimed to be a saint, forgive me
    feel like the light that i was blessed with has diminished
    i'm haunted, by the visions of my youth turned true
    i've come to expect my expectations aren't true
    but i'm a master of believing my lies
    and you can't break me, and i can't brake at the speed of ligi'm afraid to share the bed, what if she want money later?
    like she got laid off, uh, hit my lawyer for some paper
    i'm afraid to speak my pains like, "you lucky where you at"
    "you cool, but quit complaining 'bout all that"
    that's why i'm showing up late
    i'm not tryna be a dick, but my time is not to waste
    for my shell, fuck the small talk with my sensei
    where my sense at? four-cylinder go round
    lincoln town car pick me up, drop me off
    i got bubble under my biceps, sneak me into the sidestep
    ego is getting sized up, i be on butterfly effect
    fuck it, i'll be myself now, tell 'em i take no shit now
    tell 'em they work for me now, tell 'em my tears, they bleed down
    tell 'em i work, like, what, what time for me now?
    wondering "who is me?" now
    wondering "where you been?" now
    lose you in crowds, i see now, 14
    i see 'em all inside of me now
    bank account move like speeds now
    make it from ways to feed now
    thinking of ways to be everything but right nit's crazy how things feel the best
    when reminiscing 'til we check ourselves
    it's crazy how people who left
    say they feeling left out when we step for health
    still accustomed to nights filled with solitude
    i don't always remember to call goodnight
    i don't always remember my altitude
    i don't always remember to stop the fight
    but i might check my sight, it ain't right
    yeah i know, but my strife overwhelms, every night
    until i'm forced to close my eyes
    brain disease, parasite, eating me from inside
    emotions bleed, i can't believe
    how i'm slipping through the night

    take it all, or leave it
    i feel ywhen there's a rough patch, don't eye for the parachute
    they goin' awol the second that the light goes on
    this a treat ain't it, soon as she hit the powder room
    i pull it back and check my rose, and yeah, i'm 'bout to bloom
    it's that '90 raised from hell shit, parlay like when the lane switch
    combat how you feel, strobe light, i hit the killswitch
    neck twist like exorcist, i'ma see you 'round
    'cause tonight's the night i'm losin' all i'm doin', i'm about thwhite cuffs, wood grain
    money in the suitcase on my way to the bank
    white cuffs, wood grain
    money in the suitcase on my way to the bank
    on my way to the bank, on my way to the bank
    on my way to the bank, suitcase
    on my way to the bank, on my way to the bank
    on my way to the ba'til the casket drops, i will play god
    fuck the world, let's start a riot
    got too much, too quick
    god damn, i'm feelin' sick, bitch, call the doctor
    don't act like i ain't been dead to ya
    don't act like i ain't deserve this shit
    couldn't last a day inside my head
    that's why i did the drugs i did
    got issues with these motherfuckers
    looking down from they pedestals
    from that petty view, on that petty shit
    pray for peace with a knife in my hand
    speak my piece like a gun to my head
    come equipped just to blast this shit
    misunderstood since birth
    fuck what you think, and fuck what you heard
    i feel betrayed, you can keep the praise
    and all of the fuck shit need to get away
    still ain't got the fright to the fickle-minded people
    i thought i knew better, wish i knew better
    should have known better, wish that i was better
    at dealing with the fame and you fake motherfuckers
    guess i'm too reexcuse we
    let we pass, rum is the gas
    we ain't play nice, little guy
    doh blame meh, blame di rum, no i be in my bag (excuse we?)
    goin' in (let we pass—)
    guess who isn't built for this, man?
    me and my thugs built for this, man
    we goin' for the gifts and the grams
    i be in my bag (excuse we?)
    goin' in (let we pass—)
    smokin' all the grams in this bag
    man, you isn't built for this, man
    run it like the gingerbread mfuck that shit, stay hydrated nigga
    i'ma lick that bitch, go home, kiss my momma, wassup?
    wassup?
    black power fist hangin' from my black 'fro
    yo, she saw me in that cereal, she want to lick a oreo, damn
    break the dam when i spit the flow
    i'm on the lamb like the fuckin' wool
    hoppin' out the van, i'm at abbey road
    fans with cameras in the bathroom, man that's difficult
    i just wanna smoke a backwoods by my lonely self
    chill, watch numbers go up, book off the shelf
    i found myself and put my face on a missing shirt
    i dropped out with no promise that this shit would
    (that this shit would work, work, work
    work, work, work, work)
    (work, work, work, work, work, work, work, worwith the dogs, in my ride know the doors suicide
    paranoid, do or die, you should know we never lie
    with the dogs, in my ride, know the doors suicide
    paranoid, do or die, you should know we never lie
    pull up with the racks to your shop
    cop a medallion or 3, i'm the don
    zim, zim, zim out the bim, get shot
    one mill, two mill, three, that's a lot
    dawhite cuffs, wood grain
    money in the suitcase on my way to the bank
    white cuffs, wood grain
    money in the suitcase on my way to the bank
    on my way to the bank, on my way to the bank
    on my way to the bank, bank, bank, suitcase
    on my way to the bank, on my way to the bank
    on my way to the bank, bank, bank

    my arms are always open, your fears always rollin'
    in the deep, and you can't control it
    what you want, what you want? emotion?
    my arms are always open, your fears always rollin'
    in the deep, and you can't control it
    what you want, what you want? emotioi need to step out with no frustration
    i need a permanent getaway vacation
    they got a permanent hit list, my nigga
    a million reasons to get rich, my nigga
    50 did it rigi could've been homeless
    i thought i moved to orphanage for the summer
    i could've been homeless
    before i had a goal, i had a coura million reasons to get rich, my nigga
    a million reasons to get rich, my nigga
    a million reasons to get rich, my nigga
    nigga, nigga, nigga, nimy people still dry snitchin' whenever they touch the mic
    that's what happens when a therapist isn't somewhere in sight
    take flight, never leaned to the left, or the right
    'cause they turn the other cheek when our niggas start to die
    when our women start to die, when our children start to die
    i don't feel their empathy, we been displaced too many times
    every summer in the city start to feel like columbine
    'cause you gotta get yours, and i gotta get mine
    one time for the paragons of the paradigm
    when you underground, they gon' only try to undermine
    use the track as a gymnasium to get into the stadium
    you couldn't match my alien, i'm glowing like uranone time for the— one time—
    one time— nigga, one time— nigga
    one time— nigga, one t—
    nigga (yes) nigga, nigga (yes)
    a million reasons to get rich, my nigga
    50 did it right, 50 did it right (yes)
    wish i could call every successful black rapper for advice
    how the fuck do i make this shit last my whole life? (yes)
    what if they don't want to come to the concert tonight? (yes)
    [segue reversed] (yes)
    nigga (yes) nigga, nigga (yes) ni(oh) tuggin' on my pinky ring (yes)
    smelling like chrysanthemum
    (honestly, i just want that) (yes)
    i just want that, i just want that, i just want that, i just want that
    (oh) tuggin' on my pinky ring (yes)
    smelling like chrysanthemum
    (honestly, i just want that) (yes)
    i just want that, i just want that, i just want that, i just want that
    (just give me what i need)
    (oh) tuggin' on my pinky ring (yes)
    smelling like chrysanthemum
    (honestly, i just want that) (yes)
    i just want that, i just want that, i just want that, i just want that
    all my jewelry, and all my niggas (yes)
    all my jewelry, and all my niggas got that, yeah (yes, yooh, ooh (yes, yes)
    and you know i got it (yes)
    just give me what i need (yes, yes)

    "yo, get—[censored]—turn that shit over, bo¿cómo se dice? don't touch on me with them dedos
    i minimize all your credentials, i maximize all of my pesos
    i want that dance that can do it, give it to me straight, don't dilute it
    i'm one-handed like odell, numb the pain like orajel
    up and down like gopher bear, hand on me like "oh, well"
    what that smell like, oh, chanel? way too deep like depths in hell
    need a smoking shot of whiskey, down this bitch like, oh, they prissy
    talking smack, oh, don't get lippy, love on you, oh, don't forgcoming like—ee, ee, ee, ee, woah, woah, woah
    take it back—ee, ee, ee, ee, woah, woah, woah
    talkin' em—ee, ee, ee, ee, no, no, no, no
    no, no, no, no, no, no, no,radiation is present, got my reflection iridescent
    every little moment i step in, might shift the planets direction
    glitch in the system is present
    you might wanna check the connection
    i don't give a fuck about freshmans
    i don't give a fuck about veterans
    if your perception ain't ascending, it's no reason for extension
    of my energy, this shit only happens once in a century
    it's elementary when all you speak is rudimentary
    paradiddles hidden in riddles vapid and accessories
    so please don't get it mistaken, opportunities taken
    didn't want to be patient, we had to fight for this thing
    ain't no acting complacent, the disrespect been too blatant
    we claim this spot from the basement, so tell me who you again
    oh you was this, you was that?
    but now you washed and you hate it?
    you taking shots with revolvers, i got two drones at the station
    hit the button, they might come and leave your legacy vacant
    you paved a path we didn't want to get demolished with awe get money, get dough
    dame más mi princesa says so (uh)
    even though my teeth not gold
    baby girl know our pockets drip folds
    (woo! woo! woo! woo!)
    we get money, get dough
    dame más mi princesa says so (uh)
    even though my teeth not gold
    baby girl know our pockets drip fmoney on my—, money on my—
    niggas that i—, niggas that i—
    we said what's up—, we said what's up—
    message that i—, message that i—
    call her brother—, call her brother—
    niggas lookin'—, niggas lookin'—
    let my niggas—, let my niggas—
    niggas with that—, niggas with tee, ee, ee, ee, woah, woah, woah
    talkin' 'bout—ee, ee, ee, ee, woah, woah, woah
    talkin' em—ee, ee, ee, ee, no, no, no, no
    no, no, no, no, no, no, no, no

    big old whiskey on them icy rocks
    flood down some veins like oxy does
    i need fresh air, i need oxygen
    who the hell you fooling? it's so obvious
    i don't feel it, i don't see it, this is blasphemy
    i can't help but feel like you is after me
    is you drinking for the pain? is you drinking for fun?
    there's a party outside, 'til the morning gon' come
    is you dancing all alone? is you dancing for someone?
    there's a party outside, know the night is young
    is you having fun?

    say it with your chest, say it with your chest
    pray it work again
    putting diamonds on my back, putting diamonds on my back, yeah
    say it with your chest, say it with your chest
    pray it work again
    putting diamonds on my back, putting diamonds on my back, yeah

    but you know if i waste my time
    talking 'bout what ain't mine
    and you know i'll be last in line
    just like last, last night

    i said, i said "who that? who that? who that? who that?"
    lurking in the shadows
    tryna catch me liberating spirits from the gallows
    they wanna blackball me, but i held my avocados
    then they melt down like the hash we mix in our tobacco
    circle tighter than the castro, they feeding you castrol
    you'd think that it's gas, you turn the key, it's a fiasco
    could be stronger than vibranium, don't mean that i ain't fragile
    grapple with reality to break out of these shackles

    but you know if i waste my time
    talking 'bout what ain't mine
    and you know i'll be last in line
    just like last, last night

    [verse 3: joba]
    suicidal thoughts, but i won't do it
    take that how you want, it's important i admit it
    i'm afraid of commitment, don't know how to fix it
    maybe codependent, can't tell the difference
    when the push comes to shove, i'd rather bend than break
    but something's gotta give, ain't that what they say
    when you're torn between reality, and a choice you could have made
    or should've made, they're not the same, i'm not the same
    maybe i'm broken, either way i'm clinging on closely
    i know it's unhealthy, appreciate your patience
    i know that i'm selfish, do my best to be selfless
    i know that i'm changing, i know that i'm changing

    i want more, i want more
    i want more out of life than this
    i want more, i want more
    i want more out of life than this
    i want more, i want more

    and mother, i am sorry, i never pick up, mm-hmm
    because i'm afraid to disappoint ooh, ooh-ah, ooh, no

    hey, and i've been feelin' like i don't matter how i used to
    hey, and i've been feelin' like i don't matter how i used to

    we were sat outside on the harvard floor
    with our feet in dirt, and our hearts in awe
    i be losin' sleep thinkin' 'bout missed calls
    and i see the names circling our thoughts
    and i think about if we lose it all
    and i turn to shit that you'd never want
    like the smoke, the drink, anything at all
    and i'll say again, "sorry i don't call"
    there's no money on my mind
    but my money or my mind
    what's the first to fall?
    i never wanted this shit, yeah

    hey, and i've been feelin' like i don't matter how i used to
    hey, and i've been feelin' like i don't matter how i used to

    sometimes, it be so spot on it hurts
    like when auntie couldn't decide between going to work or church
    i've been in my feelings on an island in the dirt
    i feel like brothers lie just so my feelings don't get hurt
    i said, "i'll try vacation, i'll try to run away"
    i deleted facebook, i'll trade fame any day
    for a quiet texas place and a barbecue plate
    i'll switch my place if that's good for you, is that good for you?
    my ghost still haunt ya, my life is i, tonya
    a big-eyed monster, only face to conquer
    i hated songs about fame 'cause that stuff meant nothin'
    until them headlines came, then first flight i'm stuck in

    and maybe it means nothing
    but i have to say i think about you often
    and if you want no part with me
    i'll walk away, i know that i have wronged you
    and maybe it means nothing
    but i have to say i think about you often
    and if you want no part with me
    i'll walk away, i know that i have wronged you

    i took a plane to somewhere that i've never been
    too many times without my sister and my brother
    dad or mother by my side but they're in spirit
    i always hear it, i know they feel it
    my momma always had these dreams that used to keep her up at night
    i smoke to keep them all away and make use of the time
    i'm void of feelin'
    the reasons i'm so out of touch now start revealin'
    but i'm not ashamed, i'm not afraid of who i am
    or how i trust my mental, yeah, it's not perfect
    but i guess that's just the shit i'm into
    i fantasize about a time when everything was simple
    my shelter sheltered me from things i needed to commit to
    the way it stands to me
    a victim of stockholm in my friendships and family

    what's costin' your time? what's the reason that you whine?
    what's in your wallet? dead whites in mine
    so sour, in this light of lime
    daddy said "study or get that cash"
    mommy said "your career ain't gon' last"
    loose change, call a cab, move out their pad
    i just need a chance to move past my past
    don't think too fast, private jets still crash
    and i'll still fly coach, and i'll still hit a roach
    and i'll still see roaches at the crib where my folks at
    touch your dreams 'fore you touch me and provoke a man
    (somebody's gonna have to tell the truth and i'm gonna tell it!)

    (i don't matter)
    i will
    (ahh)
    can i tell you how?
    can i tell you now?
    i will

    "take it all or leave it"

    i can't sleep like i used to
    the world will try to tell you who you are before you get to
    explain yourself, your thoughts
    your motives and all of your reasons
    two albums every season, what the hell do y’all believe in?
    why the hell do y'all keep reachin'?
    in the evenings when i see ’em
    i tell myself that love will be the thing to keep us from grieving
    need something new to believe in
    'cause these new niggas'll change on you
    i mean they change on you
    why the hell the bbc only writes about me
    when it comes down to controversy?
    what about three cd's in one year with no label?
    then we signed and our story turned into a fucking fable
    i was that nigga in a room
    with no motherfuckin' cable and no table
    now my mom call me whenever she need her car note
    cellphone, whatever bill paid too, y'all niggas losers
    you don't understand why i do what i do, so let me do it
    get the hell on, let me do it, get the hell on, let me do it

    i don't speak like i used to
    i’m thinking of a way to change the world that i move through
    i feel like nikola, what i invent is what i’m true to
    i feel for nikola with these ideas that i grew through
    i know that when they see a brilliant mind they'll just abuse you
    it’s hard to feel what's real, some nights i'm scared that i'm delusional
    i’m scared i'm more like nikola than i'd ever collude to
    i'm scared of what can happen when ideas will consume you
    'cause there isn't room for peace i can achieve

    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout

    stay rough, get buff, get out, hey, boy
    stay rough, get buff, get out
    the monsters swarm 'round with them toys
    the monsters swarm 'round with them toys
    hey, boy, stay rough, get buff, get out
    hey, boy, stay rough, get buff, get out
    the monsters swarm 'round with them toys
    the monsters swarm 'round with them toys

    don't mind me, i'm just killin' time (you can pick me to pieces)
    but if you've got a lifeline, throw it, throw it
    don't mind me, i'm just killin' time (you can pick me to pieces)
    but if you've got a lifeline, throw it, throw it

    why the fuck would you share this shit with these people?
    i don't know these people, i don't know you either, no more
    i'm at war with myself
    every time i see this shit i wanna kill myself
    and they coming for my mother, sending bullets for my head
    think they fallin' in love but i'd rather be dead
    please just leave me alone, i don't wanna be read
    yeah, yeah

    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout
    you don't understand why i can't get up and shout
    you don't understand why i can't get up and shout

    it's the best years of our lives, motherfucker
    you are now about to experience
    these are the best years of our lives
    i feel you

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
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
