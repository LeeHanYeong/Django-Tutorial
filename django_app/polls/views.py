from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question


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
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
