#!/usr/bin/python3
#
# decoder.py
# v0.01 (2025/8/13)
#
import json

INPUT_DATA = 'tokenized.json'
 
with open(INPUT_DATA, 'r') as f:
   tokened = json.load(f)

#print(tokened)

for id in tokened['text']:
    if 'word_' in id:
        id = id.split('_')[1]
        if id in tokened['id2word']['word_tbl']:
              print(tokened['id2word']['word_tbl'][id], end='')
        else:
            print("error unk id",id)
    elif 'sp_' in id:
        id = id.split('_')[1]
        if id in tokened['id2word']['spacer_tbl']:
            print(tokened['id2word']['spacer_tbl'][id], end='')
        else:
            print("error unk id",id)
    else:
        print('unk internal error')