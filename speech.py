# -*- coding: utf-8 -*-

import os
try:
	from google.cloud import texttospeech
except:
	pass

# supported languages: da, de, en, fr, it, ja, ko, nl, pt, ru, sk, sv, tr ,es

def text_to_speech(text, lang):
	try:
		client = texttospeech.TextToSpeechClient()
		input_text = texttospeech.types.SynthesisInput(text=text)
		voice = texttospeech.types.VoiceSelectionParams(language_code=lang,
			ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
		audio_config = texttospeech.types.AudioConfig(
			audio_encoding=texttospeech.enums.AudioEncoding.MP3)

		response = client.synthesize_speech(input_text, voice, audio_config)
	except:
		return
	try:
		print('🔉')
		with open('output-95af1670a84.mp3', 'wb') as out:
			out.write(response.audio_content)
		os.system('afplay output-95af1670a84.mp3')
		os.system('rm -f output-95af1670a84.mp3')
	except:
		print('Error: Audio could not be played')
		os.system('rm =f output-95af1670a84.mp3')
