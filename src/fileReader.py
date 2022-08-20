import json
from fileHolder import ConversationInfoList, ConversationInfo
import glob


def save_object_to_json(object_to_save, file_name):   # for future
    file_name = json_file_name_from(file_name)
    with open(file_name, 'w') as file_object:
        json.dump(object_to_save, file_object, indent=4)


def read_conversation_info_from_json(file_name):
    conversation_info = read_object_from_json(ConversationInfo, file_name)
    return conversation_info


def read_object_from_json(class_to_be_read, file_name):
    dictionary = read_from_json(file_name)
    output = class_to_be_read.from_dictionary(dictionary)
    return output


def read_from_json(file_name):
    file_name = json_file_name_from(file_name)
    with open(file_name, 'r') as file_object:
        dictionary = json.load(file_object)
    return dictionary


def json_file_name_from(name):
    if name.endswith('.json'):
        return name
    return name + '.json'


def directory_read(dir_name):
    files = glob.glob(dir_name + '/*.json')
    cil = ConversationInfoList()
    try:
        for file in files:
            cil.add_conversation(read_conversation_info_from_json(file))
        if len(cil.conversations) == 0:
            raise FileNotFoundError
        conversation_info = ConversationInfo()
        conversation_info.title = cil.conversations[0].title
        conversation_info.participants = cil.conversations[0].participants
        for conversation in cil.conversations:
            conversation_info.messages.extend(conversation.messages)
        return conversation_info
    except FileNotFoundError:
        return None


def multi_directory_read(inbox, window, path_variable, bar, results):
    dirs = glob.glob(inbox + '/**')
    cil = ConversationInfoList()
    for dir_name in dirs:
        path_variable.set(dir_name)
        conversation = directory_read(dir_name)
        if conversation is not None:
            cil.add_conversation(conversation)
        if bar['value'] is not None:
            bar['value'] += (1 / len(dirs) * 100)
        window.update_idletasks()
    window.quit()
    results[0] = cil
