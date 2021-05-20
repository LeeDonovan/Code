import speech_recognition as sr
import distance as d
import os
import matplotlib.pyplot as plt




class Speech:
    def __init__(self):
        self.original = []  # from text file
        self.recognized = []  # converted audio to text
        self.distances = []  # comparison btw original vs recog

    def read_original(self, inFile):  # reads each line of text file
        file = open(inFile, 'r')
        Lines = file.readlines()
        for line in Lines:
            line = line.lower()
            self.original.append(line)
        print("Finished transferring og text")

    def conv_audio(self, inDir):  # converts audio to string
        allSent = []
        allGroups = []
        allGroupDictionaries = []
        count = 1
        with inDir as entries:
            group = []
            for entry in entries:
                if (entry.name[2] == '-'):
                    audio = sr.AudioFile(entry.name)
                    with audio as src:
                        a = r.record(src)
                        group.append(str(r.recognize_google(a)))
                    if count == 25:
                        c = ','
                        c = c.join(group)
                        allGroups.append(group)
                        count = 0
                        group = []
                    count += 1

        for i in allGroups:
            s.recognized.append(i)
        print("finished audio conversion...")

        # count = 1
        # for i in allGroups:

        #     d = {}

        #     d[count] = i
        #     allGroupDictionaries.append(d)
        #     count += 1

        # for i in allGroupDictionaries:
        #     s.recognized.append(i)

    # og[0] -> 1:[0], 2:[0]...
    def comp_string(self):  # self.comp_string()

        allOriginalWords = []
        allNLD = []

        # rec = j[count][wordPos].split() #j is entry, count is dict key, wordPos is sentence called

        for i in self.original:
            split = i.split()  # this splits one whole sentence to words
            allOriginalWords.append(split)

        for i in allOriginalWords:
            groupNLD = []
            allNLD.append(groupNLD)

        for i in self.recognized:
            count = 0
            #print("Self.recognized", self.recognized)
            for j in range(25):
                #print(j)
                sentence = i[j].split()
                #print(allOriginalWords[j])
                #print(sentence)
                ld = d.levenshtein(allOriginalWords[j], sentence)
                nld = 0
                nld = ld /( max(len(allOriginalWords[j]), len(sentence)))
                allNLD[j].append(nld)
                # print(nld)
            count += 1
        for i in allNLD:
            s.distances.append(i)
            #print(i)
        print("finished distance NLD")


if __name__ == '__main__':
    print("code is running...")
    r = sr.Recognizer()
    s = Speech()
    # directory to where ever audio files
    base = "E:\Code\CECS_451\Assignment11"  # directory to where ever audio files
    og = 'How Speech Recognition Works.txt'  # read lines in txt
    # directory iteration function getting names of files in path
    path = os.scandir(base)
    s.read_original(og)
    s.conv_audio(path)
    # print("Finished Product\n")
    # print(s.recognized)
    s.comp_string()
    x_labels = ["Sent 1","Sent 2","Sent 3","Sent 4","Sent 5","Sent 6","Sent 7","Sent 8","Sent 9","Sent 10","Sent 11","Sent 12","Sent 13","Sent 14","Sent 15","Sent 16","Sent 17","Sent 18","Sent 19","Sent 20","Sent 21","Sent 22","Sent 23","Sent 24","Sent 25",]

    fig = plt.figure(figsize = (18, 8))
    ax = fig.add_subplot()

    plt.title("Box-and-Whisker plot of distance")
    plt.xlabel("")
    plt.ylabel("Normalized distance")

    ax.boxplot(s.distances)

    ax.set_xticklabels(x_labels)

    plt.show()


