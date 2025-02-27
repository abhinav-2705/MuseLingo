# JUST A BASIC PROJECT , STILL TRYING TO BUILD IT BIGGER!

# Example Usage of MuseLingo

from muse_lingo import MuseLingo

# Create a new MuseLingo instance
muse = MuseLingo()

# Generate a haiku in Japanese about nature with a sense of wonder
print("Japanese Haiku about Nature with Wonder:")
print("=======================================")
japanese_haiku = muse.generate_poem("japanese", "nature", "wonder", "haiku")
for line in japanese_haiku:
    print(line)
print()

# Generate a free verse in Spanish about love with longing emotion
print("Spanish Free Verse about Love with Longing:")
print("=========================================")
spanish_poem = muse.generate_poem("spanish", "love", "longing", "free_verse", lines=5)
for line in spanish_poem:
    print(line)
print()

# Generate a poem in English and translate it to French
print("English Poem about Freedom with Serenity (with French translation):")
print("==============================================================")
translator = muse.build_translator("english", "french")
english_poem = muse.generate_poem("english", "freedom", "serenity", "quatrain", translator=translator)
for i, line in enumerate(english_poem):
    parts = line.split(" | ")
    if len(parts) > 1:
        print(f"EN: {parts[0]}")
        print(f"FR: {parts[1]}")
    else:
        print(line)
print()

# Add new vocabulary to a language
muse.add_vocabulary("arabic", "hope", ["مستقبل", "إيمان", "تفاؤل"])
print("Arabic Tanka about Hope with Joy (with new vocabulary):")
print("==================================================")
arabic_poem = muse.generate_poem("arabic", "hope", "joy", "tanka")
for line in arabic_poem:
    print(line)

# Save the updated language data
muse.save_language_data()
