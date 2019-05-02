'''
    chatbot을 훈련시키는 부분.

    HOWTO:
    python trainer.py

    TODO:
    - 구문 비교 방법 개선
'''


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.comparisons import JaccardSimilarity
from myTrainer import DummyTrainer
from qaset import qaset

chatbot = ChatBot("Dummy",
        logic_adapters=[
            {
                'import_path': "chatterbot.logic.BestMatch",
                # 응답의 정확도가 90% 이하면 기본 응답 반환
                'default_response': '잘 못 알아들었습니다?',
                'maximum_similarity_threshold': 0.90
            }
        ],
        # JaccardSimilarity라는 정확도 계산 방식을 사용
        statement_comparison_function=JaccardSimilarity,
        # sqlite3를 이용
        database="db.sqlite3",
        )

corpustrainer = ChatterBotCorpusTrainer(chatbot)
mytrainer = DummyTrainer(chatbot)
listtrainer = ListTrainer(chatbot)

corpustrainer.train(
    # 한국어 corpus를 이용하여 기초 훈련
    "chatterbot.corpus.korean.greetings"
)
mytrainer.train(qaset)
listtrainer.train([
    "유통기한",
    "어느 음식의 유통기한을 알려드릴까요?",
    "쌈장",
    "쌈장의 유통기한은 제조일로부터 3개월입니다.",])
