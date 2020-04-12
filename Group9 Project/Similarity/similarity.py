import numpy as np
import pandas as pd
import jieba

import jieba
import jieba.posseg as pseg
import jieba.analyse as anls

punctuation = ["，", "。", "：", "；", "？"]
question_path = 'C:/Users/kyrie/Desktop/Year3/Machine Learning and AI/testProject/Group9 Project/Similarity/question.txt'
answer_path = 'C:/Users/kyrie/Desktop/Year3/Machine Learning and AI/testProject/Group9 Project/Similarity/answer.txt'
input_text = []
#compute cosine similarity


def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA**0.5)*(normB**0.5)) * 100, 2)

with open(question_path, 'r', encoding='utf-8')as f:
    input_text = f.read().split('\n')
    #read the question

 #cut the word
segs_1 = [jieba.lcut(con) for con in input_text]

# remove the space in each sentence
for sentence in segs_1:
    while ' 'in sentence:
        sentence.remove(' ')

tokenized = []
for sentence in segs_1:
    words = []
    for word in sentence:
        if word not in punctuation:
            words.append(word)

    tokenized.append(words)
#get the key word of all the data into a list
#求并集
bag_of_words = [x for item in segs_1 for x in item if x not in punctuation]
#去重
bag_of_words = list(set(bag_of_words))
#change the question into vectors
bag_of_word2vec = []
for sentence in tokenized:
    tokens = [1 if token in sentence else 0 for token in bag_of_words]
    bag_of_word2vec.append(tokens)

#read the answer
output_text = []
with open(answer_path, 'r', encoding='UTF-8')as f:
    output_text = f.read().split('\n')


prompt="Enter your question:(enter quit to quit) "
question=" "
while question!="quit":
    question=input(prompt)
    input_q=[question]
    segs_question=[jieba.lcut(con) for con in input_q]
    #delete the punctuation in the sentence
    tokenized_q=[]
    for sentence in segs_question:
        words = []
        for word in sentence:
            if word not in punctuation:
                words.append(word)

        tokenized_q.append(words)
    # change the input question to vector
    input_vec = []
    for sentence in tokenized_q:
        tokens = [1 if token in sentence else 0 for token in bag_of_words]
        input_vec.append(tokens)

    #use cosine similarity to find the match question in the data set
    temp = 0
    fit = 0
    for i in range(121):
        if cosine_similarity(input_vec[0], bag_of_word2vec[i]) > temp:
            temp = cosine_similarity(input_vec[0], bag_of_word2vec[i])
            fit = i
    if question!="quit":
        print(output_text[fit])






