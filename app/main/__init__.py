from flask import Blueprint  
  #Blueprint é uma planta, que serve para definir as rotas (planta de construção no caso, plano da estrutura)
  #Basicamente, blueprint é um gerenciador de rotas.
  
main = Blueprint('main', __name__)
  #note que definimos o main como uma planta, então na hora de definir as rotas, usa-se main.routes.
    
from app.main import views
  #para acessar pastas dentro de outras, utiliza-se o ponto
  #note que estamos importando o views depois de criar o main, isso porque o arquivo views importa a variável main (que contém a blueprint). Se fizéssemos essa importação antes da criação do main, entraríamos numa importação circular. (um loop de uma importação importando outro)
  #views é onde estão as rotas de visualização (views), podemos criar mais futuramente como login, erros, etc). Ou seja, estamos organizando nossa blueprint com todas as rotas da aplicação.
