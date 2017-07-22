from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

# @login_required()
# def homepage(request):
#      return render(request, 'pta/home.html')


def startpage(request):
     return render(request, 'pta/index.html')
     return HttpResponse("Hello, world. You're at the PTA index.")

#def startpage(request):
#     print("login_user", request)
#      messages = []
#      if request.method == 'POST':
#          print("POST method")
#          form = LoginForm(request.POST)
#         if form.is_valid():
#             print("form is valid", form)
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('user_detail', args=[user.id]))
#             else:
#                 messages.append('Invalid login')
#         else:
#             messages.append('Login data incomplete')
#     else:
#         form = LoginForm()
#     return render(request, 'clubs/login.html', {'form': form, 'messages': messages})


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]