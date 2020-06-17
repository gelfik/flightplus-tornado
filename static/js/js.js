/** Dropdown on hover */
$(".nav-link.dropdown-toggle").hover(function () {
    $(this).removeAttr('data-toggle');
    $(this).parent().addClass('show');
    $(this).next().addClass('show');
}, function () {
    var isDropdownHovered = $(this).next().filter(":hover").length;
    var isThisHovered = $(this).filter(":hover").length;
    if (isDropdownHovered || isThisHovered) {
    } else {
        $(this).attr('data-toggle', 'dropdown');
        $(this).parent().removeClass('show');
        $(this).next().removeClass('show');
    }
});

$(".dropdown-menu").hover(function () {
}, function () {
    var isDropdownHovered = $(this).prev().filter(":hover").length;
    var isThisHovered = $(this).filter(":hover").length;
    if (isDropdownHovered || isThisHovered) {
    } else {
        $(this).parent().removeClass('show');
        $(this).removeClass('show');
    }
});


function closenavbar() {
    elem = document.getElementById("navbarSupportedContent").classList.remove('show')
};

/** Проверка даты типа докуменнта и даты пассажира при добавлении */
$(function () {
    $('#birthday').on('change', function () {
        var ThisTime = new Date();
        ThisTime.setFullYear(ThisTime.getFullYear() - 14)
        var InputTime = new Date(document.getElementById("birthday").value);
        elem_valid_date = document.getElementById("valid_date");
        for (let elem of document.getElementById("id_document_type").getElementsByTagName('option')) {
            if (((+ThisTime) < (+InputTime))) {
                if (elem.value == 1) {
                    elem.setAttribute('disabled', true);
                    elem.removeAttribute('selected');
                    elem_valid_date.removeAttribute('disabled');
                } else if (elem.value == 3) {
                    elem.removeAttribute('disabled');
                    elem.setAttribute('selected', true);
                    elem_valid_date.setAttribute('disabled', true);
                }
            } else {
                if (elem.value == 3) {
                    elem.setAttribute('disabled', true);
                    elem.removeAttribute('selected');
                    elem_valid_date.removeAttribute('disabled');
                } else if (elem.value == 1) {
                    elem.removeAttribute('disabled');
                    elem.setAttribute('selected', true);
                    elem_valid_date.setAttribute('disabled', true);
                }
            }
        }
    });
});

$(function () {
    $('#DocumentType').on('change', function () {
        elem_valid_date = document.getElementById("valid_date");
        elem_option = document.getElementById("id_document_type").getElementsByTagName('option')
        if (elem_option == 3) {
            elem_valid_date.setAttribute('disabled', true);
        } else {
            elem_valid_date.removeAttribute('disabled');
        }
    });
});


/** Вывод ошибки в модальном окне */
function show_error_snack(text) {
    $.toast({
        title: text,
        type: 'error',
        delay: 3000
    });
}

function show_success_snack(text) {
    $.toast({
        title: text,
        type: 'success',
        delay: 3000
    });
}

(function (b) {
    b.toast = function (a, h, g, l, k) {
        b("#toast-container").length || (b("body").prepend('<div id="toast-container" aria-live="polite" aria-atomic="true"></div>'), b("#toast-container").append('<div id="toast-wrapper" style="top: 56px;"></div>'));
        var c = "", d = "", e = "text-muted", f = "", m = "object" === typeof a ? a.title || "" : a || "Notice!";
        h = "object" === typeof a ? a.subtitle || "" : h || "";
        g = "object" === typeof a ? a.content || "" : g || "";
        k = "object" === typeof a ? a.delay || 3E3 : k || 3E3;
        switch ("object" === typeof a ? a.type || "" : l || "info") {
            case "info":
                c = "bg-info";
                f = e = d = "text-white";
                break;
            case "success":
                c = "bg-success";
                f = e = d = "text-white";
                break;
            case "warning":
            case "warn":
                c = "bg-warning";
                f = e = d = "text-white";
                break;
            case "error":
            case "danger":
                c = "bg-danger", f = e = d = "text-white"
        }
        a = '<div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-delay="' + k + '">' + ('<div class="toast-header ' + c + " " + d + '">') + ('<strong class="mr-auto">' + m + "</strong>");
        a += '<small class="' + e + '">' + h + "</small>";
        a += '<button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">';
        a += '<span aria-hidden="true" class="' + f + '">&times;</span>';
        a += "</button>";
        a += "</div>";
        "" !== g && (a += '<div class="toast-body">', a += g, a += "</div>");
        a += "</div>";
        b("#toast-wrapper").append(a);
        b("#toast-wrapper .toast:last").toast("show")
    }
})(jQuery);


/** API */
function apiv1_login() {
    let r = {
        url: '/api/v1/login',
        type: 'POST',
        data: {email: document.getElementById("email").value, password: document.getElementById("password").value},
        dataType: 'json',
        success: function (request) {
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_register() {
    let r = {
        url: '/api/v1/register',
        type: 'POST',
        data: {
            RulesAcceptCheak: $("#RegRulesAcceptCheak").prop("checked"),
            confirmpassword: document.getElementById("RegConfirmPassword").value,
            password: document.getElementById("RegPassword").value,
            phone: document.getElementById("RegPhone").value,
            email: document.getElementById("RegEmail").value,
            surname: document.getElementById("RegSurname").value,
            name: document.getElementById("RegName").value
        },
        dataType: 'json',
        success: function (request) {
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_delPassenger(id) {
    console.log(id);
    let r = {
        url: '/api/v1/delPassenger',
        type: 'POST',
        data: {passangerid: id},
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}


function apiv1_addPassenger() {
    let r = {
        url: '/api/v1/addPassenger',
        type: 'POST',
        data: {
            id_document_type: document.getElementById("id_document_type").value,
            last_name: document.getElementById("last_name").value,
            first_name: document.getElementById("first_name").value,
            patronymic: document.getElementById("patronymic").value,
            birthday: document.getElementById("birthday").value,
            phone: document.getElementById("phone").value,
            email: document.getElementById("passenger_email").value,
            id_gender: document.getElementById("id_gender").value,
            id_document_type: document.getElementById("id_document_type").value,
            document_number: document.getElementById("document_number").value,
            valid_date: document.getElementById("valid_date").value
        },
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_addairlaine() {
    var formData = new FormData($('#load_pic')[0]);
    let pic = {
        type: 'POST', // тип запроса
        url: '/api/v1/admin/load_img', // куда будем отправлять, можно явно указать
        data: formData, // данные, которые передаем
        cache: false, // кэш и прочие настройки писать именно так (для файлов)
        // (связано это с кодировкой и всякой лабудой)
        contentType: false, // нужно указать тип контента false для картинки(файла)
        processData: false, // для передачи картинки(файла) нужно false
        async: false,
        success: function (data) { // в случае успешного завершения
            console.log("Завершилось успешно"); // выведем в консоли успех
            console.log(data); // и что в ответе получили, если там что-то есть
            return data
        },
        error: function (data) { // в случае провала
            console.log("Завершилось с ошибкой"); // сообщение об ошибке
            console.log(data); // и данные по ошибке в том числе
            return data
        }
    };
    let pic_link = $.ajax(pic);
    if (pic_link.responseJSON['status_code'] == 200) {
        let r = {
            url: '/api/v1/admin/addAirplane',
            type: 'POST',
            data: {
                airplane_num: document.getElementById("airplane_num").value,
                airplane_name: document.getElementById("airplane_name").value,
                column_of_seats: document.getElementById("column_of_seats").value,
                row_of_seats: document.getElementById("row_of_seats").value,
                status: document.getElementById("status").value,
                seats_scheme: pic_link.responseJSON['success']
            },
            dataType: 'json',
            success: function (request) {
                show_success_snack('Успешно!');
                location.reload();
            },
            error: function (request) {
                console.log(request.responseJSON['error']);
                show_error_snack(request.responseJSON['error'])
            }
        };
        $.ajax(r);
    } else {
        show_error_snack(pic_link.responseJSON['error'])
    }
}

function apiv1_geteditairlaine(id) {
    let r = {
        url: '/api/v1/admin/editAirplane',
        type: 'GET',
        data: {airplane_id: id},
        dataType: 'html',
        success: function (request) {
            // request.responseJSON['success']
            $('#AdminAirplaneEditModalBody').html(request);
            $('#AdminAirplaneEditModal').modal();
        },
        error: function (request) {
            console.log(request);
            show_error_snack(request.responseJSON['error']);
        }
    };
    $.ajax(r);
}

function apiv1_posteditairlaine(id) {
    let r = {
        url: '/api/v1/admin/editAirplane',
        type: 'POST',
        data: {
            airplane_id: id,
            airplane_num: document.getElementById("airplane_num_edit").value,
            airplane_name: document.getElementById("airplane_name_edit").value,
            column_of_seats: document.getElementById("column_of_seats_edit").value,
            row_of_seats: document.getElementById("row_of_seats_edit").value,
            status: document.getElementById("status_edit").value
        },
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_returnairplanebutton(id) {
    let r = {
        url: '/api/v1/admin/returnAirplane',
        type: 'POST',
        data: {airplane_id: id},
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_addcountry() {
    let r = {
        url: '/api/v1/admin/country',
        type: 'PUT',
        data: {
            country_name: document.getElementById("country_name").value,
            abbreviation: document.getElementById("country_abbreviation").value
        },
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_delcountry() {
    let r = {
        url: '/api/v1/admin/country',
        type: 'DELETE',
        data: {country_id: $('#country_selector :selected').val()},
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_addcity() {
    let r = {
        url: '/api/v1/admin/city',
        type: 'PUT',
        data: {
            country_id: document.getElementById("city_country_select").value,
            city_name: document.getElementById("city_name").value,
            abbreviation: document.getElementById("city_abbreviation").value
        },
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_delcity() {
    let r = {
        url: '/api/v1/admin/city',
        type: 'DELETE',
        data: {city_id: $('#city_selector :selected').val()},
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_addairport() {
    let r = {
        url: '/api/v1/admin/airport',
        type: 'PUT',
        data: {
            airport_country_select: document.getElementById("airport_country_select").value,
            airport_city_select: document.getElementById("airport_city_select").value,
            airport_name: document.getElementById("airport_name").value,
            airport_abbreviation: document.getElementById("airport_abbreviation").value
        },
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_delairport() {
    let r = {
        url: '/api/v1/admin/airport',
        type: 'DELETE',
        data: {airport_id: $('#airport_selector :selected').val()},
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_addroute() {
    let r = {
        url: '/api/v1/admin/route',
        type: 'PUT',
        data: {
            airport_from: document.getElementById("airport_from").value,
            airport_to: document.getElementById("airport_to").value,
            departure_date: document.getElementById("departure_date").value,
            arrival_date: document.getElementById("arrival_date").value,
            airplane_id: document.getElementById("airplane").value,
            price: document.getElementById("price").value
        },
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            location.reload();
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_getairportslist() {
    country_id = $('#airport_country_select :selected').val();
    let r = {
        url: '/api/v1/admin/getCityList',
        type: 'GET',
        data: {country_id: country_id},
        dataType: 'json',
        success: function (request) {
            show_success_snack('Успешно!');
            console.log(request['city_inf']);
            text = '';
            request['city_inf'].forEach(function (item, i) {
                // alert(i + ": " + item);
                text += '<option value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
            });
            $('#airport_city_select').html(text);
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function apiv1_getcitylist(id) {
    let r = {
        url: '/api/v1/admin/getCityList',
        type: 'GET',
        data: {country_id: id},
        dataType: 'json',
        async: false,
        success: function (request) {

        },
        error: function (request) {
            console.log(request['error']);
        }
    };
    ask = $.ajax(r)
    if (ask.status == 200) {
        return ask.responseJSON
    } else {
        return []
    }
}

function apiv1_getairportlist(id) {
    let r = {
        url: '/api/v1/admin/getAirportList',
        type: 'GET',
        data: {city_id: id},
        dataType: 'json',
        async: false,
        success: function (request) {

        },
        error: function (request) {
            console.log(request['error']);
        }
    };
    ask = $.ajax(r)
    if (ask.status == 200) {
        return ask.responseJSON
    } else {
        return []
    }
}

function apiv1_getSearchResult(str) {
    let r = {
        url: '/api/v1/search',
        type: 'GET',
        data: {query: str},
        dataType: 'text',
        async: false,
        success: function (request) {
            console.log(request['result']);
        },
        error: function (request) {
            console.log(request);
        }
    };
    ask = $.ajax(r)
    if (ask.status == 200) {
        return ask.responseJSON
    } else {
        return []
    }
}


function getcitylist_add() {
    country_id = $('#airport_country_select :selected').val();
    req = apiv1_getcitylist(country_id);
    if (req != []) {
        if (req['city_inf'].length > 0) {
            text = '';
            req['city_inf'].forEach(function (item, i) {
                text += '<option value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
            });
            $('#airport_city_select').html(text);
        }
    }
}

function getCityList_main() {
    country_id = $('#country_selector :selected').val();
    req = apiv1_getcitylist(country_id);
    text = '';
    if (req != []) {
        if (req['city_inf'].length > 0) {
            req['city_inf'].forEach(function (item, i) {
                if (i == 0) {
                    text += '<option selected value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
                } else {
                    text += '<option value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
                }
            })
        }
    }
    $('#city_selector').html(text);
    if (text != '') {
        getAirportList_main();
    } else {
        $('#airport_selector').html(text);
    }
}


function getAirportList_main() {
    city_id = $('#city_selector :selected').val();
    req = apiv1_getairportlist(city_id);
    text = '';
    if (req != []) {
        if (req['airport_inf'].length > 0) {
            req['airport_inf'].forEach(function (item, i) {
                if (i == 0) {
                    text += '<option selected value=' + item['id'] + '>' + item['airport_name'] + ' [' + item['abbreviation'] + ']</option>'
                } else {
                    text += '<option value=' + item['id'] + '>' + item['airport_name'] + ' [' + item['abbreviation'] + ']</option>'
                }
            })
        }
    }
    $('#airport_selector').html(text);
}

function getCityList_AddRoute_From() {
    country_id = $('#country_from :selected').val();
    req = apiv1_getcitylist(country_id);
    text = '';
    if (req != []) {
        if (req['city_inf'].length > 0) {
            req['city_inf'].forEach(function (item, i) {
                if (i == 0) {
                    text += '<option selected value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
                } else {
                    text += '<option value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
                }
            })
        }
    }
    $('#city_from').html(text);
    if (text != '') {
        getAirportList_AddRoute_From();
    } else {
        $('#airport_from').html(text);
    }
    ;

}


function getAirportList_AddRoute_From() {
    city_id = $('#city_from :selected').val();
    req = apiv1_getairportlist(city_id);
    text = '';
    if (req != []) {
        if (req['airport_inf'].length > 0) {
            req['airport_inf'].forEach(function (item, i) {
                if (i == 0) {
                    text += '<option selected value=' + item['id'] + '>' + item['airport_name'] + ' [' + item['abbreviation'] + ']</option>'
                } else {
                    text += '<option value=' + item['id'] + '>' + item['airport_name'] + ' [' + item['abbreviation'] + ']</option>'
                }
            })
        }
    }
    $('#airport_from').html(text);
}

function getCityList_AddRoute_To() {
    country_id = $('#country_to :selected').val();
    req = apiv1_getcitylist(country_id);
    text = '';
    if (req != []) {
        if (req['city_inf'].length > 0) {
            req['city_inf'].forEach(function (item, i) {
                if (i == 0) {
                    text += '<option selected value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
                } else {
                    text += '<option value=' + item['id'] + '>' + item['city_name'] + ' [' + item['abbreviation'] + ']</option>'
                }
            })
        }
    }
    $('#city_to').html(text);
    if (text != '') {
        getAirportList_AddRoute_To();
    } else {
        $('#airport_to').html(text);
    }
    ;

}


function getAirportList_AddRoute_To() {
    city_id = $('#city_to :selected').val();
    req = apiv1_getairportlist(city_id);
    text = '';
    if (req != []) {
        if (req['airport_inf'].length > 0) {
            req['airport_inf'].forEach(function (item, i) {
                if (i == 0) {
                    text += '<option selected value=' + item['id'] + '>' + item['airport_name'] + ' [' + item['abbreviation'] + ']</option>'
                } else {
                    text += '<option value=' + item['id'] + '>' + item['airport_name'] + ' [' + item['abbreviation'] + ']</option>'
                }
            })
        }
    }
    $('#airport_to').html(text);
}

function api_getsearch(id, query) {
    $.ajax({
        type: 'GET',
        url: "/api/v1/search", //Путь к обработчику
        data: {query: query},
        dataType: 'json',
        async: false,
        success: function (data) {
            console.log(data['result'])
            $("#" + id).html(data['result']).fadeIn(); //Выводим полученые данные в списке
        }
    })
}

$(function () {
    $('#query_to').bind("keyup", function () {
        if (this.value.length >= 2) {
            api_getsearch('search_result_to', this.value)
        }
    })

    $("#search_result_to").hover(function () {
        $("#query_to").blur(); //Убираем фокус с input
    })

//При выборе результата поиска, прячем список и заносим выбранный результат в input
    $("#search_result_to").on("click", "li", function () {
        let item = $(this);
        if (item.text() === 'Ничего не найдено') {
            $("#search_result_to").fadeOut();
            $("#query_to").val('');
            $("#query_to").attr('data-id_to', '');
        } else {
            $("#search_result_to").fadeOut();
            $("#query_to").val(item.text());
            $("#query_to").attr('data-id_to', item.attr('id'));
        }
    })

    $('#query_from').bind("keyup", function () {
        if (this.value.length >= 2) {
            api_getsearch('search_result_from', this.value)
        }
    })

    $("#search_result_from").hover(function () {
        $("#query_to").blur(); //Убираем фокус с input
    })

//При выборе результата поиска, прячем список и заносим выбранный результат в input
    $("#search_result_from").on("click", "li", function () {
        let item = $(this);
        if (item.text() === 'Ничего не найдено') {
            $("#search_result_from").fadeOut();
            $("#query_from").val('');
            $("#query_from").attr('data-id_from', '');
        } else {
            $("#search_result_from").fadeOut();
            $("#query_from").val(item.text());
            $("#query_from").attr('data-id_from', item.attr('id'));
        }
    })
})

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(function () {
    $('#addpassanger').on('click', function () {
        if ($('#place_count').text() > $('#passenger').find('.passanger_add').length) {
            $('#passenger').find('.passanger_add').first().clone().insertAfter($('#passenger').find('.passanger_add').last())
        } else {
            alert('Нельзя добавить массажиров, больше, чем доступно мест на рейсе!')
        }
    });
})


$(document).ready(function () {
    $('#delpassanger').on('click', function () {
        if ($('#passenger').find('.passanger_add').length > 1) {
            $('#passenger').find('.passanger_add').last().remove()
        } else {
            alert('Должен остатся минимум один пассажир, для продолжения покупки!!')
        }
    });
})


function check_passenger_inf() {
    let passenger_id = [];
    let passenger_place = [];
    $('#passenger').find('.passenger_select option:selected').each(function (index) {
        passenger_id.push($(this).val())
    })
    $('#passenger').find('.passenger_select_place option:selected').each(function (index) {
        passenger_place.push($(this).val())
    })

    let r = {
        url: '/api/v1/checkticket',
        type: 'POST',
        data: {'route_id': $('#route_id').val(), 'passenger_id': passenger_id, 'passenger_place': passenger_place},
        dataType: 'json',
        success: function (request) {
            show_success_snack(request['success']);
            total_price = request['total_price'];
            total_price_text = '<h5>Итоговая цена: ' + total_price + 'р.</h5>'
            accept_button_text = '<button class="btn btn-dark" type="submit">Перейти к оплате</button>'
            $('#final_price').html(total_price_text);
            $('#addpassanger').empty();
            $('#delpassanger').empty();
            $('#addnewpassanger').empty();
            $('#accept_button').html(accept_button_text);
            $("[name='passenger']").prop('disabled', true)
            $("[name='places']").prop('disabled', true)
        },
        error: function (request) {
            console.log(request.responseJSON['error']);
            show_error_snack(request.responseJSON['error'])
        }
    };
    $.ajax(r);
}

function change_passenger_id(elem) {
    (function ($) {
        $.fn.findNext = function (sel) {
            var $result = $(sel).first();
            if ($result.length <= 0) {
                return $result;
            }
            $result = [];
            var thisIndex = $('*').index($(this));
            var selIndex = Number.MAX_VALUE;
            $(sel).each(function (i, val) {
                var valIndex = $('*').index($(val));
                if (thisIndex < valIndex && valIndex < selIndex) {
                    selIndex = valIndex;
                    $result = $(val);
                }
            });
            return $result;
        };
    })(jQuery);
    console.log($(elem))
    $($(elem)).findNext('input[name="passenger_id"]').val($(elem).val())
    console.log($($(elem)).findNext('input[name="passenger_id"]'))
}

function change_places_id(elem) {
    (function ($) {
        $.fn.findNext = function (sel) {
            var $result = $(sel).first();
            if ($result.length <= 0) {
                return $result;
            }
            $result = [];
            var thisIndex = $('*').index($(this));
            var selIndex = Number.MAX_VALUE;
            $(sel).each(function (i, val) {
                var valIndex = $('*').index($(val));
                if (thisIndex < valIndex && valIndex < selIndex) {
                    selIndex = valIndex;
                    $result = $(val);
                }
            });
            return $result;
        };
    })(jQuery);
    console.log($(elem))
    $($(elem)).findNext('input[name="places_id"]').val($(elem).val())
    console.log($($(elem)).findNext('input[name="places_id"]'))
}

function open_ticket_print(ticket_id) {
    show_success_snack('Билет формируется, пожалуйста подождите!');
    setTimeout(window.open, 5000, 'https://flightplus.ru/static/tickets/ticket-' + ticket_id + '.pdf');
}