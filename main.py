import datetime
import os
import time
import threading
import jenv
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web
from api import api_v1
from sql import myreq

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "xsrf_cookies": False,
    "cookie_secret": "SECRETCODE",
    "login_url": "/login",
    "template_loader": jenv.jinja2_loader,
    "debug": True
}

title = 'FlightPlus'


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        print(self.request.remote_ip)
        self.clear_header('Server')
        self.clear_header('Date')
        if self.request.protocol == 'http':
            self.redirect('https://' + self.request.host, permanent=False)

    def get_current_user(self):
        return self.get_secure_cookie("user")


class IndexHandler(BaseHandler):
    # @tornado.web.authenticated
    def get(self):
        count = []
        for i in range(50):
            count.append(i)

        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=title)
        if user_inf:
            arguments.update(user_inf=user_inf)
            self.render("mainpage.html", arguments=arguments)
        else:
            if self.current_user:
                myreq.delete_user_for_token(self.current_user)
            self.render("mainpage.html", arguments=arguments)


class LogoutHandler(BaseHandler):
    def get(self):
        if self.current_user:
            myreq.delete_user_for_token(self.current_user)
            self.clear_cookie('user')
        self.redirect("/")


class ProfileHandler(BaseHandler):
    def write_error(self, status_code: int, **kwargs):
        self.set_status(status_code)
        self.finish(kwargs)

    def get(self):
        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Профиль')
        if user_inf:
            arguments.update(user_inf=user_inf)
            self.render("profile.html", arguments=arguments)
        else:
            self.set_status(401)
            self.redirect('/')

    def post(self):
        arguments = {}
        arguments.update(title=f'{title} - Профиль')
        user_inf = isToken(self.current_user)
        if user_inf:
            arguments.update(user_inf=user_inf)
            if self.get_argument("password") == self.get_argument("confirmpassword"):
                myreq.update_user_password_for_email(user_inf['email'], self.get_argument("password"))
                arguments.update(error='Пароль обновлен!')
                self.render("profile.html", arguments=arguments)
            else:
                arguments.update(error='Пароли не совпадают!')
                self.render("profile.html", arguments=arguments)
        else:
            self.set_status(401)
            self.redirect('/')


class PassengerHandler(BaseHandler):
    def get(self):
        arguments = {}
        arguments.update(title=f'{title} - Управление пассажирами')
        user_inf = isToken(self.current_user)
        if user_inf:
            arguments.update(user_inf=user_inf)
            documet_type = myreq.get_document_type()
            arguments.update(documet_type=documet_type)
            passenger_inf = myreq.get_passenger_list(user_inf['id'])
            if len(passenger_inf) > 0:
                arguments.update(passenger_inf=passenger_inf)
                self.render("passenger.html", arguments=arguments)
            else:
                self.render("passenger.html", arguments=arguments)
        else:
            self.set_status(401)
            self.redirect('/')


class AdminAirplanesHandler(BaseHandler):
    def get(self):
        arguments = {}
        arguments.update(title=f'{title} - Управление самолетами')
        user_inf = isToken(self.current_user)
        if user_inf and user_inf['id_users_lvl'] > 0:
            arguments.update(user_inf=user_inf)
            airplane_status = myreq.get_airplane_status()
            arguments.update(airplane_status=airplane_status)
            airplane = myreq.get_airplane_list()
            arguments.update(airplane=airplane)
            self.render("admin/airplane.html", arguments=arguments)
        else:
            self.set_status(404)
            self.render("404.html", arguments=arguments)


class AdminAirportsHandler(BaseHandler):
    def get(self):
        arguments = {}
        arguments.update(title=f'{title} - Управление аэропортами')
        user_inf = isToken(self.current_user)
        if user_inf and user_inf['id_users_lvl'] > 0:
            arguments.update(user_inf=user_inf)
            country_list = myreq.get_country_list()
            if len(country_list) > 0:
                arguments.update(country_list=country_list)
                city_list = myreq.get_city_list()
                if len(city_list) > 0:
                    arguments.update(city_list=city_list)
                    airport_list = myreq.get_airport_list()
                    if len(airport_list) > 0:
                        arguments.update(airport_list=airport_list)
            self.render("admin/airport.html", arguments=arguments)
        else:
            self.set_status(404)
            self.render("404.html", arguments=arguments)


class AdminRoutesHandler(BaseHandler):
    def get(self):
        arguments = {}
        arguments.update(title=f'{title} - Управление маршрутами')
        user_inf = isToken(self.current_user)
        arguments.update(user_inf=user_inf)
        if user_inf and user_inf['id_users_lvl'] > 0:
            route_list = myreq.get_route_list()
            if len(route_list) > 0:
                arguments.update(route_list=route_list)
            try:
                country_list = myreq.get_country_list()
                city_list = myreq.get_city_list_country(country_list[0]['id'])
                airport_list = myreq.get_airport_list_city(city_list[0]['id'])
                airplane_list = myreq.get_airplane_list()
                if len(country_list) > 0:
                    arguments.update(country_list=country_list)
                if len(city_list) > 0:
                    arguments.update(city_list=city_list)
                if len(airport_list) > 0:
                    arguments.update(airport_list=airport_list)
                if len(airplane_list) > 0:
                    arguments.update(airplane_list=airplane_list)
            except Exception as e:
                print(e)
            self.render("admin/route.html", arguments=arguments)
        else:
            self.set_status(404)
            self.render("404.html", arguments=arguments)


class SearchHandler(BaseHandler):
    def get(self):
        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Поиск маршрута')
        query_to = self.get_argument("query_to", None)
        query_from = self.get_argument("query_from", None)
        date_to = self.get_argument("date_to", None)
        if user_inf:
            arguments.update(user_inf=user_inf)
        if query_to and query_from and date_to:
            query_to = myreq.get_city_abbr(query_to.split(') ')[1].split("']")[0])
            query_from = myreq.get_city_abbr(query_from.split(') ')[1].split("']")[0])
            if query_to and query_from:
                args = {'query_to': f'{query_to["city_name"]}({query_to["country_name"]}) {query_to["city_abbr"]}',
                        'query_from': f'''{query_from["city_name"]}({query_from["country_name"]}) {query_from[
                            "city_abbr"]}''',
                        'date_to': date_to}
                arguments.update(args=args)
        self.render("search.html", arguments=arguments)

    def post(self):
        query_to = self.get_argument("query_to", None)
        query_from = self.get_argument("query_from", None)
        date_to = self.get_argument("date_to", None)
        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Поиск маршрута')
        if user_inf:
            arguments.update(user_inf=user_inf)
        if query_to and query_from and date_to:
            query_to = myreq.get_city_abbr(query_to.split(') ')[1].split("']")[0])
            query_from = myreq.get_city_abbr(query_from.split(') ')[1].split("']")[0])
            if query_to and query_from:
                args = {'query_to': f'{query_to["city_name"]}({query_to["country_name"]}) {query_to["city_abbr"]}',
                        'query_from': f'''{query_from["city_name"]}({query_from["country_name"]}) {query_from[
                            "city_abbr"]}''',
                        'date_to': date_to}
                arguments.update(search_arg=args)
                answ = myreq.search_route_list(query_to['city_id'], query_from['city_id'],
                                               int(datetime.datetime.strptime(date_to, '%Y-%m-%d').timestamp()))
                if answ:
                    arguments.update(answ=answ)
        self.render("search.html", arguments=arguments)


class CreateTicketHandler(BaseHandler):
    def get(self):
        self.redirect('/search')

    def post(self):
        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Формирование билета')
        if user_inf:
            arguments.update(user_inf=user_inf)
            passenger_inf = myreq.get_passenger_list(user_inf['id'])
            if len(passenger_inf) > 0:
                arguments.update(passenger_inf=passenger_inf)
        route_id = self.get_argument("route_id", None)
        if isInt(route_id) > 0:
            route = myreq.get_route_for_id(route_id)
            arguments.update(route=route)
            places = myreq.get_place_for_routeid(route_id)
            if len(places) > 0:
                arguments.update(places=places)
            documet_type = myreq.get_document_type()
            arguments.update(documet_type=documet_type)
        self.render("create_ticket.html", arguments=arguments)


class BuyTicketHandler(BaseHandler):
    def get(self):
        self.redirect('/search')

    def post(self):
        def get_file():
            import convertapi
            convertapi.api_secret = 'APIKEY'
            result = convertapi.convert('pdf', {'Url': f'https://flightplus.ru/ticketPDF?ticket_id={ticket_id}'},
                                        from_format='web')
            result.file.save(f'static/tickets/ticket-{ticket_id}.pdf')

        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Билет')
        if user_inf:
            arguments.update(user_inf=user_inf)
        route_id = self.get_argument("route_id", None)
        passenger_id = self.get_arguments("passenger_id")
        places_id = self.get_arguments("places_id")
        if isInt(route_id) > 0 and len(passenger_id) > 0 and len(places_id) > 0:
            route = myreq.get_route_for_id(route_id)
            arguments.update(route=route)
            ticket = []
            for i, item in enumerate(passenger_id):
                age_type_id = myreq.get_age_type_passenger(item)
                ticket_id = myreq.add_buy_ticket(passenger_id[i], age_type_id, places_id[i], route['route_price'])
                ticket_inf = myreq.get_ticket_info(ticket_id)
                ticket.append(ticket_inf)
                file_load = threading.Thread(target=get_file)
                file_load.start()
            arguments.update(ticket=ticket)
        self.render("ticket_buy.html", arguments=arguments)


class TicketPDFHandler(BaseHandler):
    def get(self):
        arguments = {}
        arguments.update(title=f'{title} - Билет')
        ticket_id = self.get_argument("ticket_id", None)
        if isInt(ticket_id) > 0:
            ticket = myreq.get_ticket_info(ticket_id)
            if ticket:
                arguments.update(ticket=ticket)
        self.render("ticket.html", arguments=arguments)


class OrdersHandler(BaseHandler):
    def get(self):
        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Заказы')
        if user_inf:
            arguments.update(user_inf=user_inf)
            orders = myreq.get_order(user_inf['id'])
            if len(orders) > 0:
                arguments.update(orders=orders)
            print(arguments)
        self.render("orders.html", arguments=arguments)


class NotFoundRequestHandler(BaseHandler):
    def prepare(self):
        self.set_status(404)
        user_inf = isToken(self.current_user)
        arguments = {}
        arguments.update(title=f'{title} - Ничего не найдено!')
        if user_inf:
            arguments.update(user_inf=user_inf)
            self.render("404.html", arguments=arguments)
        else:
            if self.current_user:
                myreq.delete_user_for_token(self.current_user)
            self.render("404.html", arguments=arguments)


def create_authtoken(email, password):
    import hashlib, time
    return hashlib.md5((f'{time.time()} | {email} | {password}').encode()).hexdigest()


def isInt(value):
    try:
        int(value)
        return int(value)
    except Exception:
        return 0


def isToken(value):
    try:
        if value:
            return myreq.get_user_for_token(value)
        else:
            return None
    except Exception:
        return None


def make_app():
    return tornado.web.Application([
        tornado.web.url(r'/', IndexHandler, name="Index"),
        tornado.web.url(r'/logout', LogoutHandler, name="Logout"),
        tornado.web.url(r'/profile', ProfileHandler, name="Profile"),
        tornado.web.url(r'/passenger', PassengerHandler, name="Passenger"),
        tornado.web.url(r'/search', SearchHandler, name="Search"),
        tornado.web.url(r'/create_ticket', CreateTicketHandler, name="CreateTicket"),
        tornado.web.url(r'/buy_ticket', BuyTicketHandler, name="BuyTicket"),
        tornado.web.url(r'/ticketPDF', TicketPDFHandler, name="TicketPDF"),
        tornado.web.url(r'/orders', OrdersHandler, name="Orders"),
        tornado.web.url(r'/admin/airplanes', AdminAirplanesHandler, name="AdminAirplanes"),
        tornado.web.url(r'/admin/airports', AdminAirportsHandler, name="AdminAirports"),
        tornado.web.url(r'/admin/routes', AdminRoutesHandler, name="AdminRoutes"),
        tornado.web.url(r'/api/v1/login', api_v1.LoginHandler, name="ApiV1Login"),
        tornado.web.url(r'/api/v1/register', api_v1.RegisterHandler, name="ApiV1Register"),
        tornado.web.url(r'/api/v1/addPassenger', api_v1.AddPassenger, name="ApiV1AddPassenger"),
        tornado.web.url(r'/api/v1/delPassenger', api_v1.DelPassenger, name="ApiV1DelPassenger"),
        tornado.web.url(r'/api/v1/search', api_v1.Search, name="ApiV1Search"),
        tornado.web.url(r'/api/v1/checkticket', api_v1.CheckTicket, name="ApiV1CheckTicket"),
        tornado.web.url(r'/api/v1/admin/addAirplane', api_v1.AdminAddAirplane, name="ApiV1AdminAddAirplane"),
        tornado.web.url(r'/api/v1/admin/load_img', api_v1.AdminLoadIMG, name="ApiV1AdminLoadIMG"),
        tornado.web.url(r'/api/v1/admin/editAirplane', api_v1.AdminEditAirplane, name="ApiV1AdminEditAirplane"),
        tornado.web.url(r'/api/v1/admin/returnAirplane', api_v1.AdminReturnAirplane, name="ApiV1AdminReturnAirplane"),
        tornado.web.url(r'/api/v1/admin/country', api_v1.AdminCountry, name="ApiV1AdminCountry"),
        tornado.web.url(r'/api/v1/admin/city', api_v1.AdminCity, name="ApiV1AdminCity"),
        tornado.web.url(r'/api/v1/admin/airport', api_v1.AdminAirport, name="ApiV1AdminAirport"),
        tornado.web.url(r'/api/v1/admin/route', api_v1.AdminRoute, name="ApiV1AdminRoute"),
        tornado.web.url(r'/api/v1/admin/getCityList', api_v1.AdminGetCityList, name="ApiV1AdminGetCityList"),
        tornado.web.url(r'/api/v1/admin/getAirportList', api_v1.AdminGetAirportList, name="ApiV1AdminGetAirportList"),
        tornado.web.url(r"/.*", NotFoundRequestHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    http_server = tornado.httpserver.HTTPServer(
        app,
        ssl_options={
            "certfile": os.path.join("./keys/", 'cert.crt'),
            "keyfile": os.path.join("./keys/", "key.key"),
        }
    )
    http_server.listen(443)
    tornado.ioloop.IOLoop.current().start()
