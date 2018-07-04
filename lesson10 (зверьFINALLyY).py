import random


def choice():
    print('\n0 - cat \n1 - dog \n2 - snake \n3 - human (be careful its illegal)\n')
    lol = input('Chose what creature u would like to have as a pet\n')
    return lol


class Creature(object):
    def __init__(self, name, hunger=100, boredom=100):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_hunger(self):
        self.hunger -= random.randint(1, 11)

    def __pass_boredom(self):
        self.boredom -= random.randint(1, 11)

    def mood(self):
        happy = self.hunger + self.boredom
        res = ''
        if happy > 200:
            res = 'i am SO happy thank you'
        elif 150 < happy <= 200:
            res = 'i am happy ^^'
        elif 100 < happy <= 150:
            res = 'i am ok'
        elif 50 < happy <= 100:
            res = 'i dont feel so good...'
        elif 0 < happy <= 50:
            res = 'i am about to die :" '
        elif happy < 0:
            res = 'I am dead x.x \n are YOU happy now??'
        return res

    def talk(self):
        print('I am', self.name, 'and', self.mood())
        self.__pass_boredom()
        self.__pass_hunger()

    def eat0(self):
        print('0 - i wont feed it \n1 - apple \n2 - meat \n3 - basic cat food \n4 - royal cat food\n')
        food = input('what food will u give to ur pet?\n')
        if food == '0':
            print(' :( ')
            food = 0
            self.hunger += food
        elif food == '1':
            print('I am CAT I do not eat apples, why did u keep me if u do not know basic things about cats')
            food = 0
            self.hunger += food
        elif food == '2':
            print('Oh thank you I like it')
            food = 10
            self.hunger += food
        elif food == '3':
            print('Thanks!!')
            food = 12
            self.hunger += food
        elif food == '4':
            print('Wow what is it its soooooooo delicious')
            food = 20
            self.hunger += food

    def eat1(self):
        print('0 - i wont feed it \n1 - apple \n2 - meat \n3 - basic dog food \n4 - royal dog food\n')
        food = input('what food will u give to ur pet?\n')
        if food == '0':
            print(' :( ')
            food = 0
            self.hunger += food
        elif food == '1':
            print('Thank you, owner, but how should I actually eat it??')
            food = 0
            self.hunger += food
        elif food == '2':
            print('Oh thank you!!! I like it!!')
            food = 10
            self.hunger += food
        elif food == '3':
            print('Thanks!!')
            food = 12
            self.hunger += food
        elif food == '4':
            print('Wow what is it its soooooooo delicious')
            food = 20
            self.hunger += food

    def eat2(self):
        print('0 - i wont feed it \n1 - apple \n2 - meat \n3 - basic snake food (idk what is it) \n4 - rat\n')
        food = input('what food will u give to ur pet?\n')
        if food == '0':
            print(' :( ')
            food = 0
            self.hunger += food
        elif food == '1':
            print('I am a SNAKE I do not eat apples, should I eat YOU instead???')
            food = 0
            self.hunger += food
        elif food == '2':
            print('Its ok now I wont eat you')
            food = 10
            self.hunger += food
        elif food == '3':
            print('Mmmmmm much better now')
            food = 12
            self.hunger += food
        elif food == '4':
            print('Finally my favourite delicious thing')
            food = 20
            self.hunger += food

    def eat3(self):
        print('ramen Ramen please RAMEN...')
        print('0 - i wont feed it \n1 - apple \n2 - pizza \n3 - vodka(wtf why) \n4 - ramen\n')
        food = input('what food will u give to ur (lol) pet?\n')
        if food == '0':
            print(' :( ')
            food = 0
            self.hunger += food
        elif food == '1':
            print('Oh thanks it gives energy but I am still hungry')
            food = 5
            self.hunger += food
        elif food == '2':
            print('Oh thank you I like it')
            food = 10
            self.hunger += food
        elif food == '3':
            print('Wtf I am feeling sO wEiRd ')
            food = 0
            ehehe = 30
            self.hunger += food
            self.boredom += ehehe
        elif food == '4':
            print('AH YEA MY FAVOURITE RAMEN THANK YOU')
            food = 20
            self.hunger += food

    def play(self, fun=random.randint(10, 21)):
        print('Reeeeeeeeeeeeee')
        self.boredom += fun
        self.__pass_hunger()

    def creat_helth(self):
        if self.hunger < 0 or self.boredom < 0:
            exit()


def main():
    forfood = choice()
    name = input('What name of your creature? \n')
    creat = Creature(name)
    while True:
        print("""
        0 - exit game;
        1 - talk to {};
        2 - feed {}
        3 - play with {}
        """.format(name, name, name))
        choic = input("What do u like to do with ur pet:\n ")
        if choic == '0':
            break
        elif choic == '1':
            creat.talk()
            creat.creat_helth()
        elif choic == '2':
            if forfood == '0':
                creat.eat0()
            elif forfood == '1':
                creat.eat1()
            elif forfood == '2':
                creat.eat2()
            elif forfood == '3':
                creat.eat3()
            else:
                print('Error')
            creat.creat_helth()
        elif choic == '3':
            creat.play()
            creat.creat_helth()
        else:
            print('This action is out of the list, what did u want to do??')


if __name__ == '__main__':
    print('Welcome to game "Creature"')
    main()
