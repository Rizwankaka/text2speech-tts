import streamlit as st
from openai import OpenAI
import tempfile
import os

# Function to convert text to speech, modified to explicitly use an API key
def text_to_speech(api_key, text: str):
    """
    Converts text to speech using OpenAI's tts-1 model and saves the output as an MP3 file,
    explicitly using an API key for authentication.
    """
    # Initialize the OpenAI client with the provided API key
    client = OpenAI(api_key=api_key)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        speech_file_path = tmpfile.name
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        # Stream the audio response to file
        response.stream_to_file(speech_file_path)
        
        # Return the path to the audio file
        return speech_file_path
# Set a solid background color
def set_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_color()

# Set a background image
# def set_background_image():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: url("https://yourimageurl.com/yourimage.jpg");
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# set_background_image()

# Streamlit UI setup
st.title("🔊 Text to Speech Converter 📝")
st.image("https://www.piecex.com/product_image/20190625044028-00000544-image2.png")
st.markdown("""
This app converts text to speech using OpenAI's tts-1 model. 
Please enter your OpenAI API key below. **Do not share your API key with others.**
""")

# Input for OpenAI API key
api_key = st.text_input("Enter your OpenAI API key", type="password")

# Text input from user
user_input = st.text_area("Enter text to convert to speech", "Hello, welcome to our text to speech converter!")

if st.button("Convert"):
    if not api_key:
        st.error("API key is required to convert text to speech.")
    else:
        try:
            speech_path = text_to_speech(api_key, user_input)
            
            # Display a link to download the MP3 file
            st.audio(open(speech_path, 'rb'), format="audio/mp3")
            
            # Clean up: delete the temporary file after use
            os.remove(speech_path)
        except Exception as e:
            st.error(f"An error occurred: {e}")
# Adding the HTML footer

footer_html = """
<div style="text-align: left;">
    <p style="font-size: 25px;"><b>Author: 🌟 Rizwan Rizwan 🌟</b></p>
    <a href="https://github.com/Rizwankaka"><img src="https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github" alt="GitHub"/></a><br>
    <a href="https://www.linkedin.com/in/rizwan-rizwan-1351a650/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a><br>
    <a href="https://twitter.com/RizwanRizwan_"><img src="https://img.shields.io/badge/Twitter-Profile-blue?style=for-the-badge&logo=twitter" alt="Twitter"/></a><br>
    <a href="https://www.facebook.com/RIZWANNAZEEER"><img src="https://img.shields.io/badge/Facebook-Profile-blue?style=for-the-badge&logo=facebook" alt="Facebook"/></a><br>
    <a href="mailto:riwan.rewala@gmail.com"><img src="https://img.shields.io/badge/Gmail-Contact%20Me-red?style=for-the-badge&logo=gmail" alt="Gmail"/></a>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)