# [Django Custom User](https://learndjango.com/tutorials/django-custom-user-model)

While Django does come with a built in [user model](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User), the django-docs highly recommends using a custom user model instead. In other words, always use a custom user model for django-projects. 

When setting up a new project and app when making a custom user model, it's _important not_ to run _migrate_ to configure the database. Wait until after creating the new customer user model

Once you're connected to the localhost URL and get proof of life there, end the server connection as you set up the user model so it doesn't spit out a bunch of errors.

There are two modern ways to create a custom user model in django:
- AbstractUser
- AbstractBaseUser

Both cases can subclass to extend existing functionality. However, AbstractBaseUser requires much more work. Recommended to use AbstractUser instead.

## Create User Model

Creating the initial custom user model requires four steps:
- update settings.py
  - add the accounts app to INSTALLED_APPS
  - At the bottom of settings, add AUTH_USER_MODEL = 'accounts.CustomUser'
- create a new CustomUser model
  - in models.py ->
  - `from django.contrib.auth.models import AbstractUser`
  - create a class that looks like this:
```
class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
```
- create new UserCreation and UserChangeForm
  - inside your app, create a `forms.py` file 
    - `from django import forms`
    - `from django.contrib.auth.forms import UserCreationForm, UserChangeForm`
    - `from .models import CustomUser`
    - create form classes for creation and change forms:
```
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
```
- update admin
  - register the above in `admin.py`
```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
```
- Next, run `makemigrations` and `migrate`
- then run `python manage.py createsuperuser`
- Then create templates with a goal to sign in, sign out, and sign up. 
  - In `settings.py`:
  - `TEMPLATES` -> `BASE_DIR / 'templates'`
  - Set redirect links for sign in/out, which will go to `home` template. Add these to settings:
```
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```
- Next, create a templates directory with a namme like **registration** and create these files up in there: `login.html`, `signup.html`, `base.html`, `home.html`

For the rest, refer to your `accounts` directory in your codefellows/python folder where you followed along with the tutorial or just click the link in the header at the top of this page to go through the source tutorial agagin. It isn't that long and it worked when you tried it.

### Additional Resources

- [DjangoX](https://github.com/wsvincent/djangox)
- [Substituting a custom User model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#auth-custom-user)

**Videos**:
- [Creating Custom User Models](https://www.youtube.com/watch?v=eCeRC7E8Z7Y&t=59s)
- [Abstract User, User Profile and Signals in Django (how to add extra fields to the user model)](https://www.youtube.com/watch?v=EudKs1HPUfE)


 (../index.md)