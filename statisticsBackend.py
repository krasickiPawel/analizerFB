class OperationTemplates:
    @staticmethod
    def sortDict(unsortedDict):
        sortedList = sorted(unsortedDict.items(), key=lambda x: x[1], reverse=True)[:40]
        return {pair[0][:20]: pair[1] for pair in sortedList}

    @staticmethod
    def prepareDict(tupleList):
        listDict = {}
        for name, amount in tupleList:
            listDict.setdefault(name, []).append(amount)
        return {person: sum(listDict.get(person)) for person in listDict}

    @staticmethod
    def receivedToReceivedPlusGivenInPercent(received, given):
        names = list(received.keys())
        givenToReceived = [(name, int(100 * (received.get(name) / (received.get(name) + given.get(name))))) for name
                           in names if given.get(name) is not None and received.get(name) is not None]
        return OperationTemplates.sortDict(OperationTemplates.prepareDict(givenToReceived))


class TotalOperationTemplates:
    def __init__(self, peopleConversationList):
        self.peopleConversationList = peopleConversationList

    def photoVideoTemplate(self, photoVideo):   # podział na ogólne i moje ze względu większej wydajności
        total = 0                               # (contains dla ogólnych się nie wykonuje wiec szybciej)
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get(photoVideo) is not None:
                    total += len(messageDict.get(photoVideo))
        return total

    def myPhotoVideoTemplate(self, photoVideo, name="Pawel Krasicki"):  # dodac funkcjonalnosc na wpisywanie imienia
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get(photoVideo) is not None and messageDict.get("sender_name") == name:
                    total += len(messageDict.get(photoVideo))
        return total

    def reactionsTemplate(self, r):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None:
                    for reaction in messageDict.get('reactions'):
                        if reaction.get("reaction").__contains__(r):
                            total += 1
        return total

    def myReactionsGivenTemplate(self, r, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None:
                    for reaction in messageDict.get('reactions'):
                        if reaction.get("reaction").__contains__(r) and reaction.get("actor") == name:
                            total += 1
        return total

    def myReactionsReceivedTemplate(self, r, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None and messageDict.get("sender_name") == name:
                    for reaction in messageDict.get('reactions'):
                        if reaction.get("reaction").__contains__(r):
                            total += 1
        return total

    def contentTemplate(self, word):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("content").lower().__contains__(word):
                    total += 1
        return total

    def myContentTemplate(self, word, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("content").lower().__contains__(word) \
                        and messageDict.get("sender_name") == name:
                    total += 1
        return total


class Total(TotalOperationTemplates):
    def __init__(self, peopleConversationList):
        super(Total, self).__init__(peopleConversationList)

    def messengerSentTotal(self):
        return sum([len(conversation.messages) for conversation in self.peopleConversationList.conversations])

    def messengerTextMessagesSentTotal(self):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None:
                    total += 1
        return total

    def myTextMessagesSentTotal(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("sender_name") == name:
                    total += 1
        return total

    def messengerAvgMessageLen(self):
        messagesLen = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None:
                    messagesLen.append(len(messageDict.get("content")))
        return int(sum(messagesLen) / len(messagesLen)) if len(messagesLen) > 0 else 0

    def myAvgMessageLen(self, name="Pawel Krasicki"):
        messagesLen = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("sender_name") == name:
                    messagesLen.append(len(messageDict.get("content")))
        return int(sum(messagesLen) / len(messagesLen)) if len(messagesLen) > 0 else 0

    def messengerReactionsTotal(self):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None:
                    total += len(messageDict.get("reactions"))
        return total

    def messengerUnsentTotal(self):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("is_unsent") is not None and messageDict.get("is_unsent"):
                    total += 1
        return total

    def myUnsentTotal(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("is_unsent") is not None and messageDict.get("is_unsent") and \
                        messageDict.get("sender_name") == name:
                    total += 1
        return total

    def topWordTotal(self):     # front
        wordList = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None:
                    for word in messageDict.get("content").split():
                        wordList.append(word)
        if len(wordList) > 0:
            maxWord = max(wordList)
            return maxWord, wordList.count(maxWord)
        else:
            return 0, 0

    def questionsToAllPercent(self):
        return int(100 * (self.questionsTotal() / self.messengerSentTotal())) if self.messengerSentTotal() > 0 else 0

    def xdToAllPercent(self):
        return int(100 * (self.xdTotal() / self.messengerSentTotal())) if self.messengerSentTotal() > 0 else 0

    def photoTotal(self):
        return self.photoVideoTemplate("photos")

    def videoTotal(self):
        return self.photoVideoTemplate("videos")

    def multimediaTotal(self):
        return self.videoTotal() + self.photoTotal()

    def heartsTotal(self):
        return self.reactionsTemplate('❤')

    def hahaTotal(self):
        return self.reactionsTemplate('😆')

    def wowTotal(self):
        return self.reactionsTemplate('😮')

    def eyeHeartsTotal(self):
        return self.reactionsTemplate('😍')

    def thumbsTotal(self):
        return self.reactionsTemplate('👍')

    def heartsReceivedTotal(self):
        return self.reactionsTemplate('❤')

    def hahaReceivedTotal(self):
        return self.reactionsTemplate('😆')

    def wowReceivedTotal(self):
        return self.reactionsTemplate('😮')

    def eyeHeartsReceivedTotal(self):
        return self.reactionsTemplate('😍')

    def thumbsReceivedTotal(self):
        return self.reactionsTemplate('👍')

    def xdTotal(self):
        return self.contentTemplate("xd")

    def questionsTotal(self):
        return self.contentTemplate("?")

    def omgTotal(self):
        return self.contentTemplate("omg")

    def loveTotal(self):
        return self.contentTemplate("kocham c")

    def kurwaTotal(self):
        return self.contentTemplate("kurwa")

    def givenWordTotal(self, word):
        return self.contentTemplate(word)

    def jaPierdoleTotal(self):
        return self.contentTemplate("ja pierdol") + self.contentTemplate("japierdol")

    def hahaWordTotal(self):
        return self.contentTemplate("haha")

    def mySentTotal(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("sender_name") == name:
                    total += 1
        return total

    def myReactionsTotal(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None and messageDict.get("sender_name") == name:
                    total += len(messageDict.get("reactions"))
        return total

    def myPhotoTotal(self, name):
        return self.myPhotoVideoTemplate("photos", name)

    def myVideoTotal(self, name):
        return self.myPhotoVideoTemplate("videos", name)

    def myMultimediaTotal(self, name):
        return self.myVideoTotal(name) + self.myPhotoTotal(name)

    def myHeartsReceived(self, name):
        return self.myReactionsReceivedTemplate('❤', name)

    def myHahaReceived(self, name):
        return self.myReactionsReceivedTemplate('😆', name)

    def myWowReceived(self, name):
        return self.myReactionsReceivedTemplate('😮', name)

    def myEyesReceived(self, name):
        return self.myReactionsReceivedTemplate('😍', name)

    def myLikesReceived(self, name):
        return self.myReactionsReceivedTemplate('👍', name)

    def myHeartsGiven(self, name):
        return self.myReactionsGivenTemplate('❤', name)

    def myHahaGiven(self, name):
        return self.myReactionsGivenTemplate('😆', name)

    def myWowGiven(self, name):
        return self.myReactionsGivenTemplate('😮', name)

    def myEyesGiven(self, name):
        return self.myReactionsGivenTemplate('😍', name)

    def myLikesGiven(self, name):
        return self.myReactionsGivenTemplate('👍', name)

    def myXDTotal(self, name):
        return self.myContentTemplate("xd", name)

    def myQuestionsTotal(self, name):
        return self.myContentTemplate("?", name)

    def myOmgTotal(self, name):
        return self.myContentTemplate("omg", name)

    def myLoveTotal(self, name):
        return self.myContentTemplate("kocham c", name)

    def myKurwaTotal(self, name):
        return self.myContentTemplate("kurwa", name)

    def myJaPierdoleTotal(self, name):
        return self.myContentTemplate("ja pierdol", name) + self.myContentTemplate("japierdol", name)

    def myGivenWordTotal(self, word, name):
        return self.myContentTemplate(word, name)

    def myTopWordTotal(self, name):     # front
        wordList = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("sender_name") == name:
                    for word in messageDict.get("content").split():
                        wordList.append(word)
        maxWord = max(wordList)
        return maxWord, wordList.count(maxWord)

    def myQuestionsToAllPercent(self, name):
        return int(100 * (self.myQuestionsTotal(name) / self.mySentTotal(name))) if self.mySentTotal() > 0 else 0

    def myXDToAllPercent(self, name):
        return int(100 * (self.myXDTotal(name) / self.mySentTotal(name))) if self.mySentTotal() > 0 else 0


class ComparePeopleOperationTemplates(OperationTemplates):
    def __init__(self, peopleConversationList):
        self.peopleConversationList = peopleConversationList

    def compareWordAmount(self, word):
        xdAmount = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("content").lower().__contains__(word):
                    xdAmount.append((conversation.title, 1))
        return self.sortDict(self.prepareDict(xdAmount))

    def comparePhotoVideoAmount(self, photo, video='brak parametru'):
        photoVideoAmount = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get(photo) is not None:
                    photoVideoAmount.append((conversation.title, 1))
                if messageDict.get(video) is not None:
                    photoVideoAmount.append((conversation.title, 1))
        return self.sortDict(self.prepareDict(photoVideoAmount))

    def compareReactionsAmount(self, reaction1, reaction2='brak parametru'):
        reactionList = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None:
                    for reaction in messageDict.get("reactions"):
                        if reaction.get("reaction").__contains__(reaction1) or \
                                reaction.get('reaction').__contains__(reaction2):
                            reactionList.append((conversation.title, 1))
        return self.sortDict(self.prepareDict(reactionList))


class ComparePeople(ComparePeopleOperationTemplates):
    def __init__(self, peopleConversationList):
        super().__init__(peopleConversationList)

    def compareMessageAmount(self):
        messageLenPerPerson = [(conversation.title, len(conversation.messages)) for conversation in
                               self.peopleConversationList.conversations]
        return self.sortDict(self.prepareDict(messageLenPerPerson))

    def comparePhotoAmount(self):
        return self.comparePhotoVideoAmount('photos')

    def compareVideoAmount(self):
        return self.comparePhotoVideoAmount('videos')

    def compareMultimediaAmount(self):
        return self.comparePhotoVideoAmount('photos', 'videos')

    def compareXDAmount(self):
        return self.compareWordAmount("xd")

    def compareLoveAmount(self):
        return self.compareWordAmount("kocham c")

    def compareHahaWordAmount(self):
        return self.compareWordAmount("haha")

    def compareKurwaAmount(self):
        return self.compareWordAmount("kurwa")

    def compareJaPierdoleAmount(self):
        return self.compareWordAmount("ja pierdol")

    def compareTopWordAmount(self, topWord):    # front
        return self.compareWordAmount(topWord)

    def compareGivenWordAmount(self, word=""):
        return self.compareWordAmount(word)

    def compareHeartsAmount(self):
        return self.compareReactionsAmount('❤', '💕')

    def compareHahaAmount(self):
        return self.compareReactionsAmount('😂', '😆')

    def compareLikesAmount(self):
        return self.compareReactionsAmount('👍')

    def compareWowAmount(self):
        return self.compareReactionsAmount('😮')

    def compareEyesAmount(self):
        return self.compareReactionsAmount('😍')


class AboutMe(OperationTemplates):
    def __init__(self, peopleConversationList):
        self.peopleConversationList = peopleConversationList

    def compareMyWordUsage(self, name="Pawel Krasicki"):   # counter koniecznie zliczający listę wszystkich moich słów
        myWordList = []
        for conversation in self.peopleConversationList.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("sender_name") == name:
                    for word in messageDict.get("content").split():
                        myWordList.append((word, 1))
        return self.sortDict(self.prepareDict(myWordList))
