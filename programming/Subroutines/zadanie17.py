def letter_count(string, letter):
    count = 0
    string = "You never get a second chance to make a first impression"
    for char in string:
        if char == letter:
            count += 1
    return count
string = "You never get a second chance to make a first impression"
print(letter_count(string, "e"))
    
    