# Telegram Prediction Bot (Render Deployment)

✅ This is a complete, 100% free Telegram Bot powered by python-telegram-bot and hosted on Render.com

---

## 📁 Files Included
- main.py → your bot logic
- requirements.txt → needed Python libraries
- render.yaml → Render deployment config

---

## 🚀 How to Deploy on Render (Free)

1. Go to [https://render.com](https://render.com) and sign up
2. Create a new service
3. Connect your GitHub and select the repo with these files
4. Fill config:

| Field             | Value              |
|------------------|--------------------|
| Runtime           | Python             |
| Build Command     | pip install -r requirements.txt |
| Start Command     | python main.py     |

5. Set Environment Variable:
   - TELEGRAM_TOKEN: 8100400385:AAGIwJ5JV-D21rU9aWlBM1lpLcO00vTvn4A

6. Click Deploy – done ✅

---

## ✅ Usage
- Start bot from Telegram
- Type /start
- Enter your "Expectation ID"
- Choose game → Get prediction results

---

If you face any issues, contact your developer or check https://render.com/docs/deploy-python.