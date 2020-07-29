## weddingshop
### Quickstart

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Docker

Build the image and run the container:

```sh
$ docker-compose up -d
```

Browse [localhost:8000](http://localhost:8000)

#### Manual Installation

```sh
$ git clone https://github.com/lfbatista/movies_project.git
```

or [download](https://github.com/lfbatista/weddingshop/archive/master.zip) this repository.

```sh
$ pip install -r requirements.txt
$ python manage.py migrate --run-syncdb
$ # to populate the db with some initial data:
$ (echo "import import_data"; echo "import_data.import_data()") | python manage.py shell
$ python manage.py runserver
```

Browse [localhost:8000](http://localhost:8000)

##### Testing

```sh
$ python manage.py test
``` 
