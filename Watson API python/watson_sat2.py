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
    These niggas take me for granted, what would hap' if I vanish?
    Bet a hunnid they'd panic, my shooters only speak Spanish
    Keep my heart with my dogs, keep my car in the yard
    I can't drive it nowhere so I'll let you niggas take off
    Seen the shit that they drop, that shit not instantly hot
    I give that instant re-bop, that replay value go off
    That make my value go up, I keep that bow in my cup
    My niggas rolling, got that going with a thousand to bust
    That nigga Kevin can't rap, he too sappy with his shit
    He don't rep me with his shit, he on that teenage bullshit
    And he 'bout 20 and shit? When he let go of that shit?
    He'll prolly be a little colder, y'all agree with me? Shit
    That nigga need to act his age, he ain't acting like a grown up
    Ain't that boy from Texas? He ain't acting like a soldier
    Knew that boy in high school, man, that nigga wasn't awkward
    And I know his mama, man, that nigga just a liar

    Cash don't last, my friends will ride with me
    Keep 'em in my bag, we robbed a limousine
    When the guns go pow, won't bother us again
    I don't wanna do it but they keep on pushing me

    Cash don't mean shit, shit
    Cried my last tears, bitch
    Cashed my last check, check
    Cash don't mean shit, shit
    Cash don't mean shit, shit
    Cried my last tears, bitch
    Cashed my last check, check
    Cash don't mean shit, shit

    Call me King of the niggas, I need a crown made of thorns
    God said, "Let there be light" on the day I was born
    Step off the ship with the slaves, then I go hit the stage
    I just left in a whip, all I need is a chain
    I don't trust no niggas and I don't trust no bitch
    'Cause people talk too much, I bought a black fo'-fifth
    And a brand new clip, that's my new best friend
    'Cause I'm a brand new nigga, in a brand new crib
    I ain't sellin' no more, but got my hand in the zip
    Whitey gave me the check, I ain't ask for the fame
    I used to deal with the grams 'til they put the cam on my face
    Now I'm evading the law, I'm on a high-speed chase
    I'm in a big-ass truck, I tell 'em, "Get out the way"
    I gotta couple of warrants, so I'm leaving my state
    Now I'm in Cali today, with the sun on my face
    I got a bag of the gas, and a blunt I can face

    How I'm gon' move at your pace? I'm busy settin' the tone
    You think we runnin' together? I'm in a lane of my own
    Don't got no friends in this game, it's me and my brothers alone
    They thinkin' that we competing, that shit depletin' my bones
    I don't need all that energy, they just fuck up my chakras
    I put my heart in a locker, they love me when I'm a martyr
    They hate me when I'm myself, I can't barter with that
    You watch us charter these tracks, it's sticking like tartar and plaque
    I need a parlour of plaques, need lobsters and helicopters
    I need peace for my niggas, need darker skin for all my doctors
    I like to speak like a scholar, like to think like a nigga
    In this world I can't wander, no honor behind the trigger
    I could get shot in my back and they'd tell the world that I fought 'em
    "We ain't taught 'em nothin' new, but somehow they been gettin' smarter"
    That's what they sayin' in private, speaking from that entitlement
    We still workin' for titles and makin' tidal environments

    Cash don't last, my friends will ride with me
    Keep 'em in my bag, we robbed a limousine
    When the guns go pow, won't bother us again
    I don't wanna do it but they keep on pushing me
    Cash don't last, my friends will ride with me
    Keep 'em in my bag, we robbed a limousine
    When the guns go pow, won't bother us again
    I don't wanna do it but they keep on pushing me

    Fuck, put ya ante up, riding in the limousine
    I'm stuck on some bud I hit, under concrete canopy
    Fuck all this energy, you just wanna bring me down
    Fuck all your energy, you just wanna bring me down
    Fuck, put the windows up, blowin' past the exit now
    Up like a money shot, swerve into the sunset
    Me and all my boys jet, swerving like a doughnut
    Off, off, off, off, swerving like a doughnut

    Nigga, what?
    Pull up, pull up, pull up, pull up, pull up if you want to
    Nigga, what?
    Pull up, pull up, pull up, pull up, pull up if you want to
    Nigga, what?
    Pull up, pull up, pull up, pull up, pull up if you want to
    Nigga, what? Y-yo

    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down
    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down

    Hi, I live a wonderful life
    Should've died twice, wonder who on my side
    Life always better keepin' two on the side
    Need no music when my niggas arrive
    We be in Van Nuys, black van with some white guys
    Keep your hand out, waiting for the appropriate time
    To ask a question like
    "Could you perform at my best friend's birthday party?
    With your friends and go crazy, just bring the shotty
    Bring the loud one with the blonde hair."
    Making out with Zayn in a lawn chair
    They kicked me out but I belong here
    Hear these songs nigga, see this long hair, see these videos
    Direct these hoes with no budgets though
    How the fuck did I land a fucking TV show?
    Met all my friends through Kanye West and I ain't met him yet

    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down

    Just shaved down to the baby face
    Clothes on me, guess it's Holiday
    Fried, no sides at the restaurant
    My sleep schedule like the power here, it's never on
    Feeling like the past year a whole escapade (uh-oh)
    Four cars, need a motherfucking Escalade
    Pack it up like a clown car (honk, honk)
    Bet you know my name from here to Hong Kong, bet I get along
    Make some commas, karma, watch 'em sing along
    Ayy, err, err, butter knife like dancing on a knuckle
    In the thunder car, rocked up in the Lumma
    Incidental, I be better by the summer
    I be better by the winter, I be hoppin' in the rental
    Maybe Tesla for all my missus sitting in the Volvo
    Damn, shoot 'em down like, hmmm, sorry, do it all here

    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down
    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down

    I'm moonwalking on the sun hot
    I used to live where the guns popped
    Made some records then we moved out
    Turned rap into the new pop
    Bandana, I'm the new Pac
    I been blowing up, I can't stop
    They need my niggas in the White House
    I do business with the white folks
    Bring that money back to black folks
    Flip it, stimulate the cash flow
    Economic, but I speak ebonics
    L.A. turned me to an asshole
    I been shopping down on Melrose
    Still a nigga but I'm livin' different
    I been looking at the bigger picture
    So I don't hear 'em when they talking to me

    I just want a friend to fall in love with
    Maybe someone I can binge drugs with
    Living like a prince but I'm dove-less
    Playin' my emotions, you a dumb bitch
    Everybody talking on some gun shit
    They don't even know where to bust it
    Cry nigga, gotta fuckin' kick back
    Gotta leave those soft niggas at the kickback
    Splittin' all my problems like a Kit-Kat
    I finessed the night that we slipped up
    I could let you know where I'm next at
    Tell my baby girl where the brakes at
    You know I got number one pick stats
    Catch me on the field, it's a mismatch
    More like an eclipse, she couldn't miss that
    Putting my ideas where my chips at

    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down
    La-di-da-di-da-di-da, do I trust 'em? Probably not
    I think that y'all prolly fraud, I think that my brain is fried
    La-di-da-di-da-di-da, do not turn my volume down
    Do not bring your friends around, only few I'm holding down

    La-di-da-di-da-di-da (La-di-da, la-di-da)
    Do-walla, do-walla-walla, do-walla
    La-di-da-di-da-di-da (La-di-da, la-di-da)
    Do-walla, do-walla-walla, do-walla
    La-di-da-di-da-di-da (La-di-da, la-di-da)
    Do-walla, do-walla-walla, do-walla

    I done been in trouble 'bout as long as I remember
    My momma tried to help me but I hardly ever listened
    So she sent me to them white schools, I learned that I was different
    They told me I'm a nigga, well, now I know I am
    I got my finger on the trigger, I'm a project baby
    A free lunch felon, and I'm hungry every minute
    Empty stomach, weed smoke can't fill it
    If you don't listen to me, I set fire to the building
    Need to listen to the children and the weapons they concealing
    Hear the voices of a million when I sell my first million
    I am bound to go diamond, ain't no luck or surprises
    I am tanning on an island
    I can feel the pressure but I see my new horizons
    Me and all my niggas getting stars down on Sunset Boulevard
    But niggas from the Southside with Xan bars and gun play
    Niggas on that "someday..."
    If you shooting for the stars, you only headed one way

    I could be here all day. You're gonna tell me what I need to know. You're gonna tell me! Are you gonna tell me? C'mon, spit it out...
    Me Ilamo Roberto, y este es el camino al éxito.

    Fucking commas up from the outside
    From the outside, from the outside
    Fu-fucking dollars up from the outside
    From the outside, from the outside
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?

    My daddy taught me how to sell dope
    Turn grams into elbows
    Light it up when the L rolled
    Black mask, used to kick doors
    Wasn't no bullets in the guns though
    Niggas still never argued
    Raid the house like the task force
    Me and my niggas like drug dogs
    Find the dope then we take off
    Fuck my girl with my chain on
    Then she tatted my name on it
    Yellowstone, I was raised on it
    Actavis in my baby bottle
    Baby stroller was an Impala
    Niggas like to talk down on me
    When I see 'em, I don't hear about it

    Fucking commas up from the outside
    From the outside, from the outside
    Fu-fucking dollars up from the outside
    From the outside, from the outside
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?

    (Merlyn! Merlyn!)
    Never would've met my friends if not for satellites
    Yeah, I'll cuff her even if she do not suck me right (suck me, suck me!)
    Always planned to be a rapper when I failed at life
    Luckily professor failed me at the proper time (yee! yee!)
    Shh-shh, shh, I say "please" all the time, bitch
    Shh-shh, shh, I like white collar crime, bitch
    Shh-shh, shh, money digital broke and
    Shh-shh, shh, Ghana prince in your messages

    I know you hate me for leavin'
    Then let's go crazy together
    When I tell ya all the things that I'm thinking
    Just so that we could get better
    But you wanna put my heart on the stretcher
    I don't got insurance for this pressure
    Wanna find the benefits, I can't measure
    Trying not to run out on my temper
    I can see the ash and the ember
    That was made from emotional texture
    I don't know why I took this endeavor
    Don't identify with oppressors
    Don't identify with surrender
    All of my old friends fair-weather
    Gotta treat my heart like a treasure
    'Cause all I know is no one else will

    Fucking commas up from the outside
    From the outside, from the outside
    Fu-fucking dollars up from the outside
    From the outside, from the outside
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?

    You do not know me, don't speak of my homies, you are a phony
    Quit pinnin' shit on me, you gon' bring out the old me
    You don't wanna know what I wanna do when y'all talk down on my name
    I don't wanna see you in the street 'cause I might catch a case
    People smile when they face to face (woo, woo, woo!)
    Then turn their back and switch up words you say (ah, ah, ah!)
    Running to the papers everyday (woo, woo, woo!)
    I'm running to the paper anyway (ah, ah, ah!)

    Fucking commas up from the outside
    From the outside, from the outside
    Fu-fucking dollars up from the outside
    From the outside, from the outside
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?
    They been talkin' down on me (huh) what ya say?

    Too many things I'd rather do different
    Woke up in a cold sweat (Uh!)
    My emotions creepin'
    Three o'clock on the weekend, might as well sleep in
    Stay down for the count when
    She hit me with the "what-ifs?"
    And the "what-whens?" and the "what-thens?"
    Wonder where my life went, living in the moment
    I been thinking 'bout my time spent, are the bills paid?
    Is it make or break? Will I find a way?
    Have my feelings changed? Will I be okay? I don’t know
    But what I do know is, life don't make sense
    If you can't pay rent, so I place my bet
    What got you shook on this Saturday?
    I take my L and I hold my place
    I split my L and I go away
    You left a spell on my Saturday
    What got you shook on this Saturday?
    I take my L and I hold my place
    I split my L and I go away (Yah)
    You left a spell on my Saturday

    I got cracks in my phone screen
    The past fuck with my psyche
    Smoke weed and get high, please
    Went to school in The Woodlands
    And that made niggas wanna fight me
    So I don't take threats lightly
    Tell them niggas, "Come and find me"
    Gotta say it in my eye view
    New house off iTunes
    New money, my perfume
    Big smile, in a good mood
    I been running out of issues
    I ain't trippin' when the rent due
    I ain't runnin' with a pistol
    I ain't locked in the system
    Taking care of my kinfolk

    Taking a book out the page of the greats
    I'm only human and I make mistakes
    Chisel my flows so they can't liberate
    Talking the time as the pendulum sways
    I gotta face what I didn't create
    Just 'cause I can't relate, I don't debate
    I educate, illuminate
    Or we can't duplicate, no more moving the plates
    Second chances feeling overrated
    Unappreciated, so I bossed up
    Missed the time when we could share space
    But it'll all be straight the day we cross up
    Nothing better than some time with you
    Because it's time I never wanna toss up
    Lose myself inside of you, you find yourself in me
    I don't wanna be cautious

    What got you shook on this Saturday?
    I take my L and I hold my place
    I split my L and I go away
    You left a spell on my Saturday
    What got you shook on this Saturday?
    I take my L and I hold my place
    I split my L and I go away (Yah)
    You left a spell on my Saturday

    What got you shook?
    What got you shook?
    What got you shook?
    What got you shook?

    I felt awesome when you walked in
    You caught me doin' something
    That I should've never been caught with
    I played the forest, my far trip
    I tripped and I fell, still think I'm living in Austin
    Remember when I was trippin' off some wack shit
    When I thought the automatic had an answer?
    When I was jammin' out Beyonce like Sampha
    And you broke up with me 'cause I'm a Cancer?
    Our relationship was toxic, cancer
    I fell in love with a dancer in Atlanta
    I'm lying, I ain't a Drake-ass nigga
    I'm more like Troye Sivan
    With a whole lotta mela-nahn
    Sendin' bombs to your lawn
    Grew up on Rockafella, so I'ma get a chain
    And sing every song in the vain of your name
    And this'll...

    Be there when they call me up
    Save me wishin' for you, I'm missing you too
    Miss the way we talk, miss the way we stop
    Miss the way we talk, ooh
    Be there when they call me up
    Save me wishin' for you, I'm missing you too
    Miss the way we talk, miss the way we stop
    Miss the way we talk, ooh

    Why you look like that? (He looks crazy as fuck)
    He look crazy as hell
    But he dress well (oh my God)
    Why his face look puff?
    Why he look like that? (You look like a)
    Why your hair like that? (Like a chipmunk or something)
    Why your teeth like that? (Or like a prairie dog)
    Why your cheeks like that?

    I got this shitty moustache, and a new haircut
    Short but tall enough to ride every ride so it's fair enough
    Teeth crooked but my breath fresh just like the evergreens
    My attitude is bit like, a psys- fuck!
    You mean a psychopath
    I bet the marble feel good on your bare foot
    I'm in the backyard hiding out like I'm Bigfoot
    And I won't cater to you
    Yeah I am not Carrabba's, and I ain't taking orders
    Here for the loot, and to inspire some of you
    To do what you do despite all the "fuck you's"
    'Cause they shit on your shit, stab you right in the back
    'Til you're shittin' on the toilet with Grammys in your lap

    Niggas talk a lot of shit, in a safe place
    Aiming with they keyboard, they shootin' uppercase
    I'm booking tour dates, money in the suitcase
    Commander and the chief like, Barack Hussein
    Same nigga, two names, I am onto new things
    Flying out of Houston, lemme say a few things
    I don't give a fuck about you or your screen name
    I'ma be a star even if I say the same things
    'Cause them same things keep me on the wavelengths
    I dropped another verse, so you gon' have to pay me
    Glock with no safety, seen niggas on the pavement
    Over gang affiliations, guns with extensions
    Seeing niggas get anxious, all these internet gangstas
    I'm running outta patience, nigga, stick to your day shift
    And watch what you're saying, and please keep praying
    'Cause niggas talk big 'til that price on their head
    I feel the voices always drown out all the noise in the room
    They don't employ you for your purpose, they just need a platoon
    Another number in a line ready to march into tombs
    I ain't the one to assume, I put the coon in tycoon
    We colonizing the moon, I see you look to the sky
    And start to wish it was you, sometimes I wish I was me
    Sometimes I'm watching my life
    I'm dissociated from what eats my heart up at night
    Sleep on a cloud of my strife
    I ain't afraid of the heights, they all afraid to appall
    I'm just afraid of excitement being a trip to the mall
    I need a summer to fall, I need a winter to spring
    Got all these seasons within me, building a story to sing
    Don't need a dollar to dream, I need a billion in facts
    I need a trillion in wealth, y'all niggas need to relax
    I wanna build up the culture, they wanna dream in the trap
    I took the zoom off my lens and I saw the world in my lap
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the bag, all my niggas in the bag
    I'm not tryna be like you, when I grow, money in the bag
    Keep the sand in the

    I spit my heart out, lookin' out for my best interests
    He gave me good head, peepin' out while the windows tinted
    I speak in tongues and I arrive without a damn mention
    It's kinda sick and I was born in 1996 and
    1999 the only year that I remember
    I slip through the cracks without havin' a damn temper
    I bleach my hair because these bitches all about they bitchin'
    I say shit when I rap and y'all niggas barely listen
    I do the most for the culture, nigga, by just existing
    Delete my tweets 'cause I'm ashamed of being a fuckin' Simpson
    I told my mom I was gay; why the fuck she ain't listen?
    I signed a pub deal and her opinion fuckin' disappearin'
    I'm payin' bills for my sister and tryna fund her business
    Is it homophobic to only hook up with straight niggas?
    You know like closet niggas, masc-type?
    Why don't you take that mask off?
    That's the thought I had last night
    "Why you always rap about bein' gay?"
    'Cause not enough niggas rap and be gay
    Where I come from, niggas get called "faggot" and killed
    So I'ma get head from a nigga right here
    And they can come and cut my head off, and
    And my legs off, and
    And I'ma still be a boss 'til my head gone, yeah
    Break the wheel, pack the steel, hold my niggas down
    Twistin' on that syrup ‘til I hear crackin’ sounds
    Break the wheel, pack the steel, hold my niggas down
    Twistin' on that syrup ‘til I hear crackin’ sounds
    Break, break, break the steel, hold my niggas down
    Twistin' on that syrup ‘til I hear crack, crack, crack
    Break the wheel, pack the steel, hold my niggas down
    Twistin' on that syrup ‘til I hear crack
    I don't trust nobody 'cause they don't deserve it
    Niggas run in your house, they know you doin' dirty
    (Go 'head, now)
    I got my hand on an ounce, and I got money servin'
    I just bought me a fifth and now I'm speedin', swervin'
    (Go 'head, now)
    I took an eighth of them shrooms and now I'm hearin' voices
    I took like two of them pills, I can't remember nothing
    (Go 'head, now)
    I ain't under control, I'm losin' motor function
    I need an intervention, I need an exorcism
    I need a therapist, paranoia and drug addiction
    It's very scary, my momma don't even recognize me
    I'm goin' crazy, don't need nobody to say they love me
    My acts of desperation, I'm on an empty stomach
    So fuck the consequences, I ain't runnin' from them
    Feelin' like a goner, put my life in locker
    Hotbox in the Hummer
    Hot bars in the summer (Merlyn, Merlyn!)
    If I had the option, I would do it all again
    If I had the option, I would do it all again
    I just wanna feel like I did the right program
    I just want to appeal to my dad and my cousins (Again)
    When I cop that feel, I do not think 'bout diplomas
    Love is knowin' that you didn’t do it by your lonesome
    So I forgive my mommy, daddy, auntie, and my uncles
    For guilt-tripping feelings whenever they call my number
    They see men dream, they see men fallin'
    But when I dream, I'm smashing on Atlanta
    Both pessimistic, drug addicted, caught in our feelings
    We spit venom then stare at the ceiling, wondering, "why?"
    My mom's no alcoholic, she just wanna drown her sorrows
    Love her to death and soon enough I'll give back all I borrowed
    Both so submissive, take turns dominating, the light has been faded
    This hate-fueled love, we don't fake it, no givin', just takin'
    I took some steps to be a bigger person
    I should've thrown ya off the highway to cars swerving
    Ain't no burden, ain't no sermon, ain't no motherfuckin' plaque
    I hate these hospitals and police and the smell of death, all that
    I hate these shady folk, that want a lady like
    But don't treat lady right, but they be sayin' like ("Just the tip!")
    And yeah you mad 'cause she ain't fuck, mad 'cause she ain't suck
    Beat your ass before you got time to say "Why not?"
    Here to catch ya slip up, wish you could just rewind
    Timing all fucked up, thought you had just lucked up
    Where the respect? Is your ass human?
    I look you in your eyes, say, "Fuck you, are you fuckin' stupid?"
    Respect my mother, 'spect my sister, 'spect these women, boy
    I get my 9-9, I don't own one, hit the store to blow your brains off
    Better hope my aim off, better hope the range off
    Better hope my tame off before I blow your brains off, boy
    Uh, no hands with the stunts
    Jump off the roof like I do what I want
    All of my life in my past wanna haunt
    And my sight of the future beginning to taunt my ambition
    Man on the moon, I'm marooned, I ain't trippin', I'm on a mission
    Every time that I speak they ain't skippin'
    Turned my inspiration to a vision, that's a given, no slippin'

    My male role models drug dealers and thugs
    My father learned how to solve problems with guns
    And when I grew up I learned what racism was
    And what teaching it does, and like my teachers would say
    "Little black boys have a place in the world
    Like hanging from trees, or dead in the street"
    Like I seen on TV
    All them boys they killed, they looked just like me
    Not like Brandon or Chandler, but Malik and Kareem
    I was born with a target, and it stuck to my skin
    And I learned in social studies, I was one of them men
    Who were locked in the chains, but not locked in the pen
    But I'm bigger than that, I'm the beginning and end
    I'm the sun and the moon
    I'm the light and the dark, I am life in the tomb
    I'm the pharaoh and slave, gentrifying my spirit
    It's like a knife in the womb, refuse to act like a parrot
    Or to dance like a monkey, see your stance is apparent
    That's why I'm here for the money, don't care to cater to merit
    Y'all fetishizing my spirit, I see your culture’s dependent
    On what you didn’t inherit, won't let my world be attempted
    I'm staying distant
    Who gonna be the reason why I get high?
    Who gonna be the reason why I turn over?
    Who gonna be the gunner that I don't trust?
    Who gonna be the gunner that get they ass whooped?
    Who gonna be the reason why I get high?
    Who gonna be the reason why I turn over?
    Who gonna be the gunner that I don't trust?
    Who gonna be the gunner that get they ass whooped?
    Who gonna be the reason why I get high? (Bloodsucka!)
    Who gonna be the reason why I turn over? (Bloodsucka!)
    Who gonna be the gunner that I don't trust? (Bloodsucka!)
    Who gonna be the gunner that get they ass whooped? (Bloodsucka!)
    Who gonna be the reason why I get high? (Bloodsucka!)
    Who gonna be the reason why I turn over? (Bloodsucka!)
    Who gonna be the gunner that I don't trust? (Bloodsucka!)
    Who gonna be the gunner that get they ass whooped? (Bloodsucka!)

    Bum, bum, beat 'em, I would never wanna be 'em
    If I catch 'em slipping, they gon' have to meet the eagle
    Bum, bum, beat 'em, treat these niggas how I see 'em
    I don't need you either, send you right back where I seen ya
    Bum, bum, beat 'em, I would never wanna be 'em
    If I catch 'em slipping, they gon' have to meet the eagle
    Bum, bum, beat 'em, treat these niggas how I see 'em
    I don't need you either, send you right back where I seen ya
    In the game, in the game, in the game, in the game (bloodsucka!)
    In the game, in the game, in the game, in the game (bloodsucka!)
    Running thangs, running, run, running, run, running thangs (bloodsucka!)
    Running thangs, running, run, running, run, running thangs
    In the game, in the game, in the game, in the, in the
    In the game, in the game, in the game, running thangs
    Running thangs, running, run, running, run, running, run
    Running thangs, running, run, running, run, running thangs

    Stripped down to my skin and my bones
    I love huskies but I feel like a wolf (Howl!)
    In a pack but I feel all alone
    I'm scatterbrained man, better offer the Clon'
    In Tejas apartments with racists doin' weird shit
    Like, this'll make the biopic (Haha!)
    Rile 'em up, hit Zaxby's, get the wing and tings (Yum!)
    Real quick bills still stacking to the ceiling (Uh-oh...)
    Whatchu mean, it ain't working? (What?)
    Whatchu mean, you ain't finding yourself? (Oh, I am, I'm trying)
    Whatchu mean, you ain't got no cash? (I got a little bit...)
    Whatchu mean? Whatchu mean?
    Shouldn't your pockets be big just like a fat chick? (Uh-huh!)
    Shouldn't your mama be done paying the house off? (I guess?)
    Shouldn't you have a real big-ass ego? (No?)
    Shouldn't these girls be flockin' just like seagulls? (Eh...)

    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit
    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit

    The original lick-splickety, higher than Yosemite
    Breaking the mold mentally, master with no limiting
    Making 'em say "ugh!", they worshipping our force viciously
    Watching the floor tip in your temple of authenticity
    Often they say I’m off it, I offer my crossed empathy
    They forgot what we on, I’ll remind 'em with hostility
    Hot-diggity damn, everyone running scams
    Gotta cover your clams and take another glance
    Running a clinic, no scans, ain't no one claimin' yo mans
    It's all pertaining to plan, call me the architect
    Lap you in a UFO, I haven't started yet
    Still gotta figure out exactly where to park it at
    Moses with the pen, each line an ocean I can part it at
    But that's too deep

    Don't call me stupid, that ain't the way my name pronounced
    Don't call me Cupid, I got too many hoes right now
    Poolside in Houston
    Tryna see if Beyoncé will take me for adoption
    Broke-ass rich suburbs
    A civilian shot in 3rd Ward, we just by the fountain
    This is Merlyn Wood, man
    Everywhere I go is the Woodlands
    I need a honey butter, vodka in a Sprite can
    When I'm in the Whataburger, all the kids know who I am
    I need a honeybutter, puttin' lean in my Sprite can

    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit
    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit

    I got a record but I'm clean as they come
    I'm Godzilla, when they see me, they run
    On 37th, used to run from the bloods
    The undercovers gotta duck when they come
    I moved out and in a couple of months
    I'ma be a pop star, they call me a thug
    I used to write raps on the back of the bus
    Now I'm in the front seat shifting the gears

    It's funny how things can change
    Three hundred dollars to my name, led to Hollywood
    I was living off Ramen and change
    Five hundred dollars on these dinners, never have to pay
    Growing up my teachers told me
    "You better get them grades up if you wanna finish high school
    And after high school, you better get a degree
    'Cause it's a dog-eat-dog world, you could live in the street"
    Flashback, I had my Walkman in the minivan
    Listening to NSYNC, saw my name on the CD
    Bleach blond tips, wanted to be JT
    Wanted to do big things, had to fulfill a dream
    One might say I was doomed from the get-go
    But those same people assume, 'cause they'll never know
    What it's like to be called to what's not set in stone
    I am one with the ebb and flow, that's all I know

    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit
    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit
    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit
    Twistin' me up like licorice
    Think I need someone who can handle it
    Ice on my boys and my wrist is fixed
    I don't need nobody tryna give me shit

    I don't know why I wanna fuck with you
    But all I know is that I really fuck with you
    Really wish you didn't like to fuck with me
    Wish you took that energy and trusted me
    I get so exhausted when you fuss with me
    'Cause all that time could be spent in love with me
    I know I need it and you deserve it
    You like to size me up to see if it's all worth it
    I don't know where it is now, but I'm searchin'
    I think you want what I don't ever want: be perfect
    'Cause I ain't perfect, I just wanna be good to you
    I would take my heart right out the hood for you
    Wanna do the things I know I should for you
    Standing by myself until I stood for you
    If I knew this love, I woulda looked for you
    But I'm glad you found me, I'm glad you found me

    [Chorus: Kevin Abstract]
    Callin', callin', callin', callin', trip, fall
    Callin', callin', callin', callin', trip
    Callin', callin', callin', callin', trip, fall
    Callin', callin', callin', callin', trip
    Callin', callin', callin', callin', trip, fall
    Callin', callin', callin', callin', trip
    What you gonna do when you older?
    What you gonna do when you grow?

    Split the diamond with us, fuck taking the bus
    I want a whip to call my own and a home to call my own
    All 14-15 of my niggas
    To figure, ooh, that's a step-back
    Ooh, my nigga, that's a step-back
    If I had to choose, I would not choose you
    If I had to stop, I would turn around and choose glue
    If I had to hit the breaks, I'ma stop right
    If I had to choose, I'ma not choose you
    If I had to turn around, I'ma turn into some glue
    If I had to hit the brakes, I'ma stop right here, yeah

    Callin', callin', callin', callin', trip, fall
    Callin', callin, callin', callin', trip
    Callin', callin', callin', callin', trip, fall
    Callin', callin', callin', callin', trip
    Callin', callin', callin', callin', trip, fall
    Callin', callin', callin', callin', trip
    What you gonna do when you older?
    What you gonna do when you grow?

    You're all I love, washing off my hands
    You're all I love, washing off my hands
    You're all I love, washing off my hands

    Don't waste your mind
    I'll be the one to settle
    To do what I am
    To say what I am
    Don't waste your mind
    I'll be the one to settle
    To do what I am
    To say what I am

    Callin', callin', callin', callin', trip, fall (you're all I love)
    Callin', callin', callin', callin', trip (washing off my hands)
    Callin', callin', callin', callin', trip, fall (you're all I love)
    Callin', callin', callin', callin', trip (washing off my hands)
    Callin', callin', callin', callin', trip, fall (you're all I love)
    Callin', callin', callin', callin', trip (washing off my hands)
    What you gonna do when you older?
    What you gonna do when you grow?

    Yeah!
    Yeah, yeah, yeah!

    All I do is work and play (Ay-yah-woo-woo!)
    Tryna' find a place to stay (Ay-yah-woo-woo!)
    Tryna' find some food today (Ay-yah-woo-woo!)
    This shit is real hard okay? (Okay)
    Take that, homie got the Lysol spray, ain’t it? (Ain't it?)
    You don't wanna see all my bad days, ain't it? (Ain't it?)
    You don't wanna see what I got to say, ain't it?
    You don't wanna see my boys, man, they ain't friendly

    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down

    It ain't my birthday yet and I'm acting like a bitch
    Screaming "motherfuck your set" like I'm 2Pac
    Ain't got no ice on me yet, still feeling how I dress
    So it's Dickies and I got these hoes from Walmart
    It ain't my birthday yet and I'm acting like a bitch
    Screaming "motherfuck your set" like I'm 2Pac
    Ain't got no ice on me yet, still feeling how I dress
    So much Dickies and I got these hoes from Walmart

    I just saw my P.O. (What up, nigga?)
    He like me, though (He like me, though)
    Clean money, tryna stay up out the streets, though
    7 days a week though, (All day!) it's that heat, though
    My daddy called me, said he seen my last video
    Looking at a younger me, coulda had a heatstroke
    In the middle of the summer with my negros
    Cool cuts and snow cones, smoking to the ozone
    Smokin' 'til it's all gone, smoking 'til my folks come home

    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down
    Trip a lot, sinned a lot, send em' all down

    Runnin' outta time again
    Runnin' outta time again
    Runnin' outta time again, mmm
    Ay-yeahh, ay-yeahh
    Ooh, ooh, oo-ooh, ooh

''',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True,limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True),
        emotion=EmotionOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
