import json

def main():
    mydict = {
        'name':'zhrngM',
        'age':21,
        'qq':231234,
        'friends':['王大锤','李元芳'],
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand':'Audi','max_speed':280},
            {'brand':'Benz','max_speed':320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')

if __name__ == '__main__':
    main()
