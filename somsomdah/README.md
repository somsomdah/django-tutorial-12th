# Django Tutorial - TIL

---
## Part 1

#### commands
- `django-admin startproject [project name] `
- `python manage.py runserver`
- `python manage.py startapp [app name]`

#### functions
```python
#polls/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'), # polls/views.py의 index 함수
]
```
```python
# mysyte/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), #polls/urls.py
    path('admin/', admin.site.urls),
]
```
- `include()` : url 연결, admin.site.urls 제외하고는 전부 include 사용
- `path(route,view,kwargs,name)`

---
## Part 2

#### commands
- `python manage.py makemigrations [app name]` # 변경사항에 대한 migration 만들기
- `python manage.py sqlmigrate [app name] [index]`
- `python manage.py migrate` # 변경사항 db에 적용
- `python manage.py shell`
- `python manage.py createsuperuser`

#### shell commands
```python
Question.objects.all() # 만들어진 객체 확인
q = Question(question_text="What's new?", pub_date=timezone.now()) # 객체 생성
q.save() # db에 객체 저장
q.question_text = "What's up?" # 객체 내용 바꾸기
q.save()
```
```python
Question.objects.filter(id=1)
Question.objects.get(pub_date__year=current_year) # 생성된 객체 가져오기
q=Question.objects.get(pk=1) # 생성된 객체 가져오기
q.choice_set.all() # 객체에 딸린 choice_set 확인
c=q.choice_set.create(choice_text='Not much', votes=0) # choice_set 생성
c.question # 해당 choice_set에 해당하는 질문
q.choice_set.count()
q.choice_set.all())
c.delete() # choice 제거

```
## Part 3

- mysite/urls.py -> polls/urls.py
- polls/urls.py : `urlpatterns =[path("[url주소]",views.[뷰이름],name=[url이름])]`
- `"<[데이터타입]:[뷰의 매개변수 이름]>"` 으로 뷰에서 값을 넘겨받아 사용할 수 있다. 
```python
# 예시
def vote(request,question_id):
    return HttpResponse("You are voting on question %s"%question_id)

urlpatterns = [
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
- `render(request, 'polls/index.html', context)`  polls/index.html에 context 전달
- `get_object_or_404` 모델로부터 객체를 가져오거나 404를 띄움

## Part 4
- request.post
```python
selected_choice = question.choice_set.get(pk=request.POST['choice']) 
#name=choice인 요소에서 선택된 것 -> pk로 쓰겠다
```
- generic view
```python
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
# path('<int:pk>/', views.DetailView.as_view(), name='detail'),
```
