from statisticsBackend import OperationTemplates


class ConversationOperationTemplates(OperationTemplates):
    def __init__(self, conversation_info):
        self.conversation_info = conversation_info

    def specific_reaction_total(self, reaction1, reaction2="brak reakcji"):
        lists_list = [message.get("reactions") for message in self.conversation_info.messages if
                      message.get("reactions") is not None]
        amount = 0
        for reaction_list in lists_list:
            for reaction in reaction_list:
                if reaction.get("reaction").__contains__(reaction1) or reaction.get("reaction").__contains__(reaction2):
                    amount += 1
        return amount

    def most_specific_reaction_giver(self, reaction1, reaction2="brak reakcji"):
        reactions_list_list = [message.get("reactions") for message in self.conversation_info.messages
                               if message.get("reactions") is not None]
        names_heart_reactions_list = []
        for reactions_list in reactions_list_list:
            for reactions in reactions_list:
                if reactions.get("reaction").__contains__(reaction1) or reactions.get("reaction").__contains__(
                        reaction2):
                    names_heart_reactions_list.append((reactions.get("actor"), 1))
        return self.sort_dict(self.prepare_dict(names_heart_reactions_list))

    def most_specific_reaction_receiver(self, reaction1, reaction2="brak reakcji"):
        names_reactions_list = [(message.get("sender_name"), len([reaction for reaction in message.get("reactions") if
                                                                  (reaction.get("reaction").__contains__(reaction1) or
                                                                   reaction.get("reaction").__contains__(reaction2))]))
                                for message in self.conversation_info.messages if message.get("reactions") is not None]
        return self.sort_dict(self.prepare_dict(names_reactions_list))

    def most_content_giver(self, word=""):
        word_message_senders = [(message.get("sender_name"), 1) for message in
                                self.conversation_info.messages if message.get("content") is not None and
                                message.get("content").lower().__contains__(word)]
        return self.sort_dict(self.prepare_dict(word_message_senders))

    def least_content_giver(self, word=""):
        wordMessageSenders = [(message.get("sender_name"), 1) for message in
                              self.conversation_info.messages if message.get("content") is None or not
                              message.get("content").lower().__contains__(word)]
        return self.sort_dict(self.prepare_dict(wordMessageSenders))

    def content_total(self, word=""):
        return len([message.get("content") for message in self.conversation_info.messages
                    if message.get("content") is not None and message.get("content").__contains__(word)])

    def content_list(self):
        return [message.get("content") for message in self.conversation_info.messages
                if message.get("content") is not None]

    def photo_video_total(self, photo_video):
        return sum([len(message.get(photo_video)) for message in self.conversation_info.messages
                    if message.get(photo_video) is not None])


class GeneralInfo(ConversationOperationTemplates):
    def __init__(self, conversation_info):
        super().__init__(conversation_info)

    def messages_total(self):
        return len(self.conversation_info.messages)

    def avg_message_amount_per_person(self):
        return int(len(self.conversation_info.messages) / len(self.conversation_info.participants)) if \
            len(self.conversation_info.participants) > 0 else 0

    def photo_total(self):
        return self.photo_video_total("photos")

    def video_total(self):
        return self.photo_video_total("videos")

    def multimedia_total(self):
        return self.photo_total() + self.video_total()

    def avg_message_length(self):
        messagesLen = [len(message.get("content")) for message in self.conversation_info.messages
                       if message.get("content") is not None]
        return int(sum(messagesLen) / len(messagesLen)) if len(messagesLen) > 0 else 0

    def reaction_total(self):
        return sum([len(message.get("reactions")) for message in self.conversation_info.messages
                    if message.get("reactions") is not None])

    def text_messages_total(self):
        return len(self.content_list())

    def xd_conversation_total(self):
        return self.content_total("xd")

    def questions_total(self):
        return self.content_total("?")

    def omg_total(self):
        return self.content_total("omg")

    def hearts_writen_total(self):
        return self.content_total('❤') + self.content_total('💕')

    def given_word_total(self, word):  # np Patron
        return self.content_total(word)

    def multimedia_reactions_total(self):
        names_reactions_multimedia_list = [(message.get("sender_name"), len(message.get("reactions"))) for message
                                           in self.conversation_info.messages if
                                           message.get("reactions") is not None and
                                           (message.get("videos") is not None or message.get("photos") is not None)]
        return sum([reaction_tuple[1] for reaction_tuple in names_reactions_multimedia_list])

    def unsent_total(self):
        return len([message.get("sender_name") for message in self.conversation_info.messages
                    if message.get("is_unsent")])

    def hearts_total(self):
        return self.specific_reaction_total('❤', '💕')

    def haha_total(self):
        return self.specific_reaction_total('😂', '😆')

    def thumbs_total(self):
        return self.specific_reaction_total('👍')

    def wow_total(self):
        return self.specific_reaction_total('😮')

    def hearts_in_eyes_total(self):
        return self.specific_reaction_total('😍')

    def word_total(self):
        return sum([len(content.split()) for content in self.content_list()])

    def char_total(self):
        return sum([len(message.get("content")) for message in self.conversation_info.messages
                    if message.get("content") is not None])

    def only_question_total(self):
        return len([None for message in self.conversation_info.messages if message.get("content") is not None and
                    message.get("content").__eq__("?")])

    def questions_to_all_percent(self):
        return int(100 * (self.questions_total() / self.messages_total())) if self.messages_total() > 0 else 0

    def xd_to_all_percent(self):
        return int(100 * (self.xd_conversation_total() / self.messages_total())) if self.messages_total() > 0 else 0

    def given_to_all_percent(self, word):
        return int(100 * (self.given_word_total(word) / self.messages_total())) if self.messages_total() > 0 else 0


class AnalConversation(ConversationOperationTemplates):
    def __init__(self, conversation_info):
        super().__init__(conversation_info)

    def most_messages_sent(self):
        names_amount = [(message.get("sender_name"), 1) for message in self.conversation_info.messages]
        return self.sort_dict(self.prepare_dict(names_amount))

    def most_reaction_receiver(self):
        names_reactions_list = [(message.get("sender_name"), len(message.get("reactions"))) for message
                                in self.conversation_info.messages if message.get("reactions") is not None]
        return self.sort_dict(self.prepare_dict(names_reactions_list))

    def most_reaction_giver(self):
        reactions_list_list = [message.get("reactions") for message in self.conversation_info.messages
                               if message.get("reactions") is not None]
        names_reactions_list = []
        for reactions_list in reactions_list_list:
            for reactions in reactions_list:
                names_reactions_list.append((reactions.get("actor"), 1))
        return self.sort_dict(self.prepare_dict(names_reactions_list))

    def most_photo_sent(self):
        names_photos_list = [(message.get("sender_name"), len(message.get("photos"))) for message in
                             self.conversation_info.messages if message.get("photos") is not None]
        return self.sort_dict(self.prepare_dict(names_photos_list))

    def most_video_sent(self):
        names_videos_list = [(message.get("sender_name"), len(message.get("videos"))) for message
                             in self.conversation_info.messages if message.get("videos") is not None]
        return self.sort_dict(self.prepare_dict(names_videos_list))

    def most_multimedia_sent(self):
        names_videos_list = [(message.get("sender_name"), len(message.get("videos"))) for message
                             in self.conversation_info.messages if message.get("videos") is not None]
        names_photos_list = [(message.get("sender_name"), len(message.get("photos"))) for message
                             in self.conversation_info.messages if message.get("photos") is not None]
        names_videos_list.extend(names_photos_list)
        return self.sort_dict(self.prepare_dict(names_videos_list))

    def most_multimedia_reactions_receiver(self):
        names_reactions_list = [(message.get("sender_name"), len(message.get("reactions"))) for message
                                in self.conversation_info.messages if message.get("reactions") is not None and
                                (message.get("videos") is not None or message.get("photos") is not None)]
        return self.sort_dict(self.prepare_dict(names_reactions_list))

    def most_multimedia_reactions_giver(self):
        reaction_list_list = [message.get("reactions") for message in self.conversation_info.messages
                              if message.get("reactions") is not None and (message.get("photos") is not None
                                                                           or message.get("videos") is not None)]
        names_multimedia_reactions_list = []
        for reactionList in reaction_list_list:
            for reaction in reactionList:
                names_multimedia_reactions_list.append((reaction.get("actor"), 1))
        return self.sort_dict(self.prepare_dict(names_multimedia_reactions_list))

    def most_char_writen(self):
        names_lengths_list = [(message.get("sender_name"), len(message.get("content"))) for message in
                              self.conversation_info.messages if message.get("content") is not None]
        return self.sort_dict(self.prepare_dict(names_lengths_list))

    def most_person_message_length(self):
        messages_per_person = self.most_messages_sent()
        char_sent_per_person = self.most_char_writen()
        names = list(messages_per_person.keys())
        avg_msg_len_per_person = [(name, int(char_sent_per_person.get(name) / messages_per_person.get(name))) for name
                                  in names
                                  if char_sent_per_person.get(name) is not None and messages_per_person.get(
                name) is not None]
        return self.sort_dict(self.prepare_dict(avg_msg_len_per_person))

    def most_xd_sent(self):
        return self.most_content_giver("xd")

    def most_love(self):
        word_message_senders = [(message.get("sender_name"), 1) for message in
                                self.conversation_info.messages if message.get("content") is not None and
                                (message.get("content").lower().__contains__('❤') or
                                 message.get("content").lower().__contains__('💕'))]
        return self.sort_dict(self.prepare_dict(word_message_senders))

    def least_xd_sent(self):
        return self.least_content_giver("xd")

    def most_question_giver(self):
        return self.most_content_giver("?")

    def least_question_giver(self):
        return self.least_content_giver("?")

    def most_omg_giver(self):
        return self.most_content_giver("omg")

    def most_given_word_giver(self, word):
        return self.most_content_giver(word)

    def most_hearts_giver(self):
        return self.most_specific_reaction_giver('❤', '💕')

    def most_hearts_receiver(self):
        return self.most_specific_reaction_receiver('❤', '💕')

    def most_unsent_giver(self):
        unsent_list = [(message.get("sender_name"), 1) for message in self.conversation_info.messages
                       if message.get("is_unsent")]
        return self.sort_dict(self.prepare_dict(unsent_list))

    def most_haha_giver(self):
        return self.most_specific_reaction_giver('😂', '😆')

    def most_haha_receiver(self):
        return self.most_specific_reaction_receiver('😂', '😆')

    def received_to_given_reactions(self):
        given = self.most_reaction_giver()
        received = self.most_reaction_receiver()
        return self.received_to_received_plus_given_in_percent(received, given)

    def received_to_given_hearts(self):
        given = self.most_hearts_giver()
        received = self.most_hearts_receiver()
        return self.received_to_received_plus_given_in_percent(received, given)

    def questions_to_answers_per_person(self):
        questions = self.most_question_giver()
        answers = self.least_question_giver()
        return self.received_to_received_plus_given_in_percent(questions, answers)

    def xd_to_no_xd_per_person(self):
        xd = self.most_xd_sent()
        no_xd = self.least_xd_sent()
        return self.received_to_received_plus_given_in_percent(xd, no_xd)

    def most_only_question_giver(self):
        only_question_marks = [(message.get("sender_name"), 1) for message in
                               self.conversation_info.messages if message.get("content") is not None and
                               message.get("content")[0] == "?"]
        return self.sort_dict(self.prepare_dict(only_question_marks))
