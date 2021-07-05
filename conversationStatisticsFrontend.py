import matplotlib.pyplot as plt
from conversationStatisticsBackend import GeneralInfo, AnalConversation
from statisticsFrontend import PlotShow


class GeneralShow(GeneralInfo, PlotShow):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)

    def generalInfoShow(self):
        plt.figure(figsize=(8, 5))
        plt.suptitle(self.conversationInfo.title)
        messagesNumber = "{} - {} wiadomości \n".format(self.conversationInfo.title, self.messagesTotal())
        textMessagesTotal = "Wiadomości tekstowych: {} \n".format(self.textMessagesTotal())
        avgMessagesPerPerson = "Średnio {} wiadomości na osobę \n".format(self.avgMessageAmountPerPerson())
        avgMessageLength = "Średnia długość wiadomości: {} znaków \n".format(self.avgMessageLength())
        xdConversationTotal = 'Ilość "XD" na konwersacji: {}\n'.format(self.xdConversationTotal())
        multimediaConversationTotal = "Multimediów na konwersacji: {} \n".format(self.multimediaTotal())
        photoConversationTotal = "   Zdjęć: {} \n".format(self.photoTotal())
        videoConversationTotal = "   Filmików: {} \n".format(self.videoTotal())
        reactionsTotal = "Wszystkich reakcji: {} \n".format(self.reactionTotal())
        heartsTotal = "   Serduszek: {}\n".format(self.heartsTotal())
        hahaTotal = "   Emotek śmiechu: {}\n".format(self.hahaTotal())
        thumbsTotal = "   Kciuków w górę: {}\n".format(self.thumbsTotal())
        eyesTotal = '   Serduszek w oczach: {}\n'.format(self.heartsInEyesTotal())
        wowTotal = "   Reakcji wow: {}\n".format(self.wowTotal())
        unsentTotal = "Usuniętych wiadomości: {}\n".format(self.unsentTotal())
        questions = "Zadanych pytań: {}\n".format(self.questionsTotal())
        questionsPercent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.questionsToAllPercent())
        xdToAllPercent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.xdToAllPercent())
        wordTotal = 'Wysłanych słów {}\n'.format(self.wordTotal())
        topWord = 'Najczęściej występujące słowo - "{x_y[0]}": {x_y[1]} razy\n'.format(x_y=self.topWordTotal())
        plt.figtext(0.1, 0.2, messagesNumber + wordTotal + topWord + avgMessagesPerPerson + avgMessageLength +
                    textMessagesTotal + multimediaConversationTotal + photoConversationTotal + videoConversationTotal +
                    questions + xdConversationTotal + unsentTotal + reactionsTotal + heartsTotal + hahaTotal + wowTotal
                    + thumbsTotal + eyesTotal + questionsPercent + xdToAllPercent)
        plt.show()

    def pieShow(self):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle(self.conversationInfo.title)
        plt.subplot(2, 2, 1)
        self.xdPie()
        plt.subplot(2, 2, 2)
        self.multimediaPie()
        plt.subplot(2, 2, 3)
        self.emoticonPie()
        plt.subplot(2, 2, 4)
        self.questionPie()
        plt.show()

    def xdPie(self):
        x = ['"XD"', 'wiadomości bez "XD"']
        y = [self.xdConversationTotal(), self.textMessagesTotal() - self.xdConversationTotal()]
        return plt.pie(y, labels=x, startangle=0)

    def multimediaPie(self):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.multimediaTotal(), self.textMessagesTotal()]
        return plt.pie(y2, labels=x2)

    def emoticonPie(self):
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.heartsTotal(), self.heartsInEyesTotal(), self.thumbsTotal(), self.hahaTotal(), self.wowTotal()]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def questionPie(self):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.questionsTotal(), self.messagesTotal() - self.questionsTotal()]
        return plt.pie(y2, labels=x2)


class ConversationPeopleShow(AnalConversation, GeneralInfo, PlotShow):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)

    def mostMessagesSentShow(self):
        title = "Ilość wiadomości wysłana przez danego użytkownika z {} wszystkich wiadomości".format(
            len(self.conversationInfo.messages))
        xLabel = "Najwięcej wiadomosci od {}: {}"
        self.showPlot(self.mostMessagesSent(), title, xLabel)

    def mostReactionsReceiverShow(self):
        title = "Otrzymane reakcje z {} wszystkich reakcji".format(self.reactionTotal())
        xLabel = "Najwięcej reakcji otrzymał {}: {}"
        self.showPlot(self.mostReactionReceiver(), title, xLabel)

    def mostReactionsGiverShow(self):
        title = "Dane reakcje z {} wszystkich reakcji".format(self.reactionTotal())
        xLabel = "Najwięcej reakcji dał {}: {}"
        self.showPlot(self.mostReactionGiver(), title, xLabel)

    def mostPhotoSentShow(self):
        title = "Wysłane zdjęcia z {} wszystkich zdjęć".format(self.photoTotal())
        xLabel = "Najwięcej zdjęć wysłał {}: {}"
        self.showPlot(self.mostPhotoSent(), title, xLabel)

    def mostVideoSentShow(self):
        title = "Wysłane filmiki z {} wszystkich filmików".format(self.videoTotal())
        xLabel = "Najwięcej filmików wysłał {}: {}"
        self.showPlot(self.mostVideoSent(), title, xLabel)

    def mostMultimediaSentShow(self):
        title = "Wysłane multimedia z {} wszystkich multimediów".format(self.multimediaTotal())
        xLabel = "Najwięcej zdjęć i filmików wysłał {}: {}"
        self.showPlot(self.mostMultimediaSent(), title, xLabel)

    def mostMultimediaReactionsReceiverShow(self):
        title = "Otrzymane reakcje z {} reakcji za zdjęcia i filmiki".format(self.multimediaReactionsTotal())
        xLabel = "Najwięcej reakcji dotyczących multimediów otrzymał {}: {}"
        self.showPlot(self.mostMultimediaReactionsReceiver(), title, xLabel)

    def mostMultimediaReactionsGiverShow(self):
        title = "Dane reakcje z {} wszystkich reakcji dla multimediów".format(self.reactionTotal())
        xLabel = "Najwięcej reakcji dla zdjęć i filmików od {}: {}"
        self.showPlot(self.mostMultimediaReactionsGiver(), title, xLabel)

    def personMessageLengthShow(self):
        title = "Średnia długość wiadomości na osobę - ogólna średnia: {} znaków".format(self.avgMessageLength())
        xLabel = "Najdłuższe wiadomości pisze {}: {} znaków średnio"
        self.showPlot(self.mostPersonMessageLength(), title, xLabel)

    def charWritenShow(self):
        title = "Napisanych pojedynczych znaków z {} wszystkich znaków na konfie".format(self.topWordTotal())
        xLabel = "Najwięcej razy w klawiaturę uderzył {}: {}"
        self.showPlot(self.mostCharWriten(), title, xLabel)

    def mostXDSentShow(self):
        title = 'Wysłane "XD" z wszystkich {} wiadomości zawierających "XD"'.format(self.xdConversationTotal())
        xLabel = 'Najwięcej "xD" od {}: {}'
        self.showPlot(self.mostXDSent(), title, xLabel)

    def leastXDSendShow(self):
        title = 'Wysłane wiadomości bez "XD" z wszystkich {} wiadomości bez "XD"'.format(self.messagesTotal() -
                                                                                         self.xdConversationTotal())
        xLabel = 'Najwięcej wiadomości bez "xD" od {}: {}'
        self.showPlot(self.leastXDSent(), title, xLabel)

    def mostQuestionGiverShow(self):
        title = "Zadane pytania na wszystkie {} pytań".format(self.questionsTotal())
        xLabel = "Najwięcej pytań od {}: {}"
        self.showPlot(self.mostQuestionGiver(), title, xLabel)

    def mostWyspaGiverShow(self):
        title = 'Ilość napisanych "wyspa" na wszystkie {} "wyspa"'.format(self.wyspaTotal())
        xLabel = 'Najwięcej "wyspa" pisze {}: {}'
        self.showPlot(self.mostWyspaGiver(), title, xLabel)

    def mostKurwaGiverShow(self):
        title = 'Ilość napisanych "kurwa" na wszystkie {} "kurwa"'.format(self.kurwaTotal())
        xLabel = 'Najwięcej "kurwa" pisze {}: {}'
        self.showPlot(self.mostKurwaGiver(), title, xLabel)

    def mostTopWordGiverShow(self):
        topWord, topWordAmount = self.topWordTotal()
        title = 'Ilość napisanych "{}" na wszystkie {} "{}"'.format(topWord, topWordAmount, topWord)
        xLabel = 'Najwięcej od {}: {}'
        self.showPlot(self.mostTopWordGiver(topWord), title, xLabel)

    def mostGivenWordGiverShow(self, word):
        title = 'Ilość napisanych "{}"'.format(word)
        xLabel = 'Najwięcej od {}: {}'
        self.showPlot(self.mostGivenWordGiver(word), title, xLabel)

    def leastQuestionGiverShow(self):
        title = "Wiadomości bez pytań na wszystkie {} wiadomości nie będące pytaniami".format(self.messagesTotal() -
                                                                                              self.questionsTotal())
        xLabel = "Najwięcej wiadomości nie będącymi pytaniami od {}: {}"
        self.showPlot(self.leastQuestionGiver(), title, xLabel)

    def mostUnsentGiverShow(self):
        title = 'Usuniętych wiadomości na wszystkie {} usunięte'.format(self.unsentTotal())
        xLabel = "Najwięcej usuniętych przez {}: {}"
        self.showPlot(self.mostUnsentGiver(), title, xLabel)

    def mostHeartsGiverShow(self):
        title = "Danych serduszek na wszystkie {} serduszka".format(self.heartsTotal())
        xLabel = "Najwięcej serduszek od {}: {}"
        self.showPlot(self.mostHeartsGiver(), title, xLabel)

    def mostHeartsReceiverShow(self):
        title = "Otrzymanych serduszek na wszystkie {} serduszka".format(self.heartsTotal())
        xLabel = "Najwiecej serduszek dostał(a) {}: {}"
        self.showPlot(self.mostHeartsReceiver(), title, xLabel)

    def mostHahaGiverShow(self):
        title = 'Danych buziek śmiechu na wszystkie {} reakcje "haha"'.format(self.hahaTotal())
        xLabel = 'Najwięcej reakcji "haha" od {}: {}'
        self.showPlot(self.mostHahaGiver(), title, xLabel)

    def mostHahaReceiverShow(self):
        title = 'Otrzymanych buziek śmiechu na wszystkie {} reakcje "haha"'.format(self.hahaTotal())
        xLabel = 'Najwiecej reakcji "haha" dostał(a) {}: {}'
        self.showPlot(self.mostHahaReceiver(), title, xLabel)

    def receivedToGivenReactionsShow(self):
        title = '% otrzymanych reakcji względem wszystkich swoich reakcji (danych i otrzymanych)'
        xLabel = 'Stosunek reakcji otrzymanych do danych wygrywa {}: {}% otrzymanych reakcji'
        self.showPlot(self.receivedToGivenReactions(), title, xLabel)

    def receivedToGivenHeartsShow(self):
        title = '% otrzymanych serduszek względem wszystkich swoich serduszek (danych i otrzymanych)'
        xLabel = 'Stosunek serduszek otrzymanych do danych wygrywa {}: {}% otrzymanych serduszek'
        self.showPlot(self.receivedToGivenHearts(), title, xLabel)

    def questionsToAnswersPerPersonShow(self):
        title = '% zadanych pytań względem wszystkich wysłanych przez siebie wiadomości'
        xLabel = 'Największy stosunek pytań do wszystkich swoich wiadomości ma {}: {}% pytań'
        self.showPlot(self.questionsToAnswersPerPerson(), title, xLabel)

    def xdToNoXDPerPersonShow(self):
        title = '% wysłanych "XD" względem wszystkich wysłanych przez siebie wiadomości'
        xLabel = 'Największy stosunek "XD" do wszystkich swoich wiadomości ma {}: {}% "XD"'
        self.showPlot(self.xdToNoXDPerPerson(), title, xLabel)

    def mostOnlyQuestionGiverShow(self):
        title = 'Wysłane "?" z wszystkich {} wiadomości będących tylko znakami zapytania'.\
            format(self.onlyQuestionTotal())
        xLabel = 'Najwięcej samych "?" od {}: {}'
        self.showPlot(self.mostOnlyQuestionGiver(), title, xLabel)


class Show(ConversationPeopleShow, GeneralShow):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)
