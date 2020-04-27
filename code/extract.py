import json
import os

lst = []

directory = '/user/research/ptan/data/Twitter/'
lstOfFile = os.listdir(directory)


f1 = open("preprocess.txt", 'w')
for i in lstOfFile:
  fileName = directory+i
  try:
    with open(fileName, encoding="utf8") as f:

      for line in f:
        if line== "\n":
          continue
        try:
          data = json.loads(line)
        except ValueError:
          continue
        try:          
          if 'IBM' in data['text'] or 'AMD' in data['text'] or 'eBay' in data['text']:
            f1.writelines([data['created_at'],'\t',str(data['text'].encode("utf-8")),'\n'])
        except KeyError:
          continue
        except ValueError:
          continue

    f.close()
    print('file close')
  except IOError:
    continue
f1.close()


