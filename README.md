# GPay Laddoo Bot

A Python script that scrapes URLs, sends notifications to Telegram, and exposes a simple Flask web server.

## Setup Instructions

### 1. Change Telegram Chat ID

- **Edit `main.py`**
- Go to **line 9** and replace the value of `chat_id` with **your own Telegram Chat ID**:
  ```python
  chat_id = 'YOUR_TELEGRAM_CHAT_ID'  # <-- Change this!
  ```

### 2. Start the Telegram Bot

- Open [https://t.me/pksyahwhbot](https://t.me/pksyahwhbot) in Telegram.
- Click **Start** to activate the bot.

---

## Running with Docker

1. **Build the Docker image:**
   ```sh
   docker build -t gpayladoo .
   ```

2. **Run the container:**
   ```sh
   docker run -p 5000:5000 gpayladoo
   ```

---

## Running with Python

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```sh
   python main.py
   ```

---

## Notes

- The Flask app will be available at [http://localhost:5000](http://localhost:5000).
- Make sure to use your own Telegram Chat ID for notifications.