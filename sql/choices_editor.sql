-- Fixer Comment (DON'T DELETE)
INSERT INTO Choices
VALUES
    ('AAA0', '', 'mia', 'Game Over', 'quit', 'AAA1', 'AAA0'),
    ('AAA1', 'Narrator', 'mia', 'So, this is a game about a person named V{p1_name}, also known as YOU!', 'na', 'AAB1', 'AAB0'),
    ('AAB1', 'Narrator', 'mia', 'You live in a fairly small house in a quiet part of the city, and it is the year 2571 so you, like everyone else, own laser guns (and it is definitely not just for plot convenience). You also own an android called Peter, which you live with.', 'na', 'AAC1', 'AAB0'),
    ('AAC1', 'Narrator', 'mia', 'It is now morning, and you decide to wake up...', 'na', 'AAD1, AAF1', 'AAD1, AAF1'),
    ('AAD1', 'Narrator', 'mia', 'You get out of bed, before heading to the kitchen to make breakfast for yourself.', 'na', 'AAE1', 'AAB0'),
    ('AAE1', 'Peter', 'peter', 'Hey, you''re up early!', 'na', 'AAI1', 'AAI1'),
    ('AAF1', 'Peter', 'peter', 'Okay, fine.', 'AAF1', 'AAG1', 'AAB0'),
    ('AAG1', 'Narrator', 'mia', 'Peter proceeds to make you breakfast, since you''re just that lazy that you need him to make it.', 'na', 'AAH1', 'AAB0'),
    ('AAH1', 'Peter', 'peter', 'Here''s your breakfast.', 'na', 'AFU1', 'AAB0'),
    ('AAI1', 'Narrator', 'mia', 'After you finish eating, you get yourself dressed and ready for the day... despite the fact that you have nothing to get ready for.', 'na', 'AAJ1', 'AAB0'),
    ('AAJ1', 'Peter', 'peter', 'Oh, I just noticed that you don''t have anything on schedule for today! Is there anything that you wanted to do?', 'na', 'AAK1, AAO1, AAL1, AAM1', 'ABG1, ABH1, ABI1, ABJ1'),
    ('AAK1', 'Peter', 'peter', 'Yeah, that sounds like a great idea!', 'AAK1', 'AAU1', 'AAB0'),
    ('AAL1', 'Peter', 'peter', 'Well I think we should go to the beach.', 'AAL1', 'AAU1, AAO1', 'AAC1, AAE1'),
    ('AAM1', 'Narrator', 'mia', 'Oh no...', 'na', 'AAN1', 'AAB0'),
    ('AAN1', 'Narrator', 'mia', 'Fine. You somehow find a plane and suicide bomb the towers. Now you''re dead, and absolutely nobody will miss you. Congratulations... dumbass.', 'na', 'ADP1', 'AAB0'),
    ('AAO1', 'Peter', 'peter', 'Seriously? You just want to stay at home to remind yourself that the only friend you have is a robot that you bought a year ago due to loneliness?', 'na', 'AAP1, AAP1', 'AAC0, AAC0'),
    ('AAP1', 'Narrator', 'mia', 'Peter then facepalms due to you picking the most boring option ever.', 'na', 'AAQ1', 'AAB0'),
    ('AAQ1', 'Peter', 'peter', 'Why did I have to be bought by the most depressing person ever???', 'na', 'AAR1', 'AAB0'),
    ('AAR1', 'Narrator', 'mia', 'You just spent your entire day messing around in you house, and the loneliness you had felt was suffocating. Why you had picked this option, nobody knows, but it''s your life now.', 'na', 'AAS1', 'AAB0'),
    ('AAS1', 'Narrator', 'mia', 'Though you didn''t have much left of it anyway, since before long, a nuke came and destroyed anyone and anything that wasn''t in a bunker.', 'na', 'AAT1', 'AAB0'),
    ('AAT1', 'Narrator', 'mia', 'Maybe if you had actually done something, you could have stopped that nuclear bomb, or at least just learn''t where it came from, but who knows, since you picked this option, so I hope you like death!', 'na', 'ADQ1', 'AAB0'),
    ('AAU1', 'Narrator', 'mia', 'After a conveniently short walk, you finally arrive at the beach. However, you instantly regret it as soon as you get there, as sand is gritty, annoying, and gets everywhere.', 'na', 'AAV1', 'AAB0'),
    ('AAV1', 'G{Narrator}', 'mia', 'Just like me!', 'none', 'AAW1', 'AAB0'),
    ('AAW1', 'Narrator', 'mia', 'Thankfully though, you find an ice cream van. After a long wait, you manage to finally get the best thing that''s happened to you in years... before someone dressed entirely in maroon and brown bumps into you and knocks it out of you hand.', 'na', 'AAX1, AAZ1, ABB1', 'AAA1, AAB1, AAG1'),
    ('AAX1', 'Man', 'gary', 'It was an accident, jeeze. No need to get all aggressive at me! G{You do know that that''s a bad idea, right?}', 'AAX1', 'AAY1', 'AAB0'),
    ('AAY1', 'Narrator', 'mia', 'You don''t know what he means by that but you have a bad feeling about it. The man runs off before you can say anything else.', 'na', 'ABF1', 'AAB0'),
    ('AAZ1', 'Man', 'gary', 'Woah woah woah, calm down! It''s just some ice cream! Here, take some money as compensation, jeeze! G{...It''s not like money will be of much use soon anyway...}', 'na', 'ABA1', 'AAB0'),
    ('ABA1', 'Narrator', 'mia', 'You don''t know what he means by that, but you have a bad feeling about it. Before you can say anything else, the man quickly pulls out £5 from his pocket and gives it to you before walking off, muttering something in an angry tone as he left.', 'ABA1', 'ABF1', 'AAB0'),
    ('ABB1', 'Man', 'gary', 'Oh, I''m sorry about that... There''s a lotta people here so I accidentally bumped into you. Here, I hope this makes it up to ya.', 'na', 'ABC1', 'AAH1'),
    ('ABC1', 'Narrator', 'mia', 'The man pulls £5 from his pocket and gives it to you.', 'ABC1', 'ABD1', 'AAB0'),
    ('ABD1', 'Man', 'gary', 'Oh, and as a warning, you may want to make this week the best week you can - G{You never know when it might be your last...}', 'na', 'ABE1', 'AAB0'),
    ('ABE1', 'Narrator', 'mia', 'You don''t know what he means by that, but you have a bad feeling about it. Before you can say anything else, he walks away.', 'na', 'ABF1', 'AAB0'),
    ('ABF1', 'Narrator', 'mia', 'Around 6 hours later, you decide to walk back home. The main pathway is crowded so you and Peter decide to take a shortcut through a shadowed alleyway instead. What could possibly go wrong?', 'na', 'ABG1', 'AAB0'),
    ('ABG1', 'Narrator', 'mia', 'Everything, apparently, as you heard the sound of a mysterious figure jumping to the floor behind you and starting to run at you.', 'na', 'ABH1, ABI1', 'AAJ1, AAK1'),
    ('ABH1', 'Narrator', 'mia', 'You start shooting at the navy-haired figure, but they somehow manage to dodge all of the lasers. They eventually shoot Peter and knock you out swiftly. You didn''t even have a chance.', 'na', 'ABJ1', 'AAB0'),
    ('ABI1', 'Narrator', 'mia', 'You try to run as fast as you can, but the bluenette catches up and shoots Peter, before knocking you out swiftly. You didn''t even have a chance.', 'na', 'ABJ1', 'AAB0'),
    ('ABJ1', 'Narrator', 'mia', 'A few hours later, you wake up and quickly notice that you are bound to a metal chair with leather straps, but before you can even think to panic, the maroon-clad man from earlier steps out of the darkness and speaks.', 'na', 'ABK1', 'AAB0'),
    ('ABK1', 'Man', 'gary', 'Wait a minute... That''s not the guy I wanted!', 'na', 'ABL1', 'AAU1'),
    ('ABL1', 'Man (to Ryan)', 'gary', 'Ryan, does this look like a golden blonde, yellow-clothed 23-year-old to you?! I mean, P1{they''re} dressed in green for Christ''s sake!', 'na', 'ABM1', 'AAB0'),
    ('ABM1', 'Narrator', 'mia', 'The navy-clad man that attacked you earlier, now known as Ryan, then also steps out of the shadowed corner of the room.', 'na', 'ABN1', 'AAB0'),
    ('ABN1', 'Ryan (to the other man)', 'ryan', 'Ugh, it was surprisingly dark, considering it was only 6pm, so I could barely see what P1{they} looked like. Plus, P1{they} were walking through a dark alleyway in the evening. Like, what did P1{they} expect to happen?', 'ABN1', 'ABO1, ABQ1', 'AAB0'),
    ('ABO1', 'Man', 'gary', 'Hey, you''re the P1{person} from earlier, right? The one I gave the fiver to?', 'na', 'ABP1', 'AAC0'),
    ('ABP1', 'Gary', 'gary', 'Listen, my name is Gary. I''m real sorry about this, okay? We were looking for someone else, and Ryan got it wrong.', 'na', 'ABS1', 'AAL1'),
    ('ABQ1', 'Man', 'gary', 'Hey, you''re the dick from earlier, right?', 'na', 'ABR1, ADC1', 'AAC0, AAM1'),
    ('ABR1', 'Gary', 'gary', 'Okay, I''m bored now - Alexa and Siri are better at this. So, uh, would you kindly remove yourself from existence by the most painless way possible?', 'na', 'ADO1', 'ABX1'),
    ('ABS1', 'Gary', 'gary', 'Look, tell us what you''re called first and then we''ll decide what to do with you.', 'na', 'ABT1, ABT9, ABU1, ABV1', 'AAO1, AAP1, AAQ1, AAD0'),
    ('ABT1', 'Gary', 'gary', 'Coolio.', 'ABT1', 'ABX1', 'AAB0'),
    ('ABU1', 'Gary', 'gary', 'Rude, but okay. To be fair, we did kidnap you...', 'ABU1', 'ABX1', 'AAB0'),
    ('ABV1', 'Gary', 'gary', 'I''m sorry?', 'na', 'ABT1, ABW1', 'AAR1, AAS1'),
    ('ABW1', 'Gary', 'gary', 'Fine, "no-name". Be that way.', 'ABW1', 'ABX1', 'AAB0'),
    ('ABX1', 'Ryan (to Gary)', 'ryan', 'So, what do we do with P1{them}? I mean, we can''t just let P1{them} out - P1{they} know too much.', 'none', 'ABY1', 'AAB0'),
    ('ABY1', 'Gary', 'gary', 'I have no idea... But we need to think of something quick. We''re meant to launch the G-bomb in 14 hours, remember? And no doubt that yellow prick will come for us if we postpone it...', 'na', 'ABZ1', 'AAT1'),
    ('ABZ1', 'Ryan', 'ryan', 'This world sucks! What did you expect?! Capitalism is corrupt as hell, so we thought we''d destroy society to rebuild anew.', 'na', 'ACA1', 'AAU1'),
    ('ACA1', 'Narrator', 'mia', 'You start to sweat a little at that revelation, and instantly decide that you need to think of a plan. The question is... do you escape to your death, survive here without freedom, or something else entirely?', 'na', 'ACN1, ACB1, ???0, ACF1', 'AAV1, AAW1, ???0, AAE0'),
    ('ACB1', 'Narrator', 'mia', 'You attempted to attack them, but then you remembered that you were still bound to the chair.', 'na', 'ACC1', 'AAY1'),
    ('ACC1', 'Narrator', 'mia', 'What are you doing?', 'na', 'ACD1', 'AAZ1'),
    ('ACD1', 'Ryan (to Gary)', 'ryan', 'P1{They''re} a danger to us! We need to off P1{them}!', 'na', 'ACE1', 'ABA1'),
    ('ACE1', 'Narrator', 'mia', 'Ryan instantly shot you before you could do anything else. Maybe trying to start a fight with them without a plan (or even a weapon) was a bad idea...', 'na', 'ADS1', 'AAB0'),
    ('ACF1', 'Gary', 'gary', 'What?', 'na', 'ACG1', 'ABB1'),
    ('ACG1', 'Ryan', 'ryan', 'What?!', 'na', 'ACH1', 'ABC1'),
    ('ACH1', 'Narrator', 'mia', 'What?!?', 'na', 'ACI1', 'ABD1'),
    ('ACI1', 'Gary', 'gary', 'Did you seriously just ask what I think you just asked?!', 'na', 'ACJ1', 'AAC0'),
    ('ACJ1', 'Gary', 'gary', 'No it is not a sex dungeon, V{gary_name_version[1]}! What the hell?', 'na', 'ACK1, ACK1', 'ABE1, ABF1'),
    ('ACK1', 'Narrator', 'mia', 'Quick, I need to do something to stop this horror! I don''t want this game to get demonetised!', 'na', 'ACL1', 'AAB0'),
    ('ACL1', 'G{Narrator}', 'mia', 'Oh, right, I know!', 'na', 'ACM1', 'AAB0'),
    ('ACM1', 'Narrator', 'mia', 'You were somehow unlucky enough that some kind of space laser miraculously shot you from the heavens... even though you were underground in a literal bunker, so that shouldn''t be possible... At least the death was swift, but it was far from painless. Maybe it was karma... G{Or maybe it was something more...}', 'na', 'ADT1', 'AAB0'),
    ('ACN1', 'Narrator', 'mia', 'You decide not to do anything for the time being, waiting for them to leave. After a while, a voice you haven''t heard before calls for your kidnappers.', 'na', 'ACO1', 'AAB0'),
    ('ACO1', 'Unknown Voice', 'matt', 'Hey, guys, we have a problem...', 'na', 'ACP1', 'AAB0'),
    ('ACP1', 'Gary', 'gary', 'Fine, we''ll be there in a minute.', 'na', 'ACQ1', 'AAB0'),
    ('ACQ1', 'Ryan', 'ryan', 'Don''t go anywhere.', 'na', 'ACR1', 'AAB0'),
    ('ACR1', 'Narrator', 'mia', 'They leave hastily out of the door to help with whatever the issue was. You''re all alone now, so nothing could stop you from escaping... or doing something else of your choice.', 'na', 'ACS1, ADW1', 'ABK1, ABL1'),
    ('ACS1', 'Narrator', 'mia', 'You decide to stay where you are. A rather boring choice if you ask me...', 'na', 'ACT1', 'AAB0'),
    ('ACT1', 'Narrator', 'mia', 'Eventually, Gary comes back, alone this time.', 'na', 'ACU1', 'AAB0'),
    ('ACU1', 'Gary', 'gary', 'Oh. You actually listened to us and stayed here? Somehow I expected something different... Weird.', 'na', 'ACV1', 'AAB0'),
    ('ACV1', 'Gary', 'gary', 'So, I''ve finally got an idea of what to do with you...', 'ABN1', 'ACW1, ACZ1', 'ABQ1'),
    ('ACW1', 'Narrator', 'mia', 'Gary cuts the ropes you are bound by and gives you a hand, before pulling you to your feet.', 'na', 'ACX1', 'ABM1'),
    ('ACX1', 'Gary', 'gary', 'Yeah. You''re a pretty cool P1{person}, V{gary_name_version[1]}, so we thought that you deserve to be set free. If you want, you can stay here - the rest of the world won''t last much longer anyway.', 'na', 'ADD1, ACY1', 'ABO1, ABP1'),
    ('ACY1', 'Narrator', 'mia', 'By the power of friendship, you somehow emotionally manipulated Gary and friends into letting you stay in their bunker after they nuked the planet, and survive it all. Congratulations because I honestly was going to have no way of beating this game, and just have every single option lead to your demise someway or another... G{just like real life!}', 'na', 'ADA1', 'AAB0'),
    ('ACZ1', 'Narrator', 'mia', 'Gary shoots you without hesitation. Maybe you should have left while you could... or maybe karma from a past choice finally caught up to you...', 'na', 'ADU1', 'AAB0'),
    ('ADA1', 'Narrator', 'mia', 'Except yes, I will be doing that! Just because I think it''ll be so damn hilarious to see the hope fade from your eyes when you realise that yes, there is no good ending here. Hahahahaha!', 'na', 'ADB1', 'ABN1'),
    ('ADB1', 'G{Narrator}', 'mia', 'You before long G{inconveniently for you} catch a mutated strain of COVID-19 somehow and die. The end. =]', 'na', 'ADV1', 'AAB0'),
    ('ADC1', 'Gary', 'gary', 'Listen, my name is Gary. I''d say I''m sorry for the mixup, but I''m actually not.', 'na', 'ABS1', 'AAN1'),
    ('ADD1', 'Narrator', 'mia', 'You decide to make a run for it before Gary can even process what happened. Unfortunately for you, you don''t even know the layout of the bunker you''re in at all, but luckily you find a random storage closet and hide in there.', 'AAX1', 'ADE1', 'AAB0'),
    ('ADE1', 'Narrator', 'mia', 'While looking for supplies, you find a map of the underground building you''re stuck in, and have a look at everywhere shown on it. While you could escape, judging by your past choices, I think I''m qualified to choose for you.', 'na', 'ADF1', 'AAB0'),
    ('ADF1', 'Narrator', 'mia', 'You "decide" to sneak towards where their nuke [aka the G-bomb] is kept, though Gary is still looking for you.', 'na', 'ADG1', 'AAB0'),
    ('ADG1', 'Gary', 'gary', 'V{p1_name}, where are you?! If ya don''t come out and surrender this instant, I''ll shoot you!', 'na', 'ADH1, AEX1', 'ABR1, AAF0'),
    ('ADH1', 'Gary', 'gary', 'Wait, you actually listened again?', 'na', 'ADI1', 'ABT1'),
    ('ADI1', 'Gary', 'gary', 'Hmmm...', 'na', 'ADJ1', 'AAB0'),
    ('ADJ1', 'Gary', 'gary', 'I think I know why you''re being as obedient as a lil'' puppy dog...', 'na', 'ADK1', 'ABU1'),
    ('ADK1', 'Gary', 'gary', 'You''re one of our old experiments, aren''tcha? The one where we put a loyalty chip in your skull to see if it would work.', 'na', 'ADL1', 'ABV1'),
    ('ADL1', 'Gary', 'gary', 'Yeah, it''s definitely you... You were such a fan of green as a child. I guess you just forgot about all this due to trauma or somethin''. Oh well... G{Nice to see it worked!}', 'na', 'ADM1', 'ABN1'),
    ('ADM1', 'Gary', 'gary', 'Do a roll, pretty please.', 'na', 'ADL1', 'ABW1'),
    ('ADN1', 'Gary', 'gary', 'Oh, and run around like a headless chicken.', 'na', 'ABR1', 'ABW1'),
    ('ADO1', 'Narrator', 'mia', 'Oh jeez... I didn''t expect it to get so dark... Um... uh... Ummmmm... So, uh, you somehow escape and um... you DEFINITELY survived that!', 'na', 'ADR1', 'AAB0'),
    ('ADP1', 'Ending', 'gold', 'You got: Death via Idiocy', 'ADP1', 'AAA0', 'AAA0'),
    ('ADQ1', 'Ending', 'gold', 'You got: Death via Idleness', 'ADQ1', 'AAA0', 'AAA0'),
    ('ADR1', 'Ending', 'gold', 'You got: "Alive" via Exploiting PG Requirements', 'ADR1', 'AAA0', 'AAA0'),
    ('ADS1', 'Ending', 'gold', 'You got: Death via Volatility', 'ADS1', 'AAA0', 'AAA0'),
    ('ADT1', 'Ending', 'gold', 'You got: Death via Vulgarity', 'ADT1', 'AAA0', 'AAA0'),
    ('ADU1', 'Ending', 'gold', 'You got: Death via Assholery', 'ADU1', 'AAA0', 'AAA0'),
    ('ADV1', 'Ending', 'gold', 'You got: Death via Unluckiness', 'ADV1', 'AAA0', 'AAA0'),
    ('ADW1', 'Narrator', 'mia', 'You decide to call upon the powers of your non-existent plot armour and deus ex machina to all of a sudden give you the ability to untie the ropes around you and the chair.', 'na', 'ADX1', 'AAB0'),
    ('ADX1', 'Narrator', 'mia', 'After you finish, you realise that you need a well thought out escape plan. Too bad they all suck! Hahahahaha!', 'na', 'ADY1, ???0, AEO1, AFV1', 'ABY1, ???0, ACA1, ACB1'),
    ('ADY1', 'Narrator', 'mia', 'You decide to attempt to bribe one of them.', 'na', 'ADZ1', 'AAB0'),
    ('ADZ1', 'Narrator', 'mia', 'After sneaking around a bit, you find a member of the group of people who you haven''t seen yet.', 'na', 'AEA1', 'AAB0'),
    ('AEA1', 'G{Unknown Person}', 'mikayla', 'Shouldn''t you be in the interrogation room?', 'na', 'AEB1', 'ACC1'),
    ('AEB1', 'G{Unknown Person}', 'mikayla', 'With what?', 'AEB1', 'AEH1, AEC1', 'ACD1'),
    ('AEC1', 'Narrator', 'mia', 'You then quickly realise that you don''t actually have anything of value on your person.', 'na', 'AED1', 'AAU1'),
    ('AED1', 'G{Unknown Person}', 'mikayla', 'Oh, you don''t have anything then? Well, there is something I do want from you...', 'na', 'AEE1', 'ABQ1'),
    ('AEE1', 'G{Unknown Person}', 'mikayla', 'Your corpse.', 'na', 'AEF1', 'ABA1'),
    ('AEF1', 'Narrator', 'mia', 'She shoots you.', 'na', 'AEG1', 'AAB0'),
    ('AEG1', 'Ending', 'gold', 'You got: Death via Worthlessness', 'AEG1', 'AAA0', 'AAA0'),
    ('AEH1', 'Narrator', 'mia', 'You pull out of your pocket the £5 Gary gave you earlier.', 'na', 'AEI1', 'ACE1'),
    ('AEI1', 'G{Unknown Person}', 'mikayla', 'Well, it''s not a lot... but screw it. I''m bored and nobody here actually likes me all that much, so sure, I''ll help you for your measly sum of money.', 'na', 'AEJ1', 'ABP1'),
    ('AEJ1', 'G{Mikayla}', 'mikayla', 'Don''t mention it. Like, seriously, don''t mention it - I''ll be killed if you do. Oh, and my name''s Mikayla by the way.', 'na', 'AEK1', 'ACF1'),
    ('AEK1', 'Narrator', 'mia', 'You give her the £5 and she half-heartedly takes it from your hand, clearly not caring about it much. After, she stands up and you both head towards the door.', 'na', 'AEL1', 'AAB0'),
    ('AEL1', 'Narrator', 'mia', 'However, perhaps it wasn''t the greatest idea abusing capitalism in an anarchist''s den, as every single member of Gary''s group immediately sensed your ill-use of money, and surrounded the door.', 'na', 'AEM1', 'ACG1'),
    ('AEM1', 'Narrator', 'mia', 'They quickly bashed down the door, and since you had nowhere to go, they shot you both immediately for the sinful act you both took part in.', 'na', 'AEN1', 'AAB0'),
    ('AEN1', 'Ending', 'gold', 'You got: Death via Your Ideology', 'AEN1', 'AAA0', 'AAA0'),
    ('AEO1', 'Narrator', 'mia', 'You look for something to dig out of the bunker with.', 'na', 'AEP1', 'AAB0'),
    ('AEP1', 'Narrator', 'mia', 'After some searching, you find the only object you could possibly dig with... a teaspoon.', 'na', 'AEQ1', 'ACH1'),
    ('AEQ1', 'Narrator', 'mia', 'Yeah, yeah, shut up. It''s my game not yours! ...Anyway, you start to dig in a secluded part of the bunker where the lead and concrete surrounding it is conveniently slightly weaker.', 'na', 'AER1', 'AAB0'),
    ('AER1', 'Narrator', 'mia', 'And you keep digging...', 'na', 'AES1', 'AAB0'),
    ('AES1', 'Narrator', 'mia', 'And digging...', 'na', 'AET1', 'AAB0'),
    ('AET1', 'Narrator', 'mia', 'Until you eventually escape to the surface!', 'na', 'AEU1', 'AAB0'),
    ('AEU1', 'Narrator', 'mia', '...Only to realise that the nuclear bomb already exploded... 30 years ago.', 'na', 'AEV1', 'ACI1'),
    ('AEV1', 'Narrator', 'mia', 'Before long, you dies from the radiation outside, since you weren''t equipped with a lead suit.', 'na', 'AEW1', 'AAB0'),
    ('AEW1', 'Ending', 'gold', 'You got: Death via Spooning', 'AEW1', 'AAA0', 'AAA0'),
    ('AEX1', 'Narrator', 'mia', 'Hmmm... You''re in a tricky situation. If you don''t do anything, they''ll find you soon. Welp, here''s the list of plans. Good luck, V{p1_name}! ...G{if that is your name}...', 'na', 'AEY1, AEZ1, AFD1, AGH1', 'ACJ1, ACK1, ACL1, ACM1'),
    ('AEY1', 'Narrator', 'mia', 'You manage to find a nearby vent in the ceiling, so quickly pull an Ikea chair (why do they have this?) under it and jump up into it.', 'na', 'AGT1', 'AAB0'),
    ('AEZ1', 'Narrator', 'mia', 'They quickly locate you. Maybe shouting that for everyone to hear wasn''t such a good idea...', 'na', 'AFA1', 'AAB0'),
    ('AFA1', 'Gary & Friends', 'gary', 'Ah, found you!', 'na', 'AFB1', 'ACN1'),
    ('AFB1', 'Narrator', 'mia', 'They shoot you without hesitation. Oopsies!', 'na', 'AFC1', 'AAB0'),
    ('AFC1', 'Ending', 'gold', 'You got: Death via Taunting', 'AFC1', 'AAA0', 'AAA0'),
    ('AFD1', 'Narrator', 'mia', 'You decide to try digging through the metal walls to the bomb room... using plastic spoons.', 'na', 'AFE1', 'ACO1'),
    ('AFE1', 'Narrator', 'mia', 'Boy, there''s a lotta digging options in this game...', 'na', 'AFF1', 'ACO1'),
    ('AFF1', 'Narrator', 'mia', 'At least I think they are,, I actually don''t remember.', 'na', 'AFG1', 'ACO1'),
    ('AFG1', 'Narrator', 'mia', 'Anyway, you eventually somehow get through the layer of steel and reach the layer of pure lead, since this, of course, is a bomb shelter.', 'na', 'AFH1', 'ACO1'),
    ('AFH1', 'Narrator', 'mia', 'Let''s hope that the pure lead you''re touching doesn''t make you go insane!', 'na', 'AFI1', 'ACO1'),
    ('AFI1', 'Narrator', 'mia', 'Remember, it IS poison...', 'na', 'AFJ1', 'ACO1'),
    ('AFJ1', 'Narrator', 'mia', 'Aaaaand you''re just gonna ignore me...', 'na', 'AFK1', 'ACO1'),
    ('AFK1', 'Narrator', 'mia', 'Can ya stop skipping my dialogue, please? Or if you''re actually reading this garbage, can you please get it through your thick skull!', 'na', 'AFL1', 'ACP1'),
    ('AFL1', 'Narrator', 'mia', 'Oh no, I think the lead got to ya.', 'na', 'AFM1', 'ACQ1'),
    ('AFM1', 'Narrator', 'mia', 'You sound drunk... and like you''ve just used 450 plastic spoons on a steel and lead wall.', 'na', 'AFN1', 'ACR1'),
    ('AFN1', 'Narrator', 'mia', 'Um...', 'AFM1', 'AFN1', 'ACS1'),
    ('AFO1', 'Silly Voice (to herself)', 'mia', 'Don''t get mad... Don''t get mad...', 'AFN1', 'AFS1', 'ACT1'),
    ('AFP1', 'Scary Voice', 'mia', 'Because that''s not something you should know yet! You know, I thought it''d be funny watching you suffer from lead poisoning, G{but it''s just making me annoyed}! This isn''t a daycare!', 'AFN1', 'AFQ1', 'ACU1'),
    ('AFQ1', 'G{Demonic Voice}', 'mia', 'You were swifly killed by m- by lead poisoning.', 'na', 'AFR1', 'AAB0'),
    ('AFR1', 'Ending', 'gold', 'You got: Death via Lead Poisoning', 'AFR1', 'AAA0', 'AAA0'),
    ('AFS1', 'Exasperated Voice', 'mia', 'You''re hallucinating, V{p1_name}. It''s all in your head.', 'AFM1', 'AFT1', 'ACV1'),
    ('AFT1', 'Slightly Deranged Voice', 'mia', 'No it doesn''t! I''m more real than even you because- I''m not even gonna tell you why.', 'AFN1', 'AFP1', 'AAG0'),
    ('AFU1', 'Narrator', 'mia', 'After you finish eating, you get yourself dressed and ready for the day... despite the fact that you have nothing to get ready for.', 'na', 'AAJ1', 'AAB0'),
    ('AFV1', 'Narrator', 'mia', 'No, you can''t just open your last save file, this definitely isn''t a video game, and we''re not going to start ripping off The Matrix.', 'AFM1', 'AFW1', 'ACW1'),
    ('AFW1', 'Narrator', 'mia', 'Oh, you''ve done it now, you little-!', 'AFN1', 'AFX1', 'ACX1'),
    ('AFX1', 'Narrator', 'mia', 'Your destiny...', 'AFM1', 'AFY1', 'ABB1'),
    ('AFY1', 'Narrator', 'mia', 'You''re living in a simulation. Nothing is real,, reality is a lie. This is a log of every time one of your parallel persons have... expired.', 'na', 'AFZ1', 'ACY1'),
    ('AFZ1', 'Narrator', 'mia', 'You have two choices. Take the green pill or the yellow pill.', 'AFN1', 'AGA1, AGC1, AGE1', 'ACZ1, ADA1, ADB1'),
    ('AGA1', 'Narrator', 'mia', 'As soon as you swallow it, you instantly die. Probably not the best idea to take drugs from strangers...', 'na', 'AGB1', 'AAB0'),
    ('AGB1', 'Ending', 'gold', 'You got: Death via The Matrix (green)', 'AGB1', 'AAA0', 'AAA0'),
    ('AGC1', 'Narrator', 'mia', 'As soon as you swallow it, you instantly die. Probably not the best idea to take drugs from strangers...', 'na', 'AGD1', 'AAB0'),
    ('AGD1', 'Ending', 'gold', 'You got: Death via The Matrix (yellow)', 'AGD1', 'AAA0', 'AAA0'),
    ('AGE1', 'Narrator', 'mia', 'We''re ripping off The Matrix now, but I can''t copy it exactly or I''ll get copyright struck, so they''re yellow and green. Both pills have the "power" to increase the counter of one of these lists by one, G{and you''re going to take at least one of them.}"', 'na', 'AGF1', 'ADC1'),
    ('AGF1', 'Narrator', 'mia', '10 pills are forced into your mouth and you instantly die.', 'na', 'AGG1', 'AAB0'),
    ('AGG1', 'Ending', 'gold', 'You got: Death via Drug Overdose', 'AGG1', 'AAA0', 'AAA0'),
    ('AGH1', 'Narrator', 'mia', 'You stupidly decide that, even though you''re currebtly, you''d like to take drugs and drink poison.', 'na', 'AGI1', 'AAB0'),
    ('AGI1', 'Narrator', 'mia', 'I swear, I''m rooting for the "bad guys" at this point!', 'na', 'AGJ1', 'AAB0'),
    ('AGJ1', 'Narrator', 'mia', 'Anyway, you pick up the sussy white powder and snort it, before drinking bleach like it''s alcohol.', 'na', 'AGK1', 'ADD1'),
    ('AGK1', 'Narrator', 'mia', 'Of course you do, you idiot! You just drank hydrogen peroxide! Anyway, whatever, I''ll continue...', 'na', 'AGL1', 'AAB0'),
    ('AGL1', 'Narry Tory', 'mia', 'You after a few minutes realise that you got superpowers from drinking that, the chemicals having mutated you into gaining telekinesis.', 'na', 'AGM1', 'ADE1'),
    ('AGM1', 'Narry Tory', 'mia', 'You start making the objects around the room float,but that noise causes Gary and 3 other members of his gang to find you. They quickly break down the door and point a gun at you.', 'na', 'AGN1, AGN9', 'ADF1, ADG1'),
    ('AGN1', 'Narry Tory', 'mia', 'It doesn''t work and they look confused at you for some reason. Maybe you didn''t activate your powers right?', 'na', 'AGO1', 'AAB0'),
    ('AGO1', 'Unknown Voice', 'darren', 'Hello? What''s up with you???', 'na', 'AGP1', 'ADH1'),
    ('AGP1', 'Narry Tory', 'mia', 'They just look at you like they can''t understand what you''re saying. But you are talking perfectly clear, right?', 'na', 'AGQ1', 'AAB0'),
    ('AGQ1', 'Narrator', 'mia', 'You start to feel sick and your vision blurs, before you out of nowhere fall to the ground. You, obviously, died of the bleach and other washing products before anyone could even think of shooting you. I told you to do something a few minutes ago to try and flush out your system, but you weren''t responding to me!', 'na', 'AGR1', 'ADI1'),
    ('AGR1', 'Narrator', 'mia', 'Either way, you die a very, very stupid death.', 'na', 'AGS1', 'AAB0'),
    ('AGS1', 'Ending', 'gold', 'You got: Death via Not Keeping Away from Children', 'AGS1', 'AAA0', 'AAA0'),
    ('AGT1', 'Narrator', 'mia', 'It''s a little dark and cramped, but you thankfully manage to fit. Around 10 seconds later, you hear tthe sound of voices coming from the room you were just in.', 'na', 'AGU1', 'AAB0'),
    ('AGU1', 'Gary', 'gary', 'Darn it, Ryan. They escape.', 'na', 'AGV1', 'AAB0'),
    ('AGV1', 'Ryan?', 'ryan', 'Damn it, I knew you shouldn''t have let them out!', 'na', 'AGW1', 'AAB0'),
    ('AGW1', 'Gary', 'gary', 'Yeah, well whatever. Maybe in another timeline they could''ve joined us and we''d be buddies.', 'na', 'AGX1', 'AAB0'),
    ('AGX1', 'Ryan', 'ryan', 'Well this isn''t that timeline. This is this one...', 'na', 'AGY1', 'AAB0'),
    ('AGY1', 'Narrator', 'mia', 'You decide that it''s probably best for you to crawl away through the vent before they think to look up and find you...', 'na', 'AGZ1, AHC1', 'ABS1, AAF0'),
    ('AGZ1', 'Narrator', 'mia', 'You crawl away for a while, before eventually part of the vent below you breaks, causing you to fall into some kind of room with many bunk beds.', 'na', 'AHA1', 'AAB0'),
    ('AHA1', 'Narrator', 'mia', 'As you look up, a bit dazed from the fall, you feeel a gun being held against your head and look up to see a girl around the same age as you holding it.', 'na', 'AHB1', 'AAB0'),
    ('AHB1', 'Unknown Girl', 'mikayla', 'Give me one reason why I shouldn''t kill you.', 'AEB1', '???0, ???0', '???0'),
    ('AHC1', 'Narrator', 'mia', 'Seriously?!', 'na', 'AHD1', 'AAB0'),
    ('AHD1', 'Unknown Person', 'darren', 'So... whatcha guys talking about?', 'na', 'AHE1', 'AAB0'),
    ('AHE1', 'Gary', 'gary', 'The one who we kidnapped, V{gary_name_version[0]}, escaped. We don''t know where P1{they} went, Darren.', 'na', 'AHF1', 'AAB0'),
    ('AHF1', 'Darren?', 'darren', 'Well first of all, I think we should stop acting like every cliche video game enemy and look up.', 'na', 'AHG1', 'AAU1'),
    ('AHG1', 'Narrator', 'mia', 'Gary immediately looks up and sees the vent.', 'na', 'AHH1', 'ADK1'),
    ('AHH1', 'Gary', 'gary', 'How are we even gonna get P1{them} from up there? Maybe Matt can do it, since he''s the youngest of us?', 'na', 'AHI1', 'AAB0'),
    ('AHI1', 'Darren', 'darren', 'No way I''m letting him do that. Who actually cares about getting P1{them} really, anyway?', 'na', 'AHJ1', 'AAB0'),
    ('AHJ1', 'Narrator', 'mia', 'Oh no...', 'na', 'AHK1', 'AAB0'),
    ('AHK1', 'Ryan', 'ryan', 'I guess yeah. I mean, we could still bomb everyone and just keep our guns on us if P1{they} try to stop us. Problem solved.', 'na', 'AHL1', 'AAB0'),
    ('AHL1', 'Narrator', 'mia', 'Oh nonono...', 'na', 'AHM1', 'AAB0'),
    ('AHM1', 'Gary', 'gary', 'Right, let''s do that right now!', 'na', 'AHN1', 'AAB0'),
    ('AHN1', 'Narrator', 'mia', 'Gary grabs a walkie talkie from his pocket and starts speaking through it.', 'na', 'AHO1', 'AAB0'),
    ('AHO1', 'Gary (To Walkie Talkie)', 'gary', 'Oi, Matt! Once the yellow scumbag''s dealt with, set the bomb off pronto!', 'na', 'AHP1', 'AAB0'),
    ('AHP1', 'Matt (From Walkie Talkie)', 'matt', 'Got it!', 'na', 'AHQ1', 'AAB0'),
    ('AHQ1', 'Narrator', 'mia', 'Okay, okay, listen. I am G{very} mad at you right now, but that can wait for another time. First, get my NPCs back on track! G{...I fear they may be gaining sentience.}', 'na', 'AHR1', 'ADL1'),
    ('AHR1', 'Narrator', 'mia', 'Just hurry up and do it already!', 'na', 'AHS1', 'ADM1'),
    ('AHS1', 'Narrator', 'mia', 'You crawl through the vent for aw while, before eventually part of it below you breaks, causing you to fall into some kind of room with many bunk beds.', 'na', 'AHT1', 'AAB0'),
    ('AHT1', 'Narrator', 'mia', 'As you look up, a bit dazed from the fall, you feel a gun being held against your head and look up to see a girl- No time!', 'na', 'AHU1', 'ADN1'),
    ('AHU1', 'Narrator', 'mia', 'The girl conveniently gets a heart attack from, I don''t know, diabetes or something before she could even say a word.', 'na', 'AHV1', 'AAB0'),
    ('AHV1', 'Narrator', 'mia', 'You then run for it to the bomb room, before being pulled aside to a dark wallway by a hooded blonde man.', 'na', '???0', '???0');

-- Extra Notes:
-- Make any choice codes use a 9 if it's a duplicate
-- Choice Template --> ('AHA1', 'Narrator', 'mia', '', 'na', 'AHB1', 'AAB0'),
-- Endings Choice Template --> ('AHA1', 'Ending', 'gold', 'You got: Death via ', 'AHA1', 'AAA0', 'AAA0'),
-- To output the table in a nice way --> SELECT Choices.code, Choices.name, Choices.speech, Choices.choice_codes, Buttons.code, Buttons.display_text FROM Choices, Buttons WHERE Choices.button_codes LIKE CONCAT('%', Buttons.code, '%')

-- Unfinished Routes:
-- Line 57: ???0 --> AAX1
-- Line 106: ???0 --> ABZ1
-- Line 188: ???0 --> ADJ1
-- Line 208: ???0 --> ADO1