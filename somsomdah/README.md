# Django Tutorial - TIL

---
## Part 1

#### commands
- django-admin startproject [project name] 
- python manage.py runserver
- python manage.py startapp [app name]

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
- include() : url 연결, admin.site.urls 제외하고는 전부 include 사용
- path(route,view,kwargs,name)

---
## Part 2

#### commands
- python manage.py makemigrations [app name]
- python manage.py sqlmigrate [app name] [index]
- python manage.py migrate
- python manage.py shell

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