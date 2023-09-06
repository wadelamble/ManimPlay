import os
import subprocess
import streamlit as st
from manim import *
import openai
from openai.error import AuthenticationError
from PIL import Image

from utils import *

openai_model = "gpt-4"

openai_api_key = "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"

prompt = "draw a blue circle with a red square inscribed on it"

# Prompt must be trimmed of spaces at the beginning and end
prompt = prompt.strip()

# Remove ", ', \ characters
prompt = prompt.replace('"', '')
prompt = prompt.replace("'", "")
prompt = prompt.replace("\\", "")

try:
  openai.api_key = openai_api_key
except AuthenticationError:
  st.error(
      "Error: The OpenAI API key is invalid. Please check if it's correct.")
  st.stop()
except:
  st.error(
      "Error: We couldn't authenticate your OpenAI API key. Please check if it's correct.")
  st.stop()

try:
  response = openai.ChatCompletion.create(
      model=openai_model.lower(),
      messages=[
          {"role": "system", "content": GPT_SYSTEM_INSTRUCTIONS},
          {"role": "user", "content": wrap_prompt(prompt)}
      ],
      max_tokens=1200
  )
except:
  if openai_model.lower() == "gpt-3.5-turbo":
    st.error(
        "Error: This is likely a rate limit error for GPT-4. Currently OpenAI accepts 25 requests every 3 hours for GPT-4. This means OpenAI will start rejecting some requests randomly. There are two solutions: Use GPT-3.5-Turbo, or use your own OpenAI API key.")
    st.stop()
  else:
    st.error(
        "Error: We couldn't generate the generated code. Please reload the page, or try again later")
    st.stop()

code_response = extract_construct_code(
    extract_code(response.choices[0].message.content))

if os.path.exists(os.path.dirname(__file__) + '/../../GenScene.py'):
  os.remove(os.path.dirname(__file__) + '/../../GenScene.py')

if os.path.exists(os.path.dirname(__file__) + '/../../GenScene.mp4'):
  os.remove(os.path.dirname(__file__) + '/../../GenScene.mp4')

try:
  with open("GenScene.py", "w") as f:
    f.write(create_file_content(code_response))
except:
  st.error("Error: We couldn't create the generated code in the Python file. Please reload the page, or try again later")
  st.stop()

COMMAND_TO_RENDER = "manim GenScene.py GenScene --format=mp4 --media_dir . --custom_folders video_dir"

problem_to_render = False
try:
  working_dir = os.path.dirname(__file__) + "/../"
  subprocess.run(COMMAND_TO_RENDER, check=True, cwd=working_dir, shell=True)
except Exception as e:
  problem_to_render = True
  st.error(
      f"Error: Apparently GPT generated code that Manim (the render engine) can't process.\n\nThis is normal, since sometimes GPT can generate buggy code after all, and needs human intervention to fix it.\n\n**Ok. But what can you do now?**\n\nYou still can download the AI generated Python file with the button below (the one that failed to render) if you want to know what failed internally.\n\nYou can modify your prompt and try again. Remember, simpler and clearer prompts are better.\n\nYou can open an issue on the [GitHub Repository](https://github.com/360macky/generative-manim), attaching your prompt.")
'''
if not problem_to_render:
  try:
    video_file = open(os.path.dirname(__file__) + '/../GenScene.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
  except FileNotFoundError:
    st.error("Error: I couldn't find the generated video file. I know this is a bug and I'm working on it. Please reload the page.")
  except:
    st.error(
        "Error: Something went wrong showing your video. Please reload the page.")
'''
'''
try:
  python_file = open(os.path.dirname(__file__) + '/../GenScene.py', 'rb')
  st.download_button("Download scene in Python",
                      python_file, "GenScene.py", "text/plain")
except:
  st.error(
      "Error: Something went wrong finding the Python file. Please reload the page.")
'''
print("made it")

