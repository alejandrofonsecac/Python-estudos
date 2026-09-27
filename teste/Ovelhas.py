sentence = "is2 Thi1s T4est 3a"
resultSentence = []
pos = [5,4,3,1]
order = 0
sentence2 = sentence.split()
# [0]is2 [1]Thi1s [2]T4est [3]3a

for word in sentence2:
    for char in word:
        if char.isnumeric():
            pos = int(char) - 1
        pos.sort()
        for i in pos:
            resultSentence[i] = word
print(resultSentence)
