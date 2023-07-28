# STT & TTS

## Preparation
* installation

  ```
  ❯ brew install awscli
  ❯ pip3 install awscli pygame boto3
  ```
* S3 bucket 생성 & aws cli configuration 필요

## Execution

```
echo "안녕하세요. 고객님 스위치 팀입니다. 말씀해주신 내용으로 보았을 때  열람권이 필요한 통화 이력을 말씀해주시는 것으로 보여집니다. 무료 플랜으로 통화해주신 내용은 통화일 기준 3일동안 자유롭게 열람이 가능하며 3일 이 초과되는 경우 열람권을 통해서만 열람이 가능합니다. (단, 열람 가능 기간(3일) 내 유료 플랜으로 변경해주시는 경우 통화 열람 가능 시간 내에서 자유롭게 열람 가능합니다.) 열람권을 통해 열람을 해주신 통화 이력은 열람일 기준 07일 동안 자유롭게 열람 가능하며, 횟수 제한 없이 음성 및 텍스 트 파일 다운로드 가능합니다" | python3 test_polly.py && python3 test_transcribe.py
```

## Ref
* 과거 자료지만 그대로 동작 가능
  * [파이썬으로 AI 음성합성하기 Amazon Polly](https://digiconfactory.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-AI-%EC%9D%8C%EC%84%B1%ED%95%A9%EC%84%B1%ED%95%98%EA%B8%B0-Amazon-Polly)
  * [boto3를 사용한 파일 업로드와 파일 다운로드](https://ahnjg.tistory.com/15)
  * [Amazon transcribe로 한국어 음성인식 Speech To Text(STT) 사용하기](https://daeunnniii.tistory.com/122)
