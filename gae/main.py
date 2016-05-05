#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")


class datetimeHandler(BaseHandler):
    def get(self):
        vars = {
            #   http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
            "date": datetime.date.today(),
            "dateFormat": datetime.date.today().strftime('%d, %b %Y'),
            "time": datetime.datetime.now(),
            "timeFormat": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        return self.render_template("15_datetime.html", vars)


class omeniindexHandler(BaseHandler):
    def get(self):
        return self.render_template("15_omeni_index.html")


class omeniomeniHandler(BaseHandler):
    def get(self):
        return self.render_template("15_omeni_omeni.html")


class omenimojiprojektiHandler(BaseHandler):
    def get(self):
        return self.render_template("15_omeni_mojiprojekti.html")


class lotoHandler(BaseHandler):
    def get(self):
        return self.render_template("15_loto.html")


class loto_zgenerirajHandler(BaseHandler):
    def get(self):
        loto_stevilke = sorted(random.sample(range(1, 39), 8))
        view_vars = {
            "loto_stevilke": loto_stevilke
        }
        return self.render_template("15_loto_zgeneriraj.html", view_vars)


class kalkulatorHandler(BaseHandler):
    def get(self):
        return self.render_template("16_kalkulator.html")
    def post(self):
        operacija = self.request.get("operacija")
        if (operacija == "+"):
            izracunaj = int(self.request.get("stevilka1")) + int(self.request.get("stevilka2"))
            self.write("</h1>Izracunano : " + str(izracunaj))
        if (operacija == "-"):
            izracunaj = int(self.request.get("stevilka1")) - int(self.request.get("stevilka2"))
            self.write("</h1>Izracunano : " + str(izracunaj))
        if (operacija == "*"):
            izracunaj = int(self.request.get("stevilka1")) * int(self.request.get("stevilka2"))
            self.write("</h1>Izracunano : " + str(izracunaj))
        if (operacija == "/"):
            izracunaj = int(self.request.get("stevilka1")) / int(self.request.get("stevilka2"))
            self.write("</h1>Izracunano : " + str(izracunaj))


class skritosteviloHandler(BaseHandler):
    def get(self):
        return self.render_template("16_skritostevilo.html")
    def post(self):
        hiddenNumber = self.request.get("hiddenNumber")
        inputNumber = self.request.get("inputNumber")
        notifyUserText = ""
        if (hiddenNumber == "" ):
            hiddenNumber = str(random.randint(0, 10))
        elif (hiddenNumber == "XYZ" ):
            hiddenNumber = str(random.randint(0, 10))
        if (hiddenNumber > inputNumber ) :
            notifyUserText = "Entered number is too low!!"
        if (hiddenNumber < inputNumber ) :
            notifyUserText = "Entered number is too HIGH!!"
        if (hiddenNumber == inputNumber ) :
            notifyUserText = "Entered number is correct!!"
        view_vars = {
            "savedNumber": hiddenNumber,
            "notifyUserText" : notifyUserText
        }
        return self.render_template("16_skritostevilo.html", view_vars)


class pretvornikenotHandler(BaseHandler):
    def get(self):
        return self.render_template("16_pretvornikenot.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/15_datetime', datetimeHandler),
    webapp2.Route('/15_omeni_index', omeniindexHandler),
    webapp2.Route('/15_omeni_omeni', omeniomeniHandler),
    webapp2.Route('/15_omeni_mojiprojekti', omenimojiprojektiHandler),
    webapp2.Route('/15_loto', lotoHandler),
    webapp2.Route('/15_loto_zgeneriraj', loto_zgenerirajHandler),
    webapp2.Route('/16_kalkulator', kalkulatorHandler),
    webapp2.Route('/16_skritostevilo', skritosteviloHandler),
    webapp2.Route('/16_pretvornikenot', pretvornikenotHandler),
], debug=True)
