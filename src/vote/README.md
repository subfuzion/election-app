# Vote service

The **vote** service provides an API for querying a Postgres database.

During development, there are a number of ways to test.

## 1. Use `docker compose` to test the database

### Run local tests against `postgres` in a container

Start `postgres` in one terminal:

```text
docker compose up postgres
```

Run database tests in another terminal:

```text
npm run postgres_test
```

Press `Ctrl-C` in the terminal running `postgres` when finished.

### Run `postgres` and database tests in containers:

In a terminal:

```text
docker compose run postgres_test
```

## 2. Use `docker compose` for integration tests

Integration tests launch both the `postgres` and `vote` services.

### Run local integration tests against `postgres` in a container

Start `postgres` and `vote` in one terminal:

```text
docker compose up postgres vote
```

Run tests in another terminal:

```text
npm run integration_test
```

### Run `postgres`, `vote`, and integration tests in containers:

In a terminal:

```text
docker compose run integration_test
```

## Important notes

When you modify source code, `docker compose` does not automatically
pick up these changes. You must run:

```text
docker compose build
docker compose restart
```

When you're finished testing, ensure you either

stop services:

```text
docker compose stop
```

or fully clean up by stopping and removing containers and netorks:

```text
docker compose down
```

To view logs, run:

    $ docker compose logs [service]
