madlibs_templates = [
    {
        "story": "Today, I went to the {place}. I saw a {adjective} {animal} jumping up and down. "
                 "It was very {emotion}. Then, I bought a {object} and went home happily.",
        "words": ["place", "adjective", "animal", "emotion", "object"]
    },
    {
        "story": "Once upon a time, in a {adjective} kingdom, there lived a {occupation}. "
                 "One day, a {creature} appeared and {verb} everyone. But a brave {hero} saved the day!",
        "words": ["adjective", "occupation", "creature", "verb", "hero"]
    },
    {
        "story": "On my way to {place}, I found a {adjective} {object} lying on the ground. "
                 "Suddenly, it started {verb} and transformed into a {animal}. What a {emotion} experience!",
        "words": ["place", "adjective", "object", "verb", "animal", "emotion"]
    }
]

import random
def generate_madlib():
  template = random.choice(madlibs_templates)
  user_inputs = {}

  print("Fill in the blanks with the requested words.")
  for word in template["words"]:
    user_inputs[word] = input(f"Enter a {word}: ").strip()

  completed_story = template["story"].format(**user_inputs)
  return completed_story


def save_story(story):
  filename = input("Enter a filename to save the story: ")
  #encoding="utf-8 "Ensures the file supports special characters (e.g., ä, é, ñ, ü, ☺).
  with open(filename,"a",encoding="utf-8") as file:
    file.write(story + "\n\n")
  print(f"Story Save To {filename}")

def main():
  print("Welcome to Madlibs Game!")
  while True:
    story = generate_madlib()

    print("Here is your madlib story:\n")
    print(story)

    save = input("Do you want to save this story? (yes/no): ").strip().lower()
    if save == "yes":
      save_story(story)
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
      print("Thanks for playing! 🎉")
      break


if __name__ == "__main__":
    main()

# cli
# Welcome to Madlibs Game!
# Fill in the blanks with the requested words.
# Enter a place: Karachi
# Enter a adjective: Beautiful
# Enter a animal: Cow
# Enter a emotion: Sad
# Enter a object: Bucket
# Here is your madlib story:

# Today, I went to the Karachi. I saw a Beautiful Cow jumping up and down. It was very Sad. Then, I bought a Bucket and went home happily.
# Do you want to save this story? (yes/no): yes
# Enter a filename to save the story: MyStory
# Story Save To MyStory

# Do you want to play again? (yes/no): no
# Thanks for playing! 🎉


