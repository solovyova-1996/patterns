from daria_framework.templator import render


class Index:
    def __call__(self, request: dict):
        return "200 ok", render('index.html', date=request.get('date', None), time=request.get('time', None),
                                location=request.get('location', None))


class About:
    def __call__(self, request: dict):
        return "200 ok", render('about.html', date=request.get('date', None), time=request.get('time', None),
                                location=request.get('location', None))


class Contacts:
    def __call__(self, request: dict):
        return "200 ok", render('contacts.html', date=request.get('date', None), time=request.get('time', None),
                                location=request.get('location', None))


class Forms:
    def __call__(self, request: dict):
        return "200 ok", render('forms.html', date=request.get('date', None), time=request.get('time', None),
                                location=request.get('location', None))
