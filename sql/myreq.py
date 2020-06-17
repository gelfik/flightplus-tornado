from sql import connect
import datetime, time


def get_user_for_token(token_user):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT users_auth.*, users_lvl.lvl_name as lvl_name FROM users_auth INNER JOIN auth_token ON users_auth.id = auth_token.id_user INNER JOIN users_lvl on users_auth.id_users_lvl=users_lvl.id WHERE (auth_token.token=%s)',
        token_user)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def get_user_for_email(email):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM users_auth where email=%s', email)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def get_passenger_list(user_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("""
select user_data.id                          as id,
       user_data.last_name                   as last_name,
       user_data.first_name                  as first_name,
       user_data.patronymic                  as patronymic,
       user_data.birthday                    as birthday,
       user_data.phone                       as phone,
       user_data.email                       as email,
       user_data_gender.gender_name          as gender_name,
       user_data_document_type.document_type as document_type,
       user_data.document_number             as document_number,
       user_data.valid_date                  as valid_date
from user_data
       inner join users_auth_user_data
                  on users_auth_user_data.id_user_data = user_data.id and users_auth_user_data.id_user = %s
       inner join user_data_gender on user_data_gender.id = user_data.id_gender
       inner join user_data_document_type on user_data_document_type.id = user_data.id_document_type;""", user_id)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def update_user_password_for_email(email, newpassword):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'update users_auth set password=%s where email=%s', (newpassword, email))
    connection.commit()
    cursor.close()
    connection.close()


def add_passenger(user_id, last_name, first_name, patronymic, birthday, phone, email, id_gender, id_document_type,
                  document_number, valid_date):
    connection = connect.getConnection()
    cursor = connection.cursor()
    if valid_date:
        cursor.execute(
            'insert into user_data (last_name, first_name, patronymic, birthday, phone, email, id_gender, id_document_type, document_number, valid_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (last_name, first_name, patronymic, birthday, phone, email, id_gender, id_document_type, document_number,
             valid_date))
    else:
        cursor.execute(
            'insert into user_data (last_name, first_name, patronymic, birthday, phone, email, id_gender, id_document_type, document_number) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (last_name, first_name, patronymic, birthday, phone, email, id_gender, id_document_type, document_number))
    connection.commit()
    add_id = cursor.lastrowid
    cursor.execute('insert into users_auth_user_data (id_user, id_user_data) values (%s,%s)', (user_id, add_id))
    connection.commit()
    cursor.close()
    connection.close()


def del_passenger(user_id, passenger_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'delete from users_auth_user_data where id_user=%s and id_user_data=%s', (user_id, passenger_id))
    connection.commit()
    cursor.close()
    connection.close()


def get_document_type():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user_data_document_type')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def add_user_for_token(token, user_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('insert into auth_token (token, id_user) values (%s,%s)', (token, user_id))
    connection.commit()
    cursor.close()
    connection.close()


def delete_user_for_token(token):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('delete from auth_token where token=%s', token)
    connection.commit()
    cursor.close()
    connection.close()


def cheak_user_for_email(email):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('select id, password from users_auth where email=%s', email)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result is not None:
        return result['id'], result['password']
    else:
        return None, None


def register_user(password, phone, email, name, surname):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('insert into users_auth (password, phone, email, user_name, user_surname) values (%s,%s,%s,%s,%s)',
                   (password, phone, email, name, surname))
    user_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return user_id


def add_airplane(name, num, status, row, col, seats_scheme):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into airplane (airplane_name, airplane_num, status, row_of_seats, column_of_seats, seats_scheme) values (%s, %s, %s, %s, %s, %s)',
        (name, num, status, row, col, seats_scheme))
    connection.commit()
    cursor.close()
    connection.close()


def update_airplane(id, name, num, status, row, col):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'update airplane set airplane_name=%s, airplane_num=%s, status=%s, row_of_seats=%s, column_of_seats=%s where id=%s',
        (name, num, status, row, col, id))
    connection.commit()
    cursor.close()
    connection.close()


def get_airplane_status():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM airplane_status')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_airplane_list():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT airplane.*, airplane_status.status_name as status_name FROM airplane JOIN airplane_status ON airplane_status.id=airplane.status ORDER BY airplane.status ASC, airplane.airplane_name ASC, airplane.airplane_num  ASC')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_airplane(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT airplane.*, airplane_status.status_name as status_name FROM airplane JOIN airplane_status ON airplane_status.id=airplane.status where airplane.id=%s',
        id)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def set_airplane_status(id, status):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('update airplane set status=%s where id=%s', (status, id))
    connection.commit()
    cursor.close()
    connection.close()


def get_country_list():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM countries WHERE status>0 ORDER BY country_name')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_country(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM countries where id=%s and status>0  ORDER BY country_name', id)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def del_country(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('update countries set status=0 where id=%s', (id))
    cursor.execute('update cities set status=0 where id_country=%s', (id))
    cursor.execute('update airports set status=0 where id_country=%s', (id))
    connection.commit()
    cursor.close()
    connection.close()


def add_country(name, abbr):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into countries (country_name, abbreviation) values (%s, %s)', (name, abbr))
    connection.commit()
    cursor.close()
    connection.close()


def get_city_list():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cities WHERE status>0 ORDER BY city_name')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_city_list_country(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cities WHERE id_country=%s and status>0 ORDER BY city_name', id)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_city(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cities WHERE id=%s and status>0 ORDER BY city_name', id)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def get_city_abbr(abbr):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT countries.country_name as country_name, countries.abbreviation as country_abbr, cities.id as city_id, cities.city_name as city_name, cities.abbreviation as city_abbr "
        "FROM countries INNER JOIN cities ON cities.id_country=countries.id "
        "WHERE cities.abbreviation='{0}'".format(abbr))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def del_city(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('update cities set status=0 where id=%s', (id))
    cursor.execute('update airports set status=0 where id_city=%s', (id))
    connection.commit()
    cursor.close()
    connection.close()


def add_city(country_id, name, abbreviation):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into cities (id_country, city_name, abbreviation) values (%s, %s, %s)',
        (country_id, name, abbreviation))
    connection.commit()
    cursor.close()
    connection.close()


def get_airport_list():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM airports WHERE status>0 ORDER BY airport_name')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_airport(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM airports WHERE id=%s and status>0 ORDER BY airport_name', id)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def get_airport_list_city(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM airports WHERE id_city=%s and status>0 ORDER BY airport_name', id)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def del_airport(id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('update airports set status=0 where id=%s', (id))
    connection.commit()
    cursor.close()
    connection.close()


def add_airport(country_id, city_id, name, abbr):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into airports (id_country, id_city, airport_name, abbreviation) values (%s, %s, %s, %s)',
        (country_id, city_id, name, abbr))
    connection.commit()
    cursor.close()
    connection.close()


def get_route_list():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT route.*,
       airports_from.airport_name as airport_from, airports_from.abbreviation as airport_from_abbr, cities_from.city_name as city_from, countries_from.country_name as country_from,
       airports_to.airport_name as airport_to, airports_to.abbreviation as airport_to_abbr, cities_to.city_name as city_to, countries_to.country_name as country_to,
       (SELECT COUNT(*) FROM places WHERE places.id_route=route.id AND places.place_status=false) as place_count,
       airplane.*
FROM route
  INNER JOIN (select * from airports) airports_from on airports_from.id=route.id_airport_where_from
  INNER JOIN (select * from airports) airports_to on airports_to.id=route.id_airport_where_to
  INNER JOIN (select * from cities) cities_from on cities_from.id=airports_from.id_city
  INNER JOIN (select * from cities) cities_to on cities_to.id=airports_to.id_city
  INNER JOIN (select * from countries) countries_from on countries_from.id=airports_from.id_country
  INNER JOIN (select * from countries) countries_to on countries_to.id=airports_to.id_country
  INNER JOIN (select airplane.*, airplane_status.status_name as status_name from airplane inner join airplane_status on airplane_status.id=airplane.status) airplane on airplane.id=route.id_airplane
WHERE route.status > 0
ORDER BY departure_date ASC, country_from ASC, city_from ASC, arrival_date ASC, country_to ASC, city_to ASC""")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def add_route(airport_from, airport_to, departure_date, arrival_date, airplane_inf, price):
    # print(f'{airport_from} {airport_to} {departure_date} {arrival_date} {price} {airplane_inf}'.encode('utf-8'))
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO route (id_airport_where_from, id_airport_where_to, departure_date, arrival_date, id_airplane, price) VALUES (%s,%s,%s,%s,%s,%s)',
        (airport_from, airport_to, departure_date, arrival_date, airplane_inf['id'], price))
    connection.commit()
    add_id = cursor.lastrowid
    row_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V',
                'W', 'X', 'Y', 'Z']
    query_list = []
    for col in range(airplane_inf['column_of_seats']):
        for row in range(airplane_inf['row_of_seats']):
            seat = f'{row_list[row]}{col + 1}'
            query_list.append((add_id, seat))
    args_str = ','.join(cursor.mogrify("(%s,%s)", x) for x in query_list)
    cursor.execute('INSERT INTO places (id_route, place_number) VALUES ' + args_str)
    connection.commit()
    cursor.close()
    connection.close()


def search_country_city(query):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT countries.country_name as country_name, countries.abbreviation as country_abbr, cities.id as city_id, cities.city_name as city_name, cities.abbreviation as city_abbr "
        "FROM countries INNER JOIN cities ON cities.id_country=countries.id "
        "WHERE cities.city_name LIKE '{0}%'"
        "ORDER BY cities.city_name ASC, countries.country_name ASC LIMIT 10".format(query))
    result = cursor.fetchall()
    if len(result) <= 10:
        cursor.execute(
            "SELECT countries.country_name as country_name, countries.abbreviation as country_abbr, cities.id as city_id, cities.city_name as city_name, cities.abbreviation as city_abbr "
            "FROM countries INNER JOIN cities ON cities.id_country=countries.id "
            "WHERE countries.country_name LIKE '{0}%' "
            "ORDER BY cities.city_name ASC, countries.country_name ASC LIMIT {1}".format(query, 10 - len(result)))
        if len(result) == 0:
            result = cursor.fetchall()
        else:
            result += cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def search_route_list(query_to, query_from, date):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("""SELECT route.*,
       airports_from.airport_name  as airport_from,
       airports_from.abbreviation  as airport_from_abbr,
       airports_from.id            as airport_from_id,
       cities_from.city_name       as city_from,
       countries_from.country_name as country_from,
       airports_to.airport_name    as airport_to,
       airports_to.abbreviation    as airport_to_abbr,
       airports_to.id              as airport_to_id,
       cities_to.city_name         as city_to,
       countries_to.country_name   as country_to,
       (SELECT COUNT(*) FROM places WHERE places.id_route=route.id AND places.place_status=false) as place_count,
       airplane.*
FROM route
       INNER JOIN (select * from airports) airports_from on airports_from.id = route.id_airport_where_from
       INNER JOIN (select * from airports) airports_to on airports_to.id = route.id_airport_where_to
       INNER JOIN (select * from cities) cities_from on cities_from.id = airports_from.id_city
       INNER JOIN (select * from cities) cities_to on cities_to.id = airports_to.id_city
       INNER JOIN (select * from countries) countries_from on countries_from.id = airports_from.id_country
       INNER JOIN (select * from countries) countries_to on countries_to.id = airports_to.id_country
       INNER JOIN (select airplane.*, airplane_status.status_name as status_name
                   from airplane
                          inner join airplane_status on airplane_status.id = airplane.status) airplane
                  on airplane.id = route.id_airplane
WHERE route.status > 0
  and (route.id_airport_where_to = airports_to.id and airports_to.id_city = cities_to.id and cities_to.id = %s)
  and (route.id_airport_where_from = airports_from.id and airports_from.id_city = cities_from.id and
       cities_from.id = %s)
  and route.arrival_date >= %s
  and route.arrival_date <= %s
ORDER BY departure_date ASC, country_from ASC, city_from ASC, arrival_date ASC, country_to ASC, city_to ASC;""",
                   (query_from, query_to, date, date + 86400))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_route_for_id(route_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("""
SELECT route.id                                                                                as route_id,
       route.arrival_date                                                                      as route_arrival_date,
       route.departure_date                                                                    as route_departure_date,
       route.price                                                                             as route_price,
       airports_from.airport_name                                                              as airport_from,
       airports_from.abbreviation                                                              as airport_from_abbr,
       cities_from.city_name                                                                   as city_from,
       countries_from.country_name                                                             as country_from,
       airports_to.airport_name                                                                as airport_to,
       airports_to.abbreviation                                                                as airport_to_abbr,
       cities_to.city_name                                                                     as city_to,
       countries_to.country_name                                                               as country_to,
       (SELECT COUNT(*) FROM places WHERE places.id_route = route.id AND place_status = false) as place_count,
       airplane.airplane_name                                                                  as airplane_name,
       airplane.airplane_num                                                                   as airplane_num,
       airplane.seats_scheme                                                                   as airplane_seats_scheme
FROM route
       INNER JOIN airports airports_from on route.id_airport_where_from = airports_from.id
       INNER JOIN cities cities_from on airports_from.id_city = cities_from.id
       INNER JOIN countries countries_from on airports_from.id_country = countries_from.id
       INNER JOIN airports airports_to on route.id_airport_where_to = airports_to.id
       INNER JOIN cities cities_to on airports_to.id_city = cities_to.id
       INNER JOIN countries countries_to on airports_to.id_country = countries_to.id
       INNER JOIN airplane on route.id_airplane = airplane.id
WHERE route.id = %s and (SELECT COUNT(*) FROM places WHERE place_status=0)>0;""", route_id)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def get_ticket_age_type():
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ticket_age_type")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def ticket_check_passanger(user_id, passenger_list):
    connection = connect.getConnection()
    cursor = connection.cursor()
    passenger_inf = []
    for i, item in enumerate(passenger_list):
        cursor.execute("""
select user_data.id                          as id,
       user_data.last_name                   as last_name,
       user_data.first_name                  as first_name,
       user_data.patronymic                  as patronymic,
       user_data.birthday                    as birthday,
       user_data.phone                       as phone,
       user_data.email                       as email,
       user_data_gender.gender_name          as gender_name,
       user_data_document_type.document_type as document_type,
       user_data.document_number             as document_number,
       user_data.valid_date                  as valid_date
from user_data
       inner join users_auth_user_data
                  on users_auth_user_data.id_user_data = user_data.id and users_auth_user_data.id_user = %s
       inner join user_data_gender on user_data_gender.id = user_data.id_gender
       inner join user_data_document_type on user_data_document_type.id = user_data.id_document_type
where user_data.id= %s;""", (user_id, item))
        result = cursor.fetchone()
        if result is not None:
            date = str(datetime.date.today()).split('-')
            date = f'{str(int(date[0]) - 12)}-{date[1]}-{date[2]}'
            if int(datetime.datetime.strptime(str(result['birthday']), '%Y-%m-%d').timestamp()) > int(
                    datetime.datetime.strptime(date, '%Y-%m-%d').timestamp()):
                result.update(ticket_age_type_id=2)
            else:
                result.update(ticket_age_type_id=1)
            passenger_inf.append(result)
    cursor.close()
    connection.close()
    return passenger_inf


def get_place_for_routeid(route_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM places WHERE id_route=%s AND place_status=0", route_id)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_final_price(user_id, passenger_list, route_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    passenger_inf = []
    total_price = 0
    for i, item in enumerate(passenger_list):
        cursor.execute("""
select user_data.id                          as id,
       user_data.birthday                    as birthday
from user_data
       inner join users_auth_user_data
                  on users_auth_user_data.id_user_data = user_data.id and users_auth_user_data.id_user = %s
where user_data.id= %s;""", (user_id, item))
        result = cursor.fetchone()
        if result is not None:
            route = get_route_for_id(route_id)
            date = str(datetime.date.today()).split('-')
            date = f'{str(int(date[0]) - 12)}-{date[1]}-{date[2]}'
            if int(datetime.datetime.strptime(str(result['birthday']), '%Y-%m-%d').timestamp()) > int(
                    datetime.datetime.strptime(date, '%Y-%m-%d').timestamp()):
                result.update(ticket_age_type_id=2)
                result.update(final_price=int(int(route['route_price']) * 0.5))
                total_price += int(int(route['route_price']) * 0.5)
            else:
                result.update(ticket_age_type_id=1)
                result.update(final_price=int(route['route_price']) * 1)
                total_price += int(route['route_price']) * 1
            passenger_inf.append(result)
    cursor.close()
    connection.close()
    return total_price


def get_age_type_passenger(passenger_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT birthday FROM user_data WHERE id=%s", passenger_id)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        date = str(datetime.date.today()).split('-')
        date = f'{str(int(date[0]) - 12)}-{date[1]}-{date[2]}'
        if int(datetime.datetime.strptime(str(result['birthday']), '%Y-%m-%d').timestamp()) > int(
                datetime.datetime.strptime(date, '%Y-%m-%d').timestamp()):
            return 2
        else:
            return 1
    else:
        return 1


def place_update_status(id_place):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'update places set place_status=1 where id=%s', (id_place))
    connection.commit()
    cursor.close()
    connection.close()


def add_buy_ticket(passenger_id, age_type_id, id_place, price):
    connection = connect.getConnection()
    cursor = connection.cursor()
    if age_type_id == 1:
        final_price = int(price * 1)
    else:
        final_price = int(price * 0.5)
    cursor.execute(
        'insert into ticket (id_user_data, id_ticket_age_type, id_places, final_price, buy_time) values (%s,%s,%s,%s,%s)',
        (passenger_id, age_type_id, id_place, final_price, int(time.time())))
    connection.commit()
    ticket_id = cursor.lastrowid
    cursor.close()
    connection.close()
    place_update_status(id_place)
    return ticket_id


def get_ticket_info(ticket_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("""
SELECT ticket.id                             as ticket_id,
       ticket.final_price                    as final_price,
       ticket.buy_time                       as buy_time,
       user_data.id                          as user_data_id,
       user_data.last_name                   as user_data_last_name,
       user_data.first_name                  as user_data_first_name,
       user_data.patronymic                  as user_data_patronymic,
       user_data.birthday                    as user_data_birthday,
       user_data.phone                       as user_data_phone,
       user_data.email                       as user_data_email,
       user_data_gender.gender_name          as user_data_gender_name,
       user_data_document_type.document_type as user_data_document_type,
       user_data.document_number             as user_data_document_number,
       user_data.valid_date                  as user_data_valid_date,
       places.place_number         as place_number,
       route.id                    as route_id,
       route.arrival_date          as route_arrival_date,
       route.departure_date        as route_departure_date,
       airports_from.airport_name  as airport_from,
       airports_from.abbreviation  as airport_from_abbr,
       cities_from.city_name       as city_from,
       countries_from.country_name as country_from,
       airports_to.airport_name    as airport_to,
       airports_to.abbreviation    as airport_to_abbr,
       cities_to.city_name         as city_to,
       countries_to.country_name   as country_to,
       airplane.airplane_name      as airplane_name,
       airplane.airplane_num       as airplane_num
FROM ticket
       INNER JOIN places ON places.id = ticket.id_places
       INNER JOIN route ON route.id = places.id_route
       INNER JOIN user_data ON user_data.id = ticket.id_user_data
       INNER JOIN airports airports_from on route.id_airport_where_from = airports_from.id
       INNER JOIN cities cities_from on airports_from.id_city = cities_from.id
       INNER JOIN countries countries_from on airports_from.id_country = countries_from.id
       INNER JOIN airports airports_to on route.id_airport_where_to = airports_to.id
       INNER JOIN cities cities_to on airports_to.id_city = cities_to.id
       INNER JOIN countries countries_to on airports_to.id_country = countries_to.id
       INNER JOIN airplane on route.id_airplane = airplane.id
       INNER JOIN user_data_gender on user_data_gender.id = user_data.id_gender
       INNER JOIN user_data_document_type on user_data_document_type.id = user_data.id_document_type
WHERE ticket.id = %s""", (ticket_id))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


def get_order(user_id):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute("""
SELECT ticket.id                   as ticket_id,
       ticket.final_price          as final_price,
       ticket.buy_time             as buy_time,
       user_data.id                as user_data_id,
       user_data.last_name         as user_data_last_name,
       user_data.first_name        as user_data_first_name,
       user_data.patronymic        as user_data_patronymic,
       places.place_number         as place_number,
       route.arrival_date          as route_arrival_date,
       route.departure_date        as route_departure_date,
       airports_from.airport_name  as airport_from,
       airports_from.abbreviation  as airport_from_abbr,
       cities_from.city_name       as city_from,
       countries_from.country_name as country_from,
       airports_to.airport_name    as airport_to,
       airports_to.abbreviation    as airport_to_abbr,
       cities_to.city_name         as city_to,
       countries_to.country_name   as country_to
FROM ticket
       INNER JOIN places ON places.id = ticket.id_places
       INNER JOIN route ON route.id = places.id_route
       INNER JOIN airports airports_from on route.id_airport_where_from = airports_from.id
       INNER JOIN cities cities_from on airports_from.id_city = cities_from.id
       INNER JOIN countries countries_from on airports_from.id_country = countries_from.id
       INNER JOIN airports airports_to on route.id_airport_where_to = airports_to.id
       INNER JOIN cities cities_to on airports_to.id_city = cities_to.id
       INNER JOIN countries countries_to on airports_to.id_country = countries_to.id
       INNER JOIN users_auth_user_data
                  on users_auth_user_data.id_user = %s and users_auth_user_data.id_user_data = ticket.id_user_data
       INNER JOIN user_data ON user_data.id = users_auth_user_data.id_user_data
ORDER BY ticket.buy_time DESC""", (user_id))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
