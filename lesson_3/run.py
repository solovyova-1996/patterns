from wsgiref.simple_server import make_server

from daria_framework.main import Framework
from urls import routes, context

application = Framework(routes, context)

with make_server('', 8080, application) as httpd:
    print("Запуск серверв на порту 8080...")
    httpd.serve_forever()
