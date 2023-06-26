class GetRequests:
    @staticmethod
    def parse_data(data: str):
        """
        Функция превращающая строку с параметрами типа - "id=7&name=daria",
        в словарь типа {"id":7,"name":"daria"}
        :param data: строка например "id=7&name=daria"
        :return: словарь
        """
        result_dict = dict()
        if data:
            params = data.split("&")
            for param in params:
                key, value = param.split("=")
                result_dict[key] = value
        return result_dict

    @staticmethod
    def get_params(environ: dict):
        """
        Функция получающая строку типа "id=7&name=daria" из словаря environ
        и отдает строку в функцию parse_data
        :param environ: словарь
        :return: словарь
        """
        param_string = environ["QUERY_STRING"]
        request_params = GetRequests.parse_data(param_string)
        return request_params


class PostRequest:
    @staticmethod
    def parse_data(data: str):
        """
        Функция превращающая строку с параметрами типа - "id=7&name=daria",
        в словарь типа {"id":7,"name":"daria"}
        :param data: строка например "id=7&name=daria"
        :return: словарь
        """
        result_dict = dict()
        if data:
            params = data.split("&")
            for param in params:
                key, value = param.split("=")
                result_dict[key] = value
        return result_dict

    @staticmethod
    def get_wsgi_input_data(environ: dict):
        """
        Функция, получающая длину тела контента  и считывающая данные в виде  bytes
        :param environ:
        :return: строка в bytes
        """
        content_length_data = environ.get("CONTENT_LENGTH")
        content_length = int(content_length_data) if content_length_data else 0
        print(f"Длина контента: {content_length}")
        data = environ["wsgi.input"].read(content_length) if content_length > 0 else b""
        print(data)
        return data

    def parse_wsgi_input_data(self, data: bytes):
        """
        Функция декодирующая из типа bytes и вызывающая parse_data
        :param data: bytes
        :return: словарт
        """
        data_str_from_bytes = data.decode(encoding="utf-8")
        print(f"Декодированная строка: {data_str_from_bytes}")
        return self.parse_data(data_str_from_bytes)

    def get_request_params(self, environ):
        """
        Функция получающая данные из словаря environ и превращающая их в словарь
        :param environ: словарь environ
        :return: словарь типа {"id":7,"name":"daria"}
        """
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
