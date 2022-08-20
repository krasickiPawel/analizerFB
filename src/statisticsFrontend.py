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
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def compareMyWordUsageShow(self, name="Pawel Krasicki"):
        title = 'Najczęściej używane przez ciebie słowa'
        xLabel = 'Najczęściej używasz "{}": {}'
        self.showPlot(self.compare_my_word_usage(name), title, xLabel)


class MyTotalShow(Total, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def my_general_info_show(self, name):
        plt.figure(figsize=(8, 5))
        plt.suptitle('Statystyki tego co {} napisał(a) na całym messengerze'.format(name))
        messagesNumber = "{} wiadomości \n".format(self.my_sent_total(name))
        textMessagesTotal = "Wiadomości tekstowych: {} \n".format(self.my_text_messages_sent_total(name))
        avgMessageLength = "Średnia długość wiadomości: {} znaków \n".format(self.my_avg_message_len(name))
        xdTotal = 'Ilość wszystkich "XD": {}\n'.format(self.my_xd_total(name))
        multimediaTotal = "Wszystkich multimediów: {} \n".format(self.my_multimedia_total(name))
        photoTotal = "   Zdjęć: {} \n".format(self.my_photo_total(name))
        videoTotal = "   Filmików: {} \n".format(self.my_video_total(name))
        reactionsTotal = "Wszystkich reakcji: {} \n".format(self.my_reactions_total(name))
        heartsTotalG = "   Serduszek danych: {}\n".format(self.my_hearts_given(name))
        heartsTotalR = "   Serduszek otrzymanych {}\n".format(self.my_hearts_received(name))
        hahaTotalG = "   Emotek śmiechu danych: {}\n".format(self.my_haha_given(name))
        hahaTotalR = "   Emotek śmiechu otrzymanych: {}\n".format(self.my_haha_received(name))
        thumbsTotalG = "   Kciuków w górę danych: {}\n".format(self.my_likes_given(name))
        thumbsTotalR = "   Kciuków w górę otrzymanych: {}\n".format(self.my_likes_received(name))
        eyesTotalG = '   Serduszek w oczach danych: {}\n'.format(self.my_eyes_given(name))
        eyesTotalR = '   Serduszek w oczach otrzymanych: {}\n'.format(self.my_eyes_received(name))
        wowTotalG = "   Reakcji wow danych: {}\n".format(self.my_wow_given(name))
        wowTotalR = "   Reakcji wow otrzymanych: {}\n".format(self.my_wow_received(name))
        unsentTotal = "Usuniętych wiadomości: {}\n".format(self.my_unsent_total(name))
        questions = "Zadanych pytań: {}\n".format(self.my_questions_total(name))
        questionsPercent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.my_questions_to_all_percent(name))
        xdToAllPercent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.my_xd_to_all_percent(name))
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
        y = [self.my_xd_total(name), self.my_text_messages_sent_total(name) - self.my_xd_total(name)]
        return plt.pie(y, labels=x, startangle=0)

    def myMultimediaPie(self, name):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.my_multimedia_total(name), self.my_text_messages_sent_total(name)]
        return plt.pie(y2, labels=x2)

    def myEmoticonPie(self, name):
        plt.title("Otrzymane reakcje")
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.my_hearts_received(name), self.my_eyes_received(name), self.my_likes_received(name),
             self.my_haha_received(name), self.my_wow_received(name)]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def myEmoticonPie2(self, name):
        plt.title("Dane reakcje")
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.my_hearts_given(name), self.my_eyes_given(name), self.my_likes_given(name),
             self.my_haha_given(name), self.my_wow_given(name)]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def myQuestionPie(self, name):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.my_questions_total(name), self.my_text_messages_sent_total(name) - self.my_questions_total(name)]
        return plt.pie(y2, labels=x2)

    def myReceivedToGivenReactionsPie(self, name):
        x = ['otrzymane reakcje', 'dane reakcje']
        y = [self.my_reactions_received_template("", name), self.my_reactions_given_template("", name)]
        return plt.pie(y, labels=x)


class TotalShow(Total, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def generalInfoShow(self):
        plt.figure(figsize=(8, 5))
        plt.suptitle('Statystyki całego Twojego messengera')
        messagesNumber = "{} wiadomości \n".format(self.messenger_sent_total())
        textMessagesTotal = "Wiadomości tekstowych: {} \n".format(self.messenger_text_messages_sent_total())
        avgMessageLength = "Średnia długość wiadomości: {} znaków \n".format(self.messenge_avg_message_len())
        xdTotal = 'Ilość wszystkich "XD": {}\n'.format(self.xd_total())
        multimediaTotal = "Wszystkich multimediów: {} \n".format(self.multimedia_total())
        photoTotal = "   Zdjęć: {} \n".format(self.photo_total())
        videoTotal = "   Filmików: {} \n".format(self.video_total())
        reactionsTotal = "Wszystkich reakcji: {} \n".format(self.messenger_reactions_total())
        heartsTotal = "   Serduszek: {}\n".format(self.hearts_total())
        hahaTotal = "   Emotek śmiechu: {}\n".format(self.haha_total())
        thumbsTotal = "   Kciuków w górę: {}\n".format(self.thumbs_total())
        eyesTotal = '   Serduszek w oczach: {}\n'.format(self.eye_hearts_total())
        wowTotal = "   Reakcji wow: {}\n".format(self.wow_total())
        unsentTotal = "Usuniętych wiadomości: {}\n".format(self.messenger_unsent_total())
        questions = "Zadanych pytań: {}\n".format(self.questions_total())
        questionsPercent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.questions_to_all_percent())
        xdToAllPercent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.xd_to_all_percent())
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
        y = [self.xd_total(), self.messenger_text_messages_sent_total() - self.xd_total()]
        return plt.pie(y, labels=x, startangle=0)

    def multimediaPie(self):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.multimedia_total(), self.messenger_text_messages_sent_total()]
        return plt.pie(y2, labels=x2)

    def emoticonPie(self):
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.hearts_total(), self.eye_hearts_total(), self.thumbs_total(), self.haha_total(), self.wow_total()]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def questionPie(self):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.questions_total(), self.messenger_text_messages_sent_total() - self.questions_total()]
        return plt.pie(y2, labels=x2)


class ComparePeopleShow(Total, ComparePeople, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def compare_message_amount_show(self):
        title = "Ilość wiadomości z daną osobą z {} wszystkich wiadomości".format(self.messenger_sent_total())
        xLabel = "Najwięcej wiadomości z {}: {}"
        self.showPlot(self.compare_message_amount(), title, xLabel)

    def compare_multimedia_amount_show(self):
        title = "Ilość zjęć i filmików z daną osobą z {} wszystkich multimediów".format(self.multimedia_total())
        xLabel = "Najwięcej zdjęć i filmików z {}: {}"
        self.showPlot(self.compare_multimedia_amount(), title, xLabel)

    def compare_photo_amount_show(self):
        title = "Ilość zdjęć z daną osobą z {} wszystkich zdjęć".format(self.photo_total())
        xLabel = "Najwięcej zdjęć z {}: {}"
        self.showPlot(self.compare_photo_amount(), title, xLabel)

    def compare_video_amount_show(self):
        title = "Ilość filmików z daną osobą z {} wszystkich filmików".format(self.video_total())
        xLabel = "Najwięcej zdjęć z {}: {}"
        self.showPlot(self.compare_video_amount(), title, xLabel)

    def compare_xd_amount_show(self):
        title = 'Ilość "XD" z daną osobą z {} wszystkich "XD"'.format(self.xd_total())
        xLabel = 'Najwięcej "XD" z {}: {}'
        self.showPlot(self.compare_xd_amount(), title, xLabel)

    def compare_haha_word_amount_show(self):
        title = 'Ilość napisanych "haha" z daną osobą z {} wszystkich "haha"'.format(self.haha_word_total())
        xLabel = 'Najwięcej tekstowych "haha" z {}: {}'
        self.showPlot(self.compare_haha_word_amount(), title, xLabel)

    def compare_given_word_amount_show(self, word=""):
        title = 'Ilość "{}" z daną osobą'.format(word)
        xLabel = 'Najwięcej "{word1}" z {blank1}: {blank2}'.format(word1=word, blank1='{}', blank2='{}')
        self.showPlot(self.compare_given_word_amount(word), title, xLabel)

    def compare_love_amount_show(self):
        title = 'Ilość wysłanych serduszek (nie reakcji) z daną osobą z {} wszystkich serduszek'.format(self.love_total())
        xLabel = 'Najwięcej wysłanych wiadomości z serduszkami z {}: {}'
        self.showPlot(self.compare_love_amount(), title, xLabel)

    def compareOmgAmountShow(self):
        title = 'Ilość napisanych "omg" z daną osobą z {} wszystkich "omg"'.format(self.omg_total())
        xLabel = 'Najwięcej "omg" z {}: {}'
        self.showPlot(self.compare_omg_amount(), title, xLabel)

    def compare_hearts_amount_show(self):
        title = 'Wysłanych serduszek z daną osobą z wszystkich {} serduszek'.format(self.hearts_total())
        xLabel = 'Najwięcej serduszek z {}: {}'
        self.showPlot(self.compare_hearts_amount(), title, xLabel)

    def compare_haha_amount_show(self):
        title = 'Wysłanych emotek "haha" z daną osobą z wszystkich {} emotek"haha"'.format(self.haha_total())
        xLabel = 'Najwięcej "haha" z {}: {}'
        self.showPlot(self.compare_haha_amount(), title, xLabel)

    def compare_wow_amount_show(self):
        title = 'Wysłanych "wow" z daną osobą z wszystkich {} "wow"'.format(self.wow_total())
        xLabel = 'Najwięcej "wow" z {}: {}'
        self.showPlot(self.compare_wow_amount(), title, xLabel)

    def compare_likes_amount_show(self):
        title = 'Wysłanych lajków z daną osobą z wszystkich {} lajków'.format(self.thumbs_total())
        xLabel = 'Najwięcej lajków z {}: {}'
        self.showPlot(self.compare_likes_amount(), title, xLabel)

    def compare_eyes_amount_show(self):
        title = 'Wysłanych serduszek w oczach z daną osobą z wszystkich {} buziek z serduszkami w oczach'.format(
            self.eye_hearts_total())
        xLabel = 'Najwięcej serduszek w oczach z {}: {}'
        self.showPlot(self.compare_eyes_amount(), title, xLabel)


class HorrorShow(AboutMeShow, MyTotalShow, TotalShow, ComparePeopleShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)
