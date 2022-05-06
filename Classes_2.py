class Matter:
    number = 0
    law = 'not defined'

    @staticmethod
    def out():
        print(f'я вселенная номер «{Matter.number}», я имею закон «{Matter.law}»')

    def set_number(self, num):
        Matter.number = num

    def set_law(self, law):
        Matter.law = law

komet = Matter()
Matter.out()
komet.set_number(5)
komet.set_law('bernulli')
komet.out()
Matter.out()