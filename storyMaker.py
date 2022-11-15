import random

when = ["Once upon a time", "A very long time ago", "One dark and stormy night", "One beautiful morning", "This is a story of"]
who = ["a horse", "a dog", "an unknown man", "a dragon", "a duck", "a cat", "a lion", "a stranger"]
name = ["Lucida", "Michael", "Tom", "Robin", "Bob", "George", "James", "Ramanand"]
went = ["cinema hall", "cave", "forest", "hospital", "school"]
happened = ["made many friends.", "fell down.", "started dancing.", "was playing alone."]

story = random.choice(when) + ', ' + random.choice(who) + " named " + random.choice(name) + " went to a " + random.choice(went) + " and " + random.choice(happened)

print(story)