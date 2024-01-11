<!-- selected option -->
<!-- favicon -->

<h1 align="center">Python + Flask + Sqlite</h1>

## usage

As everything is installed correctly, you can run app with:

```sh
python app.py
```

## Environment description

We all know how backend works: with `GET` and `POST` requests (and not only) front communicates to server, which responds with some actual data. `flask` lives within `Python`, it is casebook of routs request methods and data gathering/sending instructions, which is stored in SQL database (database.db). `flask` works like real server: it gets request from html `form`, executes proper SQL query, gets data from database and displays it in HTML via `jinja2`. `sqlite` is just one lightweight library which works according to SQL principles

you will find `log.sql` file in project. it helps to execute SQL queries and test them while implementing it in flask. you can simultaneously launch second terminal and execute queries written in `log.sql`.

```sh
cat log.sql | sqlite3 database.db
```

- [Sqlite.org](https://www.sqlite.org/doclist.html)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/#user-s-guide)
- [W3schools](https://www.w3schools.com/sql/default.asp)
