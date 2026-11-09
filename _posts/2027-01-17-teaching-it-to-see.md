---
date: 2027-01-17 10:00:00
title: "Teaching the app to see"
categories: [building-with-ai]
---
Answering twenty questions works, but it's a lot of tapping. The next step was a photo: point your phone at a plant and let the app take the first guess. We started on October 31.

**A few ways to do it**

Claude laid out the options. Apple's own photo lookup can identify plants, but it can't hand the name to another app. We could use a service in the cloud, or a free model somebody else had trained, after checking its license. Or we could train our own on photos we're allowed to use. I wanted to do it "without buying anything," so we trained our own.

The idea, in plain words: you show a computer thousands of photos with the right name on each one. It learns the look of a maple leaf. Then you test it on photos it has never seen and count how often its first guess is right.

The photos come from GBIF and iNaturalist, where people share their sightings. Daily Brief is a paid app, so we only use photos whose owners allow that, and we keep a credit for every photographer.

**The first tries**

The first test used 216 garden plants. Its first guess was right 49% of the time. The worst mix-ups had a good excuse: beets and Swiss chard are the same species, and so are zucchini and pumpkins. And about a third of the photos turned out to be herbarium sheets, pressed, dried plants on museum paper. Claude dropped those and merged the look-alike crops, and it went up to 57%.

Then we added the wild plants, 1,190 in all, and it fell back to 48%. So we got more photos, about 300 per plant, 339,305 in all, and it climbed back to 57%. Claude built its own final layer for the model and it reached 64%, then 66.4%.

That version was twice the size of the one before, so I asked, "So we doubled the size for a 1% gain?" Claude stored the numbers more compactly. Same answers, half the size.

**Where and when**

One big jump didn't come from the photos at all. It came from where and when the photo was taken. A plant that's common in your state this month is more likely than one that has never been recorded near you. Weighing the guesses that way took the first guess from 66.9% to 76.1%.

The app also learned to say "Not sure from this photo" when its best guess is under 35%, instead of pretending.

**My yellow mums**

Remember the mums from an earlier post? My yellow mums came back "Garden Mum, 77%," which was right, but drawn pink. Now the app looks at the colors in the middle of your photo and draws its guess in that color.

I also asked to take photos right in the app. After taking car photos in an insurance app that shows an outline to line up, I asked for that here too. Now you pick a flower, a leaf, the whole plant or bark, and the camera shows an outline to fill.

**Birds, then everything**

Birds were harder. With 543 birds, the first model got 47.3% right, and 55.7% with where and when. Claude found a better free photo reader, released by Meta, that reads the picture before our part of the model makes the call. Birds jumped to 74.5%.

I asked, "Can we do it with all of the photo identifiers?" So now there's one model for everything: plants, birds, mammals, reptiles, frogs, bugs, mushrooms, even mosses and lichens, 4,878 names in all. It's 95 MB, so it downloads on Wi-Fi after you first open the app, and you can remove it in Settings.

I tested it on my own photos. Gray squirrels: 97%. A green iguana: 85%. Some things were outside what it knows, like a Japanese sika deer and domestic ducks. Show it a dog and it says, "That looks like a dog. A pet, not wildlife." A photo of a person says so, too.

The photo doesn't replace the questions. It starts them. The photo's guesses become the starting list, the questions narrow it, and once one answer is 90% likely, the app shows it.

**Still learning**

It isn't done. My neighbor's weeping cherry came back as "sweet cherry, 45%," because the model had never seen a weeping tree. For now, a photo of a tree also offers its weeping garden forms, which works for 16 of the 24 weepers. The new trees from last time are being added to the photo model itself next.

What I learned: the AI part was only half the work. The other half was licenses, file sizes, where the photos came from, and me in the yard taking pictures.

Next time: teaching the app to listen.
