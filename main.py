import os
import telebot
import openai
from gtts import gTTS
import subprocess

# 1. टोकन्स और API Keys सेट अप
API_TOKEN = '822758544:AAGtAPJs4oi7AcR8RB88FA2kN'
bot = telebot.TeleBot(API_TOKEN)
openai.api_key = os.getenv("OPENAI_API_KEY")

# 2. टेलीग्राम मैसेज हैंडलर (जो पहले से चल रहा था)
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text.lower()
    
    if any(word in user_text for word in ['loan', 'लोन', 'credit']):
        reply_msg = "मैंने आपकी रिक्वेस्ट हमारे सीनियर लोन एडवाइजर को भेज दी है। जल्द ही आपको कॉल आएगा!"
    else:
        reply_msg = "नमस्ते! मैं आपका लोन एडवाइजर हूँ। लोन या क्रेडिट कार्ड से जुड़ी किसी भी मदद के लिए अपना मोबाइल नंबर यहाँ भेजें।"
        
    bot.reply_to(message, reply_msg)

# 3. मास्टर ऑटोमेशन फंक्शन (वीडियो और स्क्रिप्ट बनाने के लिए)
def master_automation():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Write a viral 30-sec script about AI."}]
        )
        script = response.choices[0].message.content
        
        tts = gTTS(text=script, lang='hi')
        tts.save("audio.mp3")
        
        subprocess.run([
            'ffmpeg', '-i', 'audio.mp3', 
            '-f', 'lavfi', '-i', 'color=s=1080x1920', 
            '-c:v', 'libx264', '-t', '30', 'final_output.mp4'
        ])
        print("वीडियो रेंडरिंग पूरी हो गई है!")
    except Exception as e:
        print(f"ऑटोमेशन में एरर आया: {e}")

if __name__ == "__main__":
    print("बोट पूरी तरह चालू हो रहा है...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
    
