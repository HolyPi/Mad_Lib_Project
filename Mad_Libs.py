import sys
from termcolor import colored, cprint
unfilled_Story_String = "‘%ingv people?' said %na. 'Of course you find this interesting! But not because of the %a %n! Because you, yourself, will be %ingv %av until you've burned out! We both know who you really are! Please %Pv %av the, just for once! You've %pv before. Could you %Pv for me instead? Then I'll give you a %n. %na would've liked it!"
unfilled_Story_List = unfilled_Story_String.split(' ')
part_Of_Speech_Dictionary = {"%ingv": "a verb ending with -ing","%pv":"a past tense verb", "%Pv": "a present verb",
                            "%na":"a name", "%n": "a single noun", "%av": "an adverb", "%a": "an adjective"}

color_coded_Part_of_speech = {"%ingv": "red","%pv": "blue", "%Pv": "green", "%na":"cyan", 
                                "%n": "yellow", "%av": "magenta", "%a": "grey"}

filledStoryList = []

def get_user_input(part_Of_Speech):
    userInput = input("Enter " + part_Of_Speech_Dictionary[part_Of_Speech] + " :")
    return colored(userInput, color_coded_Part_of_speech[part_Of_Speech])

def get_segment_prefix(segment, part_of_speech):
    return segment[0:segment.find(part_of_speech)]

def get_segment_suffix(segment, part_of_speech):
     return segment[segment.find(part_of_speech) + len(part_of_speech): len(segment)]

def append_user_modified_segment(segment, part_Of_Speech):
    segment_preffix = get_segment_prefix(segment, part_Of_Speech)
    user_input = get_user_input(part_Of_Speech)
    segment_suffix =  get_segment_suffix(segment, part_Of_Speech)
    filledStoryList.append(segment_preffix + user_input + segment_suffix)

def contains_Specific_Parts_Of_Speech(segment):
    for specific_Part_Of_Speech in part_Of_Speech_Dictionary:
        if specific_Part_Of_Speech in segment:
            append_user_modified_segment(segment, specific_Part_Of_Speech)
            return
    filledStoryList.append(segment)

for segment in unfilled_Story_List:
    contains_Specific_Parts_Of_Speech(segment)

print()
print ("Color Key:")

for part_of_speech in part_Of_Speech_Dictionary:
    cprint (part_of_speech, color_coded_Part_of_speech[part_of_speech])

print()    
print("Christopher Francisco's Story:")
print()

for story_segment in filledStoryList:
    print(story_segment, end = " ")