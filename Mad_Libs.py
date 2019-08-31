import sys
from termcolor import colored, cprint
unfilled_Story_String = "‘%ingv people?' said %na. 'Of course you find this interesting! But not because of the %a %n! Because you, yourself, will be %ingv %av until you've burned out! We both know who you really are! For one %Pv, please, just for once! You've %pv Could you %Pv for me instead? Then I'll give you a %n."
unfilled_Story_List = unfilled_Story_String.split(' ')
part_Of_Speech_Dictionary = {"%ingv": "a verb ending with -ing","%pv":"a past tense verb", "%Pv": "a present verb",
                            "%na":"a name", "%n": "a single noun", "%av": "an adverb", "%a": "an adjective"}
filledStoryList = []

def get_user_input(part_Of_Speech):
    return input("Enter " + part_Of_Speech_Dictionary[part_Of_Speech] + " :")

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
for story_segment in filledStoryList:
    cprint(story_segment, "red", end = " ")