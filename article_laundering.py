# -*- coding: utf-8 -*-
"""Article Laundering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9
"""

import gensim
#    !pip3 install opencc-python-reimplemented
from opencc import OpenCC
import jieba
import jieba.posseg as pseg
import jieba.analyse
import string
import textwrap

#from google.colab import drive
#drive.mount('/content/drive/')

from gensim.models.word2vec import Word2Vec
model = gensim.models.KeyedVectors.load_word2vec_format('C:/Users/W7/Downloads/qqqq.model.bin', unicode_errors='ignore', binary=True)

#篩選門檻值
turnout = 0.7
#修改幅度上限
spread = 0.25
#隨機詞
#rand = false


input2=input('輸入文章內容:')


tag_pocket=[]
token_pocket=[]

#input2='很感謝你願意拍影片分享給我們這些教學，你的技術分析真的很有邏輯很厲害，影片雖然都短短的，但是教了很多很重要很精闢的東西.真心感謝，而且你講話的風格很棒，聽起來像在罵人，但其實不是，就是真的說實話而已，哈哈。'
context = input2

before = context

cc = OpenCC('tw2sp')
input2 = cc.convert(input2)

keywords = jieba.analyse.extract_tags(input2, topK=int(len(input2)*spread) ,withWeight=True)

for item,v in keywords:
  cc = OpenCC('s2twp')
  tag_master=cc.convert(item)
  tag_pocket.append(tag_master)
  print(tag_master)
print(tag_pocket)

xxx=[]
for i in tag_pocket:
    try:
        lst = model.most_similar(i)
    except:
        lst = []
    if lst and lst[0][1] > turnout:
        xxx.append(lst[0][0])
        print(str(lst[0][0]),str(lst[0][1]))
        context=context.replace(i,str(lst[0][0]))
print()
print('before:\n'+'\n'.join(textwrap.wrap(before,width=150))+'\n'+'\nafter:\n'+'\n'.join(textwrap.wrap(context,width=250)))

for i in set(xxx):
  context=context.replace(i, '['+i+']')
print('before:\n'+'\n'.join(textwrap.wrap(before,width=150))+'\n'+'\nafter:\n'+'\n'.join(textwrap.wrap(context,width=250)))