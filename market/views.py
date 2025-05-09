from django.shortcuts import render, get_object_or_404
from .models import Bb, Rubric
from .forms import BbForm
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import GoITeen, Rubric
from django.shortcuts import render, redirect
from .forms import GoITeenForm
from django.shortcuts import render, redirect
from .forms import DjangoFormSet
from .models import ModelFormsetModel
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from .forms import LoginForm, RegisterForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cart, Bb
from django.contrib.auth import authenticate, login as auth_login

def temp_redirect(request):
    return HttpResponseRedirect(reverse('new_page'))

def perm_redirect(request):
    return HttpResponsePermanentRedirect('http://www.example.com/')

def new_page(request):
    return render(request, 'new_page.html')

@require_http_methods(['GET', 'POST'])
def index(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    rubric_id = request.GET.get('rubric')

    bbs = Bb.objects.all()

    if min_price:
        bbs = bbs.filter(price__gte=min_price)
    if max_price:
        bbs = bbs.filter(price__lte=max_price)
    if rubric_id:
        bbs = bbs.filter(rubric_id=rubric_id)

    rubrics = Rubric.objects.all()
    cart_items = Cart.objects.filter(user=request.user) if request.user.is_authenticated else None

    return render(request, 'index.html', {'bbs': bbs, 'rubrics': rubrics, 'cart_items': cart_items})
def by_rubric(request, rubric_id):
    rubric = get_object_or_404(Rubric, pk=rubric_id)
    bbs = Bb.objects.filter(rubric=rubric)
    return render(request, 'by_rubric.html', {'bbs': bbs, 'rubric': rubric})

def add_and_save(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric',
            kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
    else:
        bbf = BbForm()
    return render(request, 'create.html', {'form': bbf})

class BbListView(ListView):
    model = Bb
    template_name = 'bb_list.html'
    context_object_name = 'bbs'

class BbCreateView(CreateView):
    model = Bb
    template_name = 'bb_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('bb_list')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

class HomePageView(TemplateView):
    template_name = 'index2.html'

class AboutPageView(TemplateView):
    template_name = 'about2.html'


class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }
        return render(request, 'data.html', context)




def pagin(request):
    rubrics = Rubric.objects.all()
    goiteens = GoITeen.objects.all()  # Changed variable name to lowercase (Python convention)

    paginator = Paginator(goiteens, 2)
    page_num = request.GET.get('page', 1)

    try:
        page_num = int(page_num)
    except ValueError:
        page_num = 1

    page = paginator.get_page(page_num)

    context = {'rubrics': rubrics, 'page': page, 'goiteens': page.object_list}
    return render(request, 'GoITeenoard/rate.html', context)






def goiteen_form_view(request):
    if request.method == 'POST':
        form = GoITeenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goiteen_form')
    else:
        form = GoITeenForm()
    return render(request, 'goiteen_form.html', {'form': form})




def master(request):
    if request.method == 'POST':
        formset = DjangoFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('master')
    else:
        formset = DjangoFormSet(queryset=ModelFormsetModel.objects.all())

    context = {'formset': formset}
    return render(request, "master.html", context)



@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Определяем значение next из GET или POST
                next_url = request.GET.get('next') or request.POST.get('next')
                # Если next задан, но он указывает на страницу логина, игнорируем его.
                if next_url and 'login' not in next_url.lower():
                    return redirect(next_url)
                else:
                    return redirect('index')
            else:
                form.add_error(None, 'Неправильное имя пользователя или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем нового пользователя в базе данных
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']  # Убедитесь, что поле пароля возвращает чистое значение
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Перенаправление на главную страницу
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})



@require_http_methods(['POST'])
def logout(request):
    auth_logout(request)  # Выполняем logout
    response = redirect('login')  # Перенаправляем на страницу логина
    response.delete_cookie('last_connection')
    response.delete_cookie('username')
    return response




@login_required
def user_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    product = Bb.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('index')  # Вы можете перенаправить на любую страницу

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('user_cart')


