from experta import *


# les faits
class Restaurant(KnowledgeEngine):
    name = ""
    photo = ""
    g = ""
    b = 0

    # les regles
    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 10 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              Fact(vegan='2'),
              Fact(sucre_sale='2'),
              Fact(cuisine='2'),
              Fact(plat='3')))
    def restaurantBurger(self):
        self.name = "Doodle Burger Bar"
        self.photo = r'.\RestaurantSE\Images\DoodleBurgerBar.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 15 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              OR(Fact(vegan='1'), Fact(vegan='2')),
              Fact(sucre_sale='2'),
              OR(Fact(cuisine='2'), Fact(cuisine='3')),
              Fact(plat='3')))
    def restaurantZinc(self):
        self.name = "Le Zink"
        self.photo = r'.\RestaurantSE\Images\leZink.png'

    # mtaa glace wla haja sucree
    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 6 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              OR(Fact(vegan='1'), Fact(vegan='2')),
              Fact(sucre_sale='1'),
              Fact(cuisine='5'),
              Fact(plat='7')))
    def restaurantGlace(self):
        self.name = "Parad'Ice Plaza"
        self.photo = r'.\RestaurantSE\Images\paradicePlaza.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 15 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              OR(Fact(vegan='1'), Fact(vegan='2')),
              Fact(sucre_sale='2'),
              Fact(cuisine='4'),
              Fact(plat='5')))
    def restaurantSuchi(self):
        self.name = "Sushiwan"
        self.photo = r'.\RestaurantSE\Images\sushiwan.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 10 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              Fact(vegan='2'),
              Fact(sucre_sale='2'),
              Fact(cuisine='4'),
              Fact(plat='5')))
    def restaurantKorean(self):
        self.name = "K-zip"
        self.photo = r'.\RestaurantSE\Images\kZip.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Bizerte'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 15 <= budget),
              OR(Fact(espace='1'), Fact(espace='2')),
              Fact(parking='2'),
              Fact(vegan='2'),
              Fact(sucre_sale='2'),
              Fact(cuisine='1'),
              Fact(plat='4')))
    def restaurantKsiba(self):
        self.name = "El Ksiba"
        self.photo = r'.\RestaurantSE\Images\ksiba.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Bizerte'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 15 <= budget),
              OR(Fact(espace='1'), Fact(espace='2')),
              OR(Fact(parking='1'), Fact(parking='2')),  # possede un parking
              OR(Fact(vegan='1'), Fact(vegan='2')),
              OR(Fact(sucre_sale='1'), Fact(sucre_sale='2')),
              Fact(cuisine='1'),
              Fact(plat='4')))
    def restaurantSportNautique(self):
        self.name = "Le Sport Nautique"
        self.photo = r'.\RestaurantSE\Images\SportNautique.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Nabeul'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 8 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              OR(Fact(vegan='1'), Fact(vegan='2')),
              Fact(sucre_sale='2'),
              Fact(cuisine='5'),
              OR(Fact(plat='1'), Fact(plat='2'), Fact(plat='4'))))
    def restaurantRoxford(self):
        self.name = "Roxford Restaurant"
        self.photo = r'.\RestaurantSE\Images\roxford.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Ariana'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 5 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              Fact(vegan='2'),
              Fact(sucre_sale='2'),
              OR(Fact(cuisine='1'), Fact(cuisine='2'), Fact(cuisine='3')),
              Fact(plat='8')))
    def restaurantCrepeFactory(self):
        self.name = "Crepe Fatory"
        self.photo = r'.\RestaurantSE\Images\crepeFactory.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Sousse'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 5 <= budget),
              OR(Fact(espace='1'), Fact(espace='2')),
              Fact(parking='2'),
              Fact(vegan='2'),
              Fact(sucre_sale='1'),
              Fact(cuisine='5'),
              Fact(plat='7')))
    def restaurantCasaDelGelato(self):
        self.name = "Casa Del Gelato"
        self.photo = r'.\RestaurantSE\Images\casaDelGelato.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Sousse'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 3500 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              Fact(vegan='1'),
              Fact(sucre_sale='1'),
              Fact(cuisine='5'),
              Fact(plat='7')))
    def restaurantParadiceSousse(self):
        self.name = "Parad'Ice"
        self.photo = r'.\RestaurantSE\Images\paradiceSousse.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Sousse'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 65 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              Fact(vegan='2'),
              Fact(sucre_sale='2'),
              Fact(cuisine='3'),
              Fact(plat='6')))
    def restaurantFarmersSteakhouse(self):
        self.name = "Farmers Steakhouse"
        self.photo = r'.\RestaurantSE\Images\steakhouse.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Ariana'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 24 <= budget),
              OR(Fact(espace='1'), Fact(espace='2')),
              OR(Fact(parking='1'), Fact(parking='2')),  # possede un parking
              Fact(vegan='2'),
              Fact(sucre_sale='2'),
              Fact(cuisine='2'),
              OR(Fact(plat='6'), Fact(plat='3'))))
    def restaurantLeReservoir(self):
        self.name = "Le Reservoir"
        self.photo = r'.\RestaurantSE\Images\leReservoir.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 20 <= budget),
              OR(Fact(espace='1'), Fact(espace='2')),
              Fact(parking='2'),
              OR(Fact(vegan='2'), Fact(vegan='1')),
              Fact(sucre_sale='2'),
              OR(Fact(cuisine='5'), Fact(cuisine='3')),
              Fact(plat='1')))
    def restaurantFarfalle(self):
        self.name = "Le Farfalle - Les Berges du Lac"
        self.photo = r'.\RestaurantSE\Images\leFarfalle.png'

    @Rule(AND(Fact(action='restaurant'),
              Fact(gouvernorat='Tunis'),
              Fact(budget=MATCH.budget),
              TEST(lambda budget: 7 <= budget),
              Fact(espace='1'),
              Fact(parking='2'),
              OR(Fact(vegan='2'), Fact(vegan='1')),
              Fact(sucre_sale='2'),
              Fact(cuisine='5'),
              Fact(plat='2')))
    def restaurantMargherita(self):
        self.name = "La Margherita"
        self.photo = r'.\RestaurantSE\Images\laMargherita.png'


engine = Restaurant()
engine.reset()
engine.run()
