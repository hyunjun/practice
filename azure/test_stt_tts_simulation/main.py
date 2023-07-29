import os
import random
import sys
import time

import azure.cognitiveservices.speech as speechsdk

EXAMPLE_DIR = 'examples'


class SpeechSynthesis:

    def __init__(self, speechKey, region):
        self.speech_config = speechsdk.SpeechConfig(subscription=speechKey, region=region)
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)

    def speech(self, text):
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

    def __init__(self, speechKey, region):
        super().__init__(speechKey, region)
        self.speech_config.speech_synthesis_voice_name='ko-KR-GookMinNeural'
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)


class Client(SpeechSynthesis):

    def __init__(self, speechKey, region):
        super().__init__(speechKey, region)
        self.speech_config.speech_synthesis_voice_name='ko-KR-JiMinNeural'
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)


if __name__ == '__main__':
    speech_key, region = os.environ.get('SPEECH_KEY'), os.environ.get('SPEECH_REGION')
    if speech_key is None or 0 == len(speech_key) or region is None or 0 == len(region):
        print('You must set SPEECH_KEY and SPEECH_REGION environmental variables')
        sys.exit(1)

    cs = CustomerSupport(speech_key, region)
    c = Client(speech_key, region)

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
