from quopri import decodestring

from .requests_framework import PostRequest, GetRequests


class Error404:
    def __call__(self, request):
        return "404 ", "error"


class Framework:
    def __init__(self, routes: dict, context: list):
        self.routes = routes
        self.context = context

    @staticmethod
    def decode_value(data:dict):
        """
        Функция декодирующая элементы словаря в соответствии с UTF-8
        :param data: словарь типа {'first_name': '%D0%B4%D0%B0', 'last_name': '%D0%94%D0%B0%D1%80%D1%8C%D1%8F', 'reason': '%D0%B0', 'phone': '89503837871'}
        :return: словарь типа {'first_name': 'да', 'last_name': 'Дарья', 'reason': 'а', 'phone': '89503378718'}
        """
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), "UTF-8")
            val_decode_str = decodestring(val).decode("UTF-8")
            new_data[k] = val_decode_str
        return new_data

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f"{path}/"
        request = {}
        request_method = environ["REQUEST_METHOD"]
        request["method"] = request_method
        if request_method == "POST":
            data = PostRequest().get_request_params(environ)
            res_data = Framework.decode_value(data)
            request['data'] = res_data
            print(f"Пришел POST-запрос: {res_data}")
        if request_method == "GET":
            request_params = GetRequests().get_params(environ)
            res_request_params = Framework.decode_value(request_params)
            request['request_params'] = res_request_params
            print(f"Пришел GET-запрос: {res_request_params}")
        if path in self.routes:
            view = self.routes[path]
        else:
            view = Error404()

        for context in self.context:
            context(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
