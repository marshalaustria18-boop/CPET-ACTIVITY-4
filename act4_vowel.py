# Name: Maderazo, Marshal Reign A.
# Section: BAET 2102

sentence = input("Sentence: ")

vowels = "aeiouAEIOU"
count = 0

for character in sentence:
    if character in vowels:
        count += 1

print(f"Vowels: {count}")