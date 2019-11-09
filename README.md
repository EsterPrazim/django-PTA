# [CITi - PTA - 2019.2] Treinamento - Django

## 1. Instalação de ferramentas
Vamos precisar de três coisas essenciais para este treinamento: **Python**, **Virtualenv** e **Django**.

### 1.1. Instalando Python na sua máquina

#### Windows
- Usem o [site do Python](https://www.python.org/downloads/) para fazer o download.

#### Linux
- Usem o seguinte comando no terminal:

```sudo apt install python3.7```

- Confiram se o **python** foi instalado digitando:

```python --version```

- No ***linux***, pode ser necessário você usar:

```python3 --version```

- No windows, caso você não tenha selecionado a opção durante a instalação, pode ser necessário configurar a [variável de ambiente](https://python.org.br/instalacao-windows/) do **python**.

- Confiram se o **pip** foi instalado digitando: 

```pip --version```

- Geralmente o **pip** já vem instalado com o python, pois é ele que é utilizado para fazer instalações adicionais como o **django** por exemplo.

### 1.2. Instalando a Virtualenv na sua máquina

#### Windows
- Usem o comando:

```pip install virtualenv```

#### Linux
- Usem o comando:

```sudo apt install python3-venv```

ou

```apt install python3-venv```


## 2. Criando um ambiente virtual

#### 2.1. Criar a pasta do projeto
Pelo terminal, vocês vão entrar na pasta onde seu projeto vai ficar:

- Entrem no Desktop:

```cd Desktop```

- Criem a pasta do projeto

```mkdir django-pta```

- Entrem na pasta:

```cd django-pta```

#### 2.2. Criar o ambiente virtual
Agora que você já está dentro da pasta, você deve criar sua *virtualenv*.

- Digite no terminal:

```virtualenv venv```

- Por convenção, utilizamos o nome *venv*, mas você pode adicionar qualquer nome.
- Obs: Lembrem-se de adicionar ***venv/*** no ***gitignore*** para caso a **venv** seja criada dentro da pasta do projeto, ela não ir para o **github**.

#### 2.3. Iniciar o ambiente virtual
Finalmente, vamos iniciar o ambiente virtual para realizar as instalações adicionais do ***python***.

#### Windows
- Usem o comando:

```venv\Scripts\activate```

#### Linux
- Usem o comando:

```source venv/bin/activate```

- Lembrem-se que para **desativar** a ***virtualenv***, basta utilizar o comando:

```deactivate```

## 3. Instalando o **Django**
Agora que você já está com a **venv** ativada, para instalar o **Django**, basta fazer:

```pip install django```

- Agora você deve verificar se o **Django** foi instalado, basta digitar:

```pip freeze```

- Esse comando vai listar todas as dependências instaladas na **venv**.
- Sempre que você instalar uma dependência nova, você deve usar:

```pip freeze > requirements.txt```

- Esse comando vai escrever as dependências num arquivo chamado **requirements.txt**
- Lembre-se de sempre que baixar o projeto ou mudar de *branch* usar o comando (com a **venv** ativada):

```pip install -r requirements.txt```

- Este comando vai instalar todas as dependências que foram instaladas no projeto.

## 4. Criando seu projeto
Você já está dentro da **venv** e também já está com todos requerimentos instalados. Vamos agora criar o projeto pelo django.

### 4.1. Criando o projeto django
Na pasta onde está a **venv** que deve ser a pasta que você está mandando pro **github**, você deve digitar:

```django-admin startproject ptaDjango .```

- Agora você criou o projeto do django e basta entrar na pasta dele.
- Digite o comando:

```cd ptaDjango```

### 4.2. Iniciando uma app
Agora que já estamos dentro da pasta do projeto, nós podemos criar um *app*, idealmente você deve separar seus projetos em *apps* diferentes como *users, blog, core, contato*... Fazendo isso seu projeto será muito mais amigável para o desenvolvedor.

- No terminal, use o comando:

```python manage.py startapp core```

- *Core* é o *app* principal do projeto e nós acabamos de criar ele.
- Agora basta você ir em `settings.py` que fica localizado em ***ptaDjango/ptaDjango*** e colocar em ***INSTALLED_APPS*** o *app core*, `'core'`.

### 4.3. Migrações
Estamos com *quase* tudo pronto, mas mesmo que agora ainda não seja necessário, é bom que você tenha em mente que sempre que baixar o projeto ou fazer alterações no model, devem rodar esses comandos:

```
python manage.py makemigrations
python manage.py migrate
```

- Esses comandos lidam com as mudanças no *banco de dados* e muitas vezes seu projeto pode não rodar porque você não utilizou os dois.

### 4.4 Rodando o projeto
Finalmente você vai rodar o projeto e ver um exemplo do **django** rodando.

- Digite o comando:

```
python manage.py runserver
```

- Com esse comando seu *app* vai rodar e você será capaz de ver uma **url** no terminal. Copiando e colando a **url** num navegador abrirá uma mensagem do **django** de sucesso como esta:

![imagem de sucesso do django](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/eb_django_deployed.png)

- Se você viu essa imagem ou algo do tipo, deu tudo certo, parabéns.