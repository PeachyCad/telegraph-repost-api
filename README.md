# telegraph-repost-api
Combination of tools for reposting https://telegra.ph posts to Telegram chat/channel with bot API

## Installation
Call next command:
```
pip install -r requirements.txt
```

## Using
You can use **main.py** like that:

* Using sys.args like that: 
```
python main.py file_path short_name author_name title telegram_bot_token source_id
``` 
Or with **telegraph_token**:
```
python main.py file_path telegraph_token title telegram_bot_token source_id
```

* Using config.json:
```
    {
        "file_path" : "file_path",
        "telegraph_token" : "telegraph_token",
        "short_name" : "short_name",
        "author_name" : "author_name",
        "title" : "title",
        "telegram_bot_token" : "telegram_bot_token",
        "source_id" : "source_id"
    }
```
