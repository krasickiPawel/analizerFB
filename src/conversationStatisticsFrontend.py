import matplotlib.pyplot as plt
from conversationStatisticsBackend import GeneralInfo, AnalConversation
from statisticsFrontend import PlotShow


class GeneralShow(GeneralInfo, PlotShow):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)

    def general_info_show(self):
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
        plt.figtext(0.1, 0.2, messagesNumber + wordTotal + avgMessagesPerPerson + avgMessageLength +
                    textMessagesTotal + multimediaConversationTotal + photoConversationTotal + videoConversationTotal +
                    questions + xdConversationTotal + unsentTotal + reactionsTotal + heartsTotal + hahaTotal + wowTotal
                    + thumbsTotal + eyesTotal + questionsPercent + xdToAllPercent)
        plt.show()

    def pie_show(self):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle(self.conversationInfo.title)
        plt.subplot(3, 2, 1)
        self.xdPie()
        plt.subplot(3, 2, 2)
        self.multimediaPie()
        plt.subplot(3, 2, 3)
        self.emoticonPie()
        plt.subplot(3, 2, 4)
        self.questionPie()
        plt.subplot(3, 2, 5)
        self.omgHahaXDPie()
        plt.subplot(3, 2, 6)
        self.superSztosMegaSwietnieZajebisciePie()
        plt.show()

    def xdPie(self):
        x = ['"XD"', 'wiadomości bez "XD"']
        y = [self.xdConversationTotal(), self.textMessagesTotal() - self.xdConversationTotal()]
        return plt.pie(y, labels=x, startangle=0)

    def multimediaPie(self):
        x = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y = [self.multimediaTotal(), self.textMessagesTotal()]
        return plt.pie(y, labels=x)

    def emoticonPie(self):
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.heartsTotal(), self.heartsInEyesTotal(), self.thumbsTotal(), self.hahaTotal(), self.wowTotal()]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def questionPie(self):
        x = ['pytania', 'wiadomości bez pytań']
        y = [self.questionsTotal(), self.messagesTotal() - self.questionsTotal()]
        return plt.pie(y, labels=x)

    def omgHahaXDPie(self):
        x = ['omg', 'napisane "haha"', 'xD', 'emotka śmiechu']
        y = [self.omgTotal(), self.hahaTotal(), self.xdConversationTotal(), self.givenWordTotal('😂')
             + self.givenWordTotal('😆')]
        return plt.pie(y, labels=x)

    def superSztosMegaSwietnieZajebisciePie(self):
        x = ['super', 'sztos', 'mega', 'świetnie', 'zajebiście']
        y = [self.givenWordTotal('super'), self.givenWordTotal('sztos'), self.givenWordTotal('mega'),
             self.givenWordTotal('świetn'), self.givenWordTotal('zajebi')]
        return plt.pie(y, labels=x)


class ConversationPeopleShow(AnalConversation, GeneralInfo, PlotShow):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)

    def most_messages_sent_show(self):
        title = "Ilość wiadomości wysłana przez danego użytkownika z {} wszystkich wiadomości".format(
            len(self.conversationInfo.messages))
        xLabel = "Najwięcej wiadomosci od {}: {}"
        self.show_plot(self.mostMessagesSent(), title, xLabel)

    def most_reactions_receiver_show(self):
        title = "Otrzymane reakcje z {} wszystkich reakcji".format(self.reactionTotal())
        xLabel = "Najwięcej reakcji otrzymał {}: {}"
        self.show_plot(self.mostReactionReceiver(), title, xLabel)

    def most_reactions_giver_show(self):
        title = "Dane reakcje z {} wszystkich reakcji".format(self.reactionTotal())
        xLabel = "Najwięcej reakcji dał {}: {}"
        self.show_plot(self.mostReactionGiver(), title, xLabel)

    def most_photo_sent_show(self):
        title = "Wysłane zdjęcia z {} wszystkich zdjęć".format(self.photoTotal())
        xLabel = "Najwięcej zdjęć wysłał {}: {}"
        self.show_plot(self.mostPhotoSent(), title, xLabel)

    def most_video_sent_show(self):
        title = "Wysłane filmiki z {} wszystkich filmików".format(self.videoTotal())
        xLabel = "Najwięcej filmików wysłał {}: {}"
        self.show_plot(self.mostVideoSent(), title, xLabel)

    def most_multimedia_sent_show(self):
        title = "Wysłane multimedia z {} wszystkich multimediów".format(self.multimediaTotal())
        xLabel = "Najwięcej zdjęć i filmików wysłał {}: {}"
        self.show_plot(self.mostMultimediaSent(), title, xLabel)

    def most_multimedia_reactions_receiver_show(self):
        title = "Otrzymane reakcje z {} reakcji za zdjęcia i filmiki".format(self.multimediaReactionsTotal())
        xLabel = "Najwięcej reakcji dotyczących multimediów otrzymał {}: {}"
        self.show_plot(self.mostMultimediaReactionsReceiver(), title, xLabel)

    def most_multimedia_reactions_giver_show(self):
        title = "Dane reakcje z {} wszystkich reakcji dla multimediów".format(self.reactionTotal())
        xLabel = "Najwięcej reakcji dla zdjęć i filmików od {}: {}"
        self.show_plot(self.mostMultimediaReactionsGiver(), title, xLabel)

    def person_message_length_show(self):
        title = "Średnia długość wiadomości na osobę - ogólna średnia: {} znaków".format(self.avgMessageLength())
        xLabel = "Najdłuższe wiadomości pisze {}: {} znaków średnio"
        self.show_plot(self.mostPersonMessageLength(), title, xLabel)

    def char_writen_show(self):
        title = "Napisanych pojedynczych znaków z {} wszystkich znaków na konfie".format(self.charTotal())
        xLabel = "Najwięcej razy w klawiaturę uderzył {}: {}"
        self.show_plot(self.mostCharWriten(), title, xLabel)

    def most_love_show(self):
        title = 'Wysłane serduszka z wszystkich {} wiadomości zawierających serduszka'.format(self.heartsWritenTotal())
        xLabel = 'Najwięcej serduszek w wiadomości (nie reakcji) od {}: {}'
        self.show_plot(self.mostLove(), title, xLabel)

    def most_xd_sent_show(self):
        title = 'Wysłane "XD" z wszystkich {} wiadomości zawierających "XD"'.format(self.xdConversationTotal())
        xLabel = 'Najwięcej "xD" od {}: {}'
        self.show_plot(self.mostXDSent(), title, xLabel)

    def leas_xd_sent_show(self):
        title = 'Wysłane wiadomości bez "XD" z wszystkich {} wiadomości bez "XD"'.format(self.messagesTotal() -
                                                                                         self.xdConversationTotal())
        xLabel = 'Najwięcej wiadomości bez "xD" od {}: {}'
        self.show_plot(self.leastXDSent(), title, xLabel)

    def most_question_giver_show(self):
        title = "Zadane pytania na wszystkie {} pytań".format(self.questionsTotal())
        xLabel = "Najwięcej pytań od {}: {}"
        self.show_plot(self.mostQuestionGiver(), title, xLabel)

    def most_omg_giver_show(self):
        title = 'Ilość napisanych "omg" na wszystkie {} "omg"'.format(self.omgTotal())
        xLabel = 'Najwięcej "omg" pisze {}: {}'
        self.show_plot(self.mostOmgGiver(), title, xLabel)

    def most_given_word_giver_show(self, word):
        title = 'Ilość napisanych "{}"'.format(word)
        xLabel = 'Najwięcej od {}: {}'
        self.show_plot(self.mostGivenWordGiver(word), title, xLabel)

    def least_question_giver_show(self):
        title = "Wiadomości bez pytań na wszystkie {} wiadomości nie będące pytaniami".format(self.messagesTotal() -
                                                                                              self.questionsTotal())
        xLabel = "Najwięcej wiadomości nie będącymi pytaniami od {}: {}"
        self.show_plot(self.leastQuestionGiver(), title, xLabel)

    def most_unsent_giver_show(self):
        title = 'Usuniętych wiadomości na wszystkie {} usunięte'.format(self.unsentTotal())
        xLabel = "Najwięcej usuniętych przez {}: {}"
        self.show_plot(self.mostUnsentGiver(), title, xLabel)

    def most_hearts_giver_show(self):
        title = "Danych serduszek na wszystkie {} serduszka".format(self.heartsTotal())
        xLabel = "Najwięcej serduszek od {}: {}"
        self.show_plot(self.mostHeartsGiver(), title, xLabel)

    def most_hearts_receiver_show(self):
        title = "Otrzymanych serduszek na wszystkie {} serduszka".format(self.heartsTotal())
        xLabel = "Najwiecej serduszek dostał(a) {}: {}"
        self.show_plot(self.mostHeartsReceiver(), title, xLabel)

    def most_haha_giver_show(self):
        title = 'Danych buziek śmiechu na wszystkie {} reakcje "haha"'.format(self.hahaTotal())
        xLabel = 'Najwięcej reakcji "haha" od {}: {}'
        self.show_plot(self.mostHahaGiver(), title, xLabel)

    def most_haha_receiver_show(self):
        title = 'Otrzymanych buziek śmiechu na wszystkie {} reakcje "haha"'.format(self.hahaTotal())
        xLabel = 'Najwiecej reakcji "haha" dostał(a) {}: {}'
        self.show_plot(self.mostHahaReceiver(), title, xLabel)

    def received_to_given_reactions_show(self):
        title = '% otrzymanych reakcji względem wszystkich swoich reakcji (danych i otrzymanych)'
        xLabel = 'Stosunek reakcji otrzymanych do danych wygrywa {}: {}% otrzymanych reakcji'
        self.show_plot(self.receivedToGivenReactions(), title, xLabel)

    def received_to_given_hearts_show(self):
        title = '% otrzymanych serduszek względem wszystkich swoich serduszek (danych i otrzymanych)'
        xLabel = 'Stosunek serduszek otrzymanych do danych wygrywa {}: {}% otrzymanych serduszek'
        self.show_plot(self.receivedToGivenHearts(), title, xLabel)

    def questions_to_answers_per_person_show(self):
        title = '% zadanych pytań względem wszystkich wysłanych przez siebie wiadomości'
        xLabel = 'Największy stosunek pytań do wszystkich swoich wiadomości ma {}: {}% pytań'
        self.show_plot(self.questionsToAnswersPerPerson(), title, xLabel)

    def xd_to_no_xd_per_person_show(self):
        title = '% wysłanych "XD" względem wszystkich wysłanych przez siebie wiadomości'
        xLabel = 'Największy stosunek "XD" do wszystkich swoich wiadomości ma {}: {}% "XD"'
        self.show_plot(self.xdToNoXDPerPerson(), title, xLabel)

    def most_only_question_giver_show(self):
        title = 'Wysłane "?" z wszystkich {} wiadomości będących tylko znakami zapytania'.\
            format(self.onlyQuestionTotal())
        xLabel = 'Najwięcej samych "?" od {}: {}'
        self.show_plot(self.mostOnlyQuestionGiver(), title, xLabel)


class Show(ConversationPeopleShow, GeneralShow):
    def __init__(self, conversationInfo):
        super().__init__(conversationInfo)
