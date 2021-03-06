import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'game_gauger.settings')

import django
django.setup()
from reviews.models import Game, Review
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

def populate():
    # list of dictionaries containing reviews to add to each game


    batman_arkham = add_game(game='Batman: Arkham Asylum',genre='Action',
                             publisher='Warner Bros. Interactive Entertainment',
                             developer='Rocksteady Studios',
                             logo='media/Batman_Arkham_Asylum_Videogame_Cover.jpg')

    nier_automata = add_game(game='Nier Automata',genre='Action',
                             publisher='Square Enix',
                             developer='PlatinumGames',
                             logo='media/Nier_Automata_Cover_JP.jpg')

    super_mario_odyssey = add_game(game='Super Mario Odyssey',genre='Platform',
                             publisher='Nintendo',
                             developer='Nintendo EPD',
                             logo='media/super-mario-boxart.jpg')

    arkham_review = add_review(game='Batman: Arkham Asylum', user_name = 'bob', comment='empty',
                               rating=4)

    # Print out the games we have added
    for g in Game.objects.all():
        for r in Review.objects.filter(game=g):
            print("- {0} - {1}".format(str(g), str(r)))


def add_review(game, user_name, comment, rating=0):
    r = Review.objects.get_or_create(game=game)[0]
    r.user_name = user_name
    r.comment = comment
    r.rating = rating
    r.save()
    return r

def add_game(game, genre, publisher, developer, logo):
    g = Game.objects.get_or_create(game=game, genre=genre, publisher=publisher,
                                   developer=developer, logo=logo)[0]
    g.save()
    return g


if __name__ == '__main__':

    print("Starting Review population script...")
    populate()



