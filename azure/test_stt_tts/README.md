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

### `speech_synthesis.py`
* `speech_config.speech_synthesis_voice_name='ko-KR-JiMinNeural'` 여기에 원하는 이름을 설정하면 목소리 변경 가능

## Ref
* [Text to speech quickstart - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech)
* [Speech to text quickstart - Speech service - Azure AI services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text)
* [cognitive-services-speech-sdk/quickstart/python/from-microphone at master · Azure-Samples/cognitive-services-speech-sdk](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python/from-microphone)
