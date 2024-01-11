<!-- selected option -->
<!-- favicon -->

<h1 align="center">Python + Django</h1>

![sdfg](https://github.com/tsotneforester/SportsApp/assets/79293287/50b37689-fffb-4768-a05c-be37fef59862)


## intro

[CS50](https://pll.harvard.edu/course/cs50-introduction-computer-science])/[CS50W](https://pll.harvard.edu/course/cs50s-web-programming-python-and-javascript]) flourished some new framworks and programming languages of web development: Python, Django, Flask, Sqlite. Despite cloud coding with CS50 libraries was piece of cake, setting up local Python working environment could have been more comfortable for final projects.
My initial desire was to create simple setup guide, but as you might have already guessed, it turned out to be setup + simple app, just to showcase general POST and GET request handling.

## about

The app is simplies in the filed of CRUD demonstaration ideas. Form submits name and sport. entries are displayes as table with edit and delete capabilities. There are 2 versions of the same app:

- using Python + Flask + Sqlite
- using Python + Django

## Environment setup + usage

- **_Python_** - Install it directly from [Python](https://www.python.org/downloads/windows/). Check installation status

```sh
python --version
```

- **_Django_** - `pip` is a package manager for Python packages, or modules. Django is one of them. To install it, run command:

```sh
py -m pip install Django
```

check status:

```sh
py -m django --version
```

- **_Flask_** - `pip` is a package manager for Python packages, or modules. Flask is one of them. To install it, run command:

```sh
pip install Flask
```

check status:

```sh
pip show flask
```

- **_Sqlite_** - Another simple step, but not classical one though, not installing `.exe` file, nor with `pip`. Here is [link](https://www.youtube.com/results?search_query=sqlite+installation+windows+10) how to do it.

As everything is installed correctly, you can run app with:

```sh
py -m manage runserver
```

## Acknowledgments

I've included a few of helpful resources!

- [Django](https://www.djangoproject.com/)
- [W3schools](https://www.w3schools.com/django/index.php)
