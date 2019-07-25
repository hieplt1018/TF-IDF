doc1 = "Người lên ngựa kẻ chia bào. Rừng phong thu đã nhốm màu quan san"
doc2 = "Ô hay buồn vương cây ngô đồng. Vàng rơi vàng rơi thu mênh mông"
doc3 = "Một chiều về bên bến sông thu. Nghe tin em cưới á cái đù."

bowA = doc1.split()
bowB = doc2.split()
bowC = doc3.split()

word_dict = set(bowA).union(set(bowB)).union(set(bowC))
# print(word_dict)
#{'vương', 'rơi', 'Ô', 'đồng.', 'đù.', 'cây', 'cưới', 'san', 'kẻ', 'về', 'ngựa',
# 'Nghe', 'quan', 'chia', 'cái', 'thu', 'màu', 'thu.', 'em', 'Vàng', 'hay', 'ngô',
# 'vàng', 'nhốm', 'sông', 'phong', 'bến', 'á', 'tin', 'bào.', 'chiều', 'lên', 'Một',
# 'mênh', 'bên', 'đã', 'Người', 'buồn', 'Rừng', 'mông'}

wordDictA = dict.fromkeys(word_dict, 0)
wordDictB = dict.fromkeys(word_dict, 0)
wordDictC = dict.fromkeys(word_dict, 0)

for word in bowA:
    wordDictA[word] += 1
# print(wordDictA)
# {'màu': 1, 'vương': 0, 'buồn': 0, 'em': 0, 'đù.': 0, 'về': 0, 'Vàng': 0, 'đã': 1, 'đồng.': 0,
#  'tin': 0, 'cây': 0, 'mênh': 0, 'bến': 0, 'lên': 1, 'bào.': 1, 'Rừng': 1, 'quan': 1, 'Một': 0,
#  'sông': 0, 'ngựa': 1, 'bên': 0, 'rơi': 0, 'mông': 0, 'chia': 1, 'vàng': 0, 'san': 1, 'Người': 1,
#  'cưới': 0, 'Ô': 0, 'thu.': 0, 'nhốm': 1, 'kẻ': 1, 'hay': 0, 'phong': 1, 'thu': 1, 'Nghe': 0, 'cái': 0, 'á': 0, 'ngô': 0, 'chiều': 0}

for word in bowB:
    wordDictB[word] += 1
for word in bowC:
    wordDictC[word] += 1

#caculate TF
def computeTF(wordDict, words):
    tfDict = {}
    wordsCount = len(words)
    for word, count in wordDict.items():
        tfDict[word] = count/float(wordsCount)
    return tfDict

tfdocA = computeTF(wordDictA, bowA)
# print(tfdocA)
# {'vàng': 0.0, 'san': 0.07142857142857142, 'đù.': 0.0, 'bến': 0.0, 'đồng.': 0.0, 'cây': 0.0, 'lên': 0.07142857142857142,
# 'nhốm': 0.07142857142857142, 'Một': 0.0, 'cái': 0.0, 'thu': 0.07142857142857142, 'em': 0.0, 'hay': 0.0, 'á': 0.0,
# 'Người': 0.07142857142857142, 'Vàng': 0.0, 'thu.': 0.0, 'Nghe': 0.0, 'chia': 0.07142857142857142, 'tin': 0.0, 'cưới': 0.0,
# 'ngô': 0.0, 'quan': 0.07142857142857142, 'rơi': 0.0, 'bào.': 0.07142857142857142, 'màu': 0.07142857142857142, 'về': 0.0,
# 'đã': 0.07142857142857142, 'Ô': 0.0, 'mông': 0.0, 'buồn': 0.0, 'ngựa': 0.07142857142857142, 'chiều': 0.0, 'kẻ': 0.07142857142857142,
# 'phong': 0.07142857142857142, 'sông': 0.0, 'mênh': 0.0, 'Rừng': 0.07142857142857142, 'bên': 0.0, 'vương': 0.0}

tfdocB = computeTF(wordDictB, bowB)
tfdocC = computeTF(wordDictC, bowC)

#caculate IDF
def computeIDF(docList):
  import math
  idfDict = {}
  N = len(docList)

  idfDict = dict.fromkeys(docList[0].keys(), 0)
  for doc in docList:
    for word, val in doc.items():
      if val > 0:
        idfDict[word] += 1

  for word, val in idfDict.items():
    idfDict[word] = math.log10(N / float(val))

  return idfDict

idfs = computeIDF([wordDictA, wordDictB, wordDictC])
# print(idfs)
# {'về': 0.47712125471966244, 'tin': 0.47712125471966244, 'chiều': 0.47712125471966244,
# 'thu.': 0.47712125471966244, 'đã': 0.47712125471966244, 'đù.': 0.47712125471966244,
# 'bến': 0.47712125471966244, 'á': 0.47712125471966244, 'Người': 0.47712125471966244,
# 'đồng.': 0.47712125471966244, 'lên': 0.47712125471966244, 'Một': 0.47712125471966244,
# 'em': 0.47712125471966244, 'vương': 0.47712125471966244, 'sông': 0.47712125471966244,
# 'buồn': 0.47712125471966244, 'hay': 0.47712125471966244, 'nhốm': 0.47712125471966244,
# 'thu': 0.17609125905568124, 'chia': 0.47712125471966244, 'san': 0.47712125471966244,
# 'mênh': 0.47712125471966244, 'Nghe': 0.47712125471966244, 'mông': 0.47712125471966244,
# 'màu': 0.47712125471966244, 'quan': 0.47712125471966244, 'vàng': 0.47712125471966244,
# 'cái': 0.47712125471966244, 'phong': 0.47712125471966244, 'bên': 0.47712125471966244,
# 'ngựa': 0.47712125471966244, 'kẻ': 0.47712125471966244, 'Ô': 0.47712125471966244,
# 'Vàng': 0.47712125471966244, 'cưới': 0.47712125471966244, 'ngô': 0.47712125471966244,
# 'rơi': 0.47712125471966244, 'cây': 0.47712125471966244, 'Rừng': 0.47712125471966244,
# 'bào.': 0.47712125471966244}

def computeTFIDF(tfDocs, idfs):
  tfidf = {}
  for word, val in tfDocs.items():
    tfidf[word] = val*idfs[word]
  return tfidf

tfidfDocA = computeTFIDF(tfdocA, idfs)
tfidfDocB = computeTFIDF(tfdocB, idfs)
tfidfDocC = computeTFIDF(tfdocC, idfs)

print(tfidfDocA)
# {'về': 0.0, 'tin': 0.0, 'chiều': 0.0, 'thu.': 0.0, 'đã': 0.03408008962283303,
# 'đù.': 0.0, 'bến': 0.0, 'á': 0.0, 'Người': 0.03408008962283303, 'đồng.': 0.0,
# 'lên': 0.03408008962283303, 'Một': 0.0, 'em': 0.0, 'vương': 0.0, 'sông': 0.0,
# 'buồn': 0.0, 'hay': 0.0, 'nhốm': 0.03408008962283303, 'thu': 0.012577947075405802,
# 'chia': 0.03408008962283303, 'san': 0.03408008962283303, 'mênh': 0.0, 'Nghe': 0.0,
# 'mông': 0.0, 'màu': 0.03408008962283303, 'quan': 0.03408008962283303, 'vàng': 0.0,
# 'cái': 0.0, 'phong': 0.03408008962283303, 'bên': 0.0, 'ngựa': 0.03408008962283303,
# 'kẻ': 0.03408008962283303, 'Ô': 0.0, 'Vàng': 0.0, 'cưới': 0.0, 'ngô': 0.0, 'rơi': 0.0,
# 'cây': 0.0, 'Rừng': 0.03408008962283303, 'bào.': 0.03408008962283303}
