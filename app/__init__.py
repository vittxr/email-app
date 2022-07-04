#O nome desse arquivo é __init__, e isso é um conceito muito importante, pois ele é usado como um pacote no python.
#pacote: conjunto de arquivos, que facilita a importação, pois você importa um pacote com todas as importações
import os
from flask import Flask
from flask_mail import Mail
from config import config

global mail
mail = Mail()

def create_app(config_name):
    #essa função é uma fábrica de app. 
    app = Flask(__name__)
    app.config.from_object(config[config_name])
      #note que, para criar a aplicação, fizemos uma função, pois só queremos que o app seja criado somente quando a função for chamada. Além disso, observe que não passamos as configurações das variáveis de ambiente aqui
    mail.init_app(app)
      #init_app é o método que inicializa o Mail().

      #o problema é que eu não estou conseguindo obter o valor das variáveis de ambiente no arquivo config.

    from app.main import main as main_bp
      #é uma boa prática importar como main_bp, pois main é algo bem abstrato...
    app.register_blueprint(main_bp)
      #estamos registrando a blueprint que criamos no app;

    return app