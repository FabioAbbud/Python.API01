import json

items = [
    {
        "id": 1,
        "name": "Bagulho",
        "description": "Apenas um bagulho",
        "location": "Em uma caixa"
    }, {
        "id": 2,
        "name": "Tranqueira",
        "description": "Em um gaveteiro"
    }, {
        "id": 3,
        "name": "Bagulete",
        "description": "Um bagulete qualquer",
        "location": "Na esquina"
    }
]

def get_all(): 
    return json.dumps(items, indent=2)
    
    
def get_one(id):
    for item in items:
        if item.get("id") == id:
            return json.dumps(items [id], indent=2)
    
    

# print (get_all())
print (get_one(1))
