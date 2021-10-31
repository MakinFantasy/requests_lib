import requests


def smartest_hero(list_of_heroes):
    result = {"name": "", "intelligence": 0}
    url = 'https://superheroapi.com/api/2619421814940190/'
    for hero in list_of_heroes:
        res = requests.get(url + 'search/' + hero)
        if res:
            id_of_hero = res.json()['results'][0]['id']
            res = requests.get(url + id_of_hero + '/powerstats')
            if res:
                if result["intelligence"] <= int(res.json()["intelligence"]):
                    result["name"] = hero
                    result["intelligence"] = int(res.json()["intelligence"])
            else:
                print("Can't scan for intelligence stat")
        else:
            print("Can't scan for heroes's names")
    return result


if __name__ == '__main__':
    list_of_heroes = ["Thanos", "Hulk", "Captain America"]
    print(smartest_hero(list_of_heroes))


