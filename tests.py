import time as t
import fileReader as fr
import matplotlib.pyplot as plt
from fileHolder import ConversationInfo
from collections import Counter
import random


def prepare1Dict(tupleList):
    listDict = {}
    for name, amount in tupleList:
        listDict.setdefault(name, []).append(amount)
    return {person: sum(listDict.get(person)) for person in listDict}


def sortDict(unsortedDict):
    sortedList = sorted(unsortedDict.items(), key=lambda x: x[1], reverse=True)[:40]
    return {pair[0][:20]: pair[1] for pair in sortedList}


def showPlot1(sortedDict, titleText="", xLabelText="{}: {}"):
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
        plt.subplots_adjust(bottom=0.35)
        plt.xlabel(xLabelText.format(firstValue(xPerson), firstValue(y)))
        print(x[:40])


def showPlot2(sortedTupleList, titleText="", xLabelText="{}: {}"):
    def firstValue(a):
        return a[0] if len(a) > 0 else 0
    plt.figure(figsize=(10, 7.25))
    plt.title(titleText)
    xPerson = [tp[0] for tp in sortedTupleList][:40]
    y = [tp[1] for tp in sortedTupleList][:40]
    x = [xPerson[i] + " " + str(y[i]) for i in range(len(xPerson))]
    plt.bar(x, y)
    plt.xticks(x, x, rotation='vertical')
    plt.margins(0.01)
    plt.subplots_adjust(bottom=0.35)
    plt.xlabel(xLabelText.format(firstValue(xPerson), firstValue(y)))
    print(x[:40])


if __name__ == '__main__':
    # listTest = [(i % 150, 1) for i in range(2000000)]
    #
    # time = t.time()
    # preparedDict1 = prepare1Dict(listTest)
    # time = t.time() - time
    # print("sort1 ", time)

    conversationInfo = fr.directoryRead("D:\\restore fb\\cały okres\messages\\inbox\\kolozdyskretnejwczwartekiwolnoscszczepaniakpokazalkotafilmnadczanimzapytasz_wtkmtqqcmq")
    # contentList = [message.get("content") for message in conversationInfo.messages
    #                if message.get("content") is not None]
    #
    # time = t.time()
    # wordList = []
    # for content in contentList:
    #     for word in content.split():
    #         wordList.append(word)
    # len(wordList)
    # time = t.time() - time
    # print("1 ", time)
    #
    # time = t.time()
    # sum([len(content.split()) for content in contentList])
    # time = t.time() - time
    # print("2 ", time)

    def mostXDSent(conversationInfo):
        xdMessageSenders = [(message.get("sender_name"), 1) for message in
                            conversationInfo.messages if message.get("content") is not None and
                            message.get("content").lower().__contains__("xd")]
        return sortDict(prepare1Dict(xdMessageSenders))

    def mostXDSent2(conversationInfo):
        xdMessageSenders = [message.get("sender_name") for message in
                            conversationInfo.messages if message.get("content") is not None and
                            message.get("content").lower().__contains__("xd")]
        return Counter(xdMessageSenders).most_common()


    time = t.time()
    showPlot1(mostXDSent(conversationInfo))
    time = t.time() - time
    print("1 ", time)

    time = t.time()
    showPlot2(mostXDSent2(conversationInfo))
    time = t.time() - time
    print("2 ", time)

    strintTest = "Xdsaf asdfasasd  DDD"
    print(True if strintTest.__contains__("") else False)

    # time = t.time()
    # itsMax = max(testingList)
    # print(itsMax)
    # print(testingList.count(itsMax))
    # time = t.time() - time
    # print("1 ", time)
    #
    # time = t.time()
    # res = Counter(testingList)
    # print(res.most_common()[0][0])  # keys
    # print(res.most_common()[0][1])     # values
    # time = t.time() - time
    # print("2 ", time)
    #
    # time = t.time()
    # tupleList = res.most_common()
    # print([tp[0] for tp in tupleList][:40])
    # print([tp[1] for tp in tupleList][:40])
    # time = t.time() - time
    # print("3 ", time)


