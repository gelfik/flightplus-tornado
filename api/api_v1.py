from sql import myreq
import json, datetime, time
import tornado.web
import jenv

url_global = 'https://flightplus.ru/'


class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code: int, **kwargs):
        self.set_status(status_code)
        if status_code == 200:
            kwargs.update({'status_code': status_code})
            kwargs.update({'error': None})
            self.finish(kwargs)
        elif status_code == 500:
            self.finish({'success': None, 'error': 'Ошибка сервера!', 'status_code': status_code})
        elif status_code == 401:
            self.finish({'success': None, 'error': 'Ошибка авторизации!', 'status_code': status_code})
        else:
            kwargs.update({'success': None, 'status_code': status_code})
            self.finish(kwargs)

    def prepare(self):
        self.clear_header('Server')
        self.clear_header('Date')
        if self.request.protocol == 'http':
            self.redirect('https://' + self.request.host, permanent=False)

    def get_current_user(self):
        return self.get_secure_cookie("user")


class LoginHandler(BaseHandler):
    def post(self):
        email = self.get_argument("email", None)
        password_arg = self.get_argument("password", None)
        if email and password_arg:
            user_id, password = myreq.cheak_user_for_email(email)
            if user_id is not None:
                if password == password_arg:
                    authtoken = create_authtoken(email, password_arg)
                    myreq.add_user_for_token(authtoken, user_id)
                    self.set_secure_cookie("user", authtoken)
                    self.write_error(status_code=200, success='Успешно!')
                else:
                    self.write_error(status_code=400, error='Данные для входа не верны!')
            else:
                self.write_error(status_code=400, error='Данный email не найден в системе!')
        else:
            self.write_error(status_code=400, error='Учетные данные не представлены!')


class RegisterHandler(BaseHandler):
    def post(self):
        RulesAcceptCheak = self.get_argument("RulesAcceptCheak", None)
        password_arg = self.get_argument("password", None)
        confirmpassword_arg = self.get_argument("confirmpassword", None)
        phone = self.get_argument("phone", None)
        email = self.get_argument("email", None)
        surname = self.get_argument("surname", None)
        name = self.get_argument("name", None)
        if RulesAcceptCheak == 'true':
            if password_arg and confirmpassword_arg and phone and email and surname and name:
                if password_arg == confirmpassword_arg:
                    user_mail = myreq.cheak_user_for_email(email)
                    id, password = user_mail
                    if password is None and id is None:
                        user_id = myreq.register_user(password_arg, phone, email, name, surname)
                        authtoken = create_authtoken(email, phone)
                        myreq.add_user_for_token(authtoken, user_id)
                        self.set_secure_cookie("user", authtoken)
                        self.write_error(status_code=200, success='Успешно!')
                    else:
                        self.write_error(status_code=400, error='Данный email уже зарегистрирован в нашей системе!')
                else:
                    self.write_error(status_code=400, error='Пароли не совпадают!')
            else:
                self.write_error(status_code=400, error='Данные не заполнены!')
        else:
            self.write_error(status_code=400, error='Вы не приняли пользовательское соглашение!')


class DelPassenger(BaseHandler):
    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None:
            if self.get_argument("passangerid"):
                myreq.del_passenger(user_inf['id'], self.get_argument("passangerid"))
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error='Вы не указали id пассажира!')
        else:
            self.write_error(status_code=401)


class AddPassenger(BaseHandler):
    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None:
            doc_id = isInt(self.get_argument("id_document_type", None))
            last_name = self.get_argument("last_name", None)
            first_name = self.get_argument("first_name", None)
            if self.get_argument("patronymic", None):
                patronymic = self.get_argument("patronymic")
            else:
                patronymic = ''
            birthday = self.get_argument("birthday", None)
            phone = self.get_argument("phone", None)
            email = self.get_argument("email", None)
            id_gender = self.get_argument("id_gender", None)
            document_number = self.get_argument("document_number", None)
            valid_date = self.get_argument("valid_date", None)
            if (doc_id == 1 or doc_id == 2 or doc_id == 4) and int(
                    datetime.datetime.strptime(valid_date, '%Y-%m-%d').timestamp()) > int(time.time()):
                myreq.add_passenger(user_inf['id'], last_name, first_name, patronymic, birthday, phone, email,
                                    id_gender, doc_id, document_number, valid_date)
            elif doc_id == 3:
                myreq.add_passenger(user_inf['id'], last_name, first_name, patronymic, birthday, phone, email,
                                    id_gender, doc_id, document_number, None)
            else:
                self.write_error(status_code=400, error='Данный документ не действителен!')
            self.write_error(status_code=200, success='Успешно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminLoadIMG(BaseHandler):
    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            def savepic(self):
                import hashlib
                file1 = self.request.files['seats_scheme'][0]
                original_fname = 'static/img/' + str(
                    hashlib.md5((str(time.time()) + file1['filename']).encode()).hexdigest()) + '.png'
                output_file = open(original_fname, 'wb')
                output_file.write(file1['body'])
                # scale_image(original_fname, original_fname, width=195)
                return f'{url_global}{original_fname}'

            file_link = savepic(self)
            self.write_error(status_code=200, success=file_link)
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminAddAirplane(BaseHandler):
    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            airplane_num = self.get_argument("airplane_num", None)
            airplane_name = self.get_argument("airplane_name", None)
            column_of_seats = self.get_argument("column_of_seats", None)
            row_of_seats = self.get_argument("row_of_seats", None)
            status = self.get_argument("status", None)
            seats_scheme = self.get_argument("seats_scheme", None)
            if isInt(row_of_seats) > 0 and isInt(
                    column_of_seats) > 0 and airplane_num and airplane_name and status and seats_scheme:
                myreq.add_airplane(airplane_name, airplane_num, status, row_of_seats, column_of_seats, seats_scheme)
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error=f'Некорректные данные!{seats_scheme}')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminEditAirplane(BaseHandler):
    def get(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            airplane_inf = myreq.get_airplane(self.get_argument("airplane_id", None))
            if airplane_inf is not None:
                airplane_status = myreq.get_airplane_status()
                arguments = {}
                arguments.update(airplane_status=airplane_status)
                arguments.update(airplane_inf=airplane_inf)
                self.render("admin/modal/admin_airplane_get_mobal.html", arguments=arguments)
            else:
                self.write_error(status_code=400, error='Некорректные данные!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')

    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            airplane_id = self.get_argument("airplane_id", None)
            airplane_num = self.get_argument("airplane_num", None)
            airplane_name = self.get_argument("airplane_name", None)
            column_of_seats = self.get_argument("column_of_seats", None)
            row_of_seats = self.get_argument("row_of_seats", None)
            status = self.get_argument("status", None)
            if isInt(airplane_id) > 0 and isInt(row_of_seats) > 0 and isInt(
                    column_of_seats) > 0 and airplane_num and status:
                myreq.update_airplane(airplane_id, airplane_name, airplane_num, status, row_of_seats, column_of_seats)
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error='Некорректные данные!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminReturnAirplane(BaseHandler):
    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            airplane_id = self.get_argument("airplane_id", None)
            if isInt(airplane_id) > 0:
                airplane_inf = myreq.get_airplane(airplane_id)
                if airplane_inf is not None:
                    myreq.set_airplane_status(airplane_inf['id'], 1)
                    self.write_error(status_code=200, success='Успешно!')
                else:
                    self.write_error(status_code=400, error='Самолет не найден!')
            else:
                self.write_error(status_code=400, error='Некорректные данные!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminCountry(BaseHandler):
    def put(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            country_name = self.get_argument("country_name", None)
            abbreviation = self.get_argument("abbreviation", None)
            if country_name and abbreviation:
                myreq.add_country(country_name, abbreviation)
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error='Данные не заполнены!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')

    def delete(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            country_id = self.get_argument("country_id", None)
            if isInt(country_id) > 0:
                myreq.del_country(country_id)
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminCity(BaseHandler):
    def put(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            country_id = self.get_argument("country_id", None)
            city_name = self.get_argument("city_name", None)
            abbreviation = self.get_argument("abbreviation", None)
            if isInt(country_id) > 0 and city_name and abbreviation:
                country_inf = myreq.get_country(country_id)
                if country_inf is not None:
                    myreq.add_city(country_inf['id'], city_name, abbreviation)
                    self.write_error(status_code=200, success='Успешно!')
                else:
                    self.write_error(status_code=400, error='Страна не найдена!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')

    def delete(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            city_id = self.get_argument("city_id", None)
            if isInt(city_id) > 0:
                myreq.del_city(city_id)
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminAirport(BaseHandler):
    def put(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            country_id = self.get_argument("airport_country_select", None)
            city_id = self.get_argument("airport_city_select", None)
            name = self.get_argument("airport_name", None)
            abbreviation = self.get_argument("airport_abbreviation", None)
            if isInt(country_id) > 0 and isInt(city_id) > 0 and name and abbreviation:
                country_inf = myreq.get_country(country_id)
                city_inf = myreq.get_city(city_id)
                if country_inf and city_inf:
                    myreq.add_airport(country_inf['id'], city_inf['id'], name, abbreviation)
                    self.write_error(status_code=200, success='Успешно!')
                else:
                    self.write_error(status_code=400, error='Страна или город не найдены!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')

    def delete(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            airport_id = self.get_argument("airport_id", None)
            if isInt(airport_id) > 0:
                myreq.del_airport(airport_id)
                self.write_error(status_code=200, success='Успешно!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminGetCityList(BaseHandler):
    def get(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            country_id = self.get_argument("country_id", None)
            if isInt(country_id) > 0:
                country_inf = myreq.get_country(country_id)
                if country_inf:
                    city_inf = myreq.get_city_list_country(country_inf['id'])
                    self.write_error(status_code=200, city_inf=city_inf)
                else:
                    self.write_error(status_code=400, error='Страна не найдена!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401, error='Ошибка авторизации!')


class AdminGetAirportList(BaseHandler):
    def get(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            city_id = self.get_argument("city_id", None)
            if isInt(city_id) > 0:
                city_inf = myreq.get_city(city_id)
                if city_inf:
                    airport_inf = myreq.get_airport_list_city(city_inf['id'])
                    self.write_error(status_code=200, airport_inf=airport_inf)
                else:
                    self.write_error(status_code=400, error='Город не найден!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401)


class AdminRoute(BaseHandler):
    def get_timestamp(self, date):
        try:
            date_processing = date[:16].replace('T', '-').replace(':', '-').split('-')
            return int(datetime.datetime(*[int(v) for v in date_processing]).timestamp())
        except:
            return 0

    def put(self):
        user_inf = isToken(self.current_user)
        if user_inf is not None and user_inf['id_users_lvl'] > 0:
            airport_from = self.get_argument("airport_from", None)
            airport_to = self.get_argument("airport_to", None)
            departure_date = self.get_timestamp(self.get_argument("departure_date", None))
            arrival_date = self.get_timestamp(self.get_argument("arrival_date", None))
            airplane_id = self.get_argument("airplane_id", None)
            price = self.get_argument("price", None)
            if isInt(airplane_id) > 0 and isInt(airport_from) > 0 and isInt(airport_to) > 0 and isInt(
                    departure_date) > 0 and isInt(arrival_date) > 0 and isInt(price) > 0:
                airplane_inf = myreq.get_airplane(airplane_id)
                airport_inf_from = myreq.get_airport(airport_from)
                airport_inf_to = myreq.get_airport(airport_to)
                if airplane_inf and airport_inf_from and airport_inf_to:
                    myreq.add_route(airport_inf_from['id'], airport_inf_to['id'], departure_date, arrival_date,
                                    airplane_inf, price)
                    self.write_error(status_code=200, success='Успешно!')
                else:
                    self.write_error(status_code=400, error='Аэропорт отправления или прибытия не найден!')
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401)


class Search(BaseHandler):
    def get(self):
        query = self.get_argument("query", None)
        if query:
            answer = myreq.search_country_city(query)
            if answer:
                text = ''
                for i, item in enumerate(answer):
                    text += f'''<li class="dropdown-item" id="{item["city_id"]}">{item["city_name"]}({item["country_name"]}) {item["city_abbr"]}</li>'''
                text += f"<!--{time.time()}-->"
                self.finish({'result': text})
            else:
                self.finish({'result': f'''<li class="dropdown-item">Ничего не найдено</li>
                                        <!--{time.time()}-->'''})
        else:
            self.write_error(status_code=400, error='Данные заполнены не корректно!')


class CheckTicket(BaseHandler):
    def post(self):
        user_inf = isToken(self.current_user)
        if user_inf:
            error = False
            route_id = self.get_argument("route_id", None)
            passenger_id = self.get_arguments("passenger_id[]")
            passenger_place = self.get_arguments("passenger_place[]")
            if isInt(route_id) > 0 and passenger_id and passenger_place:
                for i, item in enumerate(passenger_place):
                    if item in passenger_place[i+1:]:
                        error = True
                if error:
                    self.write_error(status_code=400, error='Нельзя выбирать одно место на нескольких пассажиров!')
                else:
                    total_price = myreq.get_final_price(user_inf['id'], passenger_id, route_id)
                    self.write_error(status_code=200, success='Успещно!', total_price=total_price)
            else:
                self.write_error(status_code=400, error='Данные заполнены не корректно!')
        else:
            self.write_error(status_code=401)

def create_authtoken(email, password):
    import hashlib, time
    return hashlib.md5((f'{time.time()} | {email} | {password}').encode()).hexdigest()


def isInt(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return 0


def isToken(value):
    try:
        if value:
            return myreq.get_user_for_token(value)
        else:
            return None
    except ValueError:
        return None