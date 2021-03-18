from django.contrib.auth.models import User
from .models import UserData
import datetime, requests, json

def check_achievements(request):
    user = request.user
    user_info = UserData.objects.get(pk = user)
    achievements = set()
    streak, n_tasks = user_info.longest_streak, user_info.tasks_completed

    if n_tasks >= 1:
        achievements.add('Completed first task')
        if n_tasks >= 5:
            achievements.add('Completed 5 tasks')
            if n_tasks >= 10:
                achievements.add('Completed 10 tasks')
                if n_tasks >= 50:
                    achievements.add('Completed 50 tasks')
    
    if streak >= 3:
        achievements.add('Completed 3 tasks in a row')
        if streak >= 5:
            achievements.add('Completed 5 tasks in a row')
            if streak >= 10:
                achievements.add('Completed 10 tasks in a row')
                if n_tasks >= 30:
                    achievements.add('Completed 30 tasks in a row')
                    achievements.add('Streak Legend')
    
    return achievements


def is_on_time(last_date):
    today = str(datetime.datetime.now()).split(' ')[0]
    y1, m1, d1 = list(map(int, today.split("-")))
    today = datetime.date(y1, m1, d1)

    if today <= last_date:
        return True
    else:
        return False


def pre_calculate(user_info):
    if user_info.weight and user_info.height:
        user_info.BMI = round(user_info.weight/((user_info.height/100)**2), 2)
    else:
        user_info.BMI = None

    user_info.health_condition = None

    BMI = user_info.BMI
    if BMI:
        if BMI < 18.5:
            user_info.health_condition = 'Underweight'
        elif BMI < 25:
            user_info.health_condition = 'Normal'
        elif BMI < 30:
            user_info.health_condition = 'Overweight'
        else:
            user_info.health_condition = 'Obese'


def dietAPI(food_name):
    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query":food_name}

    headers = {
        'x-rapidapi-key': "9f0af9423cmsh58e1da4ca98d157p1ab761jsn284ecac77bbe",
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def merge_diet(prev_diet, added_diet, quantity):
    nutrients = added_diet["items"][0]

    for fact, val in nutrients.items():
        if fact == "serving_size_g" or fact == "name":
            continue
        else:
            if not prev_diet.get(fact):
                prev_diet[fact] = 0.0
            prev_diet[fact] += (int(val)*quantity/100)

    return prev_diet