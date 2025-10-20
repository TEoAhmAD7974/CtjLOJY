# 代码生成时间: 2025-10-21 07:50:40
#!/usr/bin/env python

"""
Text-to-Speech Application using Bottle Framework
==================
This application demonstrates how to create a simple text-to-speech tool using the Bottle web framework.
It takes text input from the user and converts it into speech using a specified voice.

Usage:
    python text_to_speech_app.py
"""

import bottle
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Define the application route
@bottle.route('/text_to_speech', method='POST')
def text_to_speech():
    # Get the input text from the request body
    input_text = bottle.request.json.get('text', '')
    if not input_text:
        return bottle.HTTPResponse(status=400, body='Text is required.')

    try:
        # Generate the speech audio file
        tts = gTTS(text=input_text, lang='en')
        audio_file = 'speech.mp3'
        tts.save(audio_file)

        # Play the generated speech audio file
        play(audio_file)

        # Return the success message
        return bottle.HTTPResponse(status=200, body='Speech generated successfully.')
    except Exception as e:
        # Return the error message if any exception occurs
        return bottle.HTTPResponse(status=500, body=str(e))

# Run the application
if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
