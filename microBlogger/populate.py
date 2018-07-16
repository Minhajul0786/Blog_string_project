import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','microBlogger.settings')
import django
django.setup()
import random
from django.contrib.auth.models import User
from blogger.models import Blog,Comment
from faker import Faker

fakegen = Faker()

def add_user(N=5):

    for item in range(N):
        name = fakegen.name()
        fake_username = name
        fake_email = fakegen.email()
        s = name.split()
        fake_firstname = s[0]
        fake_lastname = s[1]
        fake_password = fake_username+"12345"
        User.objects.get_or_create(username=fake_username,first_name=fake_firstname,last_name=fake_lastname,email=fake_email,password=fake_password)

def populate(N=5):

    for item in range(N):
        user = random.choice(User.objects.all())
        fake_content = fakegen.text()
        fake_dt = fakegen.date_time_ad()
        Blog.objects.get_or_create(username=user,content=fake_content,date_time=fake_dt)

    for item in range(N):
        user = random.choice(User.objects.all())
        blog = random.choice(Blog.objects.all())
        fake_content = fakegen.sentence(nb_words=6,variable_nb_words=True,ext_word_list=None)
        fake_dt = fakegen.date_time_ad()
        Comment.objects.get_or_create(username=user,blogtext=blog,content=fake_content,date_time=fake_dt)

if __name__=='__main__':
    print("populating script!")
    add_user(1)
    populate(2)
    print("populating complete!")
