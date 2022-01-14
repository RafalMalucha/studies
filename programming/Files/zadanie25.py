import re

sentence = "To be, or not to be, that is the question"

vowels = re.findall("\a|i|e|o|u|y", sentence)

vowels_count = len(vowels) + 1

print(f"There are {vowels_count} vowels in this sentence")