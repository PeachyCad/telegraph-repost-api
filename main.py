import requests
from initialize import initialization_params
from telegraph import Telegraph
from html_telegraph_content import html_from_md, format_html_to_telegraph

def send_telegraph(file_path: str, telegraph_token: str, short_name : str, author_name : str, title : str):
    if (telegraph_token == ''):
        telegraph = Telegraph()
        telegraph.create_account(short_name = short_name, author_name = author_name)['access_token']
    else :
        telegraph = Telegraph(telegraph_token)

    html = html_from_md(file_path)
    formated_html = format_html_to_telegraph(html)

    response = telegraph.create_page(title, html_content = formated_html)
    return response

def send_telegram(text: str, token: str, source_id: str):
    url = "https://api.telegram.org/bot" + token
    channel_id = source_id
    method = url + "/sendMessage"

    r = requests.post(method, data={"chat_id": channel_id, "text": text})

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == "__main__":
    params = initialization_params()
    
    send_response = send_telegraph(params['file_path'], params['telegraph_token'], params['short_name'], params['author_name'], params['title'])
    send_telegram(send_response["url"], params['telegram_token'], params['source_id'])
