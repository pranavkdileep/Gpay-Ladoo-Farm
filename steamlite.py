import requests
import bs4
import random
import string
import threading

globlerror = ''


def send_telegram_message(msg):
    bot_token = '6408802782:AAF0J0pTg_tpAmzLmqy2B54i8d--97y9Q6g'
    chat_id = '1196575861'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': msg
    }

    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message:", response.text)

def generate_random_string(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def send_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = bs4.BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        imageurl = soup.find('meta', property='og:image')
        if imageurl:
            imageurl = imageurl['content'].split('&')[1].split('@')[0]
        else:
            imageurl = 'No image URL found'
        if title != 'No title found' and title != 'Can you gift me a Sparky Laddoo?':
            send_telegram_message(f"{title} - {url}")
            with open('urls.txt', 'a') as file:
                file.write(f"{imageurl} - {url}\n")
            return {
                'title': title,
                'imageurl': imageurl,
                'url': url
            }
        else:
            print("Title is either 'No title found' or 'Can you gift me a Sparky Laddoo?'")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        global globlerror
        globlerror = str(e)
        return None

def worker():
    while True:
        base_url = "https://gpay.app.goo.gl/"
        url = base_url + generate_random_string(6)
        send_request(url)

def main():
    try:
        num_threads = 100
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()