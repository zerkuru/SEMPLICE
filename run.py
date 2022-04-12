from wsgiref.simple_server import make_server
import simba_framework.main
import simba_framework.templator
from urls import routes, fronts


application = simba_framework.main.Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Start 8080")
    httpd.serve_forever()
