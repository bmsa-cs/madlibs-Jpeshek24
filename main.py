"""
MadLibs
Author: Jasper Peshek
Period/Core: 7


"""

name_1 = input("Enter a name: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
adjective_1 = input("Enter an adjective: ")
noun_1 = input("Enter a noun: ")
pronoun = input("Enter a pronoun: ")
name_2 = input("Enter a different name: ")
adjective_2 = input("Enter an adjective: ")
noun_2 = input("Enter an noun: ")

print('{} '.format(name_1), "has always wanted to go to", place, ".")
print(pronoun, "wants to go there to", verb, adverb + ".")
print(name_1, "is a", adjective_1, noun_1, ", and", pronoun, "does what\n" + pronoun, "likes.")
print(name_2, "does not want to go to", place, ".")
print("That is why", name_2, adjective_2, noun_2)
