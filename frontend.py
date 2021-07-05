from tkinter import PhotoImage, Toplevel, StringVar, HORIZONTAL, Label, Tk, filedialog, Button, Entry, messagebox
from tkinter.ttk import Progressbar
from conversationStatisticsFrontend import Show
from statisticsFrontend import HorrorShow
from fileReader import multiDirectoryRead, directoryRead
from threading import Thread


class Main:
    def __init__(self):
        self.fileLoadingWindow = None
        self.statisticsWindow = None
        self.peopleComparison = None
        self.conversation = None
        self.title = 'analFB'
        self.startWindow = self.starter()

    def starter(self):
        window = Tk()
        icon = PhotoImage(file='analFB logo.png')
        window.title(self.title)
        window.iconphoto(True, icon)
        textLabel = Label(text="Wybierz co chcesz zrobić", font=('Arial', 12))
        textLabel.pack(pady=10)
        allConv = Button(window, text="Przeanalizuj wszystkie konwersacje na tle innych konwersacji",
                         command=self.chooseInbox)
        allConv.pack(pady=5)
        Label(text="(wskaż folder inbox)", font=('Arial', 7)).pack()
        conv = Button(window, text="Przeanalizuj ludzi w danej konwersacji", command=self.chooseConversation)
        conv.pack(pady=5)
        Label(text="(wskaż folder danej konwersacji)", font=('Arial', 7)).pack()
        infoButton = Button(window, text="Instrukcja", command=self.info)
        infoButton.pack(pady=5)
        signLabel = Label(text="Created by Paweł Krasicki 2021", font=('Calibri', 8), fg='grey')
        signLabel.pack(pady=15)
        window.geometry("350x230")
        return window

    def info(self):
        infoWindow = Toplevel()
        infoWindow.title(self.title)
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
        Label(infoWindow, text=infoText, font=("Consolas", 12)).pack(pady=50, padx=50)
        infoWindow.wait_window()

    def prepareLoadingWindow(self, pathVariable):
        window = Toplevel()
        window.title(self.title)
        bar = Progressbar(window, orient=HORIZONTAL, length=400)
        bar.pack(pady=10)
        Label(window, textvariable=pathVariable).pack()
        window.geometry("500x100")
        return window, bar

    def chooseInbox(self):
        pathVariable = StringVar()
        inbox = filedialog.askdirectory()
        try:
            window, bar = self.prepareLoadingWindow(pathVariable)
            self.fileLoadingWindow = window
            results = [None]
            t1 = Thread(target=multiDirectoryRead, args=(inbox, window, pathVariable, bar, results))
            t1.start()
            window.mainloop()
            t1.join()
            self.peopleComparison = results[0]
            window.destroy()
            analWindow = self.analAllWindow()
            analWindow.wait_window()
        except Exception:
            messagebox.showwarning(title="ERROR 1", message="Wskazany folder niemożliwy do analizy!")

    def analAllWindow(self):
        s = HorrorShow(self.peopleComparison)

        def general():
            activeLabel.pack(pady=5)
            window.update_idletasks()
            s.generalInfoShow()
            s.pieShow()
            activeLabel.pack_forget()

        def myGeneral():
            if entry.get() is not "":
                activeLabel.pack(pady=5)
                entry.configure(fg="green")
                window.update_idletasks()
                name = entry.get()
                s.myGeneralInfoShow(name)
                s.myPieShow(name)
                activeLabel.pack_forget()
                entry.configure(fg="black")
            else:
                messagebox.showwarning(title="BRAK UŻYTKOWNIKA!", message="Podaj imię i nazwisko!")

        def aboutPeople():
            activeLabel.pack(pady=5)
            window.update_idletasks()
            s.compareMessageAmountShow()
            s.compareTopWordAmountShow()
            s.compareMultimediaAmountShow()
            s.comparePhotoAmountShow()
            s.compareVideoAmountShow()
            s.compareXDAmountShow()
            s.compareLoveAmountShow()
            s.compareKurwaAmountShow()
            s.compareJaPierdoleAmountShow()
            s.compareHahaWordAmountShow()
            s.compareGivenWordAmountShow("nudes")
            s.compareTopWordAmountShow()
            s.compareHeartsAmountShow()
            s.compareHahaAmountShow()
            s.compareWowAmountShow()
            s.compareLikesAmountShow()
            s.compareEyesAmountShow()
            activeLabel.pack_forget()

        def aboutMe():
            if entry.get() is not "":
                activeLabel.pack(pady=5)
                name = entry.get()
                entry.configure(fg="green")
                window.update_idletasks()
                s.compareMyWordUsageShow(name)
                activeLabel.pack_forget()
                entry.configure(fg="black")
            else:
                messagebox.showwarning(title="BRAK UŻYTKOWNIKA!", message="Podaj imię i nazwisko!")

        def analWordWindow():
            def analWord():
                if entryWord.get() is not "":
                    activeWordLabel.pack(pady=5)
                    entryWord.configure(fg="green")
                    wordWindow.update_idletasks()
                    givenWord = entryWord.get()
                    s.compareGivenWordAmountShow(givenWord.lower())
                    activeWordLabel.pack_forget()
                    entryWord.configure(fg="black")
                else:
                    messagebox.showwarning(title="BRAK WYRAZU!", message="Podaj wyraz do analizy!")
            wordWindow = Toplevel()
            wordWindow.title(self.title)
            Label(wordWindow, text="Wprowadź wyraz do przeanalizowania jego stopnia użycia",
                  font=("Arial", 8)).pack(pady=5)
            entryWord = Entry(wordWindow, font=("Arial", 14))
            entryWord.pack()
            analButt = Button(wordWindow, text="Analizuj", command=analWord)
            analButt.pack(pady=5)
            activeWordLabel = Label(wordWindow, text="przetwarzam...", font=("Arial", 8), fg="green")
            wordWindow.geometry("300x150")
            wordWindow.wait_window()

        window = Toplevel()
        window.title(self.title)
        infoLabel = Label(window, text="Wpisz swoje imię i nazwisko dokładnie tak, jak masz na facebooku",
                          font=("Arial", 8))
        infoLabel.pack()
        entry = Entry(window, font=("Arial", 14))
        entry.pack()
        wholeFB = Button(window, text="Info ogólne analizując wszystkich", command=general)
        wholeFB.pack(pady=5)
        myFB = Button(window, text="Info ogólne analizując Ciebie", command=myGeneral)
        myFB.pack(pady=5)
        everyone = Button(window, text="Przeanalizuj wszystkich", command=aboutPeople)
        everyone.pack(pady=5)
        me = Button(window, text="Przeanalizuj siebie", command=aboutMe)
        me.pack(pady=5)
        wordButton = Button(window, text="Przeanalizuj wyraz", command=analWordWindow)
        wordButton.pack(pady=5)
        activeLabel = Label(window, text="przetwarzam...", font=("Arial", 8), fg="green")
        window.geometry("350x270")
        return window

    def chooseConversation(self):  # tu skończyć
        convDir = filedialog.askdirectory()
        try:
            self.conversation = directoryRead(convDir)
            analWindow = self.analConvWindow()
            analWindow.wait_window()
        except Exception:
            messagebox.showwarning(title="ERROR 2", message="Wskazany folder niemożliwy do analizy!")

    def analConvWindow(self):
        s = Show(self.conversation)

        def analConv():
            activeLabel.pack(pady=10)
            window.update_idletasks()
            s.mostMessagesSentShow()
            s.mostReactionsReceiverShow()
            s.mostReactionsGiverShow()
            s.mostPhotoSentShow()
            s.mostVideoSentShow()
            s.mostMultimediaSentShow()
            s.mostMultimediaReactionsReceiverShow()
            s.mostMultimediaReactionsGiverShow()
            s.personMessageLengthShow()
            s.charWritenShow()
            s.mostXDSentShow()
            s.leastXDSendShow()
            s.mostQuestionGiverShow()
            s.leastQuestionGiverShow()
            s.mostWordUsageShow()
            s.mostUnsentGiverShow()
            s.mostHeartsGiverShow()
            s.mostHeartsReceiverShow()
            s.mostHahaGiverShow()
            s.mostHahaReceiverShow()
            s.receivedToGivenReactionsShow()
            s.questionsToAnswersPerPersonShow()
            s.xdToNoXDPerPersonShow()
            s.mostOnlyQuestionGiverShow()
            s.mostWyspaGiverShow()
            s.mostKurwaGiverShow()
            s.receivedToGivenHeartsShow()
            activeLabel.pack_forget()

        def analConvGeneral():
            activeLabel.pack(pady=10)
            window.update_idletasks()
            s.generalInfoShow()
            s.pieShow()
            activeLabel.pack_forget()

        def analConvGivenWord():
            def analWord():
                if entryWord.get() is not "":
                    activeWordLabel.pack(pady=5)
                    entryWord.configure(fg="green")
                    wordWindow.update_idletasks()
                    givenWord = entryWord.get()
                    s.mostGivenWordGiverShow(givenWord.lower())
                    activeWordLabel.pack_forget()
                    entryWord.configure(fg="black")
                else:
                    messagebox.showwarning(title="BRAK WYRAZU!", message="Podaj wyraz do analizy!")

            wordWindow = Toplevel()
            wordWindow.title(self.title)
            Label(wordWindow, text="Wprowadź wyraz do przeanalizowania jego stopnia użycia",
                  font=("Arial", 8)).pack(pady=5)
            entryWord = Entry(wordWindow, font=("Arial", 14))
            entryWord.pack()
            analButt = Button(wordWindow, text="Analizuj", command=analWord)
            analButt.pack(pady=5)
            activeWordLabel = Label(wordWindow, text="przetwarzam...", font=("Arial", 8), fg="green")
            wordWindow.geometry("300x120")
            wordWindow.wait_window()

        window = Toplevel()
        window.title(self.title)
        general = Button(window, text="Info ogólne o konfie", command=analConvGeneral)
        general.pack(pady=5)
        convMost = Button(window, text="Wykresy osób z konfy", command=analConv)
        convMost.pack(pady=5)
        givenWordButt = Button(window, text="Przeanalizuj słowo lub ciąg wyrazów", command=analConvGivenWord)
        givenWordButt.pack(pady=5)
        activeLabel = Label(window, text="przetwarzam...", font=("Arial", 8), fg="green")
        window.geometry("350x160")
        return window

    def run(self):
        self.startWindow.mainloop()
