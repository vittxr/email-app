import os  
import app
from app import create_app
  #observe que estamos importando create_app de uma pasta e não de um arquivo. Quando se tem um arquivo __init__.py dentro de uma pasta, o python entende que ele é o pacote, então a pasta é importada por completo. Dentro de __init__ fica todos os arquivos que precisamos. Para ficar mais claro, há um exemplo nas aulas de backend.

app = create_app('default')

if __name__ == "__main__":
    app.run(debug=True)
 