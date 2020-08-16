from apps.startPage.utils import page_view, page_context_view
from .models import User

class register(page_view):
    template = 'user/register_page.html'

class login(page_view):
    template = 'user/login_page.html'

class profile(page_context_view):
    template = 'user/profile_page.html'
    model = User
