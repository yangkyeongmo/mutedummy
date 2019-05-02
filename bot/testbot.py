'''
    훈련된 chatbot을 실행하여 대화를 구동하는 부분.

    Required:
    https://github.com/gunthercox/chatterbot-corpus.git
    https://github.com/gunthercox/chatterbot.git

    HOWTO:

    # 아래 두 줄은 필요한 라이브러리 가져오는 부분. 최초 1회만 하면 됨. 이미 되어있어 직접 할 필요 없음
    git clone https://github.com/gunthercox/ChatterBot.git
    git clone https://github.com/gunthercox/chatterbot-corpus.git
    # 훈련 데이터 생성
    python trainer.py
    # 챗봇 구동
    python testbot.py
'''


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 읽기 전용으로 새로운 챗봇을 생성
chatbot = ChatBot("Dummy", read_only=True,)

if __name__ == "__main__":
    # 최초 사용자 입력을 받아옴
    _in = input('You: ')
    # 사용자 입력이 있으면 반복
    while(_in is not None):
        # 챗봇의 응답을 출력
        response = chatbot.get_response(_in)
        print(chatbot.name + ":", response)
        # 응답의 정확도를 출력
        print("Score:", response.confidence)
        # 다음 응답을 가져옴
        _in = input('You: ')
        # 응답이 있는 이상 무한루프를 돌기때문에 Ctrl+C로 종료
