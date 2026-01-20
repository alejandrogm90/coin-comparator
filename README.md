[![Version][version-shield]][version-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/alejandrogm90/coin-comparator)

About The Project

### Built With

Frameworks and libraries used to bootstrap the project:

* [![Bash][bash-shield]][bash-url]
* [![Python][python-shield]][python-url]
* [![Django][django-shield]][django-url]
* Chartjs [Official Website](https://www.chartjs.org/)

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You need install first:

* _Bash_
* _Python3_

### Installation

- Go to main project at [https://github.com/alejandrogm90/coin-comparator][project-url]
- Clone the repo:

```shell
$ git clone https://github.com/alejandrogm90/coin-comparator.git
```

- Install all requirements:

```shell
$ pip install -r requirements.txt
```

- Configure django:
  Create basic database

```shell
$ ./web/manage.py migrate
$ ./web/manage.py makemigrations
```

Create coins database

```shell
$ ./web/manage.py migrate coins
$ ./web/manage.py makemigrations coins
```

Create admin for all

```shell
$ ./web/manage.py createsuperuser
```

## Usage

How to get data from web:

```shell
# If we are using coinlayer
# To launch a specific month and download data saving it in json
$ ./src/launch_month.sh src/connectors/coinlayer_json.py 2022 1
# To launch a specific month and download data saving it in sqlitle
$ ./src/launch_month.sh src/connectors/coinlayer_sqlittle.py 2022 1
# To launch a specific month and download data saving it in mongodb
$ ./src/launch_month.sh src/connectors/coinlayer_mongodb.py 2022 1
# To launch a specific month and loading from our data and saving in sqlitle
$ ./src/launch_month.sh src/connectors/coinlayer_json_load_sqlittle.py 2022 1
```

Changing our data:

```shell
# If we are using coinlayer
# To launch a specific month and loading from our data and saving in sqlitle
$ ./src/launch_month.sh src/connectors/coinlayer_json_load_sqlittle.py 2022 1
# To launch a specific year and save it in XLSX, CSV, JSON and PARQET
$ ./src/save_year_using_dataframe.py 2022 coinlayer
# To load a complete year in parquet format
$ pipenv run python src/save_year_using_dataframe.py 2022
```

To run web server is required to use this sentence:

```shell
$ ./web/manage.py runserver
```

To run agents:

```shell
$ pipenv run python run_test.py
```

To run tests:

```shell
$ pipenv run python run_test.py
```

_For more examples, please refer to the [Documentation][project-url]_

## Roadmap

- [X] Add basic microservices
- [X] Add basic WEB UI
- [ ] Add other languages
    - [ ] Spanish
    - [ ] French
    - [ ] Chinese

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the License. See `LICENSE.txt` for more information.

## Contact

Alejandro Gómez - [@alejandrogm90][project-url]

[Project Link][project-url]

<!-- 
pip freeze > requirements.txt 
pipreqs --force

# Test
python3 -m pip install coverage
python3 -m unittest discover

# Coverage - https://coverage.readthedocs.io/en/7.6.10/
pipenv run python -m coverage run my_program.py arg1 arg2
pipenv run python -m coverage run --source=tests
pipenv run python -m coverage --source=tests html
pipenv run python -m coverage --source=tests --directory=DIR html

-->

[product-screenshot]: config/logo.png

[version-shield]: https://img.shields.io/badge/version-0.1.0-blue?style=for-the-badge

[bash-shield]: https://img.shields.io/badge/bash-000000?style=for-the-badge&logo=gnubash&logoColor=white

[python-shield]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white

[django-shield]: https://img.shields.io/badge/django-000000?style=for-the-badge&logo=django&logoColor=white

[contributors-shield]: https://img.shields.io/github/contributors/alejandrogm90/coin-comparator.svg?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/alejandrogm90/coin-comparator.svg?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/alejandrogm90/coin-comparator.svg?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/alejandrogm90/coin-comparator.svg?style=for-the-badge

[license-shield]: https://img.shields.io/github/license/alejandrogm90/coin-comparator.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[project-url]: https://github.com/alejandrogm90/coin-comparator

[version-url]: https://github.com/alejandrogm90/coin-comparator/

[bash-url]: https://www.gnu.org/software/bash/

[python-url]: https://www.python.org/

[django-url]: https://www.djangoproject.com/

[contributors-url]: https://github.com/alejandrogm90/coin-comparator/graphs/contributors

[forks-url]: https://github.com/alejandrogm90/coin-comparator/network/members

[stars-url]: https://github.com/alejandrogm90/coin-comparator/stargazers

[issues-url]: https://github.com/alejandrogm90/coin-comparator/issues

[license-url]: https://github.com/alejandrogm90/coin-comparator/blob/master/LICENSE.txt

[linkedin-url]: https://www.linkedin.com/in/alejandro-g-762869129/
