# Initializing my unfilled story as a string
unfilled_Story_String = "‘%v to?' said %n. 'Of course you've got %n! But not because of the %a %n! Because you, yourself, will %v %av until you've %v! We both know %a %n! %v, please, just for a %n, that you had %v %av that %n! How would you %v about %n now? %v!'"

# Initializing my unfilled_Story_String split into a list
unfilled_Story_List = unfilled_Story_String.split(' ')

# Initializing my filledStoryList as an empty list to fill in afterwards
filledStoryList = []

# Initializing specificPartsOfSpeechReference containing 
# the specific parts of speech that correspong to my story
specific_Parts_Of_Speech_Dictionary = {"%v": "verb", "%n": "noun", "%a": "adjective", "%av": "adverb"}

def fills_story_list_given_input(segment, specific_Part_Of_Speech):
    initial_index_of_specific_part_of_speech = segment.find(specific_Part_Of_Speech)
    final_index_of_specific_part_of_speech = initial_index_of_specific_part_of_speech + len(specific_Part_Of_Speech)
    users_Substitution = input("Enter a " + specific_Parts_Of_Speech_Dictionary[specific_Part_Of_Speech])
    user_modified_segment = segment[0:initial_index_of_specific_part_of_speech] + users_Substitution + segment[final_index_of_specific_part_of_speech: len(segment)]
    filledStoryList.append(user_modified_segment)
    
def contains_Specific_Parts_Of_Speech(segment):
    for specific_Part_Of_Speech in specific_Parts_Of_Speech_Dictionary:
        if specific_Part_Of_Speech in segment:
            fills_story_list_given_input(segment, specific_Part_Of_Speech)
            return
    filledStoryList.append(segment)

for segment in unfilled_Story_List:
    contains_Specific_Parts_Of_Speech(segment)

for story_segment in filledStoryList:
    print(story_segment)





