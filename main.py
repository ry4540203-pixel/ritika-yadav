import telebot

API_TOKEN = '7993459299:AAGeoHtMZDyky1fPUkeODPy06ZHK74nxVWY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text.lower()
    
    if any(word in user_text for word in ['loan', 'लोन', 'home loan', 'personal loan', 'help', 'expert']):
        reply_msg = "मैंने आपकी रिक्वेस्ट हमारे सीनियर लोन एक्सपर्ट को फॉरवर्ड कर दी है, वे जल्द ही आपसे संपर्क करेंगे। कृपया अपना फोन नंबर शेयर करें।"
    else:
        reply_msg = "नमस्ते! मैं आपका लोन एडवाइज़र हूँ। बताइए, आपको किस प्रकार के लोन के बारे में जानकारी चाहिए?"
        
    bot.reply_to(message, reply_msg)

print("बॉट पूरी तरह चालू हो गया है!")
bot.infinity_polling(timeout=10, long_polling_timeout=5)

