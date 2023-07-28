# STT & TTS

## Preparation
* installation

  ```
  ❯ pip3 install azure-cognitiveservices-speech
  ```
* azure service key

## Execution

```
❯ SPEECH_KEY=<speech key> SPEECH_REGION=eastus python3 speech_synthesis.py
❯ SPEECH_KEY=<speech key> SPEECH_REGION=eastus python3 stt.py
```

### speech key
* 다음 설정 화면의 KEY 1 사용
<img width="995" alt="Screenshot 2023-07-28 at 7 10 24 PM" src="https://github.com/hyunjun/practice/assets/248764/f98e8b98-b512-45af-97cb-28858e34ba3d">

### `speech_synthesis.py`
* `speech_config.speech_synthesis_voice_name='ko-KR-JiMinNeural'` 여기에 원하는 이름을 설정하면 목소리 변경 가능
<img width="1469" alt="Screenshot 2023-07-28 at 7 08 33 PM" src="https://github.com/hyunjun/practice/assets/248764/93524450-475f-4fdc-94e3-cd9680ab4a0d">

## Ref
* [Text to speech quickstart - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech)
* [Speech to text quickstart - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text)
* [cognitive-services-speech-sdk/quickstart/python/from-microphone at master · Azure-Samples/cognitive-services-speech-sdk](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python/from-microphone)
