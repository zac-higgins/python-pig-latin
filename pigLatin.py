'''
The pig latin rules can be found here: https://en.wikipedia.org/wiki/Pig_Latin
'''

def pigLatinator(string):
    vowels = ["a", "e", "i", "o", "u"]
    lowercase_string = string.lower()
    if lowercase_string[0] in vowels:
        return string + "yay"
    if lowercase_string[:2] == "ho":
        return string + "yay"
    if lowercase_string[0] and lowercase_string[1] not in vowels:
        return string[2:] + string[:2] + "ay"
    else:
        return string[1:] + string[0] + "ay"

def pigLatinTest(arr):
    for word in arr:
        print(f"{word} --> {pigLatinator(word)}")

#--------Vowels-------------#
vowels = ["eat", "omlet", "are", "egg", "explain", "always", "ends", "honest", "I"]
print("#--------Vowels-------------#")
pigLatinTest(vowels)

#-------Consonants--------#
consonants = ["pig", "latin", "banana", "will", "butler", "happy", "duck", "me", "yellow"]
print("#--------Consonants-------------#")
pigLatinTest(consonants)

#------Consonant Clusters------#
consonant_clusters = ["smile", "string", "stupid", "glove", "trash", "floor", "store"]
print("#--------Consonant Clusters-------------#")
pigLatinTest(consonant_clusters)