"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import pyttsx3
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCD29nqgv4Xym4aQ7oz3kd9tfngC-5t13A")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("Who are the members of the BTS?")

print(response.text)
engine=pyttsx3.init()
engine.say(response.text)
engine.runAndWait()