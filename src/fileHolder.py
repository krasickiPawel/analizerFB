import fileDecoder


class ConversationInfo:
    def __init__(self):
        self.messages = []
        self.participants = []
        self.title = str()

    @staticmethod
    def from_dictionary(dictionary):
        output = ConversationInfo()
        output.messages = dictionary.get("messages")
        output.participants = dictionary.get("participants")
        output.title = dictionary.get("title")
        return fileDecoder.decodeFile(output)


class ConversationInfoList:
    def __init__(self):
        self.conversations = []

    def add_conversation(self, dictionary):
        self.conversations.append(dictionary)

