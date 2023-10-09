import json



    
def add_items(index=[None], **kwargs):
    
    if (index != [None]):
        with open("type.json", "r") as item:
            data = json.load(item)
        
        for item in index:
            for key,value in data.items():
                if (item == key):
                    
        
