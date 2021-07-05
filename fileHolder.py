import fileDecoder


class ConversationInfo:
    def __init__(self):
        self.messages = []
        self.participants = []
        self.title = str()

    @staticmethod
    def fromDictionary(dictionary):
        output = ConversationInfo()
        output.messages = dictionary.get("messages")
        output.participants = dictionary.get("participants")
        output.title = dictionary.get("title")
        return fileDecoder.decodeFile(output)


class ConversationInfoList:
    def __init__(self):
        self.conversations = []

    def addConversation(self, dictionary):
        self.conversations.append(dictionary)

