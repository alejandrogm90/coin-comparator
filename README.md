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

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You need install first:

* _Bash_
* _Python3_

```sh
pip install -r requirements.txt
```

### Installation

- Go to main project at [https://github.com/alejandrogm90/coin-comparator][project-url]
- Clone the repo:
```sh
git clone https://github.com/alejandrogm90/coin-comparator.git
```

- Install all requirements:
```python
pip3 install -r 
```

- Configure django:

Create database
```python
python manage.py migrate
```
```python
python manage.py makemigrations coins
```
Create admin
```python
python manage.py createsuperuser
```


## Usage
To get a specific month use:
```sh
cd src 
./launch_month.sh connector_coinlayer_sqlitle.py 2022 1
```

To run server is required to use this sentence: 
```python
python manage.py runserver
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

Alejandro Gómez - [@alejandrogm90](https://github.com/alejandrogm90)

Project Link: [https://github.com/alejandrogm90/coin-comparator][project-url]

<!-- pip freeze > requirements.txt -->

[product-screenshot]: config/logo.png

[bash-shield]: https://img.shields.io/badge/bash-000000?style=for-the-badge&logo=gnubash&logoColor=white
[python-shield]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[django-shield]: https://img.shields.io/badge/django-000000?style=for-the-badge&logo=django&logoColor=white
[contributors-shield]: https://img.shields.io/github/contributors/alejandrogm90/coin-comparator.svg?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/alejandrogm90/coin-comparator.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/alejandrogm90/coin-comparator.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/alejandrogm90/coin-comparator.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/alejandrogm90/coin-comparator.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[bash-url]: https://www.gnu.org/software/bash/
[python-url]: https://www.python.org/
[django-url]: https://www.djangoproject.com/
[contributors-url]: https://github.com/alejandrogm90/coin-comparator/graphs/contributors
[forks-url]: https://github.com/alejandrogm90/coin-comparator/network/members
[stars-url]: https://github.com/alejandrogm90/coin-comparator/stargazers
[issues-url]: https://github.com/alejandrogm90/coin-comparator/issues
[license-url]: https://github.com/alejandrogm90/coin-comparator/blob/master/LICENSE.txt
[linkedin-url]: https://www.linkedin.com/in/alejandro-g-762869129/
[project-url]: https://github.com/alejandrogm90/coin-comparator
