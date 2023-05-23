from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self, address):
        pass


class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        file = open(address)
        x = file.readline().split()
        list_words = []
        for i in x:
            if i not in list_words:
                list_words.append(i)
        for i in range(0, len(list_words)):
            print("Frequency of ", list_words[i], "is :", x.count(list_words[i]))


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        file = open(address)
        x = file.readline()
        dict_words = {}
        for word in x.split():
            dict_words[word] = dict_words.get(word, 0) + 1
        for key in dict_words:
            print("{} : {}".format(key, dict_words[key]))


address1 = '/Users/ezgi/Desktop/strange.txt'
list_file = ListCount(address1)
list_file.calculateFreqs(address1)

dict_file = DictCount(address1)
dict_file.calculateFreqs(address1)