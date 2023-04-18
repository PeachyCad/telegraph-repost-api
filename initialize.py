import sys, json

def initialization_params():
    params = {}

    match len(sys.argv):
        case 8:
            params['file_path'] = sys.argv[1] 
            params['telegraph_token'] = '' 
            params['short_name'] = sys.argv[2] 
            params['author_name'] = sys.argv[3] 
            params['title'] = sys.argv[4] 
            params['telegram_token'] = sys.argv[5] 
            params['source_id'] = sys.argv[6] 
        case 6:
            params['file_path'] = sys.argv[1] 
            params['telegraph_token'] = sys.argv[2]
            params['short_name'] = ''
            params['author_name'] = ''
            params['title'] = sys.argv[3] 
            params['telegram_token'] = sys.argv[4] 
            params['source_id'] = sys.argv[5] 
        case _:
            cfg = json.load(open("config.json", "r"))
            params = cfg
        
    return params
            