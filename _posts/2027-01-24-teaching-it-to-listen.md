---
date: 2027-01-24 10:00:00
title: "Teaching the app to listen"
categories: [building-with-ai]
---
This is the newest part of the story, and it isn't finished. It's also the part that failed first.

**The listener, in September**

When the history picks up on September 3, the app could already listen, using a free bird-sound model from Google that runs right on the phone.

First I got nothing. "I have been trying to use the bird listening app on my phone while I've been walking," I told Claude. "It's working, but I'm not getting any identification." It turned out the app stopped listening the moment my screen locked. A phone in your pocket on a walk is locked the whole walk.

Next I tried it in my yard, with my son, two puppies and a road nearby. My bar was simple: "If it's not going to work for most of us, I don't think it's worth shipping." Even after Claude reworked it, it caught 57% of birds within a minute, and that was in clean conditions.

Another morning it found a mourning dove and a cardinal, and printed them off the bottom of the screen. I saw nothing and decided it was broken. "I didn't scroll far enough," I said later.

Then a construction site half a mile away made the app say it was too noisy, while Merlin, Cornell's bird app, picked up birds right away on the same morning. Claude's note: "Merlin was right." The app was hearing the rumble, not the birds.

At night I tried the insects. "I have no idea what's making these noises. That's why I would love this to work... I do know it is possible, because Cornell's Merlin makes it work." It turned out the app had never asked the model about a single insect.

**Cutting it**

On September 18, on a dog walk, I compared our sample songs with real ones and made the call: "I love the idea, but it just isn't panning out to what I wanted, so I don't think it's worth keeping."

Out it came, with the sample recordings and the made-up songs: 140 MB of extra files, down to 4.3 MB.

**Sounds on the cards**

The cards still needed sounds. In October, Claude wrote a small recipe for each species' song from two written descriptions, and the phone plays it: 898 birds, frogs and insects. The first ones sounded like dial tones, so Claude added a little waver and echo.

Then real recordings. I picked one clip each for ten birds I hear on my walks. Claude found clean recordings for hundreds more using my rule: good quality, no other birds in the background, trimmed to about eight seconds. Then frogs and singing insects. About 500 cards now have a real recording, each one crediting the person who recorded it. I asked for the play button right under "I saw one," so it's easy to check that the bird in front of you is the one on the card.

**Trying again**

On November 8 I asked, "In the meantime, do you want to start with the sound ID?" This time is different. It uses a newer, much smaller version of Google's model. Our own final layer weighs where you are and the month. And it has a different job: record a clip, get a top five, play each card's recording to compare, then confirm. It only ships if it works on recordings from my own noisy yard.

The first test covered 55 backyard birds. Using recordings people have shared on iNaturalist, not my yard, the right bird came first about 85% of the time, combining Google's answer with ours. The hardest for our own layer were the Yellow Warbler at 53% and the Mourning Dove at 55%, the same bird the first listener got right. Claude asked me for 15 to 30 second voice memos from the yard, with a note of the birds I'm sure are in each one.

My design for the screen: an ear button next to the camera, the finder's usual questions if you can see the animal, and a play button on every result to compare. The next round covers 906 species. It's still running.

**The little bugs from walks**

Most of what I find these days is small:

- Two soccer games I moved to our Sports calendar stayed in Fun.
- I couldn't tap a weather alert banner.
- A search result left the keyboard covering the event I'd just opened.

Each one gets a sentence from me, a fix from Claude, and a line on my list of things to try next time I'm home. That's really what building with AI looks like for me: a short walk, a few honest notes, and a lot of work done while I'm away from the Mac.

Thanks for reading along this far.
