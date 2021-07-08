import matplotlib.pyplot as plt
from statisticsBackend import ComparePeople, Total, AboutMe


class PlotShow:
    @staticmethod
    def showPlot(sortedDict, titleText, xLabelText):
        def firstValue(a):
            return a[0] if len(a) > 0 else 0
        plt.figure(figsize=(10, 7.25))
        plt.title(titleText)
        xPerson = list(sortedDict.keys())
        y = list(sortedDict.values())
        x = [xPerson[i] + " " + str(y[i]) for i in range(len(xPerson))]
        plt.bar(x, y)
        plt.xticks(x, x, rotation='vertical')
        plt.margins(0.01)
        plt.subplots_adjust(bottom=0.42)
        plt.xlabel(xLabelText.format(firstValue(xPerson), firstValue(y)))
        plt.show()


class AboutMeShow(AboutMe, PlotShow):
    def __init__(self, peopleConversationList):
        super().__init__(peopleConversationList)

    def compareMyWordUsageShow(self, name="Pawel Krasicki"):
        title = 'Najczęściej używane przez ciebie słowa'
        xLabel = 'Najczęściej używasz "{}": {}'
        self.showPlot(self.compareMyWordUsage(name), title, xLabel)


class MyTotalShow(Total, PlotShow):
    def __init__(self, peopleConversationList):
        super().__init__(peopleConversationList)

    def myGeneralInfoShow(self, name):
        plt.figure(figsize=(8, 5))
        plt.suptitle('Statystyki tego co {} napisał(a) na całym messengerze'.format(name))
        messagesNumber = "{} wiadomości \n".format(self.mySentTotal(name))
        textMessagesTotal = "Wiadomości tekstowych: {} \n".format(self.myTextMessagesSentTotal(name))
        avgMessageLength = "Średnia długość wiadomości: {} znaków \n".format(self.myAvgMessageLen(name))
        xdTotal = 'Ilość wszystkich "XD": {}\n'.format(self.myXDTotal(name))
        multimediaTotal = "Wszystkich multimediów: {} \n".format(self.myMultimediaTotal(name))
        photoTotal = "   Zdjęć: {} \n".format(self.myPhotoTotal(name))
        videoTotal = "   Filmików: {} \n".format(self.myVideoTotal(name))
        reactionsTotal = "Wszystkich reakcji: {} \n".format(self.myReactionsTotal(name))
        heartsTotalG = "   Serduszek danych: {}\n".format(self.myHeartsGiven(name))
        heartsTotalR = "   Serduszek otrzymanych {}\n".format(self.myHeartsReceived(name))
        hahaTotalG = "   Emotek śmiechu danych: {}\n".format(self.myHahaGiven(name))
        hahaTotalR = "   Emotek śmiechu otrzymanych: {}\n".format(self.myHahaReceived(name))
        thumbsTotalG = "   Kciuków w górę danych: {}\n".format(self.myLikesGiven(name))
        thumbsTotalR = "   Kciuków w górę otrzymanych: {}\n".format(self.myLikesReceived(name))
        eyesTotalG = '   Serduszek w oczach danych: {}\n'.format(self.myEyesGiven(name))
        eyesTotalR = '   Serduszek w oczach otrzymanych: {}\n'.format(self.myEyesReceived(name))
        wowTotalG = "   Reakcji wow danych: {}\n".format(self.myWowGiven(name))
        wowTotalR = "   Reakcji wow otrzymanych: {}\n".format(self.myWowReceived(name))
        unsentTotal = "Usuniętych wiadomości: {}\n".format(self.myUnsentTotal(name))
        questions = "Zadanych pytań: {}\n".format(self.myQuestionsTotal(name))
        questionsPercent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.myQuestionsToAllPercent(name))
        xdToAllPercent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.myXDToAllPercent(name))
        plt.figtext(0.1, 0.08, messagesNumber + avgMessageLength + textMessagesTotal +
                    multimediaTotal + photoTotal + videoTotal + questions +
                    xdTotal + unsentTotal + reactionsTotal + heartsTotalG + heartsTotalR + hahaTotalG + hahaTotalR +
                    thumbsTotalG + thumbsTotalR + eyesTotalG + eyesTotalR + wowTotalG + wowTotalR + questionsPercent +
                    xdToAllPercent)
        plt.show()

    def myPieShow(self, name):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle('Statystyka wiadomości wysłanych przez {}'.format(name))
        plt.subplot(3, 2, 1)
        self.myXDPie(name)
        plt.subplot(3, 2, 2)
        self.myMultimediaPie(name)
        plt.subplot(3, 2, 3)
        self.myEmoticonPie(name)
        plt.subplot(3, 2, 4)
        self.myEmoticonPie2(name)
        plt.subplot(3, 2, 5)
        self.myQuestionPie(name)
        plt.subplot(3, 2, 6)
        self.myReceivedToGivenReactionsPie(name)
        plt.show()

    def myXDPie(self, name):
        x = ['"XD"', 'wiadomości bez "XD"']
        y = [self.myXDTotal(name), self.myTextMessagesSentTotal(name) - self.myXDTotal(name)]
        return plt.pie(y, labels=x, startangle=0)

    def myMultimediaPie(self, name):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.myMultimediaTotal(name), self.myTextMessagesSentTotal(name)]
        return plt.pie(y2, labels=x2)

    def myEmoticonPie(self, name):
        plt.title("Otrzymane reakcje")
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.myHeartsReceived(name), self.myEyesReceived(name), self.myLikesReceived(name),
             self.myHahaReceived(name), self.myWowReceived(name)]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def myEmoticonPie2(self, name):
        plt.title("Dane reakcje")
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.myHeartsGiven(name), self.myEyesGiven(name), self.myLikesGiven(name),
             self.myHahaGiven(name), self.myWowGiven(name)]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def myQuestionPie(self, name):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.myQuestionsTotal(name), self.myTextMessagesSentTotal(name) - self.myQuestionsTotal(name)]
        return plt.pie(y2, labels=x2)

    def myReceivedToGivenReactionsPie(self, name):
        x = ['otrzymane reakcje', 'dane reakcje']
        y = [self.myReactionsReceivedTemplate("", name), self.myReactionsGivenTemplate("", name)]
        return plt.pie(y, labels=x)


class TotalShow(Total, PlotShow):
    def __init__(self, peopleConversationList):
        super().__init__(peopleConversationList)

    def generalInfoShow(self):
        plt.figure(figsize=(8, 5))
        plt.suptitle('Statystyki całego Twojego messengera')
        messagesNumber = "{} wiadomości \n".format(self.messengerSentTotal())
        textMessagesTotal = "Wiadomości tekstowych: {} \n".format(self.messengerTextMessagesSentTotal())
        avgMessageLength = "Średnia długość wiadomości: {} znaków \n".format(self.messengerAvgMessageLen())
        xdTotal = 'Ilość wszystkich "XD": {}\n'.format(self.xdTotal())
        multimediaTotal = "Wszystkich multimediów: {} \n".format(self.multimediaTotal())
        photoTotal = "   Zdjęć: {} \n".format(self.photoTotal())
        videoTotal = "   Filmików: {} \n".format(self.videoTotal())
        reactionsTotal = "Wszystkich reakcji: {} \n".format(self.messengerReactionsTotal())
        heartsTotal = "   Serduszek: {}\n".format(self.heartsTotal())
        hahaTotal = "   Emotek śmiechu: {}\n".format(self.hahaTotal())
        thumbsTotal = "   Kciuków w górę: {}\n".format(self.thumbsTotal())
        eyesTotal = '   Serduszek w oczach: {}\n'.format(self.eyeHeartsTotal())
        wowTotal = "   Reakcji wow: {}\n".format(self.wowTotal())
        unsentTotal = "Usuniętych wiadomości: {}\n".format(self.messengerUnsentTotal())
        questions = "Zadanych pytań: {}\n".format(self.questionsTotal())
        questionsPercent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.questionsToAllPercent())
        xdToAllPercent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.xdToAllPercent())
        plt.figtext(0.1, 0.2, messagesNumber + avgMessageLength + textMessagesTotal +
                    multimediaTotal + photoTotal + videoTotal + questions +
                    xdTotal + unsentTotal + reactionsTotal + heartsTotal + hahaTotal + wowTotal +
                    thumbsTotal + eyesTotal + questionsPercent + xdToAllPercent)
        plt.show()

    def pieShow(self):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle('Statystyka całego Twojego messengera')
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
        y = [self.xdTotal(), self.messengerTextMessagesSentTotal() - self.xdTotal()]
        return plt.pie(y, labels=x, startangle=0)

    def multimediaPie(self):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.multimediaTotal(), self.messengerTextMessagesSentTotal()]
        return plt.pie(y2, labels=x2)

    def emoticonPie(self):
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.heartsTotal(), self.eyeHeartsTotal(), self.thumbsTotal(), self.hahaTotal(), self.wowTotal()]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def questionPie(self):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.questionsTotal(), self.messengerTextMessagesSentTotal() - self.questionsTotal()]
        return plt.pie(y2, labels=x2)


class ComparePeopleShow(Total, ComparePeople, PlotShow):
    def __init__(self, peopleConversationList):
        super().__init__(peopleConversationList)

    def compareMessageAmountShow(self):
        title = "Ilość wiadomości z daną osobą z {} wszystkich wiadomości".format(self.messengerSentTotal())
        xLabel = "Najwięcej wiadomości z {}: {}"
        self.showPlot(self.compareMessageAmount(), title, xLabel)

    def compareMultimediaAmountShow(self):
        title = "Ilość zjęć i filmików z daną osobą z {} wszystkich multimediów".format(self.multimediaTotal())
        xLabel = "Najwięcej zdjęć i filmików z {}: {}"
        self.showPlot(self.compareMultimediaAmount(), title, xLabel)

    def comparePhotoAmountShow(self):
        title = "Ilość zdjęć z daną osobą z {} wszystkich zdjęć".format(self.photoTotal())
        xLabel = "Najwięcej zdjęć z {}: {}"
        self.showPlot(self.comparePhotoAmount(), title, xLabel)

    def compareVideoAmountShow(self):
        title = "Ilość filmików z daną osobą z {} wszystkich filmików".format(self.videoTotal())
        xLabel = "Najwięcej zdjęć z {}: {}"
        self.showPlot(self.compareVideoAmount(), title, xLabel)

    def compareXDAmountShow(self):
        title = 'Ilość "XD" z daną osobą z {} wszystkich "XD"'.format(self.xdTotal())
        xLabel = 'Najwięcej "XD" z {}: {}'
        self.showPlot(self.compareXDAmount(), title, xLabel)

    def compareHahaWordAmountShow(self):
        title = 'Ilość napisanych "haha" z daną osobą z {} wszystkich "haha"'.format(self.hahaWordTotal())
        xLabel = 'Najwięcej tekstowych "haha" z {}: {}'
        self.showPlot(self.compareHahaWordAmount(), title, xLabel)

    def compareGivenWordAmountShow(self, word=""):
        title = 'Ilość "{}" z daną osobą'.format(word)
        xLabel = 'Najwięcej "{word1}" z {blank1}: {blank2}'.format(word1=word, blank1='{}', blank2='{}')
        self.showPlot(self.compareGivenWordAmount(word), title, xLabel)

    def compareLoveAmountShow(self):
        title = 'Ilość wysłanych serduszek (nie reakcji) z daną osobą z {} wszystkich serduszek'.format(self.loveTotal())
        xLabel = 'Najwięcej wysłanych wiadomości z serduszkami z {}: {}'
        self.showPlot(self.compareLoveAmount(), title, xLabel)

    def compareOmgAmountShow(self):
        title = 'Ilość napisanych "omg" z daną osobą z {} wszystkich "omg"'.format(self.omgTotal())
        xLabel = 'Najwięcej "omg" z {}: {}'
        self.showPlot(self.compareOmgAmount(), title, xLabel)

    def compareHeartsAmountShow(self):
        title = 'Wysłanych serduszek z daną osobą z wszystkich {} serduszek'.format(self.heartsTotal())
        xLabel = 'Najwięcej serduszek z {}: {}'
        self.showPlot(self.compareHeartsAmount(), title, xLabel)

    def compareHahaAmountShow(self):
        title = 'Wysłanych emotek "haha" z daną osobą z wszystkich {} emotek"haha"'.format(self.hahaTotal())
        xLabel = 'Najwięcej "haha" z {}: {}'
        self.showPlot(self.compareHahaAmount(), title, xLabel)

    def compareWowAmountShow(self):
        title = 'Wysłanych "wow" z daną osobą z wszystkich {} "wow"'.format(self.wowTotal())
        xLabel = 'Najwięcej "wow" z {}: {}'
        self.showPlot(self.compareWowAmount(), title, xLabel)

    def compareLikesAmountShow(self):
        title = 'Wysłanych lajków z daną osobą z wszystkich {} lajków'.format(self.thumbsTotal())
        xLabel = 'Najwięcej lajków z {}: {}'
        self.showPlot(self.compareLikesAmount(), title, xLabel)

    def compareEyesAmountShow(self):
        title = 'Wysłanych serduszek w oczach z daną osobą z wszystkich {} buziek z serduszkami w oczach'.format(
            self.eyeHeartsTotal())
        xLabel = 'Najwięcej serduszek w oczach z {}: {}'
        self.showPlot(self.compareEyesAmount(), title, xLabel)


class HorrorShow(AboutMeShow, MyTotalShow, TotalShow, ComparePeopleShow):
    def __init__(self, peopleConversationList):
        super().__init__(peopleConversationList)