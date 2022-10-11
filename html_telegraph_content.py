import markdown, re

def html_from_md(file: str):
    with open(file, "r") as f:
        text = f.read()
        return markdown.markdown(text)

def format_html_to_telegraph(html: str):
    result = re.sub(r"(<\/?h2>)|(<\/?kbd>)|(<\/?code>)|(\n)", ' ', html)
    return result
