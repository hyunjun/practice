# STT & TTS

## Preparation
* installation

  ```
  ❯ pip3 install azure-cognitiveservices-speech
  ```
* azure service key

## Execution

```
❯ SPEECH_KEY=<speech key> SPEECH_REGION=eastus python3 main.py
```

### speech key
* 다음 설정 화면의 KEY 1 사용
<img width="995" alt="Screenshot 2023-07-28 at 7 10 24 PM" src="https://github.com/hyunjun/practice/assets/248764/f98e8b98-b512-45af-97cb-28858e34ba3d">

* `speech_config.speech_synthesis_voice_name='ko-KR-JiMinNeural'` 여기에 원하는 이름을 설정하면 목소리 변경 가능
<img width="1469" alt="Screenshot 2023-07-28 at 7 08 33 PM" src="https://github.com/hyunjun/practice/assets/248764/93524450-475f-4fdc-94e3-cd9680ab4a0d">

### conversation text file
* `EXAMPLE_DIR`로 설정한 directory의 text file에 설정
* `C:`로 시작하면 client
* `CS:`로 시작하면 customer support

## Ref
* [Text to speech quickstart - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech)
* [Speech to text quickstart - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text)
* [cognitive-services-speech-sdk/quickstart/python/from-microphone at master · Azure-Samples/cognitive-services-speech-sdk](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python/from-microphone)
* 대화 데이터 예제는 여기서 가져옴
  * [상담 예시로 보는 굿콜(Good Call), 배드콜(Bad Call) 2탄｜ (CS쉐어링은 채용중!, 콜센터업무) - CS쉐어링](http://cssharing.com/cs-%EA%BF%80%ED%8C%81-cs%EA%BF%80%ED%8C%81-%EC%83%81%EB%8B%B4-%EC%98%88%EC%8B%9C%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EA%B5%BF%EC%BD%9Cgood-call-%EB%B0%B0%EB%93%9C%EC%BD%9Cbad-call-2%ED%83%84%EF%BD%9C/)
