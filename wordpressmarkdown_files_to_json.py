import io
import os
import json
from datetime import datetime

paths = os.listdir("/Users/jasweeney/Documents/Wordpress Markdown files/")
directory = "/Users/jasweeney/Documents/Wordpress Markdown files/"

for path in paths:
    
    with io.open(directory + path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    
#     try:
        title = lines[3][6:].replace('\n', '')
        title = datetime.strptime(title, '%Y-%m-%d %H:%M')
        title = title.strftime('%B %d, %Y')
        title = title + " " +lines[2][7:].replace("\n", "").replace("|", "-").replace(":", "-").replace("/", "-").replace("?", ".").replace('"', "")
        created = lines[3][6:].replace("\n", "")
        created = datetime.strptime(created, '%Y-%m-%d %H:%M')
        created_full = created.strftime('%Y%m%d%H%M' + '00000')
        modified_full = created.strftime('%Y%m%d%H%M' + '00001')
        text_full = "".join(lines[8:])

        dictionary = {}

        dictionary['title'] = title
        dictionary['tags'] = lines[6][12:].replace("[", "").replace("]", "").replace("\n", "").replace(",", "")
        dictionary['created'] = created_full
        dictionary['modified'] = modified_full
        dictionary['text'] = text_full
        
        print(dictionary['title'])
        

        with open(f"{dictionary['title']}.json", 'w') as json_file:
                json.dump(dictionary, json_file)

#     except:
#         print(lines[1:4])
#         print("***************\nfailed") 
#         pass
