# _*_ coding:utf-8 _*_
import jieba
import hanziconv
import time, os

# def write_token_to_f(open_file, output_file):
#     words = []
#     for line in open(open_file, encoding='utf-8'):
#         w = list(jieba.cut(line))
#         ## 繁体字转换成简体字
#         str_w = ' '.join(str(i) for i in w)
#         simple_w = hanziconv.HanziConv.toSimplified(str_w)
#         list_w = []
#         list_w.append(simple_w)
#         words += list_w + ['\n']
#     output_file.writelines(' '.join(words))
#
# target_files = os.listdir()
# start = time.time()
# num = 0
# with open('wiki_training.txt', 'w', encoding='utf-8') as output_f:
#     for f in target_files:
#         if not f.startswith('wiki'): continue
#         print('processing: {}'.format(num))
#         num += 1
#         write_token_to_f(f, output_f)
# end = time.time()
# print('used time {}'.format(end - start))
# # 训练模型
from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence
# s = time.time()
# mini_model = Word2Vec(LineSentence('wiki_training.txt'), min_count=1, size=100)
#
# # 4保存模型，以便重用
# mini_model.save("test_01.model")   #保存模型
# mini_model.wv.save_word2vec_format('test_01.model.txt','test_01.vocab.txt',binary=False) # 将模型保存成文本，model.wv.save_word2vec_format()来进行模型的保存的话，会生成一个模型文件。里边存放着模型中所有词的词向量。这个文件中有多少行模型中就有多少个词向量。
# #5词向量验证
# #加载训练好的模型
model = Word2Vec.load("test_01.model")  #加载训练好的语料模型
#
# e = time.time()
# print('train model use time: {}'.format(e-s))
# print(model.wv['中国'])
print(model.most_similar('说话'))

