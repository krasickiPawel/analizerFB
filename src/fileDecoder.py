def decode_file(conversation_info):
    conversation_info.participants = decode_dictionary_list(conversation_info.participants)
    conversation_info.messages = decode_dictionary_list(conversation_info.messages)
    conversation_info.title = decode_single_string(conversation_info.title)
    return conversation_info


def decode_single_string(text):
    text = text.encode('latin_1').decode('utf-8')
    return text


def decode_dictionary_list(conversation_info_list):
    new_list = []
    for obj in conversation_info_list:
        for key in obj:
            if isinstance(obj[key], str):
                obj[key] = obj[key].encode('latin_1').decode('utf-8')
            elif isinstance(obj[key], list):
                for dictionary in obj[key]:
                    for reactions_key in dictionary:
                        if isinstance(dictionary[reactions_key], str):
                            dictionary[reactions_key] = dictionary[reactions_key].encode('latin_1').decode('utf-8')
            pass
        new_list.append(obj)
    return new_list
