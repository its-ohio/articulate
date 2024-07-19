import pandas as pd

actions = pd.read_csv("data/actions.csv")
nature = pd.read_csv("data/nature.csv")
objects = pd.read_csv("data/objects.csv")
people = pd.read_csv("data/people.csv")
random = pd.read_csv("data/random.csv")
spade = pd.read_csv("data/spade.csv")
world = pd.read_csv("data/world.csv")

result = pd.concat([actions, nature, objects, people, random, spade, world], axis=1, join='inner')
# l = result["nature"].to_list()
print(result.keys())
# result.to_csv("words.csv", index=False)
