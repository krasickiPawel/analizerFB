import json
from fileHolder import ConversationInfoList, ConversationInfo
import glob


def saveObjectToJson(objectToSave, fileName):   # for future
    fileName = jsonFileNameFrom(fileName)
    with open(fileName, 'w') as fileObject:
        json.dump(objectToSave, fileObject, indent=4)


def readConversationInfoFromJson(fileName):
    conversationInfo = readObjectFromJson(ConversationInfo, fileName)
    return conversationInfo


def readObjectFromJson(classToBeRead, fileName):
    dictionary = readFromJson(fileName)
    output = classToBeRead.fromDictionary(dictionary)
    return output


def readFromJson(fileName):
    fileName = jsonFileNameFrom(fileName)
    with open(fileName, 'r') as fileObject:
        dictionary = json.load(fileObject)
    return dictionary


def jsonFileNameFrom(name):
    if name.endswith('.json'):
        return name
    return name + '.json'


def directoryRead(dirName):
    files = glob.glob(dirName + '/*.json')
    cil = ConversationInfoList()
    try:
        for file in files:
            cil.addConversation(readConversationInfoFromJson(file))
        if len(cil.conversations) == 0:
            raise FileNotFoundError
        conversationInfo = ConversationInfo()
        conversationInfo.title = cil.conversations[0].title
        conversationInfo.participants = cil.conversations[0].participants
        for conversation in cil.conversations:
            conversationInfo.messages.extend(conversation.messages)
        return conversationInfo
    except FileNotFoundError:
        return None


def multi_directory_read(inbox, window, pathVariable, bar, results):
    dirs = glob.glob(inbox + '/**')
    cil = ConversationInfoList()
    for dirName in dirs:
        pathVariable.set(dirName)
        conversation = directoryRead(dirName)
        if conversation is not None:
            cil.addConversation(conversation)
        if bar['value'] is not None:
            bar['value'] += (1 / len(dirs) * 100)
        window.update_idletasks()
    window.quit()
    results[0] = cil
