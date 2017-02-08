from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Question, Choice


def index(request):
    # pub_date컬럼(필드)를 기준으로 내림차순 정렬한 결과를 latest_question_list에 할당
    latest_question_list = Question.objects.order_by('-pub_date')

    context = {
        'latest_question_list': latest_question_list,
    }
    ## shortcut을 이용해 짧게 처리
    # 'polls/index.html' 템플릿을 이용해서
    # request, context객체를 이용해 HttpResponse를 반환
    return render(request, 'polls/index.html', context)

    ## loader.get_template, template.render를 사용 (과정 2번 거침)
    # # 템플릿 로더를 이용해서 'polls/index.html'에서 템플릿파일을 가져온다
    # template = loader.get_template('polls/index.html')
    #
    # # 템플릿 파일에 전달할 context객체를 정의
    # context = {
    #     # 'latest_question_list'라는 키에 값을 할당, 해당 키로 템플릿에서 사용가능하다
    #     'latest_question_list': latest_question_list,
    # }
    # # 템플릿에 context와 request객체를 사용해서 render해준 결과를 돌려줌
    # return HttpResponse(template.render(context, request))


    # 돌려줄 문자열을 작성
    output = ', '.join([q.question_text for q in latest_question_list])

    # output2 = ''
    ## for문과 enumerate, index를 활용
    # for index, q in enumerate(latest_question_list):
    #     output2 += q.question_text
    #     if index != latest_question_list.count() - 1:
    #         output2 += ', '

    # 전부 붙인 후 마지막만 slice
    # for q in latest_question_list:
    #     output2 += q.question_text + ', '
    # output2 = output2[:-2]
    # return HttpResponse(output2)


def detail(request, question_id):
    """
    request.method == 'POST'일 때
    전달받은 데이터를 출력

    POST형식이 아닐경우에는 polls/detail.html을 render

    POST요청이 왔을 때,
    전달받은 POST객체에서
    'choice'키의 값을 HttpResponse로 되돌려준다

    'choice'키로 전달된 Choice객체의 id를 이용해서
    해당 Choice객체의 votes값을 1늘려주고 데이터베이스에 업데이트
    완료되면 다시 Question detail페이지로 이동

    1. request.POST['choice']의 값(Choice객체의 ID)을 이용해서 Choice객체를 가져온다
    2. 해당 객체의 votes값을 늘려주고, 데이터베이스에 변경사항을 업데이트
    3. redirect, question_id를 이용해서 detail페이지로 다시 돌아간다.
    """
    if request.method == 'POST':
        # 1번
        choice_id = request.POST['choice']
        choice = Choice.objects.get(id=choice_id)

        # 2번
        choice.votes += 1
        choice.save()

        # 3번
        return redirect('polls:results', question_id=question_id)
    else:
        question = Question.objects.get(id=question_id)
        context = {
            'question': question,
        }
        return render(request, 'polls/detail.html', context)


def results(request, question_id):
    # 인자로 주어진 question_id에 해당하는 Question객체를 context에 담아 render에 보낸다
    question = Question.objects.get(id=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
