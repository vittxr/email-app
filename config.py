import os 
   #operate system
   #com a lib os, podemos ter acesso ao sistema operacional

class Config:
   MAIL_SERVER=os.getenv("MAIL_SERVER") or 'alguma coisa'
   MAIL_PORT=os.getenv("MAIL_PORT") or 'alguma coisa'
   MAIL_USE_TLS=os.getenv("MAIL_USE_TLS") or 'alguma coisa'
   MAIL_USE_SSL=False#os.getenv("MAIL_USE_SSL") or 'alguma coisa'
   MAIL_USERNAME=os.getenv("MAIL_USERNAME") or 'alguma coisa'
   MAIL_PASSWORD=os.getenv("MAIL_PASSWORD") or 'alguma coisa'
       #Dessa forma, estamos pegando as variáveis de ambientes setadas em vars.ps1.
       #obs: o valor das variáveis é sempre 'alguma' coisa, pois não se está pegando as vars de ambiente.

class Desenvolvimento(Config):
   DEBUG = True

class Teste(Config):
   DEBUG = True

class Producao(Config):
   DEBUG = False

config = {
   'dev': Desenvolvimento, 
   'test': Teste,
   'prod': Producao,

   'default': Desenvolvimento  
      #Observe que não instanciamos as classes, mas só chamamos. Sem o construtor __init__ na classe, os atributos são criadas qnd o arquivo é executado. Por isso, não é necessário instanciar, pois não estamos criando um objeto, mas só pegando as informações da classe. Poderíamos fazer isso com função, mas uma vez que a função é chamada, ela executa um processo. Nesse caso, estamos só acessando os atributos da classe já criados.
}