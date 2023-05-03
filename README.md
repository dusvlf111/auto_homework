# 과제 자동화 프로그램!!!


# GPT-3 API를 이용한 챗봇

본 프로젝트는 OpenAI의 GPT-3 API를 이용하여 과제파일을 만들어주는 챗봇을 구현하는 예제입니다. 

## 사용 방법

1. Config 클래스를 이용하여 OpenAI API key를 설정합니다.
2. ChangeText 클래스를 이용하여 입력할 텍스트를 작성합니다. 특정폴더에 있는 문서를 인식해 텍스트로 변환합니다.
3. GPT 클래스를 이용하여 생성된 텍스트를 입력으로 받아 GPT-3 API를 호출하여 응답을 생성합니다.
4. 생성된 응답을 확인합니다.

## 필요한 라이브러리

- OpenAI
- PyMuPDF
- hwp5py
- pptx
- docx

## 사용 예시

```python
from GPT import GPT, ChangeText

# API key 설정
config = Config()

# 텍스트 생성
change = ChangeText()
text = change.run()

# GPT 생성 및 응답 생성
gpt_obj = GPT(text)
response_list = gpt_obj.chat_with_gpt(["Hello, how are you?", "What is your name?"])
print(response_list)
