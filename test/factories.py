import factory
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone

class SUserFactory(factory.Factory):
    FACTORY_FOR = User

    username = 'admin'
    email = 'admin@admin.com'
    password = 'admin1234'
    is_superuser = True
    is_staff = True
    is_active = True


class AUserFactory(factory.Factory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: 'usera{0}'.format(n))
    password = factory.Sequence(lambda n: 'apassword{0}'.format(n))
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username).lower())
    admin = False
    is_active = True

class NAUserFactory(factory.Factory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: 'userna{0}'.format(n))
    password = factory.Sequence(lambda n: 'napassword{0}'.format(n))
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username).lower())
    admin = False
    is_active = False

class PostFactory(factory.Factory):
    FACTORY_FOR = Post
    author = factory.LazyAttribute(lambda a: UserFactory())
    title = factory.Sequence(lambda n: 'Post{0}'.format(n))
    text = factory.LazyAttribute(lambda a: 'A some text written by {0}'.format(a.autor))
