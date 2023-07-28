import time
import boto3

transcribe = boto3.client('transcribe')
job_name = "test_transcribe"
job_uri = "s3://juntest-mp3/speech.mp3"
transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='ko-KR'
    )
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Waiting")
    time.sleep(5)
print(status)
