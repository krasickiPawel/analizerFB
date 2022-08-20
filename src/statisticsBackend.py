class OperationTemplates:
    @staticmethod
    def sort_dict(unsorted_dict):
        sorted_list = sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=True)[:40]
        return {pair[0][:24]: pair[1] for pair in sorted_list}

    @staticmethod
    def prepare_dict(tuple_list):
        listDict = {}
        for name, amount in tuple_list:
            listDict.setdefault(name, []).append(amount)
        return {person: sum(listDict.get(person)) for person in listDict}

    @staticmethod
    def received_to_received_plus_given_in_percent(received, given):
        names = list(received.keys())
        given_to_received = [(name, int(100 * (received.get(name) / (received.get(name) + given.get(name))))) for name
                             in names if given.get(name) is not None and received.get(name) is not None]
        return OperationTemplates.sort_dict(OperationTemplates.prepare_dict(given_to_received))


class TotalOperationTemplates:
    def __init__(self, people_conversation_list):
        self.people_conversation_list = people_conversation_list

    def photo_video_template(self, photo_video):  # podział na ogólne i moje ze względu większej wydajności
        total = 0  # (contains dla ogólnych się nie wykonuje wiec szybciej)
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get(photo_video) is not None:
                    total += len(message_dict.get(photo_video))
        return total

    def my_photo_video_template(self, photo_video, name="Pawel Krasicki"):  # dodac funkcjonalnosc na wpisywanie imienia
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for messageDict in conversation.messages:
                if messageDict.get(photo_video) is not None and messageDict.get("sender_name") == name:
                    total += len(messageDict.get(photo_video))
        return total

    def reactions_template(self, r):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("reactions") is not None:
                    for reaction in message_dict.get('reactions'):
                        if reaction.get("reaction").__contains__(r):
                            total += 1
        return total

    def my_reactions_given_template(self, r, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None:
                    for reaction in messageDict.get('reactions'):
                        if reaction.get("reaction").__contains__(r) and reaction.get("actor") == name:
                            total += 1
        return total

    def my_reactions_received_template(self, r, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("reactions") is not None and messageDict.get("sender_name") == name:
                    for reaction in messageDict.get('reactions'):
                        if reaction.get("reaction").__contains__(r):
                            total += 1
        return total

    def content_template(self, word):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("content").lower().__contains__(word):
                    total += 1
        return total

    def my_content_template(self, word, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("content").lower().__contains__(word) \
                        and messageDict.get("sender_name") == name:
                    total += 1
        return total


class Total(TotalOperationTemplates):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def messenger_sent_total(self):
        return sum([len(conversation.messages) for conversation in self.people_conversation_list.conversations])

    def messenger_text_messages_sent_total(self):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("content") is not None:
                    total += 1
        return total

    def my_text_messages_sent_total(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("content") is not None and message_dict.get("sender_name") == name:
                    total += 1
        return total

    def messenge_avg_message_len(self):
        messages_len = []
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("content") is not None:
                    messages_len.append(len(message_dict.get("content")))
        return int(sum(messages_len) / len(messages_len)) if len(messages_len) > 0 else 0

    def my_avg_message_len(self, name="Pawel Krasicki"):
        messagesLen = []
        for conversation in self.people_conversation_list.conversations:
            for messageDict in conversation.messages:
                if messageDict.get("content") is not None and messageDict.get("sender_name") == name:
                    messagesLen.append(len(messageDict.get("content")))
        return int(sum(messagesLen) / len(messagesLen)) if len(messagesLen) > 0 else 0

    def messenger_reactions_total(self):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("reactions") is not None:
                    total += len(message_dict.get("reactions"))
        return total

    def messenger_unsent_total(self):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("is_unsent") is not None and message_dict.get("is_unsent"):
                    total += 1
        return total

    def my_unsent_total(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("is_unsent") is not None and message_dict.get("is_unsent") and \
                        message_dict.get("sender_name") == name:
                    total += 1
        return total

    def questions_to_all_percent(self):
        return int(
            100 * (self.questions_total() / self.messenger_sent_total())) if self.messenger_sent_total() > 0 else 0

    def xd_to_all_percent(self):
        return int(100 * (self.xd_total() / self.messenger_sent_total())) if self.messenger_sent_total() > 0 else 0

    def photo_total(self):
        return self.photo_video_template("photos")

    def video_total(self):
        return self.photo_video_template("videos")

    def multimedia_total(self):
        return self.video_total() + self.photo_total()

    def hearts_total(self):
        return self.reactions_template('❤')

    def haha_total(self):
        return self.reactions_template('😆')

    def wow_total(self):
        return self.reactions_template('😮')

    def eye_hearts_total(self):
        return self.reactions_template('😍')

    def thumbs_total(self):
        return self.reactions_template('👍')

    def hearts_received_total(self):
        return self.reactions_template('❤')

    def haha_received_total(self):
        return self.reactions_template('😆')

    def wow_received_total(self):
        return self.reactions_template('😮')

    def eye_hearts_received_total(self):
        return self.reactions_template('😍')

    def thumbs_received_total(self):
        return self.reactions_template('👍')

    def xd_total(self):
        return self.content_template("xd")

    def love_total(self):
        return self.content_template('❤') + self.content_template('💕')

    def questions_total(self):
        return self.content_template("?")

    def omg_total(self):
        return self.content_template("omg")

    def given_word_total(self, word):
        return self.content_template(word)

    def haha_word_total(self):
        return self.content_template("haha")

    def my_sent_total(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("sender_name") == name:
                    total += 1
        return total

    def my_reactions_total(self, name="Pawel Krasicki"):
        total = 0
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("reactions") is not None and message_dict.get("sender_name") == name:
                    total += len(message_dict.get("reactions"))
        return total

    def my_photo_total(self, name):
        return self.my_photo_video_template("photos", name)

    def my_video_total(self, name):
        return self.my_photo_video_template("videos", name)

    def my_multimedia_total(self, name):
        return self.my_video_total(name) + self.my_photo_total(name)

    def my_hearts_received(self, name):
        return self.my_reactions_received_template('❤', name)

    def my_haha_received(self, name):
        return self.my_reactions_received_template('😆', name)

    def my_wow_received(self, name):
        return self.my_reactions_received_template('😮', name)

    def my_eyes_received(self, name):
        return self.my_reactions_received_template('😍', name)

    def my_likes_received(self, name):
        return self.my_reactions_received_template('👍', name)

    def my_hearts_given(self, name):
        return self.my_reactions_given_template('❤', name)

    def my_haha_given(self, name):
        return self.my_reactions_given_template('😆', name)

    def my_wow_given(self, name):
        return self.my_reactions_given_template('😮', name)

    def my_eyes_given(self, name):
        return self.my_reactions_given_template('😍', name)

    def my_likes_given(self, name):
        return self.my_reactions_given_template('👍', name)

    def my_xd_total(self, name):
        return self.my_content_template("xd", name)

    def my_questions_total(self, name):
        return self.my_content_template("?", name)

    def my_omg_total(self, name):
        return self.my_content_template("omg", name)

    def my_given_word_total(self, word, name):
        return self.my_content_template(word, name)

    def my_questions_to_all_percent(self, name):
        return int(100 * (self.my_questions_total(name) / self.my_sent_total(name))) if self.my_sent_total() > 0 else 0

    def my_xd_to_all_percent(self, name):
        return int(100 * (self.my_xd_total(name) / self.my_sent_total(name))) if self.my_sent_total() > 0 else 0


class ComparePeopleOperationTemplates(OperationTemplates):
    def __init__(self, people_conversation_list):
        self.people_conversation_list = people_conversation_list

    def compare_word_amount(self, word):
        xd_amount = []
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("content") is not None and message_dict.get("content").lower().__contains__(word):
                    xd_amount.append((conversation.title, 1))
        return self.sort_dict(self.prepare_dict(xd_amount))

    def compare_photo_video_amount(self, photo, video='brak parametru'):
        photo_video_amount = []
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get(photo) is not None:
                    photo_video_amount.append((conversation.title, 1))
                if message_dict.get(video) is not None:
                    photo_video_amount.append((conversation.title, 1))
        return self.sort_dict(self.prepare_dict(photo_video_amount))

    def compare_reactions_amount(self, reaction1, reaction2='brak parametru'):
        reactionList = []
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("reactions") is not None:
                    for reaction in message_dict.get("reactions"):
                        if reaction.get("reaction").__contains__(reaction1) or \
                                reaction.get('reaction').__contains__(reaction2):
                            reactionList.append((conversation.title, 1))
        return self.sort_dict(self.prepare_dict(reactionList))


class ComparePeople(ComparePeopleOperationTemplates):
    def __init__(self, people_conversation_list):
        super().__init__(people_conversation_list)

    def compare_message_amount(self):
        message_len_per_person = [(conversation.title, len(conversation.messages)) for conversation in
                                  self.people_conversation_list.conversations]
        return self.sort_dict(self.prepare_dict(message_len_per_person))

    def compare_photo_amount(self):
        return self.compare_photo_video_amount('photos')

    def compare_video_amount(self):
        return self.compare_photo_video_amount('videos')

    def compare_multimedia_amount(self):
        return self.compare_photo_video_amount('photos', 'videos')

    def compare_xd_amount(self):
        return self.compare_word_amount("xd")

    def compare_haha_word_amount(self):
        return self.compare_word_amount("haha")

    def compare_omg_amount(self):
        return self.compare_word_amount("omg")

    def compare_love_amount(self):
        love_amount = []
        for conversation in self.people_conversation_list.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("content") is not None and (message_dict.get("content").__contains__('❤') or
                                                                message_dict.get("content").__contains__('💕')):
                    love_amount.append((conversation.title, 1))
        return self.sort_dict(self.prepare_dict(love_amount))

    def compare_given_word_amount(self, word=""):
        return self.compare_word_amount(word)

    def compare_hearts_amount(self):
        return self.compare_reactions_amount('❤', '💕')

    def compare_haha_amount(self):
        return self.compare_reactions_amount('😂', '😆')

    def compare_likes_amount(self):
        return self.compare_reactions_amount('👍')

    def compare_wow_amount(self):
        return self.compare_reactions_amount('😮')

    def compare_eyes_amount(self):
        return self.compare_reactions_amount('😍')


class AboutMe(OperationTemplates):
    def __init__(self, people_conversation_list):
        self.peopleConversationList = people_conversation_list

    def compare_my_word_usage(self, name="Pawel Krasicki"):  # counter koniecznie zliczający listę wszystkich moich słów
        my_word_list = []
        for conversation in self.peopleConversationList.conversations:
            for message_dict in conversation.messages:
                if message_dict.get("content") is not None and message_dict.get("sender_name") == name:
                    for word in message_dict.get("content").split():
                        my_word_list.append((word, 1))
        return self.sort_dict(self.prepare_dict(my_word_list))
