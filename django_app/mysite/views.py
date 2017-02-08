"""
루트 URL (r'^$')에
polls/와 admin/으로 갈 수 있는 링크 페이지를 구현한다

1. 뷰는 mysite/views.py안에
    def index(request)에 작성

2. 템플릿은 templates/index.html을 사용
    polls/, admin/ 연결하는 부분은 {% url %}태그 쓰지 않고 직접 구현

3. URL은 mysite/urls.py에
"""
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
