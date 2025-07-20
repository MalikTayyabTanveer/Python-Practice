"""Take a word from user. Display: length, first character, last character, uppercase version,
lowercase version, and check if it contains the letter 'a'."""

sentence = input("enter your sentence: ")
print(f"lenght of the string is {len(sentence)}")
print(f"the first character of the string is {sentence[0]}")
print(f"the last character of the string is {sentence[-1]}")
print(f"the upper version of the sentence is {sentence.upper()}")
print(f"the lower version of the sentence is {sentence.lower()}")
if "a" in sentence:
    print(f"the 'a' in the sentence occures {sentence.count('a')} times")
else:
    print("there is no 'a' in the strig")