# 🤖 SupportBot Webhook (Dialogflow + Flask)

This is a simple **Dialogflow chatbot webhook** built using **Python Flask** and deployed on **Render**.

---

## 🚀 Features
- Webhook built with Flask
- Integrated with Dialogflow Essentials
- Hosted on Render with live URL
- Responds to intent: `fallback_to_webhook`

---

## 🧠 How It Works
1. Dialogflow agent listens for user queries.
2. If the matched intent has webhook enabled (`fallback_to_webhook`), it sends a POST request to the webhook URL.
3. Flask receives the request, checks the intent, and sends back a response message.

---

## 🛠️ Files

| File              | Description                          |
|-------------------|--------------------------------------|
| `app.py`          | Flask server with webhook logic      |
| `requirements.txt`| Libraries needed for deployment      |
| `README.md`       | Project documentation                |

---

## 🌐 Live Webhook URL
This project is hosted on [Render](https://render.com):

**🔗 https://supportbot-webhook.onrender.com/webhook**

> Use this URL in Dialogflow's Fulfillment section.

---

## 📦 Setup Locally

```bash
git clone https://github.com/Ujjvalsharma/supportbot-webhook.git
cd supportbot-webhook
pip install -r requirements.txt
python app.py
