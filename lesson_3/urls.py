import datetime
from views import Index, About, Contacts, Forms

routes = {"/": Index(),
          "/about/": About(),
          "/contacts/": Contacts(),
          "/forms/": Forms()
          }


def front_date_time(request: dict):
    """
    Функция наполняющая словарь request параметрами date и time
    :param request: словарь
    :return: ничего не возвращает
    """
    request['date'] = datetime.date.today()
    request['time'] = f"{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}"


def front_locations(request: dict):
    """
    Функция добавляющая в словарь request параметр location
    :param request: словарь
    :return: ничего не возвращает
    """
    request["location"] = "Omsk"


context = [front_date_time, front_locations]
