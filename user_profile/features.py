from django.contrib.auth.models import User
from .models import UserData
import datetime

def check_achievements(request):
    user = request.user
    user_info = UserData.objects.get(pk = user)
    achievements = set()
    streak, n_tasks = user_info.longest_streak, user_info.tasks_completed

    if n_tasks >= 1:
        achievements.add('Completed first task')
        if n_tasks >= 5:
            achievements.add('Completed five tasks')
            if n_tasks >= 10:
                achievements.add('Completed ten tasks')
                if n_tasks >= 50:
                    achievements.add('Completed fifty tasks')
    
    if streak >= 3:
        achievements.add('Completed three tasks in a row')
        if streak >= 5:
            achievements.add('Completed five tasks in a row')
            if streak >= 10:
                achievements.add('Completed ten tasks in a row')
                if n_tasks >= 30:
                    achievements.add('Completed thirty tasks in a row')
    
    return achievements


def is_on_time(last_date):
    today = str(datetime.datetime.now()).split(' ')[0]
    y1, m1, d1 = list(map(int, today.split("-")))
    today = datetime.date(y1, m1, d1)

    if today <= last_date:
        return True
    else:
        return False