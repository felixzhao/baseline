#!/usr/bin/env python

import sys

process_percent = sys.argv[1]
topnum = sys.argv[2]

## log
print 'percent : ' + process_percent
print 'width : ' + topnum

train_file_path = 'corpus/src-' + process_percent + 'percent/train-word.txt'
test_file_path = 'corpus/src-' + process_percent + 'percent/test-word-count.txt'
out_file_path = 'out/baseline_result_' + process_percent + 'per_' + topnum + 'width.txt'

ftrainwords = open(train_file_path, 'r')
ftestwords = open(test_file_path, 'r')
fout = open(out_file_path, 'w')

trainwords = [x.strip() for x in ftrainwords.readlines()]
testwords = []

wordmap = {}
#Reading Word Map Info
for line in ftestwords.readlines():
    parts = line.split()
    testwords.append(parts[0])
    if len(parts)>1:
        wordmap[parts[0]] = True
    else:
        wordmap[parts[0]] = False

step = [0]
cur = 1
while abs(cur)<topnum:
    step.append(cur)
    step.append(-cur)
    cur += 1

for i in range(len(testwords)):
    word = testwords[i]
    if wordmap[word]:
## log
        print word + ': '

        print >>fout, word, ':',
        k  =  0
        for j in range(topnum):
            while not (i+step[k] in range(len(trainwords))):
                k+=1
## log
            print trainwords[i+step[k]], j, '|'

            print >>fout, trainwords[i+step[k]], j, '|',
            k+=1
## log
        print '\n'

        print >>fout, '\n'

