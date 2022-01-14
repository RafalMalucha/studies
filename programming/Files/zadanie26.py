import re

sentence = "To be, or not to be, that is the question"

words = re.findall("\w+", sentence)

print(f"Threre are {len(words)} in this sentence")
