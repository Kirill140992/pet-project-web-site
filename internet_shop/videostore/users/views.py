from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistraion, ProfileImage, UserUpdateForm
from django.views import View
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('user')
    else:
        form = UserOurRegistraion()
    return render(request, 'users/registraion.html', {'form': form, 'title':'Регистрация пользователя'})

@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)

class LogoutWithPostView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'users/exit.html')

    def get(self, request, *args, **kwargs):
        # Если кто-то попытается сделать GET-запрос, перенаправьте их на страницу выхода
        return render(request, 'users/exit.html')