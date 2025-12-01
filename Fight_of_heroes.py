import random


class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def __str__(self):
        return f'Name:{self.name}  HP{self.hp}  Attack{self.attack}'


class Team:
    def __init__(self):
        self.heroes = {
            'Gon': Hero('Gon', 1000, 100)
        }

    def __add__(self, other):
        self.heroes[other.name] = other
        return self

    def __str__(self):
        return '\n'.join(str(hero) for hero in self.heroes.values()) # '\n'.join(...) — соединяет в одну строку с переносами строк


    def game_over(self):
        # sample_heroes = random.sample(list(self.heroes.items()), 2)
        sample_heroes = random.sample(list(self.heroes.values()),2)
        random_hero = sample_heroes[0]  # ✅ достаём объект
        random_hero_1 = sample_heroes[1]
        # sample_heroes_02 = random.sample(list(self.heroes.values()), 1)
        print(random_hero, random_hero_1)

        while True:
            # урон героя 1 по герою 2 — случайный от 80% до 120% базовой атаки
            damage_1h = random.randint(int(random_hero_1.attack * 0.8),
                                      int(random_hero_1.attack * 1.2))
            # урон героя 2 по герою 1
            damage_2h = random.randint(int(random_hero.attack * 0.8),
                                      int(random_hero.attack * 1.2))
            # random_hero.hp -= random_hero_1.attack * random.uniform(0.8, 1.2)
            # random_hero_1.hp -= random_hero.attack * random.uniform(0.8, 1.2)
            random_hero.hp -= damage_1h
            random_hero_1.hp -= damage_2h
            print(f'{random_hero.name}:  {random_hero.hp} HP ,{random_hero_1.name}:  {random_hero_1.hp} HP')
            if random_hero.hp <= 0:
                print(random_hero.name + ' the END')
                break
            elif random_hero_1.hp <= 0:
                print(random_hero_1.name + ' the END')
                break


Team = Team()

Ged = Hero('Ged', 1000, 100)
Wiwi = Hero('Wiwi', 1000, 100)

Team + Ged + Wiwi

Team.game_over()