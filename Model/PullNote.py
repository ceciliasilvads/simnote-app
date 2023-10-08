import json

def pullNote(note):
    filename = './Notes.json'
    listObj = []
    item = {}
    
    item['title'] = note.title
    item['content'] = note.content

    with open(filename, 'r') as fp:
        listObj = json.load(fp)

    listObj.append(item)
    
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, indent=4, separators=(',',': '))
    
    return True