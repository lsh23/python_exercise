import os


def get_file_list(keyward):
    return os.listdir(keyward)
# os의 힘을 빌려서 폴더에있는 파일명들을 리스트로

def get_conetents(file_list):
    y_class = []
    X_text = []   
    class_dict = {
        1: "0", 2: "0", 3:"0", 4:"0", 5:"1", 6:"1", 7:"1", 8:"1"}

    for file_name in file_list:
        try:
            f = open(file_name, "r",  encoding="cp949")
            # 파일리스트로 부터 파일명을 받아서 파일을 cp949 로 디코딩하여서 읽어 들여서
            category = int(file_name.split(os.sep)[1].split("_")[0])
            # os.sep은 separater로 서 win은 \\ mac/linux는 /이다.
            # 1_Dae-Ho Lee walk-off homer gives Mariners 4-2 win over Rangers.txt
            # 에서 1만 추출됨
            y_class.append(class_dict[category])
            # y_class에서 축구인지 야구인지
            X_text.append(f.read())
            # X_text에서는 해당 기사 Data
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class


def get_cleaned_text(text):
    import re
    text = re.sub('\W+','', text.lower() )
    return text
    #정규표현식 표현 중 하나로서 의미없는 문장부호들을 다 제거해주고 반환해줌

def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    clenad_words = [get_cleaned_text(word) for words in text for word in words]
    # text에는 각 문장에 대해서 split된 list들이 2차원으로 저장되어있다.
    # clenaa_words에는 1차원으로 모든 word들만 깨끗하게 정리되어서 저장되어있다

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(clenad_words)):
        corpus_dict[v] = i
    return corpus_dict
    # cleand_words들에대해서 set화 해주고 이것을 enmerate해줘서 dict로 만들어준다.
    # corpus_dict = [ 'word' = i , .... ]



def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]
    # 단어들이 존재하는 인덱스들의 2차원정보
    # I = 300 LOVE = 243 YOU = 32 일때
    # [ [300, 243 , 32 , - - -] , [],[]]

    X_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]
    # vector를 0으로 초기화해주고
    for i, text in enumerate(word_number_list):
        for word_number in text:
            X_vector[i][word_number] += 1
    return X_vector
    # 해당 인덱스의 해당하는 Word가 존재하면 1씩 더해준다.

import math
def get_cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)
    # 내적 공식을 이용해서 cosine_similarity 값을 구한다.


def get_similarity_score(X_vector, source):
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector))
    return similarity_list
    #source_vector 분석대상 벡터
    #X_vector 데이터 벡터

def get_top_n_similarity_news(similarity_score, n):
    import operator
    x = {i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n+1]
    #유사도가 높은 데이터들을 뽑아준다.

def get_accuracy(similarity_list, y_class, source_news):
    source_class = y_class[source_news]

    return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)


if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    X_text, y_class = get_conetents(file_list)
    corpus = get_corpus_dict(X_text)
    print("Number of words : {0}".format(len(corpus)))

    X_vector = get_count_vector(X_text, corpus)
    source_number = 10

    result = []

    for i in range(80):
        source_number = i
        similarity_score = get_similarity_score(X_vector, source_number)
        similarity_news = get_top_n_similarity_news(similarity_score, 10)
        accuracy_score = get_accuracy(similarity_news, y_class, source_number)
        result.append(accuracy_score)
    print(sum(result) / 80)
