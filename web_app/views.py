from django.shortcuts import render
from django.shortcuts import HttpResponse
from web_app import models
from django.forms.models import model_to_dict

# Create your views here.
def getRank(score, pool):
    if score != None:
        score = int(score)
    else:
        return "  ", "  "
    intervals = [0, 301, 351, 361, 371, 381, 391, 401, 411, 421, 431, 441, 451, 601, 1201]
    position = -1
    for i in range(len(intervals) - 1):
        if score in range(intervals[i], intervals[i + 1]):
            position = i
            break
    # If position is -1 then the score input is invalid
    # return immediately
    if position == -1:
        return "invalid", "invalid"

    # If the input score is valid, then calculate the bottom and top rank possible
    rank_bot = sum(pool[position:])
    if position == 13:
        rank_top = 1
    else:
        rank_top = sum(pool[position + 1:])
    return str(rank_bot), str(rank_top)

def dissemble(draw_list, draw_range):
    if draw_range <= 0:
        wanted = draw_list
    else:
        wanted = draw_list[:draw_range]
    scores = [x['score'] for x in wanted]
    ID = ["#"+str(x['drawid']) for x in wanted]
    dates = [x['date'] for x in wanted]
    pop = [x['population'] for x in wanted]
    return scores[::-1], ID[::-1], dates[::-1], pop[::-1]

def index(request):
    draw_list = list(models.Draws.objects.values())
    recent = draw_list[-1]
    return render(request, 'Index.html', {'info': recent})

def table(request):
    draw_list = list(models.Draws.objects.values())
    all_draws = draw_list[::-1]
    return render(request, 'table.html', {'info': all_draws})

def draw(request):
    draw_list = list(models.Draws.objects.values())
    draw_list = draw_list[::-1]
    draw_range = request.POST.get('draw_range', None)
    if draw_range != None:
        draw_range = int(draw_range)
        if draw_range != 0:
            score, ID, dates, pop = dissemble(draw_list, draw_range)
            if draw_range <0:
                title = ["All draws"]
            else:
                title = ["Past "+str(draw_range)+" draws"]
            print(title)
            return render(request, 'draw.html', {'score': score, 'id': ID, 'dates': dates,
                                                 'pop': pop, 'wid': "800",
                                                 'hei': "480", 'chartTitle': title})
    score, ID, dates, pop = dissemble(draw_list, 0)
    print(score)
    print(ID)
    return render(request, 'draw.html', {'score': score, 'id': ID, 'dates': dates,
                                         'pop': pop, 'wid': "0",
                                         'hei': '0', 'label': str(draw_range)})

    # print(draw_range, type(draw_range))
    # return render(request, 'draw.html', {'info': draw_list[::-1]})

def pool(request):
    info = list(models.Pool.objects.values())
    pool_data = list(info[0].values())[1:]
    user_score = request.POST.get('score', None)
    rank_bot, rank_top = getRank(user_score, pool_data)
    if rank_top == "  ":
        before = " "
        connect = " "
        after = " "
    elif rank_top == "invalid":
        before = " "
        connect = "Invalid score input"
        after = " "
        rank_top = ""
        rank_bot = ""
    else:
        before = "You rank between"
        connect = "and"
        after = "in the Candidate Pool"
    return render(request, 'Pool.html', {'before': before, 'connect': connect,
                                         'after': after, 'r_low': rank_bot,
                                         'r_high': rank_top, 'pool_data': pool_data[::-1]})