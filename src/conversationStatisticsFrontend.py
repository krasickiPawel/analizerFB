import matplotlib.pyplot as plt
from conversationStatisticsBackend import GeneralInfo, AnalConversation
from statisticsFrontend import PlotShow


class GeneralShow(GeneralInfo, PlotShow):
    def __init__(self, conversation_info):
        super().__init__(conversation_info)

    def general_info_show(self):
        plt.figure(figsize=(8, 5))
        plt.suptitle(self.conversation_info.title)
        messages_number = "{} - {} wiadomości \n".format(self.conversation_info.title, self.messages_total())
        text_messages_total = "Wiadomości tekstowych: {} \n".format(self.text_messages_total())
        avg_messages_per_person = "Średnio {} wiadomości na osobę \n".format(self.avg_message_amount_per_person())
        avg_message_length = "Średnia długość wiadomości: {} znaków \n".format(self.avg_message_length())
        xd_conversation_total = 'Ilość "XD" na konwersacji: {}\n'.format(self.xd_conversation_total())
        multimedia_conversation_total = "Multimediów na konwersacji: {} \n".format(self.multimedia_total())
        photo_conversation_total = "   Zdjęć: {} \n".format(self.photo_total())
        video_conversation_total = "   Filmików: {} \n".format(self.video_total())
        reactions_total = "Wszystkich reakcji: {} \n".format(self.reaction_total())
        hearts_total = "   Serduszek: {}\n".format(self.hearts_total())
        haha_total = "   Emotek śmiechu: {}\n".format(self.haha_total())
        thumbs_total = "   Kciuków w górę: {}\n".format(self.thumbs_total())
        eyes_total = '   Serduszek w oczach: {}\n'.format(self.hearts_in_eyes_total())
        wow_total = "   Reakcji wow: {}\n".format(self.wow_total())
        unsent_total = "Usuniętych wiadomości: {}\n".format(self.unsent_total())
        questions = "Zadanych pytań: {}\n".format(self.questions_total())
        questions_percent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.questions_to_all_percent())
        xd_to_all_percent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.xd_to_all_percent())
        word_total = 'Wysłanych słów {}\n'.format(self.word_total())
        plt.figtext(0.1, 0.2, messages_number + word_total + avg_messages_per_person + avg_message_length +
                    text_messages_total + multimedia_conversation_total + photo_conversation_total +
                    video_conversation_total + questions + xd_conversation_total + unsent_total + reactions_total +
                    hearts_total + haha_total + wow_total + thumbs_total + eyes_total + questions_percent +
                    xd_to_all_percent)
        plt.show()

    def pie_show(self):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle(self.conversation_info.title)
        plt.subplot(3, 2, 1)
        self.xd_pie()
        plt.subplot(3, 2, 2)
        self.multimedia_pie()
        plt.subplot(3, 2, 3)
        self.emoticon_pie()
        plt.subplot(3, 2, 4)
        self.question_pie()
        plt.subplot(3, 2, 5)
        self.omg_haha_xd_pie()
        plt.show()

    def xd_pie(self):
        x = ['"XD"', 'wiadomości bez "XD"']
        y = [self.xd_conversation_total(), self.text_messages_total() - self.xd_conversation_total()]
        return plt.pie(y, labels=x, startangle=0)

    def multimedia_pie(self):
        x = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y = [self.multimedia_total(), self.text_messages_total()]
        return plt.pie(y, labels=x)

    def emoticon_pie(self):
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.hearts_total(), self.hearts_in_eyes_total(), self.thumbs_total(), self.haha_total(), self.wow_total()]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def question_pie(self):
        x = ['pytania', 'wiadomości bez pytań']
        y = [self.questions_total(), self.messages_total() - self.questions_total()]
        return plt.pie(y, labels=x)

    def omg_haha_xd_pie(self):
        x = ['omg', 'napisane "haha"', 'xD', 'emotka śmiechu']
        y = [self.omg_total(), self.haha_total(), self.xd_conversation_total(), self.given_word_total('😂')
             + self.given_word_total('😆')]
        return plt.pie(y, labels=x)


class ConversationPeopleShow(AnalConversation, GeneralInfo, PlotShow):
    def __init__(self, conversation_info):
        super().__init__(conversation_info)

    def most_messages_sent_show(self):
        title = "Ilość wiadomości wysłana przez danego użytkownika z {} wszystkich wiadomości".format(
            len(self.conversation_info.messages))
        x_label = "Najwięcej wiadomosci od {}: {}"
        self.show_plot(self.most_messages_sent(), title, x_label)

    def most_reactions_receiver_show(self):
        title = "Otrzymane reakcje z {} wszystkich reakcji".format(self.reaction_total())
        x_label = "Najwięcej reakcji otrzymał {}: {}"
        self.show_plot(self.most_reaction_receiver(), title, x_label)

    def most_reactions_giver_show(self):
        title = "Dane reakcje z {} wszystkich reakcji".format(self.reaction_total())
        x_label = "Najwięcej reakcji dał {}: {}"
        self.show_plot(self.most_reaction_giver(), title, x_label)

    def most_photo_sent_show(self):
        title = "Wysłane zdjęcia z {} wszystkich zdjęć".format(self.photo_total())
        x_label = "Najwięcej zdjęć wysłał {}: {}"
        self.show_plot(self.most_photo_sent(), title, x_label)

    def most_video_sent_show(self):
        title = "Wysłane filmiki z {} wszystkich filmików".format(self.video_total())
        x_label = "Najwięcej filmików wysłał {}: {}"
        self.show_plot(self.most_video_sent(), title, x_label)

    def most_multimedia_sent_show(self):
        title = "Wysłane multimedia z {} wszystkich multimediów".format(self.multimedia_total())
        x_label = "Najwięcej zdjęć i filmików wysłał {}: {}"
        self.show_plot(self.most_multimedia_sent(), title, x_label)

    def most_multimedia_reactions_receiver_show(self):
        title = "Otrzymane reakcje z {} reakcji za zdjęcia i filmiki".format(self.multimedia_reactions_total())
        x_label = "Najwięcej reakcji dotyczących multimediów otrzymał {}: {}"
        self.show_plot(self.most_multimedia_reactions_receiver(), title, x_label)

    def most_multimedia_reactions_giver_show(self):
        title = "Dane reakcje z {} wszystkich reakcji dla multimediów".format(self.reaction_total())
        x_label = "Najwięcej reakcji dla zdjęć i filmików od {}: {}"
        self.show_plot(self.most_multimedia_reactions_giver(), title, x_label)

    def person_message_length_show(self):
        title = "Średnia długość wiadomości na osobę - ogólna średnia: {} znaków".format(self.avg_message_length())
        x_label = "Najdłuższe wiadomości pisze {}: {} znaków średnio"
        self.show_plot(self.most_person_message_length(), title, x_label)

    def char_writen_show(self):
        title = "Napisanych pojedynczych znaków z {} wszystkich znaków na konfie".format(self.char_total())
        x_label = "Najwięcej razy w klawiaturę uderzył {}: {}"
        self.show_plot(self.most_char_writen(), title, x_label)

    def most_love_show(self):
        title = 'Wysłane serduszka z wszystkich {} wiadomości zawierających serduszka'.format(self.hearts_writen_total())
        x_label = 'Najwięcej serduszek w wiadomości (nie reakcji) od {}: {}'
        self.show_plot(self.most_love(), title, x_label)

    def most_xd_sent_show(self):
        title = 'Wysłane "XD" z wszystkich {} wiadomości zawierających "XD"'.format(self.xd_conversation_total())
        x_label = 'Najwięcej "xD" od {}: {}'
        self.show_plot(self.most_xd_sent(), title, x_label)

    def leas_xd_sent_show(self):
        title = 'Wysłane wiadomości bez "XD" z wszystkich {} wiadomości bez "XD"'.format(self.messages_total() -
                                                                                         self.xd_conversation_total())
        x_label = 'Najwięcej wiadomości bez "xD" od {}: {}'
        self.show_plot(self.least_xd_sent(), title, x_label)

    def most_question_giver_show(self):
        title = "Zadane pytania na wszystkie {} pytań".format(self.questions_total())
        x_label = "Najwięcej pytań od {}: {}"
        self.show_plot(self.most_question_giver(), title, x_label)

    def most_omg_giver_show(self):
        title = 'Ilość napisanych "omg" na wszystkie {} "omg"'.format(self.omg_total())
        x_label = 'Najwięcej "omg" pisze {}: {}'
        self.show_plot(self.most_omg_giver(), title, x_label)

    def most_given_word_giver_show(self, word):
        title = 'Ilość napisanych "{}"'.format(word)
        x_label = 'Najwięcej od {}: {}'
        self.show_plot(self.most_given_word_giver(word), title, x_label)

    def least_question_giver_show(self):
        title = "Wiadomości bez pytań na wszystkie {} wiadomości nie będące pytaniami".format(self.messages_total() -
                                                                                              self.questions_total())
        x_label = "Najwięcej wiadomości nie będącymi pytaniami od {}: {}"
        self.show_plot(self.least_question_giver(), title, x_label)

    def most_unsent_giver_show(self):
        title = 'Usuniętych wiadomości na wszystkie {} usunięte'.format(self.unsent_total())
        x_label = "Najwięcej usuniętych przez {}: {}"
        self.show_plot(self.most_unsent_giver(), title, x_label)

    def most_hearts_giver_show(self):
        title = "Danych serduszek na wszystkie {} serduszka".format(self.hearts_total())
        x_label = "Najwięcej serduszek od {}: {}"
        self.show_plot(self.most_hearts_giver(), title, x_label)

    def most_hearts_receiver_show(self):
        title = "Otrzymanych serduszek na wszystkie {} serduszka".format(self.hearts_total())
        x_label = "Najwiecej serduszek dostał(a) {}: {}"
        self.show_plot(self.most_hearts_receiver(), title, x_label)

    def most_haha_giver_show(self):
        title = 'Danych buziek śmiechu na wszystkie {} reakcje "haha"'.format(self.haha_total())
        x_label = 'Najwięcej reakcji "haha" od {}: {}'
        self.show_plot(self.most_haha_giver(), title, x_label)

    def most_haha_receiver_show(self):
        title = 'Otrzymanych buziek śmiechu na wszystkie {} reakcje "haha"'.format(self.haha_total())
        x_label = 'Najwiecej reakcji "haha" dostał(a) {}: {}'
        self.show_plot(self.most_haha_receiver(), title, x_label)

    def received_to_given_reactions_show(self):
        title = '% otrzymanych reakcji względem wszystkich swoich reakcji (danych i otrzymanych)'
        x_label = 'Stosunek reakcji otrzymanych do danych wygrywa {}: {}% otrzymanych reakcji'
        self.show_plot(self.received_to_given_reactions(), title, x_label)

    def received_to_given_hearts_show(self):
        title = '% otrzymanych serduszek względem wszystkich swoich serduszek (danych i otrzymanych)'
        x_label = 'Stosunek serduszek otrzymanych do danych wygrywa {}: {}% otrzymanych serduszek'
        self.show_plot(self.received_to_given_hearts(), title, x_label)

    def questions_to_answers_per_person_show(self):
        title = '% zadanych pytań względem wszystkich wysłanych przez siebie wiadomości'
        x_label = 'Największy stosunek pytań do wszystkich swoich wiadomości ma {}: {}% pytań'
        self.show_plot(self.questions_to_answers_per_person(), title, x_label)

    def xd_to_no_xd_per_person_show(self):
        title = '% wysłanych "XD" względem wszystkich wysłanych przez siebie wiadomości'
        x_label = 'Największy stosunek "XD" do wszystkich swoich wiadomości ma {}: {}% "XD"'
        self.show_plot(self.xd_to_no_xd_per_person(), title, x_label)

    def most_only_question_giver_show(self):
        title = 'Wysłane "?" z wszystkich {} wiadomości będących tylko znakami zapytania'.\
            format(self.only_question_total())
        x_label = 'Najwięcej samych "?" od {}: {}'
        self.show_plot(self.most_only_question_giver(), title, x_label)


class Show(ConversationPeopleShow, GeneralShow):
    def __init__(self, conversation_info):
        super().__init__(conversation_info)
