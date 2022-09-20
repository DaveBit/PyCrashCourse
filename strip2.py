
favorite_language = "python  "
print(favorite_language)
print(len(favorite_language))

favorite_language2 = favorite_language.rstrip()  # rstrip needs to be stored to save the changes.
print(len(favorite_language2))

# rstrip and lstrip eliminate whitespaces from the right
favorite_language3 = " Python "
print(len(favorite_language3))

# lstrip to eliminate form the left. You can use also rstrip on the same line.
favorite_language4 = favorite_language3.lstrip().rstrip()
print(len(favorite_language4))

favorite_language5 = favorite_language3.strip()
print(len(favorite_language5))
