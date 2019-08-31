# importing modules for color terminal output
import sys
from termcolor import colored, cprint

# Splitting story into a list
unfilled_Story_String = "‘%ingv people?' said %na. 'Of course you find this interesting! But not because of the %a %n! Because you, yourself, will be %ingv %av until you burn out! We both know who you really are! Please %Pv %av, just for once! %na would really like it! You've %pv before. Could you %Pv for me instead? Then I'll give you a %n."
unfilled_Story_List = unfilled_Story_String.split(' ')

# Dictionary used to identify when input should be realized
Part_of_speech_User_prompt_Dictionary = {"%ingv": "a verb ending with -ing","%pv":"a past tense verb", "%Pv": "a present verb",
                                "%na":"a name", "%n": "a single noun", "%av": "an adverb", "%a": "an adjective"}

# Dictionary used to print the color key table
Part_of_speech_Color_Dictionary = {"%ingv": "red","%pv": "blue", "%Pv": "green", "%na":"cyan", 
                                "%n": "yellow", "%av": "magenta", "%a": "grey"}

filled_story_list = []

# Checks to see if the user input ends with -ing when applicable
def ends_with_ing(part_of_speech, user_input):
    if "ing" in part_of_speech:
        if "ing" in user_input:
            return True
        else:
            return False
    else:
        return True
    
    # Returns the user's input after satisfying the test cases
def get_user_input(part_Of_Speech):
    user_input = input("Enter " + Part_of_speech_User_prompt_Dictionary[part_Of_Speech] + ": ")
    #While conditional established by checking for letter input and verb ending with -ing when applicable 
    while (not user_input.isalpha() or not ends_with_ing(part_Of_Speech, user_input)):
        print("Let's try this again!", end = " ")
        user_input = input("Enter " + Part_of_speech_User_prompt_Dictionary[part_Of_Speech] + ": ")
    return colored(user_input, Part_of_speech_Color_Dictionary[part_Of_Speech])

# Returns the text segment before the part_of_speech
def get_segment_prefix(segment, part_of_speech):
    return segment[0:segment.find(part_of_speech)]

# Returns the text segment after the part_of_speech
def get_segment_suffix(segment, part_of_speech):
     return segment[segment.find(part_of_speech) + len(part_of_speech): len(segment)]

# Returns the story segment including user input
def append_segment_including_user_modification(segment, part_Of_Speech):
    segment_preffix = get_segment_prefix(segment, part_Of_Speech)
    user_input = get_user_input(part_Of_Speech)
    segment_suffix =  get_segment_suffix(segment, part_Of_Speech)
    return segment_preffix + user_input + segment_suffix

# Returns a color-user altered segment or the segment passed in
def get_revised_segment(segment):
    for specific_Part_Of_Speech in Part_of_speech_User_prompt_Dictionary:
        if specific_Part_Of_Speech in segment:
            return append_segment_including_user_modification(segment, specific_Part_Of_Speech)
    return segment

# Genrating filled story
for segment in unfilled_Story_List:
    filled_story_list.append(get_revised_segment(segment))

print()
print ("Color Key:")

# Prints the parts of speech color key
for part_of_speech in Part_of_speech_User_prompt_Dictionary:
    cprint (Part_of_speech_User_prompt_Dictionary[part_of_speech], Part_of_speech_Color_Dictionary[part_of_speech])

print()    
print("Your Story:")

# Prints the filled in story
for story_segment in filled_story_list:
    print(story_segment, end = " ")