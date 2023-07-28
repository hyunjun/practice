import boto3
from pygame import mixer
import os

polly = boto3.client('polly')

korean = input()
#text = "<speak>Hi<break time='300ms'/> I am Matthew.<break time='500ms'/> It is nice to talk to you. I hope everything is well</speak>"
#text = "<speak>안녕하세요. 고객님 스위치 팀입니다. 말씀해주신 내용으로 보았을 때  열람권이 필요한 통화 이력을 말씀해주시는 것으로 보여집니다. 무료 플랜으로 통화해주신 내용은 통화일 기준 3일동안 자유롭게 열람이 가능하며 3일 이 초과되는 경우 열람권을 통해서만 열람이 가능합니다. (단, 열람 가능 기간(3일) 내 유료 플랜으로 변경해주시는 경우 통화 열람 가능 시간 내에서 자유롭게 열람 가능합니다.) 열람권을 통해 열람을 해주신 통화 이력은 열람일 기준 07일 동안 자유롭게 열람 가능하며, 횟수 제한 없이 음성 및 텍스 트 파일 다운로드 가능합니다.</speak>"
text = f"<speak>{korean}</speak>"
#aws polly synthesize-speech --text-type ssml --text "<speak>안녕하세요. 고객님 스위치 팀입니다. 말씀해주신 내용으로 보았을 때  열람권이 필요한 통화 이력을 말씀해주시는 것으로 보여집니다. 무료 플랜으로 통화해주신 내용은 통화일 기준 3일동안 자유롭게 열람이 가능하며 3일 이 초과되는 경우 열람권을 통해서만 열람이 가능합니다. (단, 열람 가능 기간(3일) 내 유료 플랜으로 변경해주시는 경우 통화 열람 가능 시간 내에서 자유롭게 열람 가능합니다.) 열람권을 통해 열람을 해주신 통화 이력은 열람일 기준 07일 동안 자유롭게 열람 가능하며, 횟수 제한 없이 음성 및 텍스 트 파일 다운로드 가능합니다.</speak>" --output-format mp3 --voice-id Seoyeon speech.mp3

#spoken_text = polly.synthesize_speech(TextType='ssml', Text=text, OutputFormat='mp3', VoiceId='Matthew')
spoken_text = polly.synthesize_speech(TextType='ssml', Text=text, OutputFormat='mp3', VoiceId='Seoyeon')

with open('output.mp3', 'wb') as f:
    f.write(spoken_text['AudioStream'].read())
    f.close()

mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()

while mixer.music.get_busy() == True:
    pass

mixer.quit()

filename = 'output.mp3'
bucket = 'juntest-mp3'
key = 'speech.mp3'
s3 = boto3.client('s3')
res = s3.upload_file(filename, bucket, key)

os.remove('output.mp3')
