from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder="templates", **kwargs):
    """
    Функция рендеринга html-страницы
    :param template_name: имя html-страницы
    :param folder: папка где расположены html-страницы
    :param kwargs: аргументы, например: date
    :return: отрендеренная html-страница
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
