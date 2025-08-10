#!/usr/bin/python3

#
# P22
#

# download sample data

import urllib.request

URL='https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/refs/heads/main/ch02/01_main-chapter-code/the-verdict.txt'

file_path='./data/the-verdict.txt'

urllib.request.urlretrieve(URL, file_path)


# list 2-1(P22)
# check file  

with open(file_path,'r') as f:
   raw_text = f.read()

print('total number of character:', len(raw_text))
print(raw_text[:99])