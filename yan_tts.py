#############yan_tts.py#############
import os
import sys
import time
import shlex
import logging
import argparse
import subprocess
import numpy as np
import wavTranscriber

print("loading model")
dirName = os.path.expanduser('./')
output_graph, scorer = wavTranscriber.resolve_models(dirName)
model_retval = wavTranscriber.load_model(output_graph, scorer)

def speech_to_text(input_wav_file):
	try:
		segments, sample_rate, audio_length = wavTranscriber.vad_segment_generator(input_wav_file, 1)
	except:
		temp_wav = "{}.wav".format(time.time())
		os.system(u"""
			sox {} {} rate 16000 remix 1
			""".format(input_wav_file, temp_wav))
		segments, sample_rate, audio_length = wavTranscriber.vad_segment_generator(temp_wav, 1)
		os.system(u"""
			rm {}
			""".format(temp_wav))
	####
	outputs = []
	for i, segment in enumerate(segments):
		audio = np.frombuffer(segment, dtype=np.int16)
		output = wavTranscriber.stt(model_retval[0], audio, sample_rate)
		outputs.append(output[0])
	####
	outputs = '\n'.join(outputs)
	return outputs

#############yan_tts.py#############
