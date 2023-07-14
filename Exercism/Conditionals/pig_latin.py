def translate(text):
    PIG_SOUND = "ay"
    VOVELS = ('a', 'e', 'i', 'o', 'u')
    SPECIAL_V = ('xr', 'yt')
    
    pig_latin_words = []
    
    for word in text.lower().split():
        if word[0] not in VOVELS and word[:2] not in SPECIAL_V: 
            for index in range(1,len(word)):
                if word[index] in VOVELS + tuple('y'):
                    break
            if word[index] == 'u' and word[index - 1] == "q":
                temp = word[index+1:] + word[:index+1] + PIG_SOUND 
            else:
                temp = word[index:] + word[:index] + PIG_SOUND
            pig_latin_words.append(temp)
        else:
            temp = word + PIG_SOUND
            pig_latin_words.append(temp)
    return " ".join(pig_latin_words)
