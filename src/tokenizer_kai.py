#!/usr/bin/python3

#
# simple tokenizer for LLM
# v0.01 (2025/12/31)
#
import re

class Tokenizer():

    UNKNOWN_TOKEN_ID = 0xff_ff_ff_ff
    UNKNOWN_TOKEN = "__UNKNOWN_TOKEN__"

    END_OF_SENTENCE_ID = 0xff_ff_ff_fe
    END_OF_PARAGRAPH = "__END_OF_PARAGRAPH__"

    END_OF_PARAGRAPH_ID = 0xff_ff_ff_fd
    END_OF_SENTENCE = chr(0x0)   # virtual string
    
    def __init__(self):
       self.token_to_id_dic={}    
       self.id_to_token_dic={}    
       self.token_id=0
       self.token_to_id_dic[Tokenizer.UNKNOWN_TOKEN] = Tokenizer.UNKNOWN_TOKEN_ID
       self.id_to_token_dic[Tokenizer.UNKNOWN_TOKEN_ID] = Tokenizer.UNKNOWN_TOKEN

       self.token_to_id_dic[Tokenizer.END_OF_PARAGRAPH] = Tokenizer.END_OF_PARAGRAPH_ID
       self.id_to_token_dic[Tokenizer.END_OF_PARAGRAPH_ID] = Tokenizer.END_OF_PARAGRAPH

       self.token_to_id_dic[Tokenizer.END_OF_SENTENCE] = Tokenizer.END_OF_SENTENCE_ID
       self.id_to_token_dic[Tokenizer.END_OF_SENTENCE_ID] = Tokenizer.END_OF_SENTENCE
  
    def encoder(self, file):
        encoded_id_list = []
        with open(file,'r') as f:
           for line in f:
               line = line.strip()
               
               if len(line)>0 and (line[-1] == '.' or line[-1] == '.'):
                    is_end_of_paragraph = True
               else:
                    is_end_of_paragraph = False
               #print(line)
               sp = re.split(r'([ ;.,?!"()])',line)
               for token in sp:
                    id = self.token_to_id(token, regist=True)
                    encoded_id_list.append(id)
               if is_end_of_paragraph:
                    id = self.token_to_id(Tokenizer.END_OF_PARAGRAPH)
                    encoded_id_list.append(id)
        return encoded_id_list
       

    def decoder(self, id_list):
      decoded_text = ''
      for id in id_list:
          token = self.id_to_token(id)
          if token == Tokenizer.END_OF_PARAGRAPH:
              token = '\n'
          decoded_text += token
      return decoded_text

    def pp(self):
        for token in self.token_to_id_dic.keys():
            print(token,self.token_to_id_dic[token])
  
    def token_to_id(self, token, regist=True):
       if token in (Tokenizer.UNKNOWN_TOKEN, Tokenizer.END_OF_PARAGRAPH, Tokenizer.END_OF_SENTENCE):
           pass
       else:
           token=token.lower()
       if token in self.token_to_id_dic:
          return self.token_to_id_dic[token]
       else:
          if regist:
             id = self._regist_token(token)
             return id
          else:
             return Tokenizer.UNKNOWN_TOKEN
  
    def _regist_token(self, token):
         token = token.lower()
         token_id = self.token_id
         if not token in self.token_to_id_dic:
               self.token_to_id_dic[token]=token_id
               self.id_to_token_dic[token_id]=token
               self.token_id += 1
         return token_id
  
    def id_to_token(self, id):
       if id == Tokenizer.UNKNOWN_TOKEN_ID:
           return Tokenizer.UNKNOWN_TOKEN
       if id in self.id_to_token_dic:
           return self.id_to_token_dic[id]
       else:
           return Tokenizer.UNKNOWN_TOKEN
  

#
#
#
#
  
