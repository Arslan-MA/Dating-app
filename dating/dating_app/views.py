from django.shortcuts import render
from dating_app.models import Profile


def profiles_print(request):
    context = {'users': Profile.objects.all()}

    return render(request, 'profiles.html', context=context)


def user_profile(request, profile):

    return render(request, 'profile.html', context={'user': Profile.objects.get(id=profile)})


def registration(request):

    if request.method == "POST":
        profile_name = request.POST.get('name')
        profile_surname = request.POST.get('surname')
        profile_password = request.POST.get('password')
        profile_age = request.POST.get('age')
        profile_profession = request.POST.get('profession')
        profile_hobby = request.POST.get('hobby')
        profile_about_me = request.POST.get('about_me')

        Profile.objects.create(name=profile_name,
                               surname=profile_surname,
                               password=profile_password,
                               age=profile_age,
                               profession=profile_profession,
                               hobby=profile_hobby,
                               about_me=profile_about_me)

    return render(request, 'registration.html')
