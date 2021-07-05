from tkinter import PhotoImage, Toplevel, StringVar, HORIZONTAL, Label, Tk, filedialog, Button
from tkinter.ttk import Progressbar
from conversationStatisticsFrontend import Show
from statisticsFrontend import ComparePeopleShow, TotalShow, MyTotalShow, AboutMeShow, HorrorShow
from fileReader import multiDirectoryRead, directoryRead
from threading import Thread


class Main:
    def __init__(self):
        self.fileLoadingWindow = None
        self.statisticsWindow = None
        self.peopleComparison = None
        self.conversation = None
        self.title = 'analFB'
        self.icon = None
        self.startWindow = self.starter()

    def starter(self):
        window = Tk()
        icon = PhotoImage(file='analFB logo.png')
        self.icon = icon
        window.title(self.title)
        window.iconphoto(True, self.icon)
        textLabel = Label(text="Wybierz co chcesz zrobić")
        textLabel.pack(pady=10)
        allConv = Button(window, text="Przeanalizuj wszystkie konwersacje na tle innych konwersacji",
                            command=self.chooseInbox2)
        allConv.pack(pady=5)
        conv = Button(window, text="Przeanalizuj ludzi w danej konwersacji", command=self.chooseConversation2)
        conv.pack(pady=5)
        window.geometry("350x120")
        return window

    # def prepareWindow(self):
    #     startWindow = tk.Tk(className="fb analyzer")
    #     inboxButt = tk.Button(startWindow, text="Choose inbox directory", command=self.chooseInbox)
    #     inboxButt.pack()
    #     convDirButt = tk.Button(startWindow, text="Choose conversation directory", command=self.chooseConversation)
    #     convDirButt.pack()
    #     analAll = tk.Button(startWindow, text="Analyze messenger statistics", command=self.analAll)
    #     analAll.pack()
    #     givenMes = tk.Button(startWindow, text="Analyze given word in messenger", command=self.analGivenMes)
    #     givenMes.pack()
    #     analButt = tk.Button(startWindow, text="Analyze conversation", command=self.analConv)
    #     analButt.pack()
    #     givenConv = tk.Button(startWindow, text="Analyze given word in conversation", command=self.analGivenConv)
    #     givenConv.pack()
    #     startWindow.geometry("250x200")
    #     return startWindow

    # def chooseInbox(self):
    #     self.peopleComparison = fr.multiDirectoryRead(tk.filedialog.askdirectory())
    #
    # def chooseConversation(self):
    #     self.conversation = fr.directoryRead(tk.filedialog.askdirectory())

    def prepareLoadingWindow(self, pathVariable):
        window = Toplevel()
        icon = PhotoImage(file='analFB logo.png')
        window.title(self.title)
        window.iconphoto(True, self.icon)
        bar = Progressbar(window, orient=HORIZONTAL, length=300)
        bar.pack(pady=10)
        Label(window, textvariable=pathVariable).pack()
        window.geometry("450x100")
        return window, bar

    def chooseInbox2(self):
        pathVariable = StringVar()
        window, bar = self.prepareLoadingWindow(pathVariable)
        inbox = filedialog.askdirectory()
        self.startWindow.withdraw()
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
        self.startWindow.deiconify()

    def analAllWindow(self):
        s = HorrorShow(self.peopleComparison)
        name = 'Pawel Krasicki'

        def general():
            window.withdraw()       # dać jakieś kręcące się kółeczko
            s.generalInfoShow()
            s.pieShow()
            window.deiconify()

        def myGeneral():
            window.withdraw()
            s.myGeneralInfoShow(name)
            s.myPieShow(name)
            window.deiconify()

        def aboutPeople():
            window.withdraw()
            s.compareMessageAmountShow()
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
            window.deiconify()

        def aboutMe():
            window.withdraw()
            s.compareMyWordUsageShow(name)
            window.deiconify()

        window = Tk()
        window.title(self.title)
        # window.iconphoto(True, self.icon)
        wholeFB = Button(window, text="Info ogólne analizując wszystkich", command=general)
        wholeFB.pack(pady=5)
        myFB = Button(window, text="Info ogólne analizując Ciebie", command=myGeneral)
        myFB.pack(pady=5)
        everyone = Button(window, text="Przeanalizuj wszystkich", command=aboutPeople)
        everyone.pack(pady=5)
        me = Button(window, text="Przeanalizuj siebie", command=aboutMe)
        me.pack(pady=5)
        window.geometry("350x200")
        return window

    def chooseConversation2(self):
        self.conversation = directoryRead(filedialog.askdirectory())

    def analAll(self):
        name = "Pawel Krasicki"
        m = TotalShow(self.peopleComparison)
        m2 = MyTotalShow(self.peopleComparison)
        m3 = AboutMeShow(self.peopleComparison)
        p = ComparePeopleShow(self.peopleComparison)

        m.generalInfoShow()
        m.pieShow()

        m2.myGeneralInfoShow(name)
        m2.myPieShow(name)

        m3.compareMyWordUsageShow(name)

        p.compareWowAmountShow()
        p.compareMultimediaAmountShow()
        p.comparePhotoAmountShow()
        p.compareVideoAmountShow()
        p.compareXDAmountShow()
        p.compareLoveAmountShow()
        p.compareKurwaAmountShow()
        p.compareJaPierdoleAmountShow()
        p.compareHahaWordAmountShow()
        p.compareHeartsAmountShow()
        p.compareHahaAmountShow()
        p.compareWowAmountShow()
        p.compareLikesAmountShow()
        p.compareEyesAmountShow()
        p.compareTopWordAmountShow()

    def analGivenMes(self):
        p = ComparePeopleShow(self.peopleComparison)
        word = ""   # TODO
        p.compareGivenWordAmountShow(word)

    def analConv(self):
        c = Show(self.conversation)
        c.generalInfoShow()
        c.pieShow()
        c.mostMessagesSentShow()
        c.mostReactionsReceiverShow()
        c.mostReactionsGiverShow()
        c.mostPhotoSentShow()
        c.mostVideoSentShow()
        c.mostMultimediaSentShow()
        c.mostMultimediaReactionsReceiverShow()
        c.mostMultimediaReactionsGiverShow()
        c.personMessageLengthShow()
        c.charWritenShow()
        c.mostXDSentShow()
        c.leastXDSendShow()
        c.mostQuestionGiverShow()
        c.leastQuestionGiverShow()
        c.mostUnsentGiverShow()
        c.mostHeartsGiverShow()
        c.mostHeartsReceiverShow()
        c.mostHahaGiverShow()
        c.mostHahaReceiverShow()
        c.receivedToGivenReactionsShow()
        c.questionsToAnswersPerPersonShow()
        c.xdToNoXDPerPersonShow()
        c.mostOnlyQuestionGiverShow()
        c.mostWyspaGiverShow()
        c.mostKurwaGiverShow()
        c.mostTopWordGiverShow()
        c.receivedToGivenHeartsShow()

    def analGivenConv(self):
        c = Show(self.conversation)
        word = ""   # TODO
        print("jeszcze nie działa xD")

    def run(self):
        self.startWindow.mainloop()
