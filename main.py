import requests, sys
from telegraph import Telegraph
from html_telegraph_content import html_from_md, format_html_to_telegraph

def send_telegraph(file: str, token: str):
    telegraph = Telegraph()
    telegraph.create_account(short_name = "somebody", author_name = "somedy_anonymous")['access_token']

    html = html_from_md(file)
    formated_html = format_html_to_telegraph(html)

    response = telegraph.create_page(title = "Test post", html_content = formated_html)
    return response

def send_telegram(text: str, token: str, source_id: str):
    url = "https://api.telegram.org/bot" + token
    channel_id = source_id
    method = url + "/sendMessage"

    r = requests.post(method, data={"chat_id": channel_id, "text": text})

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == "__main__":
    send_response = send_telegraph("post.md", sys.argv[1])
    send_telegram(send_response["url"], sys.argv[2], sys.argv[3])
