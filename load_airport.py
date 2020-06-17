import connect

def cheak_country(country_name):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT id FROM countries WHERE country_name=%s',country_name)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    try:
        return result['id']
    except:
        return None

def add_country(name, abbr):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into countries (country_name, abbreviation) values (%s, %s)', (name, abbr))
    connection.commit()
    country_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return country_id

def get_city_country(city_name):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM cities WHERE city_name=%s', city_name)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    try:
        return result['id']
    except:
        return None

def add_city(country_id, name, abbreviation):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into cities (id_country, city_name, abbreviation) values (%s, %s, %s)', (country_id, name, abbreviation))
    connection.commit()
    city_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return city_id

def get_airport(airport_name):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM airports WHERE airport_name=%s', airport_name)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    try:
        return result['id']
    except:
        return None

def add_airport(country_id, city_id, name, abbr):
    connection = connect.getConnection()
    cursor = connection.cursor()
    cursor.execute(
        'insert into airports (id_country, id_city, airport_name, abbreviation) values (%s, %s, %s, %s)',
        (country_id, city_id, name, abbr))
    connection.commit()
    cursor.close()
    connection.close()

query = {
    "data": {
        "cities": [
            {
                "airports": [
                    {
                        "code": "ABA",
                        "name": "Абакан"
                    }
                ],
                "code": "ABA",
                "country": "RU",
                "country_name": "Россия",
                "name": "Абакан"
            },
            {
                "airports": [
                ],
                "code": "ABZ",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Абердин"
            },
            {
                "airports": [
                ],
                "code": "AGA",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Агадир"
            },
            {
                "airports": [
                ],
                "code": "ADA",
                "country": "TR",
                "country_name": "Турция",
                "name": "Адана"
            },
            {
                "airports": [
                    {
                        "code": "ADL",
                        "name": "Международный аэропорт Аделаиды"
                    }
                ],
                "code": "ADL",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Аделаида"
            },
            {
                "airports": [
                ],
                "code": "ACC",
                "country": "GH",
                "country_name": "Гана",
                "name": "Аккра"
            },
            {
                "airports": [
                    {
                        "code": "SCO",
                        "name": "Aktau Airport"
                    }
                ],
                "code": "SCO",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Актау"
            },
            {
                "airports": [
                    {
                        "code": "AKX",
                        "name": "Международный Аэропорт Актобе"
                    }
                ],
                "code": "AKX",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Актобе"
            },
            {
                "airports": [
                ],
                "code": "AXD",
                "country": "GR",
                "country_name": "Греция",
                "name": "Александруполис"
            },
            {
                "airports": [
                ],
                "code": "ALG",
                "country": "DZ",
                "country_name": "Алжир",
                "name": "Алжир"
            },
            {
                "airports": [
                    {
                        "code": "ALC",
                        "name": "Аликанте"
                    }
                ],
                "code": "ALC",
                "country": "ES",
                "country_name": "Испания",
                "name": "Аликанте"
            },
            {
                "airports": [
                    {
                        "code": "ALA",
                        "name": "Международный аэропорт Алматы"
                    }
                ],
                "code": "ALA",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Алматы"
            },
            {
                "airports": [
                    {
                        "code": "ABQ",
                        "name": "Международный аэропорт Альбукерке"
                    }
                ],
                "code": "ABQ",
                "country": "US",
                "country_name": "США",
                "name": "Альбукерке"
            },
            {
                "airports": [
                ],
                "code": "ATQ",
                "country": "IN",
                "country_name": "Индия",
                "name": "Амритсар"
            },
            {
                "airports": [
                    {
                        "code": "AMS",
                        "name": "Схипхол"
                    }
                ],
                "code": "AMS",
                "country": "NL",
                "country_name": "Нидерланды",
                "name": "Амстердам"
            },
            {
                "airports": [
                ],
                "code": "DYR",
                "country": "RU",
                "country_name": "Россия",
                "name": "Анадырь"
            },
            {
                "airports": [
                    {
                        "code": "AAQ",
                        "name": "Витязево"
                    }
                ],
                "code": "AAQ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Анапа"
            },
            {
                "airports": [
                    {
                        "code": "ANK",
                        "name": "Аэропорт Этимесгут"
                    }
                ],
                "code": "ANK",
                "country": "TR",
                "country_name": "Турция",
                "name": "Анкара"
            },
            {
                "airports": [
                ],
                "code": "AOI",
                "country": "IT",
                "country_name": "Италия",
                "name": "Анкона"
            },
            {
                "airports": [
                    {
                        "code": "AYT",
                        "name": "Анталья"
                    }
                ],
                "code": "AYT",
                "country": "TR",
                "country_name": "Турция",
                "name": "Анталья"
            },
            {
                "airports": [
                ],
                "code": "ANR",
                "country": "BE",
                "country_name": "Бельгия",
                "name": "Антверпен"
            },
            {
                "airports": [
                    {
                        "code": "ARH",
                        "name": "Талаги"
                    }
                ],
                "code": "ARH",
                "country": "RU",
                "country_name": "Россия",
                "name": "Архангельск"
            },
            {
                "airports": [
                    {
                        "code": "ASF",
                        "name": "Астрахань"
                    }
                ],
                "code": "ASF",
                "country": "RU",
                "country_name": "Россия",
                "name": "Астрахань"
            },
            {
                "airports": [
                ],
                "code": "OVD",
                "country": "ES",
                "country_name": "Испания",
                "name": "Астурия"
            },
            {
                "airports": [
                ],
                "code": "ATL",
                "country": "US",
                "country_name": "США",
                "name": "Атланта"
            },
            {
                "airports": [
                    {
                        "code": "GUW",
                        "name": "Атырау"
                    }
                ],
                "code": "GUW",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Атырау"
            },
            {
                "airports": [
                    {
                        "code": "ATH",
                        "name": "Елефтериос Венизелос"
                    }
                ],
                "code": "ATH",
                "country": "GR",
                "country_name": "Греция",
                "name": "Афины"
            },
            {
                "airports": [
                ],
                "code": "AMD",
                "country": "IN",
                "country_name": "Индия",
                "name": "Ахмедабад"
            },
            {
                "airports": [
                ],
                "code": "ASB",
                "country": "TM",
                "country_name": "Туркменистан",
                "name": "Ашхабад"
            },
            {
                "airports": [
                    {
                        "code": "GYD",
                        "name": "Баку"
                    }
                ],
                "code": "BAK",
                "country": "AZ",
                "country_name": "Азербайджан",
                "name": "Баку"
            },
            {
                "airports": [
                    {
                        "code": "BWI",
                        "name": "Международный аэропорт Балтимор-Вашингтон"
                    }
                ],
                "code": "BWI",
                "country": "US",
                "country_name": "США",
                "name": "Балтимор"
            },
            {
                "airports": [
                ],
                "code": "BLR",
                "country": "IN",
                "country_name": "Индия",
                "name": "Бангалор"
            },
            {
                "airports": [
                    {
                        "code": "BKK",
                        "name": "Бангкок"
                    }
                ],
                "code": "BKK",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Бангкок"
            },
            {
                "airports": [
                ],
                "code": "BNX",
                "country": "BA",
                "country_name": "Босния и Герцеговина",
                "name": "Баня-Лука"
            },
            {
                "airports": [
                    {
                        "code": "BAV",
                        "name": "Аэропорт Баотоу"
                    }
                ],
                "code": "BAV",
                "country": "CN",
                "country_name": "Китай",
                "name": "Баотоу"
            },
            {
                "airports": [
                ],
                "code": "BRI",
                "country": "IT",
                "country_name": "Италия",
                "name": "Бари"
            },
            {
                "airports": [
                    {
                        "code": "BAX",
                        "name": "Барнаул"
                    }
                ],
                "code": "BAX",
                "country": "RU",
                "country_name": "Россия",
                "name": "Барнаул"
            },
            {
                "airports": [
                    {
                        "code": "BCN",
                        "name": "Барселона"
                    }
                ],
                "code": "BCN",
                "country": "ES",
                "country_name": "Испания",
                "name": "Барселона"
            },
            {
                "airports": [
                    {
                        "code": "BEY",
                        "name": "Бейрут"
                    }
                ],
                "code": "BEY",
                "country": "LB",
                "country_name": "Ливан",
                "name": "Бейрут"
            },
            {
                "airports": [
                    {
                        "code": "EGO",
                        "name": "Белгород"
                    }
                ],
                "code": "EGO",
                "country": "RU",
                "country_name": "Россия",
                "name": "Белгород"
            },
            {
                "airports": [
                    {
                        "code": "BEG",
                        "name": "Белград"
                    }
                ],
                "code": "BEG",
                "country": "RS",
                "country_name": "Сербия",
                "name": "Белград"
            },
            {
                "airports": [
                ],
                "code": "BFS",
                "country": "IE",
                "country_name": "Ирландия",
                "name": "Белфаст"
            },
            {
                "airports": [
                ],
                "code": "BGO",
                "country": "NO",
                "country_name": "Норвегия",
                "name": "Берген"
            },
            {
                "airports": [
                    {
                        "code": "SXF",
                        "name": "Шенефельд"
                    }
                ],
                "code": "BER",
                "country": "DE",
                "country_name": "Германия",
                "name": "Берлин"
            },
            {
                "airports": [
                ],
                "code": "BTV",
                "country": "US",
                "country_name": "США",
                "name": "Берлингтон"
            },
            {
                "airports": [
                ],
                "code": "BIQ",
                "country": "FR",
                "country_name": "Франция",
                "name": "Биарриц"
            },
            {
                "airports": [
                ],
                "code": "BLL",
                "country": "DK",
                "country_name": "Дания",
                "name": "Биллунн"
            },
            {
                "airports": [
                ],
                "code": "BIO",
                "country": "ES",
                "country_name": "Испания",
                "name": "Бильбао"
            },
            {
                "airports": [
                ],
                "code": "BHX",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Бирмингем"
            },
            {
                "airports": [
                    {
                        "code": "FRU",
                        "name": "Манас"
                    }
                ],
                "code": "FRU",
                "country": "KG",
                "country_name": "Киргизия",
                "name": "Бишкек"
            },
            {
                "airports": [
                ],
                "code": "BQS",
                "country": "RU",
                "country_name": "Россия",
                "name": "Благовещенск"
            },
            {
                "airports": [
                ],
                "code": "BXN",
                "country": "TR",
                "country_name": "Турция",
                "name": "Бодрум"
            },
            {
                "airports": [
                    {
                        "code": "BLQ",
                        "name": "Болонья"
                    }
                ],
                "code": "BLQ",
                "country": "IT",
                "country_name": "Италия",
                "name": "Болонья"
            },
            {
                "airports": [
                ],
                "code": "BOD",
                "country": "FR",
                "country_name": "Франция",
                "name": "Бордо"
            },
            {
                "airports": [
                ],
                "code": "BOS",
                "country": "US",
                "country_name": "США",
                "name": "Бостон"
            },
            {
                "airports": [
                ],
                "code": "BTS",
                "country": "SK",
                "country_name": "Словакия",
                "name": "Братислава"
            },
            {
                "airports": [
                ],
                "code": "BTK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Братск"
            },
            {
                "airports": [
                ],
                "code": "BES",
                "country": "FR",
                "country_name": "Франция",
                "name": "Брест"
            },
            {
                "airports": [
                ],
                "code": "BDS",
                "country": "IT",
                "country_name": "Италия",
                "name": "Бриндизи"
            },
            {
                "airports": [
                ],
                "code": "BNE",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Брисбен"
            },
            {
                "airports": [
                ],
                "code": "BRS",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Бристоль"
            },
            {
                "airports": [
                    {
                        "code": "ZYR",
                        "name": "Брюссель-Южный вокзал, Бельгия"
                    },
                    {
                        "code": "BRU",
                        "name": "Брюссель(Националь)"
                    }
                ],
                "code": "BRU",
                "country": "BE",
                "country_name": "Бельгия",
                "name": "Брюссель"
            },
            {
                "airports": [
                    {
                        "code": "BUD",
                        "name": "Международный аэропорт им. Ференца Листа"
                    }
                ],
                "code": "BUD",
                "country": "HU",
                "country_name": "Венгрия",
                "name": "Будапешт"
            },
            {
                "airports": [
                ],
                "code": "BUR",
                "country": "US",
                "country_name": "США",
                "name": "Бурбанк"
            },
            {
                "airports": [
                    {
                        "code": "BOJ",
                        "name": "Бургас"
                    }
                ],
                "code": "BOJ",
                "country": "BG",
                "country_name": "Болгария",
                "name": "Бургас"
            },
            {
                "airports": [
                    {
                        "code": "PUS",
                        "name": "Международный аэропорт Кимхэ"
                    }
                ],
                "code": "PUS",
                "country": "KR",
                "country_name": "Корея",
                "name": "Бусан"
            },
            {
                "airports": [
                ],
                "code": "BUF",
                "country": "US",
                "country_name": "США",
                "name": "Буффало"
            },
            {
                "airports": [
                    {
                        "code": "BHK",
                        "name": "Бухара"
                    }
                ],
                "code": "BHK",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Бухара"
            },
            {
                "airports": [
                    {
                        "code": "OTP",
                        "name": "Отопени"
                    }
                ],
                "code": "BUH",
                "country": "RO",
                "country_name": "Румыния",
                "name": "Бухарест"
            },
            {
                "airports": [
                    {
                        "code": "EZE",
                        "name": "Международный аэропорт Эсейса"
                    },
                    {
                        "code": "AEP",
                        "name": "Aeroparque J.Newberry"
                    }
                ],
                "code": "BUE",
                "country": "AR",
                "country_name": "Аргентина",
                "name": "Буэнос-Айрес"
            },
            {
                "airports": [
                ],
                "code": "BBI",
                "country": "IN",
                "country_name": "Индия",
                "name": "Бхубанесвар"
            },
            {
                "airports": [
                ],
                "code": "VAA",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Вааса"
            },
            {
                "airports": [
                ],
                "code": "BDQ",
                "country": "IN",
                "country_name": "Индия",
                "name": "Вадодара"
            },
            {
                "airports": [
                ],
                "code": "VLC",
                "country": "ES",
                "country_name": "Испания",
                "name": "Валенсия"
            },
            {
                "airports": [
                    {
                        "code": "VAR",
                        "name": "Варна"
                    }
                ],
                "code": "VAR",
                "country": "BG",
                "country_name": "Болгария",
                "name": "Варна"
            },
            {
                "airports": [
                    {
                        "code": "WAW",
                        "name": "Фредерика Шопена"
                    }
                ],
                "code": "WAW",
                "country": "PL",
                "country_name": "Польша",
                "name": "Варшава"
            },
            {
                "airports": [
                    {
                        "code": "DCA",
                        "name": "Национальный аэропорт Рональд Рейган"
                    },
                    {
                        "code": "IAD",
                        "name": "Даллес"
                    }
                ],
                "code": "WAS",
                "country": "US",
                "country_name": "США",
                "name": "Вашингтон"
            },
            {
                "airports": [
                ],
                "code": "WLG",
                "country": "NZ",
                "country_name": "Новая Зеландия",
                "name": "Веллингтон"
            },
            {
                "airports": [
                    {
                        "code": "VIE",
                        "name": "Швехат"
                    }
                ],
                "code": "VIE",
                "country": "AT",
                "country_name": "Австрия",
                "name": "Вена"
            },
            {
                "airports": [
                    {
                        "code": "VCE",
                        "name": "Аэропорт Венеции имени Марко Поло"
                    }
                ],
                "code": "VCE",
                "country": "IT",
                "country_name": "Италия",
                "name": "Венеция"
            },
            {
                "airports": [
                    {
                        "code": "VRN",
                        "name": "Верона"
                    }
                ],
                "code": "VRN",
                "country": "IT",
                "country_name": "Италия",
                "name": "Верона"
            },
            {
                "airports": [
                    {
                        "code": "PBI",
                        "name": "Международный аэропорт Вест-Палм-Бич"
                    }
                ],
                "code": "PBI",
                "country": "US",
                "country_name": "США",
                "name": "Вест-Палм-Бич"
            },
            {
                "airports": [
                ],
                "code": "VGO",
                "country": "ES",
                "country_name": "Испания",
                "name": "Виго"
            },
            {
                "airports": [
                    {
                        "code": "VNO",
                        "name": "Вильнюс"
                    }
                ],
                "code": "VNO",
                "country": "LT",
                "country_name": "Литва",
                "name": "Вильнюс"
            },
            {
                "airports": [
                ],
                "code": "VTZ",
                "country": "IN",
                "country_name": "Индия",
                "name": "Вишакхапатнам"
            },
            {
                "airports": [
                    {
                        "code": "VVO",
                        "name": "Владивосток"
                    }
                ],
                "code": "VVO",
                "country": "RU",
                "country_name": "Россия",
                "name": "Владивосток"
            },
            {
                "airports": [
                    {
                        "code": "OGZ",
                        "name": "Международный аэропорт Владикавказ"
                    }
                ],
                "code": "OGZ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Владикавказ"
            },
            {
                "airports": [
                    {
                        "code": "VOG",
                        "name": "Волгоград"
                    }
                ],
                "code": "VOG",
                "country": "RU",
                "country_name": "Россия",
                "name": "Волгоград"
            },
            {
                "airports": [
                    {
                        "code": "VOZ",
                        "name": "Чертовицкое"
                    }
                ],
                "code": "VOZ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Воронеж"
            },
            {
                "airports": [
                ],
                "code": "WRO",
                "country": "PL",
                "country_name": "Польша",
                "name": "Вроцлав"
            },
            {
                "airports": [
                    {
                        "code": "WUS",
                        "name": "Аэропорт Вуйшань"
                    }
                ],
                "code": "WUS",
                "country": "CN",
                "country_name": "Китай",
                "name": "Вуйшань"
            },
            {
                "airports": [
                ],
                "code": "VTE",
                "country": "LA",
                "country_name": "Лаос",
                "name": "Вьентьян"
            },
            {
                "airports": [
                ],
                "code": "WEF",
                "country": "CN",
                "country_name": "Китай",
                "name": "Вэйфан"
            },
            {
                "airports": [
                ],
                "code": "WNZ",
                "country": "CN",
                "country_name": "Китай",
                "name": "Вэньчжоу"
            },
            {
                "airports": [
                    {
                        "code": "HAV",
                        "name": "Хосе Марти межд."
                    }
                ],
                "code": "HAV",
                "country": "CU",
                "country_name": "Куба",
                "name": "Гавана"
            },
            {
                "airports": [
                    {
                        "code": "GZT",
                        "name": "Международный аэропорт Газиантеп"
                    }
                ],
                "code": "GZT",
                "country": "TR",
                "country_name": "Турция",
                "name": "Газиантеп"
            },
            {
                "airports": [
                    {
                        "code": "HAM",
                        "name": "Гамбург"
                    }
                ],
                "code": "HAM",
                "country": "DE",
                "country_name": "Германия",
                "name": "Гамбург"
            },
            {
                "airports": [
                    {
                        "code": "HAJ",
                        "name": "Ганновер"
                    }
                ],
                "code": "HAJ",
                "country": "DE",
                "country_name": "Германия",
                "name": "Ганновер"
            },
            {
                "airports": [
                ],
                "code": "KHH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Гаосюн"
            },
            {
                "airports": [
                ],
                "code": "GDN",
                "country": "PL",
                "country_name": "Польша",
                "name": "Гданьск"
            },
            {
                "airports": [
                    {
                        "code": "GDZ",
                        "name": "Геленджик"
                    }
                ],
                "code": "GDZ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Геленджик"
            },
            {
                "airports": [
                ],
                "code": "GOA",
                "country": "IT",
                "country_name": "Италия",
                "name": "Генуя"
            },
            {
                "airports": [
                ],
                "code": "GOT",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Гетеборг"
            },
            {
                "airports": [
                ],
                "code": "GLA",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Глазго"
            },
            {
                "airports": [
                ],
                "code": "GOI",
                "country": "IN",
                "country_name": "Индия",
                "name": "Гоа"
            },
            {
                "airports": [
                    {
                        "code": "OOL",
                        "name": "Аэропорт Голд Кост"
                    }
                ],
                "code": "OOL",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Голд Кост"
            },
            {
                "airports": [
                    {
                        "code": "HKG",
                        "name": "Гонконг"
                    }
                ],
                "code": "HKG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Гонконг"
            },
            {
                "airports": [
                    {
                        "code": "GRV",
                        "name": "Аэропорт Грозный"
                    }
                ],
                "code": "GRV",
                "country": "RU",
                "country_name": "Россия",
                "name": "Грозный"
            },
            {
                "airports": [
                ],
                "code": "GUM",
                "country": "US",
                "country_name": "США",
                "name": "Гуам"
            },
            {
                "airports": [
                    {
                        "code": "CAN",
                        "name": "Байюнь"
                    }
                ],
                "code": "CAN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Гуанчжоу"
            },
            {
                "airports": [
                    {
                        "code": "KWL",
                        "name": "Гуйлинь"
                    }
                ],
                "code": "KWL",
                "country": "CN",
                "country_name": "Китай",
                "name": "Гуйлинь"
            },
            {
                "airports": [
                    {
                        "code": "KWE",
                        "name": "Гуйян Лундунбао"
                    }
                ],
                "code": "KWE",
                "country": "CN",
                "country_name": "Китай",
                "name": "Гуйян"
            },
            {
                "airports": [
                    {
                        "code": "DAB",
                        "name": "Дайтона-Бич"
                    }
                ],
                "code": "DAB",
                "country": "US",
                "country_name": "США",
                "name": "Дайтона-Бич"
            },
            {
                "airports": [
                ],
                "code": "DAC",
                "country": "BD",
                "country_name": "Бангладеш",
                "name": "Дакка"
            },
            {
                "airports": [
                ],
                "code": "DLM",
                "country": "TR",
                "country_name": "Турция",
                "name": "Даламан"
            },
            {
                "airports": [
                ],
                "code": "DLI",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Далат"
            },
            {
                "airports": [
                ],
                "code": "DFW",
                "country": "US",
                "country_name": "США",
                "name": "Даллас"
            },
            {
                "airports": [
                    {
                        "code": "DLC",
                        "name": "Далянь"
                    }
                ],
                "code": "DLC",
                "country": "CN",
                "country_name": "Китай",
                "name": "Далянь"
            },
            {
                "airports": [
                ],
                "code": "DAM",
                "country": "SY",
                "country_name": "Сирия",
                "name": "Дамаск"
            },
            {
                "airports": [
                ],
                "code": "DAD",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Дананг"
            },
            {
                "airports": [
                    {
                        "code": "DRW",
                        "name": "Международный Аэропорт Дарвин"
                    }
                ],
                "code": "DRW",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Дарвин"
            },
            {
                "airports": [
                ],
                "code": "MME",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Дарем Долина Тиса"
            },
            {
                "airports": [
                    {
                        "code": "DEL",
                        "name": "Международный аэропорт Индиры Ганди"
                    }
                ],
                "code": "DEL",
                "country": "IN",
                "country_name": "Индия",
                "name": "Дели"
            },
            {
                "airports": [
                ],
                "code": "DEN",
                "country": "US",
                "country_name": "США",
                "name": "Денвер"
            },
            {
                "airports": [
                    {
                        "code": "DPS",
                        "name": "Международный аэропорт Нгура Рай"
                    }
                ],
                "code": "DPS",
                "country": "ID",
                "country_name": "Индонезия",
                "name": "Денпасар Бали"
            },
            {
                "airports": [
                ],
                "code": "DTT",
                "country": "US",
                "country_name": "США",
                "name": "Детройт"
            },
            {
                "airports": [
                    {
                        "code": "JMU",
                        "name": "Аэропорт Джаймуси"
                    }
                ],
                "code": "JMU",
                "country": "CN",
                "country_name": "Китай",
                "name": "Джаймуси"
            },
            {
                "airports": [
                ],
                "code": "JAI",
                "country": "IN",
                "country_name": "Индия",
                "name": "Джайпур"
            },
            {
                "airports": [
                    {
                        "code": "CGK",
                        "name": "Сукарно"
                    }
                ],
                "code": "JKT",
                "country": "ID",
                "country_name": "Индонезия",
                "name": "Джакарта"
            },
            {
                "airports": [
                ],
                "code": "JED",
                "country": "SA",
                "country_name": "Саудовская Аравия",
                "name": "Джидда"
            },
            {
                "airports": [
                ],
                "code": "JAX",
                "country": "US",
                "country_name": "США",
                "name": "Джэксонвилл"
            },
            {
                "airports": [
                    {
                        "code": "DIY",
                        "name": "Аэропорт Диярбакир"
                    }
                ],
                "code": "DIY",
                "country": "TR",
                "country_name": "Турция",
                "name": "Диярбакир"
            },
            {
                "airports": [
                ],
                "code": "DNK",
                "country": "UA",
                "country_name": "Украина",
                "name": "Днепропетровск"
            },
            {
                "airports": [
                    {
                        "code": "DRS",
                        "name": "Дрезден"
                    }
                ],
                "code": "DRS",
                "country": "DE",
                "country_name": "Германия",
                "name": "Дрезден"
            },
            {
                "airports": [
                    {
                        "code": "DWC",
                        "name": "Международный аэропорт Аль-Мактум"
                    },
                    {
                        "code": "DXB",
                        "name": "Дубай"
                    }
                ],
                "code": "DXB",
                "country": "AE",
                "country_name": "Объединенные Арабские Эмираты",
                "name": "Дубай"
            },
            {
                "airports": [
                    {
                        "code": "DUB",
                        "name": "Дублин"
                    }
                ],
                "code": "DUB",
                "country": "IE",
                "country_name": "Ирландия",
                "name": "Дублин"
            },
            {
                "airports": [
                ],
                "code": "DBV",
                "country": "HR",
                "country_name": "Хорватия",
                "name": "Дубровник"
            },
            {
                "airports": [
                    {
                        "code": "DYU",
                        "name": "Душанбе"
                    }
                ],
                "code": "DYU",
                "country": "TJ",
                "country_name": "Таджикистан",
                "name": "Душанбе"
            },
            {
                "airports": [
                    {
                        "code": "DUS",
                        "name": "Дюссельдорф"
                    }
                ],
                "code": "DUS",
                "country": "DE",
                "country_name": "Германия",
                "name": "Дюссельдорф"
            },
            {
                "airports": [
                    {
                        "code": "SVX",
                        "name": "Кольцово"
                    }
                ],
                "code": "SVX",
                "country": "RU",
                "country_name": "Россия",
                "name": "Екатеринбург"
            },
            {
                "airports": [
                    {
                        "code": "EVN",
                        "name": "Международный аэропорт Звартноц"
                    }
                ],
                "code": "EVN",
                "country": "AM",
                "country_name": "Армения",
                "name": "Ереван"
            },
            {
                "airports": [
                    {
                        "code": "GVA",
                        "name": "Женева"
                    }
                ],
                "code": "GVA",
                "country": "CH",
                "country_name": "Швейцария",
                "name": "Женева"
            },
            {
                "airports": [
                ],
                "code": "ILZ",
                "country": "SK",
                "country_name": "Словакия",
                "name": "Жилина"
            },
            {
                "airports": [
                    {
                        "code": "ZAG",
                        "name": "Загреб"
                    }
                ],
                "code": "ZAG",
                "country": "HR",
                "country_name": "Хорватия",
                "name": "Загреб"
            },
            {
                "airports": [
                ],
                "code": "ZAD",
                "country": "HR",
                "country_name": "Хорватия",
                "name": "Задар"
            },
            {
                "airports": [
                    {
                        "code": "ZSB",
                        "name": "Зальцбург"
                    }
                ],
                "code": "SZG",
                "country": "AT",
                "country_name": "Австрия",
                "name": "Зальцбург"
            },
            {
                "airports": [
                ],
                "code": "IBZ",
                "country": "ES",
                "country_name": "Испания",
                "name": "Ибица"
            },
            {
                "airports": [
                ],
                "code": "IVL",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Ивало"
            },
            {
                "airports": [
                    {
                        "code": "IAA",
                        "name": "Igarka Airport"
                    }
                ],
                "code": "IAA",
                "country": "RU",
                "country_name": "Россия",
                "name": "Игарка"
            },
            {
                "airports": [
                    {
                        "code": "IJK",
                        "name": "Аэропорт Ижевск"
                    }
                ],
                "code": "IJK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ижевск"
            },
            {
                "airports": [
                    {
                        "code": "ADB",
                        "name": "Аэропорт Измир"
                    }
                ],
                "code": "IZM",
                "country": "TR",
                "country_name": "Турция",
                "name": "Измир"
            },
            {
                "airports": [
                    {
                        "code": "IND",
                        "name": "Международный аэропорт Индианаполиса"
                    }
                ],
                "code": "IND",
                "country": "US",
                "country_name": "США",
                "name": "Индианаполис"
            },
            {
                "airports": [
                ],
                "code": "IDR",
                "country": "IN",
                "country_name": "Индия",
                "name": "Индор"
            },
            {
                "airports": [
                    {
                        "code": "IOB",
                        "name": "Инсбрук"
                    },
                    {
                        "code": "INN",
                        "name": "Инсбрук"
                    }
                ],
                "code": "INN",
                "country": "AT",
                "country_name": "Австрия",
                "name": "Инсбрук"
            },
            {
                "airports": [
                ],
                "code": "INC",
                "country": "CN",
                "country_name": "Китай",
                "name": "Иньчуань"
            },
            {
                "airports": [
                    {
                        "code": "HER",
                        "name": "Ираклион"
                    }
                ],
                "code": "HER",
                "country": "GR",
                "country_name": "Греция",
                "name": "Ираклион"
            },
            {
                "airports": [
                    {
                        "code": "IKT",
                        "name": "Иркутск"
                    }
                ],
                "code": "IKT",
                "country": "RU",
                "country_name": "Россия",
                "name": "Иркутск"
            },
            {
                "airports": [
                ],
                "code": "ISB",
                "country": "PK",
                "country_name": "Пакистан",
                "name": "Исламабад"
            },
            {
                "airports": [
                ],
                "code": "YIH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Ичан"
            },
            {
                "airports": [
                ],
                "code": "JOE",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Йоэнсуу"
            },
            {
                "airports": [
                ],
                "code": "KVA",
                "country": "GR",
                "country_name": "Греция",
                "name": "Кавала"
            },
            {
                "airports": [
                    {
                        "code": "KOJ",
                        "name": "Кагошима"
                    }
                ],
                "code": "KOJ",
                "country": "JP",
                "country_name": "Япония",
                "name": "Кагосима"
            },
            {
                "airports": [
                    {
                        "code": "KZN",
                        "name": "Казань"
                    }
                ],
                "code": "KZN",
                "country": "RU",
                "country_name": "Россия",
                "name": "Казань"
            },
            {
                "airports": [
                    {
                        "code": "CAI",
                        "name": "Каир"
                    }
                ],
                "code": "CAI",
                "country": "EG",
                "country_name": "Египет",
                "name": "Каир"
            },
            {
                "airports": [
                ],
                "code": "ASR",
                "country": "TR",
                "country_name": "Турция",
                "name": "Кайсери"
            },
            {
                "airports": [
                    {
                        "code": "KGD",
                        "name": "Храброво"
                    }
                ],
                "code": "KGD",
                "country": "RU",
                "country_name": "Россия",
                "name": "Калининград"
            },
            {
                "airports": [
                ],
                "code": "CAG",
                "country": "IT",
                "country_name": "Италия",
                "name": "Кальяри"
            },
            {
                "airports": [
                ],
                "code": "CBR",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Канберра"
            },
            {
                "airports": [
                ],
                "code": "MCI",
                "country": "US",
                "country_name": "США",
                "name": "Канзас-Сити"
            },
            {
                "airports": [
                    {
                        "code": "CUN",
                        "name": "Канкун"
                    }
                ],
                "code": "CUN",
                "country": "MX",
                "country_name": "Мексика",
                "name": "Канкун"
            },
            {
                "airports": [
                    {
                        "code": "KGF",
                        "name": "Караганда"
                    }
                ],
                "code": "KGF",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Караганда"
            },
            {
                "airports": [
                ],
                "code": "KHI",
                "country": "PK",
                "country_name": "Пакистан",
                "name": "Карачи"
            },
            {
                "airports": [
                ],
                "code": "CWL",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Кардифф"
            },
            {
                "airports": [
                    {
                        "code": "KLV",
                        "name": "Карловы Вары"
                    }
                ],
                "code": "KLV",
                "country": "CZ",
                "country_name": "Чехия",
                "name": "Карловы Вары"
            },
            {
                "airports": [
                    {
                        "code": "KSQ",
                        "name": "Карши-Ханабад"
                    }
                ],
                "code": "KSQ",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Карши"
            },
            {
                "airports": [
                ],
                "code": "CAS",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Касабланка"
            },
            {
                "airports": [
                ],
                "code": "CTA",
                "country": "IT",
                "country_name": "Италия",
                "name": "Катания"
            },
            {
                "airports": [
                ],
                "code": "KTM",
                "country": "NP",
                "country_name": "Непал",
                "name": "Катманду"
            },
            {
                "airports": [
                ],
                "code": "KTW",
                "country": "PL",
                "country_name": "Польша",
                "name": "Катовице"
            },
            {
                "airports": [
                    {
                        "code": "KUN",
                        "name": "Каунас"
                    }
                ],
                "code": "KUN",
                "country": "LT",
                "country_name": "Литва",
                "name": "Каунас"
            },
            {
                "airports": [
                    {
                        "code": "KEJ",
                        "name": "Кемерово"
                    }
                ],
                "code": "KEJ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Кемерово"
            },
            {
                "airports": [
                    {
                        "code": "CNS",
                        "name": "Международный аэропорт Кэрнс"
                    }
                ],
                "code": "CNS",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Кернс"
            },
            {
                "airports": [
                ],
                "code": "EFL",
                "country": "GR",
                "country_name": "Греция",
                "name": "Кефалония"
            },
            {
                "airports": [
                ],
                "code": "IEV",
                "country": "UA",
                "country_name": "Украина",
                "name": "Киев"
            },
            {
                "airports": [
                ],
                "code": "KRN",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Кируна"
            },
            {
                "airports": [
                ],
                "code": "KTT",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Киттиля"
            },
            {
                "airports": [
                    {
                        "code": "KIV",
                        "name": "Кишинев"
                    }
                ],
                "code": "KIV",
                "country": "MD",
                "country_name": "Молдова",
                "name": "Кишинев"
            },
            {
                "airports": [
                ],
                "code": "KLU",
                "country": "AT",
                "country_name": "Австрия",
                "name": "Клагенфурт"
            },
            {
                "airports": [
                ],
                "code": "CFE",
                "country": "FR",
                "country_name": "Франция",
                "name": "Клермон-Ферран"
            },
            {
                "airports": [
                ],
                "code": "CLE",
                "country": "US",
                "country_name": "США",
                "name": "Кливленд"
            },
            {
                "airports": [
                ],
                "code": "CJB",
                "country": "IN",
                "country_name": "Индия",
                "name": "Коимбаторе"
            },
            {
                "airports": [
                ],
                "code": "CCU",
                "country": "IN",
                "country_name": "Индия",
                "name": "Колката"
            },
            {
                "airports": [
                    {
                        "code": "CMB",
                        "name": "Бандаранаике"
                    }
                ],
                "code": "CMB",
                "country": "LK",
                "country_name": "Шри-Ланка",
                "name": "Коломбо"
            },
            {
                "airports": [
                    {
                        "code": "KMQ",
                        "name": "Аэропорт Коматсу"
                    }
                ],
                "code": "KMQ",
                "country": "JP",
                "country_name": "Япония",
                "name": "Коматсу"
            },
            {
                "airports": [
                ],
                "code": "KXK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Комсомольск-на-Амуре"
            },
            {
                "airports": [
                    {
                        "code": "CPH",
                        "name": "Каструп"
                    }
                ],
                "code": "CPH",
                "country": "DK",
                "country_name": "Дания",
                "name": "Копенгаген"
            },
            {
                "airports": [
                ],
                "code": "CFU",
                "country": "GR",
                "country_name": "Греция",
                "name": "Корфу"
            },
            {
                "airports": [
                ],
                "code": "KGS",
                "country": "GR",
                "country_name": "Греция",
                "name": "Кос"
            },
            {
                "airports": [
                    {
                        "code": "KSN",
                        "name": "Кустанай"
                    }
                ],
                "code": "KSN",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Костанай"
            },
            {
                "airports": [
                    {
                        "code": "USM",
                        "name": "Кох Самуи"
                    }
                ],
                "code": "USM",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Кох Самуи"
            },
            {
                "airports": [
                ],
                "code": "COK",
                "country": "IN",
                "country_name": "Индия",
                "name": "Кочин"
            },
            {
                "airports": [
                ],
                "code": "KSC",
                "country": "SK",
                "country_name": "Словакия",
                "name": "Кошице"
            },
            {
                "airports": [
                ],
                "code": "KBV",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Краби"
            },
            {
                "airports": [
                ],
                "code": "CHC",
                "country": "NZ",
                "country_name": "Новая Зеландия",
                "name": "Крайстчерч"
            },
            {
                "airports": [
                ],
                "code": "KRK",
                "country": "PL",
                "country_name": "Польша",
                "name": "Краков"
            },
            {
                "airports": [
                    {
                        "code": "KRR",
                        "name": "Пашковский"
                    }
                ],
                "code": "KRR",
                "country": "RU",
                "country_name": "Россия",
                "name": "Краснодар"
            },
            {
                "airports": [
                    {
                        "code": "KJA",
                        "name": "Емельяново"
                    }
                ],
                "code": "KJA",
                "country": "RU",
                "country_name": "Россия",
                "name": "Красноярск"
            },
            {
                "airports": [
                ],
                "code": "KRS",
                "country": "NO",
                "country_name": "Норвегия",
                "name": "Кристиансанн"
            },
            {
                "airports": [
                ],
                "code": "KUL",
                "country": "MY",
                "country_name": "Малайзия",
                "name": "Куала-Лампур"
            },
            {
                "airports": [
                ],
                "code": "ZQN",
                "country": "NZ",
                "country_name": "Новая Зеландия",
                "name": "Куинстаун"
            },
            {
                "airports": [
                    {
                        "code": "KMG",
                        "name": "Куньмин Чаньшу"
                    }
                ],
                "code": "KMG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Куньмин"
            },
            {
                "airports": [
                ],
                "code": "KUO",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Куопио"
            },
            {
                "airports": [
                ],
                "code": "KAO",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Куусамо"
            },
            {
                "airports": [
                    {
                        "code": "KZO",
                        "name": "Аэропорт Кызылорда"
                    }
                ],
                "code": "KZO",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Кызылорда"
            },
            {
                "airports": [
                    {
                        "code": "QKL",
                        "name": "Центральный вокзал Кёльна"
                    }
                ],
                "code": "QKL",
                "country": "DE",
                "country_name": "Германия",
                "name": "Кёльн"
            },
            {
                "airports": [
                ],
                "code": "LCG",
                "country": "ES",
                "country_name": "Испания",
                "name": "Ла Корунья"
            },
            {
                "airports": [
                    {
                        "code": "LPT",
                        "name": "Лампанг"
                    }
                ],
                "code": "LPT",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Лампанг"
            },
            {
                "airports": [
                ],
                "code": "ACE",
                "country": "ES",
                "country_name": "Испания",
                "name": "Ланцароте"
            },
            {
                "airports": [
                    {
                        "code": "LHW",
                        "name": "Аэропорт Ланчжоу"
                    }
                ],
                "code": "LHW",
                "country": "CN",
                "country_name": "Китай",
                "name": "Ланчжоу"
            },
            {
                "airports": [
                    {
                        "code": "LCA",
                        "name": "Ларнака"
                    }
                ],
                "code": "LCA",
                "country": "CY",
                "country_name": "Кипр",
                "name": "Ларнака"
            },
            {
                "airports": [
                ],
                "code": "LAS",
                "country": "US",
                "country_name": "США",
                "name": "Лас-Вегас"
            },
            {
                "airports": [
                ],
                "code": "LPA",
                "country": "ES",
                "country_name": "Испания",
                "name": "Лас-Пальмас-де-Гран-Канария"
            },
            {
                "airports": [
                ],
                "code": "SUF",
                "country": "IT",
                "country_name": "Италия",
                "name": "Лемезиа Терме"
            },
            {
                "airports": [
                ],
                "code": "LXS",
                "country": "GR",
                "country_name": "Греция",
                "name": "Лемнос"
            },
            {
                "airports": [
                ],
                "code": "LBA",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Лидс"
            },
            {
                "airports": [
                    {
                        "code": "XDB",
                        "name": "Аэропорт Лилль-Европейский вокзал"
                    }
                ],
                "code": "XDB",
                "country": "FR",
                "country_name": "Франция",
                "name": "Лилль"
            },
            {
                "airports": [
                    {
                        "code": "LYS",
                        "name": "Сент Экзюпери"
                    }
                ],
                "code": "LYS",
                "country": "FR",
                "country_name": "Франция",
                "name": "Лион"
            },
            {
                "airports": [
                    {
                        "code": "LIS",
                        "name": "Лиссабон"
                    }
                ],
                "code": "LIS",
                "country": "PT",
                "country_name": "Португалия",
                "name": "Лиссабон"
            },
            {
                "airports": [
                ],
                "code": "LGB",
                "country": "US",
                "country_name": "США",
                "name": "Лонг-Бич"
            },
            {
                "airports": [
                    {
                        "code": "STN",
                        "name": "Стенстед"
                    },
                    {
                        "code": "LHR",
                        "name": "Хитроу"
                    },
                    {
                        "code": "LGW",
                        "name": "Гатвик"
                    }
                ],
                "code": "LON",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Лондон"
            },
            {
                "airports": [
                    {
                        "code": "LST",
                        "name": "Аэропорт Лонсестон"
                    }
                ],
                "code": "LST",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Лонсестон"
            },
            {
                "airports": [
                    {
                        "code": "LAX",
                        "name": "Лос-Анджелес"
                    }
                ],
                "code": "LAX",
                "country": "US",
                "country_name": "США",
                "name": "Лос-Анджелес"
            },
            {
                "airports": [
                ],
                "code": "LPQ",
                "country": "LA",
                "country_name": "Лаос",
                "name": "Луанг Прабанг"
            },
            {
                "airports": [
                ],
                "code": "LLA",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Лулео"
            },
            {
                "airports": [
                    {
                        "code": "LXA",
                        "name": "Аэропорт Лхаса Гонггар"
                    }
                ],
                "code": "LXA",
                "country": "CN",
                "country_name": "Китай",
                "name": "Лхаса"
            },
            {
                "airports": [
                    {
                        "code": "LJU",
                        "name": "Любляна"
                    }
                ],
                "code": "LJU",
                "country": "SI",
                "country_name": "Словения",
                "name": "Любляна"
            },
            {
                "airports": [
                ],
                "code": "LUX",
                "country": "LU",
                "country_name": "Люксембург",
                "name": "Люксембург"
            },
            {
                "airports": [
                    {
                        "code": "MRU",
                        "name": "Международный аэропорт имени сэра Сивусагура Рамгулама, Маврикий"
                    }
                ],
                "code": "MRU",
                "country": "MU",
                "country_name": "Маврикий",
                "name": "Маврикий"
            },
            {
                "airports": [
                    {
                        "code": "GDX",
                        "name": "Магадан(Сокол)"
                    }
                ],
                "code": "GDX",
                "country": "RU",
                "country_name": "Россия",
                "name": "Магадан"
            },
            {
                "airports": [
                    {
                        "code": "IGT",
                        "name": "Аэропорт Магас"
                    }
                ],
                "code": "IGT",
                "country": "RU",
                "country_name": "Россия",
                "name": "Магас"
            },
            {
                "airports": [
                    {
                        "code": "MQF",
                        "name": "Магнитогорск"
                    }
                ],
                "code": "MQF",
                "country": "RU",
                "country_name": "Россия",
                "name": "Магнитогорск"
            },
            {
                "airports": [
                    {
                        "code": "MAD",
                        "name": "Барахас"
                    }
                ],
                "code": "MAD",
                "country": "ES",
                "country_name": "Испания",
                "name": "Мадрид"
            },
            {
                "airports": [
                    {
                        "code": "MIA",
                        "name": "Майами"
                    }
                ],
                "code": "MIA",
                "country": "US",
                "country_name": "США",
                "name": "Майами"
            },
            {
                "airports": [
                    {
                        "code": "AGP",
                        "name": "Малага"
                    }
                ],
                "code": "AGP",
                "country": "ES",
                "country_name": "Испания",
                "name": "Малага"
            },
            {
                "airports": [
                    {
                        "code": "MLX",
                        "name": "Аэропорт Малатия"
                    }
                ],
                "code": "MLX",
                "country": "TR",
                "country_name": "Турция",
                "name": "Малатия"
            },
            {
                "airports": [
                    {
                        "code": "MLE",
                        "name": "Мале"
                    }
                ],
                "code": "MLE",
                "country": "MV",
                "country_name": "Мальдивы",
                "name": "Мале"
            },
            {
                "airports": [
                ],
                "code": "MMX",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Мальмё"
            },
            {
                "airports": [
                ],
                "code": "MLA",
                "country": "MT",
                "country_name": "Мальта",
                "name": "Мальта"
            },
            {
                "airports": [
                ],
                "code": "MDL",
                "country": "MM",
                "country_name": "Мьянма",
                "name": "Мандалай"
            },
            {
                "airports": [
                ],
                "code": "MNL",
                "country": "PH",
                "country_name": "Филиппины",
                "name": "Манила"
            },
            {
                "airports": [
                ],
                "code": "MAN",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Манчестер"
            },
            {
                "airports": [
                ],
                "code": "NZH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Маньчжурия"
            },
            {
                "airports": [
                ],
                "code": "RAK",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Марракеш"
            },
            {
                "airports": [
                    {
                        "code": "MRS",
                        "name": "Марсель"
                    }
                ],
                "code": "MRS",
                "country": "FR",
                "country_name": "Франция",
                "name": "Марсель"
            },
            {
                "airports": [
                ],
                "code": "MVY",
                "country": "US",
                "country_name": "США",
                "name": "Мартас-Винъярд"
            },
            {
                "airports": [
                    {
                        "code": "MCX",
                        "name": "Махачкала"
                    }
                ],
                "code": "MCX",
                "country": "RU",
                "country_name": "Россия",
                "name": "Махачкала"
            },
            {
                "airports": [
                ],
                "code": "MEL",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Мельбурн"
            },
            {
                "airports": [
                ],
                "code": "MEM",
                "country": "US",
                "country_name": "США",
                "name": "Мемфис"
            },
            {
                "airports": [
                ],
                "code": "MAH",
                "country": "ES",
                "country_name": "Испания",
                "name": "Менорка"
            },
            {
                "airports": [
                ],
                "code": "MEX",
                "country": "MX",
                "country_name": "Мексика",
                "name": "Мехико"
            },
            {
                "airports": [
                ],
                "code": "JMK",
                "country": "GR",
                "country_name": "Греция",
                "name": "Миконос"
            },
            {
                "airports": [
                    {
                        "code": "MXP",
                        "name": "Малпенса"
                    }
                ],
                "code": "MIL",
                "country": "IT",
                "country_name": "Италия",
                "name": "Милан"
            },
            {
                "airports": [
                    {
                        "code": "MRV",
                        "name": "Минеральные Воды"
                    }
                ],
                "code": "MRV",
                "country": "RU",
                "country_name": "Россия",
                "name": "Минеральные Воды"
            },
            {
                "airports": [
                ],
                "code": "MSP",
                "country": "US",
                "country_name": "США",
                "name": "Миннеаполис"
            },
            {
                "airports": [
                    {
                        "code": "MSQ",
                        "name": "Минск-2"
                    }
                ],
                "code": "MSQ",
                "country": "BY",
                "country_name": "Беларусь",
                "name": "Минск"
            },
            {
                "airports": [
                ],
                "code": "MJT",
                "country": "GR",
                "country_name": "Греция",
                "name": "Митилини"
            },
            {
                "airports": [
                    {
                        "code": "MIR",
                        "name": "Monastir Habib Bourguiba International Airport, Monastir, Tunicia"
                    }
                ],
                "code": "MIR",
                "country": "TN",
                "country_name": "Тунис",
                "name": "Монастир"
            },
            {
                "airports": [
                ],
                "code": "MPL",
                "country": "FR",
                "country_name": "Франция",
                "name": "Монпелье"
            },
            {
                "airports": [
                    {
                        "code": "YUL",
                        "name": "Международный эропорт Монреаль Пьер Трюдо"
                    }
                ],
                "code": "YMQ",
                "country": "CA",
                "country_name": "Канада",
                "name": "Монреаль"
            },
            {
                "airports": [
                ],
                "code": "MTY",
                "country": "MX",
                "country_name": "Мексика",
                "name": "Монтеррей"
            },
            {
                "airports": [
                    {
                        "code": "DME",
                        "name": "Домодедово"
                    },
                    {
                        "code": "SVO",
                        "name": "Шереметьево"
                    },
                    {
                        "code": "VKO",
                        "name": "Внуково"
                    }
                ],
                "code": "MOW",
                "country": "RU",
                "country_name": "Россия",
                "name": "Москва"
            },
            {
                "airports": [
                    {
                        "code": "BOM",
                        "name": "Международный аэропорт Чатрапати Шиваджи"
                    }
                ],
                "code": "BOM",
                "country": "IN",
                "country_name": "Индия",
                "name": "Мумбай"
            },
            {
                "airports": [
                    {
                        "code": "MMK",
                        "name": "Мурманск"
                    }
                ],
                "code": "MMK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Мурманск"
            },
            {
                "airports": [
                    {
                        "code": "MUC",
                        "name": "Мюнхен"
                    }
                ],
                "code": "MUC",
                "country": "DE",
                "country_name": "Германия",
                "name": "Мюнхен"
            },
            {
                "airports": [
                    {
                        "code": "NVI",
                        "name": "Навои"
                    }
                ],
                "code": "NVI",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Навои"
            },
            {
                "airports": [
                ],
                "code": "NGO",
                "country": "JP",
                "country_name": "Япония",
                "name": "Нагоя"
            },
            {
                "airports": [
                ],
                "code": "NDR",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Надор"
            },
            {
                "airports": [
                ],
                "code": "NBO",
                "country": "KE",
                "country_name": "Кения",
                "name": "Найроби"
            },
            {
                "airports": [
                    {
                        "code": "NAL",
                        "name": "Международный аэропорт Нальчик"
                    }
                ],
                "code": "NAL",
                "country": "RU",
                "country_name": "Россия",
                "name": "Нальчик"
            },
            {
                "airports": [
                    {
                        "code": "NMA",
                        "name": "Наманган"
                    }
                ],
                "code": "NMA",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Наманган"
            },
            {
                "airports": [
                    {
                        "code": "NKG",
                        "name": "Международный аэропорт Нанкин Лукоу"
                    }
                ],
                "code": "NKG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Нанкин"
            },
            {
                "airports": [
                ],
                "code": "NTE",
                "country": "FR",
                "country_name": "Франция",
                "name": "Нант"
            },
            {
                "airports": [
                    {
                        "code": "ACK",
                        "name": "Аэропорт Нантакет"
                    }
                ],
                "code": "ACK",
                "country": "US",
                "country_name": "США",
                "name": "Нантакет"
            },
            {
                "airports": [
                ],
                "code": "NNG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Наньнин"
            },
            {
                "airports": [
                    {
                        "code": "KHN",
                        "name": "Наньчан Чанбэй"
                    }
                ],
                "code": "KHN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Наньчан"
            },
            {
                "airports": [
                ],
                "code": "NNM",
                "country": "RU",
                "country_name": "Россия",
                "name": "Нарьян-Мар"
            },
            {
                "airports": [
                    {
                        "code": "NAP",
                        "name": "Неаполь"
                    }
                ],
                "code": "NAP",
                "country": "IT",
                "country_name": "Италия",
                "name": "Неаполь"
            },
            {
                "airports": [
                    {
                        "code": "NYT",
                        "name": "Международный аэропорт Нейпьидо"
                    }
                ],
                "code": "NYT",
                "country": "MM",
                "country_name": "Мьянма",
                "name": "Нейпьидо"
            },
            {
                "airports": [
                    {
                        "code": "QYG",
                        "name": "Немецкие железные дороги"
                    }
                ],
                "code": "QYG",
                "country": "DE",
                "country_name": "Германия",
                "name": "Немецкие железные дороги"
            },
            {
                "airports": [
                ],
                "code": "NER",
                "country": "RU",
                "country_name": "Россия",
                "name": "Нерюнгри"
            },
            {
                "airports": [
                    {
                        "code": "NJC",
                        "name": "Нижневартовск"
                    }
                ],
                "code": "NJC",
                "country": "RU",
                "country_name": "Россия",
                "name": "Нижневартовск"
            },
            {
                "airports": [
                    {
                        "code": "NBC",
                        "name": "Аэропорт Бегишево"
                    }
                ],
                "code": "NBC",
                "country": "RU",
                "country_name": "Россия",
                "name": "Нижнекамск (Набережные Челны)"
            },
            {
                "airports": [
                    {
                        "code": "GOJ",
                        "name": "Стригино"
                    }
                ],
                "code": "GOJ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Нижний Новгород"
            },
            {
                "airports": [
                ],
                "code": "KIJ",
                "country": "JP",
                "country_name": "Япония",
                "name": "Ниигата"
            },
            {
                "airports": [
                    {
                        "code": "NLI",
                        "name": "Аэропорт Николаевск-на-Амуре"
                    }
                ],
                "code": "NLI",
                "country": "RU",
                "country_name": "Россия",
                "name": "Николаевск-на-Амуре"
            },
            {
                "airports": [
                ],
                "code": "NGB",
                "country": "CN",
                "country_name": "Китай",
                "name": "Нинбо"
            },
            {
                "airports": [
                    {
                        "code": "NCE",
                        "name": "Ницца"
                    }
                ],
                "code": "NCE",
                "country": "FR",
                "country_name": "Франция",
                "name": "Ницца"
            },
            {
                "airports": [
                ],
                "code": "XYK",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Но́ррчёпинг"
            },
            {
                "airports": [
                    {
                        "code": "NOZ",
                        "name": "Новокузнецк-Спиченково"
                    }
                ],
                "code": "NOZ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Новокузнецк"
            },
            {
                "airports": [
                    {
                        "code": "OVB",
                        "name": "Толмачево"
                    }
                ],
                "code": "OVB",
                "country": "RU",
                "country_name": "Россия",
                "name": "Новосибирск"
            },
            {
                "airports": [
                ],
                "code": "MSY",
                "country": "US",
                "country_name": "США",
                "name": "Новый Орлеан"
            },
            {
                "airports": [
                    {
                        "code": "NUX",
                        "name": "Новый Уренгой"
                    }
                ],
                "code": "NUX",
                "country": "RU",
                "country_name": "Россия",
                "name": "Новый Уренгой"
            },
            {
                "airports": [
                ],
                "code": "NGK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ноглики"
            },
            {
                "airports": [
                ],
                "code": "NWI",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Норидж"
            },
            {
                "airports": [
                ],
                "code": "NSK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Норильск"
            },
            {
                "airports": [
                ],
                "code": "NOU",
                "country": "NC",
                "country_name": "Новая Каледония",
                "name": "Нумеа"
            },
            {
                "airports": [
                    {
                        "code": "TSE",
                        "name": "Нур-Султан"
                    }
                ],
                "code": "TSE",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Нур-Султан"
            },
            {
                "airports": [
                    {
                        "code": "JFK",
                        "name": "Кеннеди"
                    },
                    {
                        "code": "LGA",
                        "name": "Аэропорт Ла Гуардия"
                    }
                ],
                "code": "NYC",
                "country": "US",
                "country_name": "США",
                "name": "Нью-Йорк"
            },
            {
                "airports": [
                ],
                "code": "NCL",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Ньюкасл"
            },
            {
                "airports": [
                    {
                        "code": "CXR",
                        "name": "Международный аэропорт Камрань"
                    }
                ],
                "code": "NHA",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Нячанг"
            },
            {
                "airports": [
                ],
                "code": "OBO",
                "country": "JP",
                "country_name": "Япония",
                "name": "Обихиро"
            },
            {
                "airports": [
                ],
                "code": "ODS",
                "country": "UA",
                "country_name": "Украина",
                "name": "Одесса"
            },
            {
                "airports": [
                    {
                        "code": "OKJ",
                        "name": "Аэропорт Окаяма"
                    }
                ],
                "code": "OKJ",
                "country": "JP",
                "country_name": "Япония",
                "name": "Окаяма"
            },
            {
                "airports": [
                ],
                "code": "OKA",
                "country": "JP",
                "country_name": "Япония",
                "name": "Окинава"
            },
            {
                "airports": [
                ],
                "code": "AKL",
                "country": "NZ",
                "country_name": "Новая Зеландия",
                "name": "Окленд"
            },
            {
                "airports": [
                ],
                "code": "OAK",
                "country": "US",
                "country_name": "США",
                "name": "Окленд"
            },
            {
                "airports": [
                ],
                "code": "AES",
                "country": "NO",
                "country_name": "Норвегия",
                "name": "Олесунн"
            },
            {
                "airports": [
                ],
                "code": "OLB",
                "country": "IT",
                "country_name": "Италия",
                "name": "Ольбия"
            },
            {
                "airports": [
                ],
                "code": "AAL",
                "country": "DK",
                "country_name": "Дания",
                "name": "Ольборг"
            },
            {
                "airports": [
                    {
                        "code": "OMS",
                        "name": "Омск"
                    }
                ],
                "code": "OMS",
                "country": "RU",
                "country_name": "Россия",
                "name": "Омск"
            },
            {
                "airports": [
                    {
                        "code": "REN",
                        "name": "Оренбург"
                    }
                ],
                "code": "REN",
                "country": "RU",
                "country_name": "Россия",
                "name": "Оренбург"
            },
            {
                "airports": [
                    {
                        "code": "MCO",
                        "name": "Орландо"
                    },
                    {
                        "code": "ORL",
                        "name": "Orlando Executive"
                    }
                ],
                "code": "ORL",
                "country": "US",
                "country_name": "США",
                "name": "Орландо"
            },
            {
                "airports": [
                    {
                        "code": "OSW",
                        "name": "Аэропорт Орск"
                    }
                ],
                "code": "OSW",
                "country": "RU",
                "country_name": "Россия",
                "name": "Орск"
            },
            {
                "airports": [
                ],
                "code": "AAR",
                "country": "DK",
                "country_name": "Дания",
                "name": "Орхус"
            },
            {
                "airports": [
                    {
                        "code": "KIX",
                        "name": "Осака-Кансай"
                    }
                ],
                "code": "OSA",
                "country": "JP",
                "country_name": "Япония",
                "name": "Осака"
            },
            {
                "airports": [
                    {
                        "code": "OSL",
                        "name": "Аэропорт Осло Гардермуэн"
                    }
                ],
                "code": "OSL",
                "country": "NO",
                "country_name": "Норвегия",
                "name": "Осло"
            },
            {
                "airports": [
                    {
                        "code": "AUS",
                        "name": "Международный аэропорт Остин Бергстром"
                    }
                ],
                "code": "AUS",
                "country": "US",
                "country_name": "США",
                "name": "Остин"
            },
            {
                "airports": [
                ],
                "code": "OSR",
                "country": "CZ",
                "country_name": "Чехия",
                "name": "Острава"
            },
            {
                "airports": [
                ],
                "code": "ITU",
                "country": "RU",
                "country_name": "Россия",
                "name": "Остров Итуруп"
            },
            {
                "airports": [
                ],
                "code": "OUL",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Оулу"
            },
            {
                "airports": [
                ],
                "code": "OHH",
                "country": "RU",
                "country_name": "Россия",
                "name": "Оха"
            },
            {
                "airports": [
                    {
                        "code": "OSS",
                        "name": "Ош"
                    }
                ],
                "code": "OSS",
                "country": "KG",
                "country_name": "Киргизия",
                "name": "Ош"
            },
            {
                "airports": [
                    {
                        "code": "PWQ",
                        "name": "Павлодар"
                    }
                ],
                "code": "PWQ",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Павлодар"
            },
            {
                "airports": [
                ],
                "code": "PLQ",
                "country": "LT",
                "country_name": "Литва",
                "name": "Паланга"
            },
            {
                "airports": [
                ],
                "code": "PMO",
                "country": "IT",
                "country_name": "Италия",
                "name": "Палермо"
            },
            {
                "airports": [
                    {
                        "code": "PMI",
                        "name": "Пальма-де-Мальорка"
                    }
                ],
                "code": "PMI",
                "country": "ES",
                "country_name": "Испания",
                "name": "Пальма-де-Мальорка"
            },
            {
                "airports": [
                ],
                "code": "PTY",
                "country": "PA",
                "country_name": "Панама",
                "name": "Панама Сити"
            },
            {
                "airports": [
                    {
                        "code": "ORY",
                        "name": "Орли"
                    },
                    {
                        "code": "CDG",
                        "name": "Шарль-де-Голль"
                    }
                ],
                "code": "PAR",
                "country": "FR",
                "country_name": "Франция",
                "name": "Париж"
            },
            {
                "airports": [
                ],
                "code": "PFO",
                "country": "CY",
                "country_name": "Кипр",
                "name": "Пафос"
            },
            {
                "airports": [
                    {
                        "code": "PKX",
                        "name": "Аэропорт Пекин Дасин"
                    },
                    {
                        "code": "PEK",
                        "name": "Пекин Столичный"
                    }
                ],
                "code": "BJS",
                "country": "CN",
                "country_name": "Китай",
                "name": "Пекин"
            },
            {
                "airports": [
                ],
                "code": "PEZ",
                "country": "RU",
                "country_name": "Россия",
                "name": "Пенза"
            },
            {
                "airports": [
                    {
                        "code": "PEE",
                        "name": "Большое Савино"
                    }
                ],
                "code": "PEE",
                "country": "RU",
                "country_name": "Россия",
                "name": "Пермь"
            },
            {
                "airports": [
                    {
                        "code": "PER",
                        "name": "Аэропорт Перт"
                    }
                ],
                "code": "PER",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Перт"
            },
            {
                "airports": [
                ],
                "code": "PEG",
                "country": "IT",
                "country_name": "Италия",
                "name": "Перуджа"
            },
            {
                "airports": [
                ],
                "code": "PSR",
                "country": "IT",
                "country_name": "Италия",
                "name": "Пескара"
            },
            {
                "airports": [
                    {
                        "code": "PKC",
                        "name": "Елизово"
                    }
                ],
                "code": "PKC",
                "country": "RU",
                "country_name": "Россия",
                "name": "Петропавловск-Камчатский"
            },
            {
                "airports": [
                ],
                "code": "PSA",
                "country": "IT",
                "country_name": "Италия",
                "name": "Пиза"
            },
            {
                "airports": [
                ],
                "code": "PIT",
                "country": "US",
                "country_name": "США",
                "name": "Питтсбург"
            },
            {
                "airports": [
                ],
                "code": "PNH",
                "country": "KH",
                "country_name": "Камбоджа",
                "name": "Пномпень"
            },
            {
                "airports": [
                ],
                "code": "PUF",
                "country": "FR",
                "country_name": "Франция",
                "name": "По"
            },
            {
                "airports": [
                ],
                "code": "TGD",
                "country": "ME",
                "country_name": "Черногория",
                "name": "Подгорица"
            },
            {
                "airports": [
                ],
                "code": "POZ",
                "country": "PL",
                "country_name": "Польша",
                "name": "Познань"
            },
            {
                "airports": [
                ],
                "code": "PDL",
                "country": "PT",
                "country_name": "Португалия",
                "name": "Понта-Делгада"
            },
            {
                "airports": [
                    {
                        "code": "PWM",
                        "name": "Международный аэропорт Портленд"
                    }
                ],
                "code": "PWM",
                "country": "US",
                "country_name": "США",
                "name": "Портленд"
            },
            {
                "airports": [
                ],
                "code": "PDX",
                "country": "US",
                "country_name": "США",
                "name": "Портленд"
            },
            {
                "airports": [
                ],
                "code": "OPO",
                "country": "PT",
                "country_name": "Португалия",
                "name": "Порту"
            },
            {
                "airports": [
                    {
                        "code": "PRG",
                        "name": "Аэропорт Вацлава Гавела"
                    }
                ],
                "code": "PRG",
                "country": "CZ",
                "country_name": "Чехия",
                "name": "Прага"
            },
            {
                "airports": [
                ],
                "code": "PRN",
                "country": "RS",
                "country_name": "Сербия",
                "name": "Приштина"
            },
            {
                "airports": [
                    {
                        "code": "PUY",
                        "name": "Пула"
                    }
                ],
                "code": "PUY",
                "country": "HR",
                "country_name": "Хорватия",
                "name": "Пула"
            },
            {
                "airports": [
                ],
                "code": "PNQ",
                "country": "IN",
                "country_name": "Индия",
                "name": "Пуна"
            },
            {
                "airports": [
                    {
                        "code": "PUJ",
                        "name": "Международный аэропорт Пунта Кана"
                    }
                ],
                "code": "PUJ",
                "country": "DO",
                "country_name": "Доминиканская Республика",
                "name": "Пунта-Кана"
            },
            {
                "airports": [
                    {
                        "code": "HKT",
                        "name": "Пхукет"
                    }
                ],
                "code": "HKT",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Пхукет"
            },
            {
                "airports": [
                ],
                "code": "REG",
                "country": "IT",
                "country_name": "Италия",
                "name": "Реггио Калабриа"
            },
            {
                "airports": [
                    {
                        "code": "KEF",
                        "name": "Кефлавик"
                    }
                ],
                "code": "REK",
                "country": "IS",
                "country_name": "Исландия",
                "name": "Рейкьявик"
            },
            {
                "airports": [
                    {
                        "code": "XIZ",
                        "name": "Международный аэропорт «Champagne-Ardenne TGV»"
                    }
                ],
                "code": "RHE",
                "country": "FR",
                "country_name": "Франция",
                "name": "Реймс"
            },
            {
                "airports": [
                ],
                "code": "RNS",
                "country": "FR",
                "country_name": "Франция",
                "name": "Ренн"
            },
            {
                "airports": [
                    {
                        "code": "RNO",
                        "name": "Международный аэропорт Рено-Тахо"
                    }
                ],
                "code": "RNO",
                "country": "US",
                "country_name": "США",
                "name": "Рено-Тахо"
            },
            {
                "airports": [
                    {
                        "code": "RIX",
                        "name": "Рига"
                    }
                ],
                "code": "RIX",
                "country": "LV",
                "country_name": "Латвия",
                "name": "Рига"
            },
            {
                "airports": [
                    {
                        "code": "FCO",
                        "name": "Фьюмичино"
                    }
                ],
                "code": "ROM",
                "country": "IT",
                "country_name": "Италия",
                "name": "Рим"
            },
            {
                "airports": [
                    {
                        "code": "RMI",
                        "name": "Римини"
                    }
                ],
                "code": "RMI",
                "country": "IT",
                "country_name": "Италия",
                "name": "Римини"
            },
            {
                "airports": [
                    {
                        "code": "RIC",
                        "name": "Международный аэропорт Ричмонд"
                    }
                ],
                "code": "RIC",
                "country": "US",
                "country_name": "США",
                "name": "Ричмонд"
            },
            {
                "airports": [
                ],
                "code": "RVN",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Рованиеми"
            },
            {
                "airports": [
                    {
                        "code": "RHO",
                        "name": "Диагорас"
                    }
                ],
                "code": "RHO",
                "country": "GR",
                "country_name": "Греция",
                "name": "Родос"
            },
            {
                "airports": [
                ],
                "code": "RDU",
                "country": "US",
                "country_name": "США",
                "name": "Роли"
            },
            {
                "airports": [
                    {
                        "code": "ROV",
                        "name": "Аэропорт «Платов»"
                    }
                ],
                "code": "ROV",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ростов-на-Дону"
            },
            {
                "airports": [
                    {
                        "code": "ROC",
                        "name": "Международный аэропорт Грэйтер Рочестер"
                    }
                ],
                "code": "ROC",
                "country": "US",
                "country_name": "США",
                "name": "Рочестер"
            },
            {
                "airports": [
                ],
                "code": "SAV",
                "country": "US",
                "country_name": "США",
                "name": "Саванна"
            },
            {
                "airports": [
                ],
                "code": "ZVK",
                "country": "LA",
                "country_name": "Лаос",
                "name": "Саваннакхет"
            },
            {
                "airports": [
                ],
                "code": "SPN",
                "country": "MP",
                "country_name": "Северные Марианские острова",
                "name": "Сайпан"
            },
            {
                "airports": [
                    {
                        "code": "SMF",
                        "name": "International"
                    },
                    {
                        "code": "SAC",
                        "name": "Международный аэропорт Сакраменто"
                    }
                ],
                "code": "SAC",
                "country": "US",
                "country_name": "США",
                "name": "Сакраменто"
            },
            {
                "airports": [
                ],
                "code": "SLY",
                "country": "RU",
                "country_name": "Россия",
                "name": "Салехард"
            },
            {
                "airports": [
                    {
                        "code": "SKG",
                        "name": "Салоники"
                    }
                ],
                "code": "SKG",
                "country": "GR",
                "country_name": "Греция",
                "name": "Салоники"
            },
            {
                "airports": [
                    {
                        "code": "KUF",
                        "name": "Курумоч"
                    }
                ],
                "code": "KUF",
                "country": "RU",
                "country_name": "Россия",
                "name": "Самара"
            },
            {
                "airports": [
                    {
                        "code": "SKD",
                        "name": "Самарканд"
                    }
                ],
                "code": "SKD",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Самарканд"
            },
            {
                "airports": [
                ],
                "code": "SMI",
                "country": "GR",
                "country_name": "Греция",
                "name": "Самос"
            },
            {
                "airports": [
                    {
                        "code": "SZF",
                        "name": "Аэропорт Самсан Карсамба"
                    }
                ],
                "code": "SZF",
                "country": "TR",
                "country_name": "Турция",
                "name": "Самсан Карсамба"
            },
            {
                "airports": [
                    {
                        "code": "SAT",
                        "name": "Международный аэропорт Сан-Антонио"
                    }
                ],
                "code": "SAT",
                "country": "US",
                "country_name": "США",
                "name": "Сан-Антонио"
            },
            {
                "airports": [
                ],
                "code": "SAN",
                "country": "US",
                "country_name": "США",
                "name": "Сан-Диего"
            },
            {
                "airports": [
                ],
                "code": "SFO",
                "country": "US",
                "country_name": "США",
                "name": "Сан-Франциско"
            },
            {
                "airports": [
                ],
                "code": "SJC",
                "country": "US",
                "country_name": "США",
                "name": "Сан-Хосе"
            },
            {
                "airports": [
                ],
                "code": "SYX",
                "country": "CN",
                "country_name": "Китай",
                "name": "Саниа"
            },
            {
                "airports": [
                    {
                        "code": "LED",
                        "name": "Пулково"
                    }
                ],
                "code": "LED",
                "country": "RU",
                "country_name": "Россия",
                "name": "Санкт-Петербург"
            },
            {
                "airports": [
                ],
                "code": "SDR",
                "country": "ES",
                "country_name": "Испания",
                "name": "Сантандер"
            },
            {
                "airports": [
                ],
                "code": "JTR",
                "country": "GR",
                "country_name": "Греция",
                "name": "Санторини"
            },
            {
                "airports": [
                    {
                        "code": "SCL",
                        "name": "Сантьяго Артуро Мерино Бенитес"
                    }
                ],
                "code": "SCL",
                "country": "CL",
                "country_name": "Чили",
                "name": "Сантьяго"
            },
            {
                "airports": [
                    {
                        "code": "SCQ",
                        "name": "Аэропорт Сантьяго-де-Компостела"
                    }
                ],
                "code": "SCQ",
                "country": "ES",
                "country_name": "Испания",
                "name": "Сантьяго Де Компостела"
            },
            {
                "airports": [
                    {
                        "code": "CTS",
                        "name": "Chitose Airport"
                    }
                ],
                "code": "SPK",
                "country": "JP",
                "country_name": "Япония",
                "name": "Саппоро"
            },
            {
                "airports": [
                ],
                "code": "SJJ",
                "country": "BA",
                "country_name": "Босния и Герцеговина",
                "name": "Сараево"
            },
            {
                "airports": [
                    {
                        "code": "SKX",
                        "name": "Аэропорт Саранск"
                    }
                ],
                "code": "SKX",
                "country": "RU",
                "country_name": "Россия",
                "name": "Саранск"
            },
            {
                "airports": [
                    {
                        "code": "SRQ",
                        "name": "Международный аэропорт Сарасота-Брадентон"
                    }
                ],
                "code": "SRQ",
                "country": "US",
                "country_name": "США",
                "name": "Сарасота-Брадентон"
            },
            {
                "airports": [
                    {
                        "code": "RTW",
                        "name": "Саратов"
                    },
                    {
                        "code": "GSV",
                        "name": "Международный аэропорт \"Гагарин\""
                    }
                ],
                "code": "RTW",
                "country": "RU",
                "country_name": "Россия",
                "name": "Саратов"
            },
            {
                "airports": [
                ],
                "code": "SOU",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Саутгемптон"
            },
            {
                "airports": [
                ],
                "code": "CEB",
                "country": "PH",
                "country_name": "Филиппины",
                "name": "Себу Мактан"
            },
            {
                "airports": [
                ],
                "code": "SVQ",
                "country": "ES",
                "country_name": "Испания",
                "name": "Севилья"
            },
            {
                "airports": [
                ],
                "code": "STL",
                "country": "US",
                "country_name": "США",
                "name": "Сент-Луис"
            },
            {
                "airports": [
                    {
                        "code": "ICN",
                        "name": "Сеул/Инчон"
                    },
                    {
                        "code": "SEL",
                        "name": "Кимпо"
                    }
                ],
                "code": "SEL",
                "country": "KR",
                "country_name": "Корея",
                "name": "Сеул"
            },
            {
                "airports": [
                ],
                "code": "SYD",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Сидней"
            },
            {
                "airports": [
                ],
                "code": "REP",
                "country": "KH",
                "country_name": "Камбоджа",
                "name": "Сием-Рип"
            },
            {
                "airports": [
                    {
                        "code": "SIP",
                        "name": "Симферополь"
                    }
                ],
                "code": "SIP",
                "country": "RU",
                "country_name": "Россия",
                "name": "Симферополь"
            },
            {
                "airports": [
                    {
                        "code": "SIN",
                        "name": "Чанги"
                    }
                ],
                "code": "SIN",
                "country": "SG",
                "country_name": "Сингапур",
                "name": "Сингапур"
            },
            {
                "airports": [
                    {
                        "code": "XNN",
                        "name": "Международный аэропорт Синин Цаоцзябао"
                    }
                ],
                "code": "XNN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Синин"
            },
            {
                "airports": [
                    {
                        "code": "XIY",
                        "name": "Аэропорт Сианьянг"
                    }
                ],
                "code": "SIA",
                "country": "CN",
                "country_name": "Китай",
                "name": "Синьян"
            },
            {
                "airports": [
                    {
                        "code": "SYR",
                        "name": "Международный аэропорт Сиракус Ханкок"
                    }
                ],
                "code": "SYR",
                "country": "US",
                "country_name": "США",
                "name": "Сиракус"
            },
            {
                "airports": [
                ],
                "code": "SEA",
                "country": "US",
                "country_name": "США",
                "name": "Сиэтл"
            },
            {
                "airports": [
                ],
                "code": "SKP",
                "country": "MK",
                "country_name": "Македония",
                "name": "Скопье"
            },
            {
                "airports": [
                ],
                "code": "GVN",
                "country": "RU",
                "country_name": "Россия",
                "name": "Советская Гавань"
            },
            {
                "airports": [
                ],
                "code": "CSH",
                "country": "RU",
                "country_name": "Россия",
                "name": "Соловецкий"
            },
            {
                "airports": [
                ],
                "code": "SLC",
                "country": "US",
                "country_name": "США",
                "name": "Солт-Лейк-Сити"
            },
            {
                "airports": [
                    {
                        "code": "SOF",
                        "name": "София"
                    }
                ],
                "code": "SOF",
                "country": "BG",
                "country_name": "Болгария",
                "name": "София"
            },
            {
                "airports": [
                    {
                        "code": "AER",
                        "name": "Адлер"
                    }
                ],
                "code": "AER",
                "country": "RU",
                "country_name": "Россия",
                "name": "Сочи"
            },
            {
                "airports": [
                    {
                        "code": "SPU",
                        "name": "Сплит"
                    }
                ],
                "code": "SPU",
                "country": "HR",
                "country_name": "Хорватия",
                "name": "Сплит"
            },
            {
                "airports": [
                ],
                "code": "SVG",
                "country": "NO",
                "country_name": "Норвегия",
                "name": "Ставангер"
            },
            {
                "airports": [
                    {
                        "code": "STW",
                        "name": "Ставрополь"
                    }
                ],
                "code": "STW",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ставрополь"
            },
            {
                "airports": [
                    {
                        "code": "IST",
                        "name": "Стамбул"
                    }
                ],
                "code": "IST",
                "country": "TR",
                "country_name": "Турция",
                "name": "Стамбул"
            },
            {
                "airports": [
                    {
                        "code": "ARN",
                        "name": "Арланда"
                    }
                ],
                "code": "STO",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Стокгольм"
            },
            {
                "airports": [
                    {
                        "code": "XWG",
                        "name": "Страсбург"
                    }
                ],
                "code": "SXB",
                "country": "FR",
                "country_name": "Франция",
                "name": "Страсбург"
            },
            {
                "airports": [
                ],
                "code": "THS",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Сукхотаи"
            },
            {
                "airports": [
                ],
                "code": "SDL",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Сундсвалль"
            },
            {
                "airports": [
                ],
                "code": "SUB",
                "country": "ID",
                "country_name": "Индонезия",
                "name": "Сурабая"
            },
            {
                "airports": [
                    {
                        "code": "SGC",
                        "name": "Сургут"
                    }
                ],
                "code": "SGC",
                "country": "RU",
                "country_name": "Россия",
                "name": "Сургут"
            },
            {
                "airports": [
                    {
                        "code": "SCW",
                        "name": "Сыктывкар"
                    }
                ],
                "code": "SCW",
                "country": "RU",
                "country_name": "Россия",
                "name": "Сыктывкар"
            },
            {
                "airports": [
                    {
                        "code": "XMN",
                        "name": "Международный аэропорт Сямынь Гаоци"
                    }
                ],
                "code": "XMN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Сямынь"
            },
            {
                "airports": [
                ],
                "code": "PPT",
                "country": "PF",
                "country_name": "Французская Полинезия",
                "name": "Таити"
            },
            {
                "airports": [
                    {
                        "code": "TSA",
                        "name": "Международный аэропорт Тайбэй Соншан"
                    }
                ],
                "code": "TPE",
                "country": "CN",
                "country_name": "Китай",
                "name": "Тайбэй"
            },
            {
                "airports": [
                ],
                "code": "TYN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Тайюань"
            },
            {
                "airports": [
                    {
                        "code": "TLL",
                        "name": "Таллин"
                    }
                ],
                "code": "TLL",
                "country": "EE",
                "country_name": "Эстония",
                "name": "Таллин"
            },
            {
                "airports": [
                ],
                "code": "TPA",
                "country": "US",
                "country_name": "США",
                "name": "Тампа"
            },
            {
                "airports": [
                ],
                "code": "TMP",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Тампере"
            },
            {
                "airports": [
                ],
                "code": "TNG",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Танжер"
            },
            {
                "airports": [
                    {
                        "code": "TAS",
                        "name": "Южный"
                    }
                ],
                "code": "TAS",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Ташкент"
            },
            {
                "airports": [
                    {
                        "code": "TBS",
                        "name": "Тбилиси"
                    }
                ],
                "code": "TBS",
                "country": "GE",
                "country_name": "Грузия",
                "name": "Тбилиси"
            },
            {
                "airports": [
                    {
                        "code": "IKA",
                        "name": "Аэропорт Имам Хомейни"
                    }
                ],
                "code": "THR",
                "country": "IR",
                "country_name": "Иран",
                "name": "Тегеран"
            },
            {
                "airports": [
                    {
                        "code": "TLV",
                        "name": "Тель-Авив"
                    }
                ],
                "code": "TLV",
                "country": "IL",
                "country_name": "Израиль",
                "name": "Тель-Авив"
            },
            {
                "airports": [
                    {
                        "code": "TFN",
                        "name": "Тенерифе северный"
                    },
                    {
                        "code": "TFS",
                        "name": "Тенерифе-Южный"
                    }
                ],
                "code": "TCI",
                "country": "ES",
                "country_name": "Испания",
                "name": "Тенерифе"
            },
            {
                "airports": [
                    {
                        "code": "TIV",
                        "name": "Тиват"
                    }
                ],
                "code": "TIV",
                "country": "ME",
                "country_name": "Черногория",
                "name": "Тиват"
            },
            {
                "airports": [
                ],
                "code": "TIA",
                "country": "AL",
                "country_name": "Албания",
                "name": "Тирана"
            },
            {
                "airports": [
                    {
                        "code": "HND",
                        "name": "Ханэда"
                    },
                    {
                        "code": "NRT",
                        "name": "Нарита"
                    }
                ],
                "code": "TYO",
                "country": "JP",
                "country_name": "Япония",
                "name": "Токио"
            },
            {
                "airports": [
                    {
                        "code": "TOF",
                        "name": "Томск Богашево"
                    }
                ],
                "code": "TOF",
                "country": "RU",
                "country_name": "Россия",
                "name": "Томск"
            },
            {
                "airports": [
                    {
                        "code": "YYZ",
                        "name": "Аэропорт Торонто Пирсон"
                    }
                ],
                "code": "YTO",
                "country": "CA",
                "country_name": "Канада",
                "name": "Торонто"
            },
            {
                "airports": [
                ],
                "code": "TOY",
                "country": "JP",
                "country_name": "Япония",
                "name": "Тояма"
            },
            {
                "airports": [
                    {
                        "code": "TZX",
                        "name": "Аэропорт Трабзон"
                    }
                ],
                "code": "TZX",
                "country": "TR",
                "country_name": "Турция",
                "name": "Трабзон"
            },
            {
                "airports": [
                ],
                "code": "TDX",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Трат"
            },
            {
                "airports": [
                ],
                "code": "TRV",
                "country": "IN",
                "country_name": "Индия",
                "name": "Тривандрам"
            },
            {
                "airports": [
                ],
                "code": "TRS",
                "country": "IT",
                "country_name": "Италия",
                "name": "Триест"
            },
            {
                "airports": [
                ],
                "code": "TRD",
                "country": "NO",
                "country_name": "Норвегия",
                "name": "Тронхейм"
            },
            {
                "airports": [
                ],
                "code": "TLS",
                "country": "FR",
                "country_name": "Франция",
                "name": "Тулуза"
            },
            {
                "airports": [
                ],
                "code": "TUN",
                "country": "TN",
                "country_name": "Тунис",
                "name": "Тунис"
            },
            {
                "airports": [
                ],
                "code": "TRN",
                "country": "IT",
                "country_name": "Италия",
                "name": "Турин"
            },
            {
                "airports": [
                ],
                "code": "TKU",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Турку"
            },
            {
                "airports": [
                ],
                "code": "TYD",
                "country": "RU",
                "country_name": "Россия",
                "name": "Тында"
            },
            {
                "airports": [
                    {
                        "code": "TJM",
                        "name": "Рощино"
                    }
                ],
                "code": "TJM",
                "country": "RU",
                "country_name": "Россия",
                "name": "Тюмень"
            },
            {
                "airports": [
                ],
                "code": "TSN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Тяньцзинь"
            },
            {
                "airports": [
                ],
                "code": "OZZ",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Уарзазат"
            },
            {
                "airports": [
                ],
                "code": "UDR",
                "country": "IN",
                "country_name": "Индия",
                "name": "Удайпур"
            },
            {
                "airports": [
                ],
                "code": "OUD",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Уджда"
            },
            {
                "airports": [
                ],
                "code": "UTH",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Удон-Тхани"
            },
            {
                "airports": [
                    {
                        "code": "ULN",
                        "name": "Буянт-Уха"
                    }
                ],
                "code": "ULN",
                "country": "MN",
                "country_name": "Монголия",
                "name": "Улан-Батор"
            },
            {
                "airports": [
                    {
                        "code": "UUD",
                        "name": "аэропорт Улан-Удэ Байкал"
                    }
                ],
                "code": "UUD",
                "country": "RU",
                "country_name": "Россия",
                "name": "Улан-Удэ"
            },
            {
                "airports": [
                ],
                "code": "USN",
                "country": "KR",
                "country_name": "Корея",
                "name": "Ульсан"
            },
            {
                "airports": [
                    {
                        "code": "ULY",
                        "name": "Восточный (Ульяновск)"
                    },
                    {
                        "code": "ULV",
                        "name": "Баратаевка"
                    }
                ],
                "code": "ULY",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ульяновск"
            },
            {
                "airports": [
                ],
                "code": "UME",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Умео"
            },
            {
                "airports": [
                    {
                        "code": "UGC",
                        "name": "Ургенч"
                    }
                ],
                "code": "UGC",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Ургенч"
            },
            {
                "airports": [
                ],
                "code": "URC",
                "country": "CN",
                "country_name": "Китай",
                "name": "Урумчи"
            },
            {
                "airports": [
                    {
                        "code": "UKK",
                        "name": "Усть-Каменогорск"
                    }
                ],
                "code": "UKK",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Усть-Каменогорск"
            },
            {
                "airports": [
                ],
                "code": "UTP",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Утапао"
            },
            {
                "airports": [
                    {
                        "code": "UFA",
                        "name": "Уфа"
                    }
                ],
                "code": "UFA",
                "country": "RU",
                "country_name": "Россия",
                "name": "Уфа"
            },
            {
                "airports": [
                ],
                "code": "WUH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Ухань"
            },
            {
                "airports": [
                    {
                        "code": "FEG",
                        "name": "Фергана"
                    }
                ],
                "code": "FEG",
                "country": "UZ",
                "country_name": "Узбекистан",
                "name": "Фергана"
            },
            {
                "airports": [
                ],
                "code": "FEZ",
                "country": "MA",
                "country_name": "Марокко",
                "name": "Фес"
            },
            {
                "airports": [
                ],
                "code": "PHL",
                "country": "US",
                "country_name": "США",
                "name": "Филадельфия"
            },
            {
                "airports": [
                ],
                "code": "PHX",
                "country": "US",
                "country_name": "США",
                "name": "Финикс"
            },
            {
                "airports": [
                ],
                "code": "FLR",
                "country": "IT",
                "country_name": "Италия",
                "name": "Флоренция"
            },
            {
                "airports": [
                    {
                        "code": "RSW",
                        "name": "Southwest Florida International Airport"
                    },
                    {
                        "code": "FMY",
                        "name": "Аэропорт Форт Майерс Пейдж Филд"
                    }
                ],
                "code": "FMY",
                "country": "US",
                "country_name": "США",
                "name": "Форт Майерс Пейдж"
            },
            {
                "airports": [
                ],
                "code": "FLL",
                "country": "US",
                "country_name": "США",
                "name": "Форт-Лодердейл"
            },
            {
                "airports": [
                    {
                        "code": "FRA",
                        "name": "Франкфурт/Майн"
                    }
                ],
                "code": "FRA",
                "country": "DE",
                "country_name": "Германия",
                "name": "Франкфурт"
            },
            {
                "airports": [
                ],
                "code": "PQC",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Фукуок"
            },
            {
                "airports": [
                ],
                "code": "FUK",
                "country": "JP",
                "country_name": "Япония",
                "name": "Фукуока"
            },
            {
                "airports": [
                ],
                "code": "FOC",
                "country": "CN",
                "country_name": "Китай",
                "name": "Фучжоу"
            },
            {
                "airports": [
                ],
                "code": "FUE",
                "country": "ES",
                "country_name": "Испания",
                "name": "Фуэртевентура"
            },
            {
                "airports": [
                    {
                        "code": "KHV",
                        "name": "Международный аэропорт Хабаровск (Новый) им. Г. И. Невельского"
                    }
                ],
                "code": "KHV",
                "country": "RU",
                "country_name": "Россия",
                "name": "Хабаровск"
            },
            {
                "airports": [
                ],
                "code": "HYD",
                "country": "IN",
                "country_name": "Индия",
                "name": "Хайдерабад"
            },
            {
                "airports": [
                ],
                "code": "HAK",
                "country": "CN",
                "country_name": "Китай",
                "name": "Хайкоу"
            },
            {
                "airports": [
                ],
                "code": "HLD",
                "country": "CN",
                "country_name": "Китай",
                "name": "Хайлар"
            },
            {
                "airports": [
                ],
                "code": "HKD",
                "country": "JP",
                "country_name": "Япония",
                "name": "Хакодате"
            },
            {
                "airports": [
                ],
                "code": "HUY",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Хамберсайд"
            },
            {
                "airports": [
                    {
                        "code": "HAN",
                        "name": "Нойбай"
                    }
                ],
                "code": "HAN",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Ханой"
            },
            {
                "airports": [
                    {
                        "code": "HMA",
                        "name": "Ханты-Мансийск"
                    }
                ],
                "code": "HMA",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ханты-Мансийск"
            },
            {
                "airports": [
                ],
                "code": "HGH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Ханчжоу"
            },
            {
                "airports": [
                    {
                        "code": "CHQ",
                        "name": "Международный аэропорт Иоаннис Даскалояннис"
                    }
                ],
                "code": "CHQ",
                "country": "GR",
                "country_name": "Греция",
                "name": "Ханья"
            },
            {
                "airports": [
                    {
                        "code": "HRB",
                        "name": "Харбин"
                    }
                ],
                "code": "HRB",
                "country": "CN",
                "country_name": "Китай",
                "name": "Харбин"
            },
            {
                "airports": [
                    {
                        "code": "HFD",
                        "name": "Аэропорт Хартфорд Брейнард"
                    },
                    {
                        "code": "BDL",
                        "name": "Международный аэропорт Брэдли"
                    }
                ],
                "code": "HFD",
                "country": "US",
                "country_name": "США",
                "name": "Хартфорд"
            },
            {
                "airports": [
                ],
                "code": "HRK",
                "country": "UA",
                "country_name": "Украина",
                "name": "Харьков"
            },
            {
                "airports": [
                ],
                "code": "HDY",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Хатъяй"
            },
            {
                "airports": [
                    {
                        "code": "HEL",
                        "name": "Вантаа"
                    }
                ],
                "code": "HEL",
                "country": "FI",
                "country_name": "Финляндия",
                "name": "Хельсинки"
            },
            {
                "airports": [
                ],
                "code": "XRY",
                "country": "ES",
                "country_name": "Испания",
                "name": "Херес"
            },
            {
                "airports": [
                    {
                        "code": "HYA",
                        "name": "Хианнис Барнстейбл"
                    }
                ],
                "code": "HYA",
                "country": "US",
                "country_name": "США",
                "name": "Хианнис"
            },
            {
                "airports": [
                ],
                "code": "HIJ",
                "country": "JP",
                "country_name": "Япония",
                "name": "Хиросима"
            },
            {
                "airports": [
                ],
                "code": "HBA",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Хобарт"
            },
            {
                "airports": [
                    {
                        "code": "SGN",
                        "name": "Тансоннхат"
                    }
                ],
                "code": "SGN",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Хошимин"
            },
            {
                "airports": [
                    {
                        "code": "HIA",
                        "name": "международный аэропорт Хуайань"
                    }
                ],
                "code": "HIA",
                "country": "CN",
                "country_name": "Китай",
                "name": "Хуайань"
            },
            {
                "airports": [
                    {
                        "code": "LBD",
                        "name": "Худжанд"
                    }
                ],
                "code": "LBD",
                "country": "TJ",
                "country_name": "Таджикистан",
                "name": "Худжанд"
            },
            {
                "airports": [
                ],
                "code": "HRG",
                "country": "EG",
                "country_name": "Египет",
                "name": "Хургада"
            },
            {
                "airports": [
                    {
                        "code": "HUI",
                        "name": "Хуэ"
                    }
                ],
                "code": "HUI",
                "country": "VN",
                "country_name": "Вьетнам",
                "name": "Хуэ"
            },
            {
                "airports": [
                    {
                        "code": "HOU",
                        "name": "Аэропорт Хьюстон Уильям Хобби"
                    },
                    {
                        "code": "IAH",
                        "name": "Хьюстон"
                    }
                ],
                "code": "QHO",
                "country": "US",
                "country_name": "США",
                "name": "Хьюстон"
            },
            {
                "airports": [
                ],
                "code": "HFE",
                "country": "CN",
                "country_name": "Китай",
                "name": "Хэфэй"
            },
            {
                "airports": [
                ],
                "code": "TNA",
                "country": "CN",
                "country_name": "Китай",
                "name": "Цзинань"
            },
            {
                "airports": [
                    {
                        "code": "JHG",
                        "name": "Аэропорт Цзинхун Сишуанбаньна Гаса"
                    }
                ],
                "code": "JHG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Цзинхун"
            },
            {
                "airports": [
                ],
                "code": "TAO",
                "country": "CN",
                "country_name": "Китай",
                "name": "Циндао"
            },
            {
                "airports": [
                ],
                "code": "CVG",
                "country": "US",
                "country_name": "США",
                "name": "Цинциннати"
            },
            {
                "airports": [
                    {
                        "code": "NDG",
                        "name": "Цицихар"
                    }
                ],
                "code": "NDG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Цицикар"
            },
            {
                "airports": [
                    {
                        "code": "ZRH",
                        "name": "Цюрих"
                    }
                ],
                "code": "ZRH",
                "country": "CH",
                "country_name": "Швейцария",
                "name": "Цюрих"
            },
            {
                "airports": [
                ],
                "code": "CIH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чангжи"
            },
            {
                "airports": [
                ],
                "code": "IXC",
                "country": "IN",
                "country_name": "Индия",
                "name": "Чандигарх"
            },
            {
                "airports": [
                ],
                "code": "CGQ",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чанчунь"
            },
            {
                "airports": [
                ],
                "code": "CSX",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чанша"
            },
            {
                "airports": [
                    {
                        "code": "CHS",
                        "name": "Аэропорт Чарльстон"
                    }
                ],
                "code": "CHS",
                "country": "US",
                "country_name": "США",
                "name": "Чарльстон"
            },
            {
                "airports": [
                ],
                "code": "CJU",
                "country": "KR",
                "country_name": "Корея",
                "name": "Чеджу"
            },
            {
                "airports": [
                    {
                        "code": "CEK",
                        "name": "Челябинск"
                    }
                ],
                "code": "CEK",
                "country": "RU",
                "country_name": "Россия",
                "name": "Челябинск"
            },
            {
                "airports": [
                ],
                "code": "MAA",
                "country": "IN",
                "country_name": "Индия",
                "name": "Ченнай"
            },
            {
                "airports": [
                    {
                        "code": "DYG",
                        "name": "Аэропорт Чжанцзяцзе Даёнг"
                    }
                ],
                "code": "DYG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чжанцзяцзе"
            },
            {
                "airports": [
                    {
                        "code": "ZUH",
                        "name": "Аэропорт Чжухай"
                    }
                ],
                "code": "ZUH",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чжухай"
            },
            {
                "airports": [
                    {
                        "code": "CGO",
                        "name": "Аэропорт Чжэнчжоу Синьчжэн"
                    }
                ],
                "code": "CGO",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чжэнчжоу"
            },
            {
                "airports": [
                ],
                "code": "CEI",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Чианг Рай"
            },
            {
                "airports": [
                ],
                "code": "CNX",
                "country": "TH",
                "country_name": "Таиланд",
                "name": "Чиангмай"
            },
            {
                "airports": [
                    {
                        "code": "CHI",
                        "name": "Аэропорт Чикаго"
                    }
                ],
                "code": "CHI",
                "country": "US",
                "country_name": "США",
                "name": "Чикаго"
            },
            {
                "airports": [
                ],
                "code": "JKH",
                "country": "GR",
                "country_name": "Греция",
                "name": "Чиос"
            },
            {
                "airports": [
                    {
                        "code": "HTA",
                        "name": "Чита"
                    }
                ],
                "code": "HTA",
                "country": "RU",
                "country_name": "Россия",
                "name": "Чита"
            },
            {
                "airports": [
                ],
                "code": "CKG",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чунцин"
            },
            {
                "airports": [
                ],
                "code": "CTU",
                "country": "CN",
                "country_name": "Китай",
                "name": "Чэнду"
            },
            {
                "airports": [
                    {
                        "code": "PVG",
                        "name": "Пудонг"
                    }
                ],
                "code": "SHA",
                "country": "CN",
                "country_name": "Китай",
                "name": "Шанхай"
            },
            {
                "airports": [
                ],
                "code": "SWA",
                "country": "CN",
                "country_name": "Китай",
                "name": "Шаньтоу"
            },
            {
                "airports": [
                    {
                        "code": "CLT",
                        "name": "Международный аэропорт Шарлотт Дуглас"
                    }
                ],
                "code": "CLT",
                "country": "US",
                "country_name": "США",
                "name": "Шарлотт"
            },
            {
                "airports": [
                ],
                "code": "SSH",
                "country": "EG",
                "country_name": "Египет",
                "name": "Шарм Эль Шейх"
            },
            {
                "airports": [
                ],
                "code": "EKS",
                "country": "RU",
                "country_name": "Россия",
                "name": "Шахтерск"
            },
            {
                "airports": [
                ],
                "code": "SFT",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Шеллефтео"
            },
            {
                "airports": [
                    {
                        "code": "STR",
                        "name": "Штутгарт"
                    }
                ],
                "code": "STR",
                "country": "DE",
                "country_name": "Германия",
                "name": "Штутгарт"
            },
            {
                "airports": [
                    {
                        "code": "CIT",
                        "name": "Чимкент"
                    }
                ],
                "code": "CIT",
                "country": "KZ",
                "country_name": "Казахстан",
                "name": "Шымкент"
            },
            {
                "airports": [
                ],
                "code": "SZX",
                "country": "CN",
                "country_name": "Китай",
                "name": "Шэньчжэнь"
            },
            {
                "airports": [
                ],
                "code": "SHE",
                "country": "CN",
                "country_name": "Китай",
                "name": "Шэньян"
            },
            {
                "airports": [
                ],
                "code": "EDI",
                "country": "GB",
                "country_name": "Великобритания",
                "name": "Эдинбург"
            },
            {
                "airports": [
                ],
                "code": "ETH",
                "country": "IL",
                "country_name": "Израиль",
                "name": "Эйлат"
            },
            {
                "airports": [
                    {
                        "code": "ASP",
                        "name": "Аэропорт  Алис-Спрингс"
                    }
                ],
                "code": "ASP",
                "country": "AU",
                "country_name": "Австралия",
                "name": "Элис Спрингз"
            },
            {
                "airports": [
                ],
                "code": "RUH",
                "country": "SA",
                "country_name": "Саудовская Аравия",
                "name": "Эр-Рияд"
            },
            {
                "airports": [
                    {
                        "code": "ECN",
                        "name": "Эрджан"
                    }
                ],
                "code": "ECN",
                "country": "CY",
                "country_name": "Кипр",
                "name": "Эрджан"
            },
            {
                "airports": [
                ],
                "code": "OER",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Эрншельдсвик"
            },
            {
                "airports": [
                ],
                "code": "OSD",
                "country": "SE",
                "country_name": "Швеция",
                "name": "Эстерсунд"
            },
            {
                "airports": [
                ],
                "code": "DEE",
                "country": "RU",
                "country_name": "Россия",
                "name": "Южно-Курильск"
            },
            {
                "airports": [
                    {
                        "code": "UUS",
                        "name": "Южно-Сахалинск"
                    }
                ],
                "code": "UUS",
                "country": "RU",
                "country_name": "Россия",
                "name": "Южно-Сахалинск"
            },
            {
                "airports": [
                ],
                "code": "UYN",
                "country": "CN",
                "country_name": "Китай",
                "name": "Юйлинь"
            },
            {
                "airports": [
                    {
                        "code": "YKS",
                        "name": "Якутск"
                    }
                ],
                "code": "YKS",
                "country": "RU",
                "country_name": "Россия",
                "name": "Якутск"
            },
            {
                "airports": [
                ],
                "code": "RGN",
                "country": "MM",
                "country_name": "Мьянма",
                "name": "Янгон"
            },
            {
                "airports": [
                ],
                "code": "IOA",
                "country": "GR",
                "country_name": "Греция",
                "name": "Янина"
            },
            {
                "airports": [
                    {
                        "code": "ENY",
                        "name": "Яньань"
                    }
                ],
                "code": "ENY",
                "country": "CN",
                "country_name": "Китай",
                "name": "Яньань"
            },
            {
                "airports": [
                    {
                        "code": "IAR",
                        "name": "Аэропорт Туношна"
                    }
                ],
                "code": "IAR",
                "country": "RU",
                "country_name": "Россия",
                "name": "Ярославль"
            }
        ]
    },
    "error": None,
    "success": None
}

cityes = query['data']['cities']

for i, item in enumerate(cityes):
    if len(item['airports']) > 0:
        country_id = cheak_country(item['country_name'])
        if country_id == None:
            country_id = add_country(item['country_name'], item['country'])
        city_id = get_city_country(item['name'])
        if city_id == None:
            city_id = add_city(country_id, item['name'], item['code'])
        for j, item_air in enumerate(item['airports']):
            airport_id = get_airport(item_air['name'])
            if airport_id == None:
                add_airport(country_id, city_id, item_air['name'], item_air['code'])