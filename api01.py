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
    var_json = json.dumps(items, indent=2)
    print(var_json)
    
def get_one(id):
    var_json = json.dumps(items [id], indent=2)
    print(var_json)

# get_all()
get_one(1)
