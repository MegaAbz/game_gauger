from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from reviews.models import Game, Review, UserProfile
from reviews.forms import UserForm, UserProfileForm, GameForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    game_list = Game.objects.all()
    context_dict = {'games': game_list}
    return render(request, 'reviews/index.html', context=context_dict)

def about(request):
    return render(request, 'reviews/about.html')

def featured(request):
    return render(request, 'reviews/featured.html')

def FAQs(request):
    return render(request, 'reviews/FAQ.html')

def categories(request):
    return render(request, 'reviews/categories.html')

def categorychange(request):
    game_list = Game.objects.filter(genre="Action")
    game_list = Game.objects.exclude(genre="Adventure")
    context_dict = {'games': game_list}
    return render(request, 'reviews/categorychange.html', context=context_dict)

def cataction(request):
    game_list = Game.objects.filter(genre="Action")
    context_dict = {'games': game_list}
    return render(request, 'reviews/action.html', context=context_dict)

def catactionadventure(request):
    game_list = Game.objects.filter(genre="Action-Adventure")
    context_dict = {'games': game_list}
    return render(request, 'reviews/actionadventure.html', context=context_dict)

def catadventure(request):
    game_list = Game.objects.filter(genre="Adventure")
    context_dict = {'games': game_list}
    return render(request, 'reviews/adventure.html', context=context_dict)

def catrpg(request):
    game_list = Game.objects.filter(genre="RPG")
    context_dict = {'games': game_list}
    return render(request, 'reviews/rpg.html', context=context_dict)

def catsim(request):
    game_list = Game.objects.filter(genre="Simulation")
    context_dict = {'games': game_list}
    return render(request, 'reviews/simulation.html', context=context_dict)

def catsport(request):
    game_list = Game.objects.filter(genre="Sport")
    context_dict = {'games': game_list}
    return render(request, 'reviews/sport.html', context=context_dict)

def catpuzzle(request):
    game_list = Game.objects.filter(genre="Puzzle")
    context_dict = {'games': game_list}
    return render(request, 'reviews/puzzle.html', context=context_dict)

def catmisc(request):
    game_list = Game.objects.filter(genre="Misc")
    context_dict = {'games': game_list}
    return render(request, 'reviews/Misc.html', context=context_dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'reviews/signup.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'reviews/signin.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def addgame(request):
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        print(form.errors)
    return render(request, 'reviews/addgame.html', {'form': form})

def detail(request, game_name_slug):
    context_dict = {}
    try:
        game = Game.objects.get(slug=game_name_slug)
        reviews = Review.objects.filter(game=game)
        context_dict['reviews'] = reviews
        context_dict['game'] = game
    except Game.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'reviews/detail.html', context=context_dict)




# Views for errors
def error_404(request):
        data = {}
        return render(request,'reviews/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'reviews/error_500.html', data)
