def decodeFile(conversationInfo):
    conversationInfo.participants = decodeDictionaryList(conversationInfo.participants)
    conversationInfo.messages = decodeDictionaryList(conversationInfo.messages)
    conversationInfo.title = decodeSingleString(conversationInfo.title)
    return conversationInfo


def decodeSingleString(text):
    text = text.encode('latin_1').decode('utf-8')
    return text


def decodeDictionaryList(conversationInfoList):
    newList = []
    for obj in conversationInfoList:
        for key in obj:
            if isinstance(obj[key], str):
                obj[key] = obj[key].encode('latin_1').decode('utf-8')
            elif isinstance(obj[key], list):
                for dictionary in obj[key]:
                    for reactionsKey in dictionary:
                        if isinstance(dictionary[reactionsKey], str):
                            dictionary[reactionsKey] = dictionary[reactionsKey].encode('latin_1').decode('utf-8')
            pass
        newList.append(obj)
    return newList
