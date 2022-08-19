from tkinter import PhotoImage, Toplevel, StringVar, HORIZONTAL, Label, Tk, filedialog, Button, Entry, messagebox
from tkinter.ttk import Progressbar
from conversationStatisticsFrontend import Show
from statisticsFrontend import HorrorShow
from fileReader import multi_directory_read, directoryRead
from threading import Thread


class FrontendWindow:
    def __init__(self):
        self.file_loading_window = None
        self.statistics_window = None
        self.people_comparison = None
        self.conversation = None
        self.title = 'analFB'
        self.start_window = self.starter()

    def starter(self):
        window = Tk()
        icon = PhotoImage(file='analFB logo.png')
        window.title(self.title)
        window.iconphoto(True, icon)
        text_label = Label(text="Wybierz co chcesz zrobić", font=('Arial', 12))
        text_label.pack(pady=10)
        all_conv = Button(window, text="Przeanalizuj wszystkie konwersacje na tle innych konwersacji",
                         command=self.chooseInbox)
        all_conv.pack(pady=5)
        Label(text="(wskaż folder inbox)", font=('Arial', 7)).pack()
        conv = Button(window, text="Przeanalizuj ludzi w danej konwersacji", command=self.choose_conversation)
        conv.pack(pady=5)
        Label(text="(wskaż folder danej konwersacji)", font=('Arial', 7)).pack()
        info_button = Button(window, text="Instrukcja", command=self.info)
        info_button.pack(pady=5)
        sign_label = Label(text="Created by Paweł Krasicki 2021", font=('Calibri', 8), fg='grey')
        sign_label.pack(pady=15)
        window.geometry("350x230")
        return window

    def info(self):
        info_window = Toplevel()
        info_window.title(self.title)
        infoText = 'W celu uruchomienia analizy wiadomości konieczne jest pobranie z Facebooka\n' \
                   'pliku JSON z kopią danych m.in. wiadomości. Aby to zrobić należy\n' \
                   'na Facebooku wejść w Ustawienia i prywatność -> Ustawienia ->\n' \
                   'Twoje informacje na Facebooku -> Pobieranie Twoich informacji,\n' \
                   'a następnie wybrać okres, FORMAT JSON i zaznaczyć wiadomości.\n' \
                   'Po kliknięciu "Utwórz plik", po pewnym czasie (kilka godzin, zależy od zakresu dat)\n' \
                   'przyjdzie powiadomienie z plikiem do pobrania. Pobrany plik wypakowujemy.\n' \
                   'Gotowe. Teraz w programie wskazujemy folder "inbox" lub w przypadku\n' \
                   'analizy konkretnej konwersacji wskazujemy folder konwersacji w folderze inbox.\n\n' \
                   'Pamiętaj, aby nie zostawiać pustych pól przewidzianych do wprowadzenia tekstu.\n\n' \
                   'Miłego analizowania!\n' \
                   'Paweł Krasicki.'
        Label(info_window, text=infoText, font=("Consolas", 12)).pack(pady=50, padx=50)
        info_window.wait_window()

    def prepare_loading_window(self, pathVariable):
        window = Toplevel()
        window.title(self.title)
        bar = Progressbar(window, orient=HORIZONTAL, length=400)
        bar.pack(pady=10)
        Label(window, textvariable=pathVariable).pack()
        window.geometry("500x100")
        return window, bar

    def chooseInbox(self):
        path_variable = StringVar()
        inbox = filedialog.askdirectory()
        try:
            window, bar = self.prepare_loading_window(path_variable)
            self.file_loading_window = window
            results = [None]
            t1 = Thread(target=multi_directory_read, args=(inbox, window, path_variable, bar, results))
            t1.start()
            window.mainloop()
            t1.join()
            self.people_comparison = results[0]
            window.destroy()
            anal_window = self.anal_all_window()
            anal_window.wait_window()
        except Exception:
            messagebox.showwarning(title="ERROR 1", message="Wskazany folder niemożliwy do analizy!")

    def anal_all_window(self):
        s = HorrorShow(self.people_comparison)

        def general():
            active_label.pack(pady=5)
            window.update_idletasks()
            s.generalInfoShow()
            s.pieShow()
            active_label.pack_forget()

        def my_general():
            if entry.get() != "":
                active_label.pack(pady=5)
                entry.configure(fg="green")
                window.update_idletasks()
                name = entry.get()
                s.my_general_info_show(name)
                s.myPieShow(name)
                active_label.pack_forget()
                entry.configure(fg="black")
            else:
                messagebox.showwarning(title="BRAK UŻYTKOWNIKA!", message="Podaj imię i nazwisko!")

        def aboutPeople():
            active_label.pack(pady=5)
            window.update_idletasks()
            s.compare_message_amount_show()
            s.compare_love_amount_show()
            s.compare_multimedia_amount_show()
            s.compare_photo_amount_show()
            s.compare_video_amount_show()
            s.compare_xd_amount_show()
            s.compare_haha_word_amount_show()
            s.compare_hearts_amount_show()
            s.compare_haha_amount_show()
            s.compare_wow_amount_show()
            s.compare_likes_amount_show()
            s.compare_eyes_amount_show()
            active_label.pack_forget()

        def about_me():
            if entry.get() != "":
                active_label.pack(pady=5)
                name = entry.get()
                entry.configure(fg="green")
                window.update_idletasks()
                s.compareMyWordUsageShow(name)
                active_label.pack_forget()
                entry.configure(fg="black")
            else:
                messagebox.showwarning(title="BRAK UŻYTKOWNIKA!", message="Podaj imię i nazwisko!")

        def anal_word_window():
            def anal_word():
                if entry_word.get() != "":
                    active_word_label.pack(pady=5)
                    entry_word.configure(fg="green")
                    word_window.update_idletasks()
                    given_word = entry_word.get()
                    s.compare_given_word_amount_show(given_word.lower())
                    active_word_label.pack_forget()
                    entry_word.configure(fg="black")
                else:
                    messagebox.showwarning(title="BRAK WYRAZU!", message="Podaj wyraz do analizy!")
            word_window = Toplevel()
            word_window.title(self.title)
            Label(word_window, text="Wprowadź wyraz do przeanalizowania jego stopnia użycia",
                  font=("Arial", 8)).pack(pady=5)
            entry_word = Entry(word_window, font=("Arial", 14))
            entry_word.pack()
            anal_butt = Button(word_window, text="Analizuj", command=anal_word)
            anal_butt.pack(pady=5)
            active_word_label = Label(word_window, text="przetwarzam...", font=("Arial", 8), fg="green")
            word_window.geometry("300x150")
            word_window.wait_window()

        window = Toplevel()
        window.title(self.title)
        info_label = Label(window, text="Wpisz swoje imię i nazwisko dokładnie tak, jak masz na facebooku",
                          font=("Arial", 8))
        info_label.pack()
        entry = Entry(window, font=("Arial", 14))
        entry.pack()
        whole_fb = Button(window, text="Info ogólne analizując wszystkich", command=general)
        whole_fb.pack(pady=5)
        my_fb = Button(window, text="Info ogólne analizując Ciebie", command=my_general)
        my_fb.pack(pady=5)
        everyone = Button(window, text="Przeanalizuj wszystkich", command=aboutPeople)
        everyone.pack(pady=5)
        me = Button(window, text="Przeanalizuj siebie", command=about_me)
        me.pack(pady=5)
        word_button = Button(window, text="Przeanalizuj wyraz", command=anal_word_window)
        word_button.pack(pady=5)
        active_label = Label(window, text="przetwarzam...", font=("Arial", 8), fg="green")
        window.geometry("350x270")
        return window

    def choose_conversation(self):  # tu skończyć
        conv_dir = filedialog.askdirectory()
        try:
            self.conversation = directoryRead(conv_dir)
            anal_window = self.anal_conv_window()
            anal_window.wait_window()
        except Exception:
            messagebox.showwarning(title="ERROR 2", message="Wskazany folder niemożliwy do analizy!")

    def anal_conv_window(self):
        s = Show(self.conversation)

        def analConv():
            active_label.pack(pady=10)
            window.update_idletasks()
            s.most_messages_sent_show()
            s.most_reactions_receiver_show()
            s.most_reactions_giver_show()
            s.most_photo_sent_show()
            s.most_video_sent_show()
            s.most_multimedia_sent_show()
            s.most_multimedia_reactions_receiver_show()
            s.most_multimedia_reactions_giver_show()
            s.person_message_length_show()
            s.char_writen_show()
            s.most_love_show()
            s.most_xd_sent_show()
            s.leas_xd_sent_show()
            s.most_question_giver_show()
            s.least_question_giver_show()
            s.most_omg_giver_show()
            s.most_unsent_giver_show()
            s.most_hearts_giver_show()
            s.most_hearts_receiver_show()
            s.most_haha_giver_show()
            s.most_haha_receiver_show()
            s.received_to_given_reactions_show()
            s.questions_to_answers_per_person_show()
            s.xd_to_no_xd_per_person_show()
            s.most_only_question_giver_show()
            s.received_to_given_hearts_show()
            active_label.pack_forget()

        def anal_conv_general():
            active_label.pack(pady=10)
            window.update_idletasks()
            s.general_info_show()
            s.pie_show()
            active_label.pack_forget()

        def anal_conv_given_word():
            def anal_word():
                if entry_word.get() != "":
                    active_word_label.pack(pady=5)
                    entry_word.configure(fg="green")
                    word_window.update_idletasks()
                    given_word = entry_word.get()
                    s.most_given_word_giver_show(given_word.lower())
                    active_word_label.pack_forget()
                    entry_word.configure(fg="black")
                else:
                    messagebox.showwarning(title="BRAK WYRAZU!", message="Podaj wyraz do analizy!")

            word_window = Toplevel()
            word_window.title(self.title)
            Label(word_window, text="Wprowadź wyraz do przeanalizowania jego stopnia użycia",
                  font=("Arial", 8)).pack(pady=5)
            entry_word = Entry(word_window, font=("Arial", 14))
            entry_word.pack()
            anal_butt = Button(word_window, text="Analizuj", command=anal_word)
            anal_butt.pack(pady=5)
            active_word_label = Label(word_window, text="przetwarzam...", font=("Arial", 8), fg="green")
            word_window.geometry("300x120")
            word_window.wait_window()

        window = Toplevel()
        window.title(self.title)
        general = Button(window, text="Info ogólne o konfie", command=anal_conv_general)
        general.pack(pady=5)
        conv_most = Button(window, text="Wykresy osób z konfy", command=analConv)
        conv_most.pack(pady=5)
        given_word_butt = Button(window, text="Przeanalizuj słowo lub ciąg wyrazów", command=anal_conv_given_word)
        given_word_butt.pack(pady=5)
        active_label = Label(window, text="przetwarzam...", font=("Arial", 8), fg="green")
        window.geometry("350x160")
        return window

    def run(self):
        self.start_window.mainloop()
