from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))

class About:
    def __call__(self, request):
        return '200 OK', 'about'

class Contacts:
    def __call__(self, request):
        return '200 OK', 'contacts'

class Courses:
    def __call__(self, request):
        return '200 OK', 'courses'

