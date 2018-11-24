import yaml
def read_yaml():
    with open("../data/data1.yaml", 'r',encoding='utf-8') as f:
        data = yaml.load(f)
        print(type(data))  # 打印data类型
        print(data)  # 打印data返回值
if __name__ == '__main__':
    print(read_yaml())
