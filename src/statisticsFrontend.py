import matplotlib.pyplot as plt
from statisticsBackend import ComparePeople, Total, AboutMe


class PlotShow:
    @staticmethod
    def show_plot(sorted_dict, title_text, x_label_text):
        def first_value(a):
            return a[0] if len(a) > 0 else 0
        plt.figure(figsize=(10, 7.25))
        plt.title(title_text)
        x_person = list(sorted_dict.keys())
        y = list(sorted_dict.values())
        x = [x_person[i] + " " + str(y[i]) for i in range(len(x_person))]
        plt.bar(x, y)
        plt.xticks(x, x, rotation='vertical')
        plt.margins(0.01)
        plt.subplots_adjust(bottom=0.42)
        plt.xlabel(x_label_text.format(first_value(x_person), first_value(y)))
        plt.show()


class AboutMeShow(AboutMe, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def compare_my_word_usage_show(self, name="Pawel Krasicki"):
        title = 'Najczęściej używane przez ciebie słowa'
        xLabel = 'Najczęściej używasz "{}": {}'
        self.show_plot(self.compare_my_word_usage(name), title, xLabel)


class MyTotalShow(Total, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def my_general_info_show(self, name):
        plt.figure(figsize=(8, 5))
        plt.suptitle('Statystyki tego co {} napisał(a) na całym messengerze'.format(name))
        messages_number = "{} wiadomości \n".format(self.my_sent_total(name))
        text_messages_total = "Wiadomości tekstowych: {} \n".format(self.my_text_messages_sent_total(name))
        avg_message_length = "Średnia długość wiadomości: {} znaków \n".format(self.my_avg_message_len(name))
        xd_total = 'Ilość wszystkich "XD": {}\n'.format(self.my_xd_total(name))
        multimedia_total = "Wszystkich multimediów: {} \n".format(self.my_multimedia_total(name))
        photo_total = "   Zdjęć: {} \n".format(self.my_photo_total(name))
        video_total = "   Filmików: {} \n".format(self.my_video_total(name))
        reactions_total = "Wszystkich reakcji: {} \n".format(self.my_reactions_total(name))
        hearts_total_g = "   Serduszek danych: {}\n".format(self.my_hearts_given(name))
        hearts_total_r = "   Serduszek otrzymanych {}\n".format(self.my_hearts_received(name))
        haha_total_g = "   Emotek śmiechu danych: {}\n".format(self.my_haha_given(name))
        haha_total_r = "   Emotek śmiechu otrzymanych: {}\n".format(self.my_haha_received(name))
        thumbs_total_g = "   Kciuków w górę danych: {}\n".format(self.my_likes_given(name))
        thumbs_total_r = "   Kciuków w górę otrzymanych: {}\n".format(self.my_likes_received(name))
        eyes_total_g = '   Serduszek w oczach danych: {}\n'.format(self.my_eyes_given(name))
        eyes_total_r = '   Serduszek w oczach otrzymanych: {}\n'.format(self.my_eyes_received(name))
        wow_total_g = "   Reakcji wow danych: {}\n".format(self.my_wow_given(name))
        wow_total_r = "   Reakcji wow otrzymanych: {}\n".format(self.my_wow_received(name))
        unsent_total = "Usuniętych wiadomości: {}\n".format(self.my_unsent_total(name))
        questions = "Zadanych pytań: {}\n".format(self.my_questions_total(name))
        questions_percent = "Stosunek pytań do wszystkich wiadomości: {}%\n".\
            format(self.my_questions_to_all_percent(name))
        xd_to_all_percent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.my_xd_to_all_percent(name))
        plt.figtext(0.1, 0.08, messages_number + avg_message_length + text_messages_total +
                    multimedia_total + photo_total + video_total + questions +
                    xd_total + unsent_total + reactions_total + hearts_total_g + hearts_total_r + haha_total_g +
                    haha_total_r + thumbs_total_g + thumbs_total_r + eyes_total_g + eyes_total_r + wow_total_g +
                    wow_total_r + questions_percent + xd_to_all_percent)
        plt.show()

    def my_pie_show(self, name):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle('Statystyka wiadomości wysłanych przez {}'.format(name))
        plt.subplot(3, 2, 1)
        self.my_xd_pie(name)
        plt.subplot(3, 2, 2)
        self.my_multimedia_pie(name)
        plt.subplot(3, 2, 3)
        self.my_emoticon_pie(name)
        plt.subplot(3, 2, 4)
        self.my_emoticon_pie2(name)
        plt.subplot(3, 2, 5)
        self.my_question_pie(name)
        plt.subplot(3, 2, 6)
        self.my_received_to_given_reactions_pie(name)
        plt.show()

    def my_xd_pie(self, name):
        x = ['"XD"', 'wiadomości bez "XD"']
        y = [self.my_xd_total(name), self.my_text_messages_sent_total(name) - self.my_xd_total(name)]
        return plt.pie(y, labels=x, startangle=0)

    def my_multimedia_pie(self, name):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.my_multimedia_total(name), self.my_text_messages_sent_total(name)]
        return plt.pie(y2, labels=x2)

    def my_emoticon_pie(self, name):
        plt.title("Otrzymane reakcje")
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.my_hearts_received(name), self.my_eyes_received(name), self.my_likes_received(name),
             self.my_haha_received(name), self.my_wow_received(name)]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def my_emoticon_pie2(self, name):
        plt.title("Dane reakcje")
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.my_hearts_given(name), self.my_eyes_given(name), self.my_likes_given(name),
             self.my_haha_given(name), self.my_wow_given(name)]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def my_question_pie(self, name):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.my_questions_total(name), self.my_text_messages_sent_total(name) - self.my_questions_total(name)]
        return plt.pie(y2, labels=x2)

    def my_received_to_given_reactions_pie(self, name):
        x = ['otrzymane reakcje', 'dane reakcje']
        y = [self.my_reactions_received_template("", name), self.my_reactions_given_template("", name)]
        return plt.pie(y, labels=x)


class TotalShow(Total, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def general_info_show(self):
        plt.figure(figsize=(8, 5))
        plt.suptitle('Statystyki całego Twojego messengera')
        messages_number = "{} wiadomości \n".format(self.messenger_sent_total())
        text_messages_total = "Wiadomości tekstowych: {} \n".format(self.messenger_text_messages_sent_total())
        avg_message_length = "Średnia długość wiadomości: {} znaków \n".format(self.messenge_avg_message_len())
        xd_total = 'Ilość wszystkich "XD": {}\n'.format(self.xd_total())
        multimedia_total = "Wszystkich multimediów: {} \n".format(self.multimedia_total())
        photo_total = "   Zdjęć: {} \n".format(self.photo_total())
        video_total = "   Filmików: {} \n".format(self.video_total())
        reactions_total = "Wszystkich reakcji: {} \n".format(self.messenger_reactions_total())
        hearts_total = "   Serduszek: {}\n".format(self.hearts_total())
        haha_total = "   Emotek śmiechu: {}\n".format(self.haha_total())
        thumbs_total = "   Kciuków w górę: {}\n".format(self.thumbs_total())
        eyes_total = '   Serduszek w oczach: {}\n'.format(self.eye_hearts_total())
        wow_total = "   Reakcji wow: {}\n".format(self.wow_total())
        unsent_total = "Usuniętych wiadomości: {}\n".format(self.messenger_unsent_total())
        questions = "Zadanych pytań: {}\n".format(self.questions_total())
        questions_percent = "Stosunek pytań do wszystkich wiadomości: {}%\n".format(self.questions_to_all_percent())
        xd_to_all_percent = 'Stosunek "XD" do wszystkich wiadomości: {}%\n'.format(self.xd_to_all_percent())
        plt.figtext(0.1, 0.2, messages_number + avg_message_length + text_messages_total +
                    multimedia_total + photo_total + video_total + questions +
                    xd_total + unsent_total + reactions_total + hearts_total + haha_total + wow_total +
                    thumbs_total + eyes_total + questions_percent + xd_to_all_percent)
        plt.show()

    def pie_show(self):
        plt.figure(figsize=(12, 6.5))
        plt.suptitle('Statystyka całego Twojego messengera')
        plt.subplot(2, 2, 1)
        self.xd_pie()
        plt.subplot(2, 2, 2)
        self.multimedia_pie()
        plt.subplot(2, 2, 3)
        self.emoticon_pie()
        plt.subplot(2, 2, 4)
        self.question_pie()
        plt.show()

    def xd_pie(self):
        x = ['"XD"', 'wiadomości bez "XD"']
        y = [self.xd_total(), self.messenger_text_messages_sent_total() - self.xd_total()]
        return plt.pie(y, labels=x, startangle=0)

    def multimedia_pie(self):
        x2 = ['zdjęcia i filmiki', 'wiadomości tekstowe']
        y2 = [self.multimedia_total(), self.messenger_text_messages_sent_total()]
        return plt.pie(y2, labels=x2)

    def emoticon_pie(self):
        x = ['serduszka ❤', 'serduszka w oczach', 'kciuki', 'haha', 'wow']
        y = [self.hearts_total(), self.eye_hearts_total(), self.thumbs_total(), self.haha_total(), self.wow_total()]
        return plt.pie(y, labels=x, startangle=0) if sum(y) > 0 else None

    def question_pie(self):
        x2 = ['pytania', 'wiadomości bez pytań']
        y2 = [self.questions_total(), self.messenger_text_messages_sent_total() - self.questions_total()]
        return plt.pie(y2, labels=x2)


class ComparePeopleShow(Total, ComparePeople, PlotShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def compare_message_amount_show(self):
        title = "Ilość wiadomości z daną osobą z {} wszystkich wiadomości".format(self.messenger_sent_total())
        x_label = "Najwięcej wiadomości z {}: {}"
        self.show_plot(self.compare_message_amount(), title, x_label)

    def compare_multimedia_amount_show(self):
        title = "Ilość zjęć i filmików z daną osobą z {} wszystkich multimediów".format(self.multimedia_total())
        x_label = "Najwięcej zdjęć i filmików z {}: {}"
        self.show_plot(self.compare_multimedia_amount(), title, x_label)

    def compare_photo_amount_show(self):
        title = "Ilość zdjęć z daną osobą z {} wszystkich zdjęć".format(self.photo_total())
        x_label = "Najwięcej zdjęć z {}: {}"
        self.show_plot(self.compare_photo_amount(), title, x_label)

    def compare_video_amount_show(self):
        title = "Ilość filmików z daną osobą z {} wszystkich filmików".format(self.video_total())
        x_label = "Najwięcej zdjęć z {}: {}"
        self.show_plot(self.compare_video_amount(), title, x_label)

    def compare_xd_amount_show(self):
        title = 'Ilość "XD" z daną osobą z {} wszystkich "XD"'.format(self.xd_total())
        x_label = 'Najwięcej "XD" z {}: {}'
        self.show_plot(self.compare_xd_amount(), title, x_label)

    def compare_haha_word_amount_show(self):
        title = 'Ilość napisanych "haha" z daną osobą z {} wszystkich "haha"'.format(self.haha_word_total())
        x_label = 'Najwięcej tekstowych "haha" z {}: {}'
        self.show_plot(self.compare_haha_word_amount(), title, x_label)

    def compare_given_word_amount_show(self, word=""):
        title = 'Ilość "{}" z daną osobą'.format(word)
        x_label = 'Najwięcej "{word1}" z {blank1}: {blank2}'.format(word1=word, blank1='{}', blank2='{}')
        self.show_plot(self.compare_given_word_amount(word), title, x_label)

    def compare_love_amount_show(self):
        title = 'Ilość wysłanych serduszek (nie reakcji) z daną osobą z {} wszystkich serduszek'.format(self.love_total())
        x_label = 'Najwięcej wysłanych wiadomości z serduszkami z {}: {}'
        self.show_plot(self.compare_love_amount(), title, x_label)

    def compareOmgAmountShow(self):
        title = 'Ilość napisanych "omg" z daną osobą z {} wszystkich "omg"'.format(self.omg_total())
        x_label = 'Najwięcej "omg" z {}: {}'
        self.show_plot(self.compare_omg_amount(), title, x_label)

    def compare_hearts_amount_show(self):
        title = 'Wysłanych serduszek z daną osobą z wszystkich {} serduszek'.format(self.hearts_total())
        x_label = 'Najwięcej serduszek z {}: {}'
        self.show_plot(self.compare_hearts_amount(), title, x_label)

    def compare_haha_amount_show(self):
        title = 'Wysłanych emotek "haha" z daną osobą z wszystkich {} emotek"haha"'.format(self.haha_total())
        x_label = 'Najwięcej "haha" z {}: {}'
        self.show_plot(self.compare_haha_amount(), title, x_label)

    def compare_wow_amount_show(self):
        title = 'Wysłanych "wow" z daną osobą z wszystkich {} "wow"'.format(self.wow_total())
        x_label = 'Najwięcej "wow" z {}: {}'
        self.show_plot(self.compare_wow_amount(), title, x_label)

    def compare_likes_amount_show(self):
        title = 'Wysłanych lajków z daną osobą z wszystkich {} lajków'.format(self.thumbs_total())
        x_label = 'Najwięcej lajków z {}: {}'
        self.show_plot(self.compare_likes_amount(), title, x_label)

    def compare_eyes_amount_show(self):
        title = 'Wysłanych serduszek w oczach z daną osobą z wszystkich {} buziek z serduszkami w oczach'.format(
            self.eye_hearts_total())
        x_label = 'Najwięcej serduszek w oczach z {}: {}'
        self.show_plot(self.compare_eyes_amount(), title, x_label)


class HorrorShow(TotalShow, AboutMeShow, MyTotalShow, ComparePeopleShow):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)
