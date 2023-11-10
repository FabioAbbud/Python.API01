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
    }, {
        "id": 4,
        "name": "Coisa",
        "description": "Uma coisa",
        "location": "Logo ali"
    }, {
        "id": 5,
        "name": "Treco",
        "description": "Um treco",
        "location": "Onde judas perdeu as botas"
    }, {
        "id": 6,
        "name": "Troço",
        "description": "Um troço",
        "location": "Belford Roxo"
    }
]

def get_all(): 
    return json.dumps(items, indent=2)
    
    
def get_one(id):
    try:
        id = int(id)
        for item in items:
            if item.get("id") == id:
                return json.dumps(items [id], indent=2)
    except:
        print("Isso não é um ID válido")
        return False
    
def get_data():
    input_id = input("Digite o ID do item: ")
    view = get_one(input_id)
    if view:
        print(view)
    else:
        print("Algo errado não deu certo!")
        
def new(json_data):
   # print('new → ',json_data)
    next_id = max(item["id"] for item in items) + 1
    print('max → ', next_id)
    return
    

my_json = '''
{
    "id": 6,
    "name": "Troço",
    "description": "Um troço",
    "location": "Belford Roxo"
}
'''
new(my_json)