import yaml

with open("../demo/data/data.yaml", 'r',encoding='utf-8') as f:
    data = yaml.load(f)
    print(type(data))
    print(data)

    """
    需求:
    
    """