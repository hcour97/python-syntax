words = ["elephant", "potato", "everyone", "garden", "dog", "echo", "canoe", "shoe"]

def print_upper_words(words):
    """capitalizes all words in a list"""
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """prints words, uppercase, one line each, that start with e or E"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """prints words, uppercase, one line each, that start with one of the given letters"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


#print_upper_words(["hello", "banana", "tomato"])
#print_upper_words(words)

print_upper_words2(["hello", "banana", "tomato"])
print_upper_words2(words)

print_upper_words3(words, {"g", "y"})



