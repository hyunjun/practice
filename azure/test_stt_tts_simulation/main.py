import os
import random
import sys
import time

import azure.cognitiveservices.speech as speechsdk

EXAMPLE_DIR = 'examples'


class SpeechSynthesis:

    def __init__(self, speechKey, region, voiceName, isSSMLEnabled=False):
        self.speech_config = speechsdk.SpeechConfig(subscription=speechKey, region=region)
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_config.speech_synthesis_voice_name = voiceName
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)
        self.isSSMLEnabled = isSSMLEnabled


    def ssmlString(self, text):
        return f'''<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="ko-KR">
    <voice name="{self.speech_config.speech_synthesis_voice_name}">
        {text}
    </voice>
</speak>'''

    def speech(self, text):
        if self.isSSMLEnabled:
            speech_synthesis_result = self.speech_synthesizer.speak_ssml_async(self.ssmlString(text)).get()
        else:
            speech_synthesis_result = self.speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            pass
            #print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")


class CustomerSupport(SpeechSynthesis):
    VOICE_NAME = 'ko-KR-GookMinNeural'

    def __init__(self, speechKey, region, isSSMLEnabled=False):
        super().__init__(speechKey, region, CustomerSupport.VOICE_NAME, isSSMLEnabled)


class Client(SpeechSynthesis):
    VOICE_NAME = 'ko-KR-JiMinNeural'

    def __init__(self, speechKey, region, isSSMLEnabled=False):
        super().__init__(speechKey, region, Client.VOICE_NAME, isSSMLEnabled)

    def ssmlString(self, text):
        return f'''<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="ko-KR">
    <voice name="{self.speech_config.speech_synthesis_voice_name}">
        <mstts:express-as role="YoungAdultFemale" style="angry" styledegree="2">
        <prosody rate="medium" pitch="x-high">
            {text}
        </prosody>
        </mstts:express-as>
    </voice>
</speak>'''

if __name__ == '__main__':
    speech_key, region = os.environ.get('SPEECH_KEY'), os.environ.get('SPEECH_REGION')
    if speech_key is None or 0 == len(speech_key) or region is None or 0 == len(region):
        print('You must set SPEECH_KEY and SPEECH_REGION environmental variables')
        sys.exit(1)

    cs = CustomerSupport(speech_key, region, True)
    c = Client(speech_key, region, True)

    while True:
        print('\nInput number or Q/q to exit')

        files = os.listdir(EXAMPLE_DIR)
        for i, filename in enumerate(files):
            print(f'[{i}] {filename}')

        inp = input()
        if inp == 'Q' or inp == 'q':
            break
        num = int(inp)
        print(f'You would like to simulate {files[num]}\n')

        with open(f'{EXAMPLE_DIR}/{files[num]}') as f:
            for line in f.readlines():
                if line.startswith('C:'):
                    text = line[2:].strip()
                    print(f'\nclient: {text}')
                    print("simulating client's voice")
                    time.sleep(1 + random.random())
                    c.speech(text)
                elif line.startswith('CS'):
                    text = line[3:].strip()
                    print("\nlistening to customer support's voice")
                    cs.speech(text)
                    print(f'customer support: {text}')
