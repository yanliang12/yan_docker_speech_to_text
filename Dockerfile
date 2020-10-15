#################################
FROM python:3.7

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl

RUN pip install deepspeech

RUN curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.pbmm

RUN curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.scorer

RUN pip install webrtcvad
RUN pip install pyqt5

RUN git clone https://github.com/yanliang12/DeepSpeech-examples.git

RUN mv /DeepSpeech-examples/vad_transcriber/* ./

RUN apt-get install -y sox

RUN git clone https://github.com/yanliang12/yan_docker_speech_to_text.git
RUN mv /yan_docker_speech_to_text/* ./

CMD bash
#################################
