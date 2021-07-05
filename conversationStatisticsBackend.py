from statisticsBackend import OperationTemplates


class ConversationOperationTemplates(OperationTemplates):
    def __init__(self, conversationInfo):
        self.conversationInfo = conversationInfo

    def specificReactionTotal(self, reaction1, reaction2="brak reakcji"):
        listsList = [message.get("reactions") for message in self.conversationInfo.messages if message.get("reactions")
                     is not None]
        amount = 0
        for reactionList in listsList:
            for reaction in reactionList:
                if reaction.get("reaction").__contains__(reaction1) or reaction.get("reaction").__contains__(reaction2):
                    amount += 1
        return amount

    def mostSpecificReactionGiver(self, reaction1, reaction2="brak reakcji"):
        reactionsListList = [message.get("reactions") for message in self.conversationInfo.messages
                             if message.get("reactions") is not None]
        namesHeartReactionsList = []
        for reactionsList in reactionsListList:
            for reactions in reactionsList:
                if reactions.get("reaction").__contains__(reaction1) or reactions.get("reaction").__contains__(
                        reaction2):
                    namesHeartReactionsList.append((reactions.get("actor"), 1))
        return self.sortDict(self.prepareDict(namesHeartReactionsList))

    def mostSpecificReactionReceiver(self, reaction1, reaction2="brak reakcji"):
        namesReactionsList = [(message.get("sender_name"), len([reaction for reaction in message.get("reactions") if
                                                                (reaction.get("reaction").__contains__(reaction1) or
                                                                 reaction.get("reaction").__contains__(reaction2))]))
                              for message in self.conversationInfo.messages if message.get("reactions") is not None]
        return self.sortDict(self.prepareDict(namesReactionsList))

    def mostContentGiver(self, word=""):
        wordMessageSenders = [(message.get("sender_name"), 1) for message in
                              self.conversationInfo.messages if message.get("content") is not None and
                              message.get("content").lower().__contains__(word)]
        return self.sortDict(self.prepareDict(wordMessageSenders))

    def leastContentGiver(self, word=""):
        wordMessageSenders = [(message.get("sender_name"), 1) for message in
                              self.conversationInfo.messages if message.get("content") is None or not
                              message.get("content").lower().__contains__(word)]
        return self.sortDict(self.prepareDict(wordMessageSenders))

    def contentTotal(self, word=""):
        return len([message.get("content") for message in self.conversationInfo.messages
                    if message.get("content") is not None and message.get("content").__contains__(word)])

    def contentList(self):
        return [message.get("content") for message in self.conversationInfo.messages
                if message.get("content") is not None]

    def photoVideoTotal(self, photoVideo):
        return sum([len(message.get(photoVideo)) for message in self.conversationInfo.messages
                    if message.get(photoVideo) is not None])


class GeneralInfo(ConversationOperationTemplates):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)

    def messagesTotal(self):
        return len(self.conversationInfo.messages)

    def avgMessageAmountPerPerson(self):
        return int(len(self.conversationInfo.messages) / len(self.conversationInfo.participants))

    def photoTotal(self):
        return self.photoVideoTotal("photos")

    def videoTotal(self):
        return self.photoVideoTotal("videos")

    def multimediaTotal(self):
        return self.photoTotal() + self.videoTotal()

    def avgMessageLength(self):
        messagesLen = [len(message.get("content")) for message in self.conversationInfo.messages
                       if message.get("content") is not None]
        return int(sum(messagesLen) / len(messagesLen))

    def reactionTotal(self):
        return sum([len(message.get("reactions")) for message in self.conversationInfo.messages
                    if message.get("reactions") is not None])

    def textMessagesTotal(self):
        return len(self.contentList())

    def xdConversationTotal(self):
        return self.contentTotal("xd")

    def questionsTotal(self):
        return self.contentTotal("?")

    def kurwaTotal(self):
        return self.contentTotal("kurwa")

    def wyspaTotal(self):
        return self.contentTotal("wyspa") + self.contentTotal("wyspe") + self.contentTotal("wyspę")

    def givenWordTotal(self, word):   # np Patron
        return self.contentTotal(word)

    def multimediaReactionsTotal(self):
        namesReactionsMultimediaList = [(message.get("sender_name"), len(message.get("reactions"))) for message
                                        in self.conversationInfo.messages if message.get("reactions") is not None and
                                        (message.get("videos") is not None or message.get("photos") is not None)]
        return sum([reactionTuple[1] for reactionTuple in namesReactionsMultimediaList])

    def unsentTotal(self):
        return len([message.get("sender_name") for message in self.conversationInfo.messages
                    if message.get("is_unsent")])

    def heartsTotal(self):
        return self.specificReactionTotal('❤', '💕')

    def hahaTotal(self):
        return self.specificReactionTotal('😂', '😆')

    def thumbsTotal(self):
        return self.specificReactionTotal('👍')

    def wowTotal(self):
        return self.specificReactionTotal('😮')

    def heartsInEyesTotal(self):
        return self.specificReactionTotal('😍')

    def wordTotal(self):
        return sum([len(content.split()) for content in self.contentList()])

    def charTotal(self):
        return sum([len(message.get("content")) for message in self.conversationInfo.messages
                    if message.get("content") is not None])

    def topWordTotal(self):
        wordList = []
        for content in self.contentList():
            for word in content.split():
                wordList.append(word)
        maxWord = max(wordList)
        return maxWord, wordList.count(maxWord)

    def onlyQuestionTotal(self):
        return len([None for message in self.conversationInfo.messages if message.get("content") is not None and
                    message.get("content").__eq__("?")])

    def questionsToAllPercent(self):
        return int(100 * (self.questionsTotal() / self.messagesTotal())) if self.messagesTotal() > 0 else 0

    def xdToAllPercent(self):
        return int(100 * (self.xdConversationTotal() / self.messagesTotal())) if self.messagesTotal() > 0 else 0

    def givenToAllPercent(self, word):
        return int(100 * (self.givenWordTotal(word) / self.messagesTotal())) if self.messagesTotal() > 0 else 0


class AnalConversation(ConversationOperationTemplates):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)

    def mostMessagesSent(self):
        namesAmount = [(message.get("sender_name"), 1) for message in self.conversationInfo.messages]
        return self.sortDict(self.prepareDict(namesAmount))

    def mostReactionReceiver(self):
        namesReactionsList = [(message.get("sender_name"), len(message.get("reactions"))) for message
                              in self.conversationInfo.messages if message.get("reactions") is not None]
        return self.sortDict(self.prepareDict(namesReactionsList))

    def mostReactionGiver(self):
        reactionsListList = [message.get("reactions") for message in self.conversationInfo.messages
                             if message.get("reactions") is not None]
        namesReactionsList = []
        for reactionsList in reactionsListList:
            for reactions in reactionsList:
                namesReactionsList.append((reactions.get("actor"), 1))
        return self.sortDict(self.prepareDict(namesReactionsList))

    def mostPhotoSent(self):
        namesPhotosList = [(message.get("sender_name"), len(message.get("photos"))) for message in
                           self.conversationInfo.messages if message.get("photos") is not None]
        return self.sortDict(self.prepareDict(namesPhotosList))

    def mostVideoSent(self):
        namesVideosList = [(message.get("sender_name"), len(message.get("videos"))) for message
                           in self.conversationInfo.messages if message.get("videos") is not None]
        return self.sortDict(self.prepareDict(namesVideosList))

    def mostMultimediaSent(self):
        namesVideosList = [(message.get("sender_name"), len(message.get("videos"))) for message
                           in self.conversationInfo.messages if message.get("videos") is not None]
        namesPhotosList = [(message.get("sender_name"), len(message.get("photos"))) for message
                           in self.conversationInfo.messages if message.get("photos") is not None]
        namesVideosList.extend(namesPhotosList)
        return self.sortDict(self.prepareDict(namesVideosList))

    def mostMultimediaReactionsReceiver(self):
        namesReactionsList = [(message.get("sender_name"), len(message.get("reactions"))) for message
                              in self.conversationInfo.messages if message.get("reactions") is not None and
                              (message.get("videos") is not None or message.get("photos") is not None)]
        return self.sortDict(self.prepareDict(namesReactionsList))

    def mostMultimediaReactionsGiver(self):
        reactionListList = [message.get("reactions") for message in self.conversationInfo.messages
                            if message.get("reactions") is not None and (message.get("photos") is not None
                            or message.get("videos") is not None)]
        namesMultimediaReactionsList = []
        for reactionList in reactionListList:
            for reaction in reactionList:
                namesMultimediaReactionsList.append((reaction.get("actor"), 1))
        return self.sortDict(self.prepareDict(namesMultimediaReactionsList))

    def mostCharWriten(self):
        namesLengthsList = [(message.get("sender_name"), len(message.get("content"))) for message in
                            self.conversationInfo.messages if message.get("content") is not None]
        return self.sortDict(self.prepareDict(namesLengthsList))

    def mostPersonMessageLength(self):
        messagesPerPerson = self.mostMessagesSent()
        charSentPerPerson = self.mostCharWriten()
        names = list(messagesPerPerson.keys())
        avgMsgLenPerPerson = [(name, int(charSentPerPerson.get(name)/messagesPerPerson.get(name))) for name in names
                              if charSentPerPerson.get(name) is not None and messagesPerPerson.get(name) is not None]
        return self.sortDict(self.prepareDict(avgMsgLenPerPerson))

    def mostXDSent(self):
        return self.mostContentGiver("xd")

    def leastXDSent(self):
        return self.leastContentGiver("xd")

    def mostQuestionGiver(self):
        return self.mostContentGiver("?")

    def leastQuestionGiver(self):
        return self.leastContentGiver("?")

    def mostWyspaGiver(self):
        return self.mostContentGiver("wyspa")

    def mostKurwaGiver(self):
        return self.mostContentGiver("kurwa")

    def mostTopWordGiver(self, topWord):
        return self.mostContentGiver(topWord)

    def mostGivenWordGiver(self, word):
        return self.mostContentGiver(word)

    def mostHeartsGiver(self):
        return self.mostSpecificReactionGiver('❤', '💕')

    def mostHeartsReceiver(self):
        return self.mostSpecificReactionReceiver('❤', '💕')

    def mostUnsentGiver(self):
        unsentList = [(message.get("sender_name"), 1) for message in self.conversationInfo.messages
                      if message.get("is_unsent")]
        return self.sortDict(self.prepareDict(unsentList))

    def mostHahaGiver(self):
        return self.mostSpecificReactionGiver('😂', '😆')

    def mostHahaReceiver(self):
        return self.mostSpecificReactionReceiver('😂', '😆')

    def receivedToGivenReactions(self):
        given = self.mostReactionGiver()
        received = self.mostReactionReceiver()
        return self.receivedToReceivedPlusGivenInPercent(received, given)

    def receivedToGivenHearts(self):
        given = self.mostHeartsGiver()
        received = self.mostHeartsReceiver()
        return self.receivedToReceivedPlusGivenInPercent(received, given)

    def questionsToAnswersPerPerson(self):
        questions = self.mostQuestionGiver()
        answers = self.leastQuestionGiver()
        return self.receivedToReceivedPlusGivenInPercent(questions, answers)

    def xdToNoXDPerPerson(self):
        xd = self.mostXDSent()
        noXD = self.leastXDSent()
        return self.receivedToReceivedPlusGivenInPercent(xd, noXD)

    def mostOnlyQuestionGiver(self):
        onlyQuestionMarks = [(message.get("sender_name"), 1) for message in
                             self.conversationInfo.messages if message.get("content") is not None and
                             message.get("content")[0] == "?"]
        return self.sortDict(self.prepareDict(onlyQuestionMarks))
