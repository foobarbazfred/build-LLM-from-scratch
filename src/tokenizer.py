#!/usr/bin/python3

#
#  tokenizer text: 2.2(P21) - 2.3(P25) 
#  v0.01 2025/8/12
#  v0.02 2025/8/13
#     add id -> word table
#
#
#

#
#  input: text
#  output: converted text into id list with
#          word index , spacer index
#          in json format
#

# bug:
#
#  if text consists only word and not spacer then can't read word
#  e.g if input_text = 'abc'  then can not read abc
#

# algo memo
#  implemented handling of character "'"
#
#  "abc's"  ->  ' is member of word 
#  " 'ab"   ->  ' is not member of word and ' is spacer
#  "bc' "   ->  ' is not member of word and ' is spacer
#


import json

INPUT_TEXT = './data/the-verdict.txt'
OUTPUT = 'tokenized.json'

spacer_dic = {}
spacer_max_idx = 0
word_dic = {}
word_max_idx = 0

target_text = []

def is_letter(ch):
    return (ch >= 'A' and ch <= 'Z') or \
        (ch >= 'a' and ch <= 'z') or \
        (ch >= '0' and ch <= '9')

word = ''
fetch = None
with open(INPUT_TEXT, 'r') as f:
    for paragraph in f:
        iter_paragraph = iter(paragraph)
        for _ in range(len(paragraph)):
            if fetch is None:
                ch = next(iter_paragraph)
            else:
                ch = fetch
                fetch = None

            is_word = None
            print('[', ch ,']',end='')
            #
            # check single quote is spacer or between letter
            # 
            if ch == "'":   
                fetch = next(iter_paragraph)
                if word != '' and is_letter(fetch):
                    is_word = True
                else:
                    is_word = False
            else:
                if is_letter(ch):
                    is_word = True
                else:
                    is_word = False

            if is_word:
                word += ch
            else:
                spacer = ch
                print(f'\nword:{word}')
                print(f'spacer{spacer}')
                # regist and convert word
                if word != '':
                    if word not in word_dic:
                        word_dic[word] = word_max_idx
                        word_max_idx += 1
                    print(word_dic[word])
                    target_text.append(f'word_{word_dic[word]}')
                    word = ''
                # regist and convert spacer
                if spacer not in spacer_dic:
                    spacer_dic[spacer] = spacer_max_idx
                    spacer_max_idx += 1
                print(spacer_dic[spacer])
                target_text.append(f'sp_{spacer_dic[spacer]}')



def rev_kv_dic(a_dic):
    rev_dic = {}
    for k,v in a_dic.items():
        if v in rev_dic:
           print('Error in rev_kv_dic')
           print('duplicate value',v)
        else:
           #pdb.set_trace()
           rev_dic[v] = k
    return rev_dic

with open(OUTPUT, 'w') as f:
    tokened = { 'text' : target_text,
                'word2id' : {'word_tbl' : word_dic, 'spacer_tbl' : spacer_dic } , 
                'id2word' : {'word_tbl' : rev_kv_dic(word_dic), 'spacer_tbl' : rev_kv_dic(spacer_dic) }
    }
    json.dump(tokened, f)


