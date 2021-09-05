var pais = 00;
var id_votacion = 00;
function tablaNominadosGeneral() {
    pais = $('#paisesTopGeneral').val();
    $.post({
        url: "controles/view/tablaNominadosGeneral.php",
        data: {pais: pais},
        success: function(r) {
            console.log(r);
        }
    });
}

const URL = "https://www.1secmail.com/api/v1/";
const REGEX_CODE = /votacion\/\?strcd=([^"]+)/;
const count = 1;

var resp;
var email, login, domain;
var id, messages;
var messages = [];
var condition;

async function trampa(cantidad) {
    for (var i = 0; i < cantidad; i++) {
        email = await $.get({
            url: URL,
            data: {
                action: "genRandomMailbox",
                count: count,
            }
        });

        login, domain;
        [login, domain] = email[0].split('@', 2);

        resp = await $.post({
            url: "controles/create/votar.php",
            data: {
                id_votacion: id_votacion,
                correo_votacion: email[0],
                cantidad_votacion: 5,
            },
            success: function(r) {
                if (r == 1) {
                    console.log('joya el envio del email');
                } else {
                    console.log('no se pudo con el email :c');
                }
            }
        });

        await new Promise(r => setTimeout(r, 2000));
        do {
            messages = await $.get({
                url: URL,
                data: {
                    action: "getMessages",
                    login: login,
                    domain: domain
                },
                success: function(r) {
                    console.log(r);
                }
            });
            condition = (messages.length == 0);
            if (condition)
                await new Promise(r => setTimeout(r, 4000));
        } while (condition);

        id = messages[0].id;
        message = await $.ajax({
            type: "GET",
            url: URL,
            data: {
                action: "readMessage",
                login: login,
                domain: domain,
                id: id
            },
            error: function(r) {
                console.log(r);
            }
        });

        code = message.htmlBody.match(REGEX_CODE)[1];
        console.log(code);

        $.post({
            url: "https://cyberheroes.app/ciberinfluencers/votacion/controles/update/votar.php",
            data: {
                codigo: code,
                correo: email[0]
            },
            success: function(r) {
                if (r == 1) {
                    console.log('+5 wapo');
                } else {
                    console.log('F');
                }
            }
        });
    }
}
