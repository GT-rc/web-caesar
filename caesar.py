def alphabet_position(letter):
    '''This function should find the index position 0-26 of the character in the alphabet.'''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    temp = letter.lower()
    idx = alpha.index(temp)
    return idx

def rotate_character(char, rot):
    '''This function should rotate the given character to the right by the amount given for rotation.'''
    punct = ['!','@','#','$','%','^','&','*','(',')','~','-','_','=','+','/',',','.','?'," ",'"', "'", ">", "<"]
    nums = ['0','1','2','3','4','5','6','7','8','9']
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if char in punct or char in nums:
        return char
    if char.isupper():
        temp = char.lower()
        idx = alphabet_position(temp)
        newidx = idx + rot
        new = newidx % 26
        #print (new, newidx, idx, rot)
        final = alpha[new].upper()
    elif char.islower():
        idx = alphabet_position(char)
        newidx = idx + rot
        new = newidx % 26
        #print (new, newidx, idx, rot)
        final = alpha[new]
    #print(final)
    return final

def encrypt(text, rot):
    '''This function should implement the Caesar cypher.'''
    new_text = ''
    for char in text:
        temp = rotate_character(char, rot)
        new_text = new_text + temp
    return new_text
