unfilledStoryString = "‘%v to?' said %n. 'Of course you've got %n! But not because of the %a %n! Because you, yourself, will %v %av until you've %v! We both know %a %n! %v, please, just for a %n, that you had %v %av that %n! How would you %v about %n now? %v!'"
unfilledStoryList = unfilledStoryString.split(' ')
filledStoryList = []

specificPartsOfSpeechReference = {"%v": "verb", "%n": "noun", "%a": "adjective", "%av": "adverb"}

def containsSpecificPartsOfSpeech(word):
    for specificPartOfSpeech in specificPartsOfSpeechReference:
        if specificPartOfSpeech in word:
            print (word, "Yes")
            return
    print (word, "No")

for word in unfilledStoryList:
    containsSpecificPartsOfSpeech(word)



