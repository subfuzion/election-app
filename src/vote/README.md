# Vote service

The **vote** service provides an API for querying a Postgres database.

## API endpoints

### `HEAD /`

Use for healthchecks; for example:

```text
test `curl -I -s -o /dev/null -w '%{http_code}' localhost:8080` = 200
```

### `POST /vote`

Submit a vote.

**Request**

All fields are required except `voter_id`.

```json
{
  "voter": {
    "voter_id": "",
    "county": "",
    "state": ""
  },
  "candidate": {
    "name": "",
    "party": ""
  }
}
```

**Response**

Success:

```json
{
    "success": true,
    "data": {}
}
```

`data`: the original request body plus the generated value for `voter_id`

Error:

```json
{
    "success": false,
    "reason": ""
}
```

### `GET /tally/candidates`

## Development

During vote service development, there are a number of ways to test.

### 1. Use `docker compose` to test the database

#### Run local tests against `postgres` in a container

Start `postgres` in one terminal:

```text
docker compose up postgres
```

Run database tests in another terminal:

```text
export PGHOST=localhost
npm run postgres_test
```

Press `Ctrl-C` in the terminal running `postgres` when finished.

#### Run `postgres` and database tests in containers:

In a terminal:

```text
docker compose run postgres_test
```

### 2. Use `docker compose` for integration tests

Integration tests launch both the `postgres` and `vote` services.

#### Run local integration tests against `postgres` in a container

Start `postgres` and `vote` in one terminal:

```text
docker compose up postgres vote
```

Run tests in another terminal:

```text
export PGHOST=localhost
npm run integration_test
```

#### Run `postgres`, `vote`, and integration tests in containers:

In a terminal:

```text
docker compose run integration_test
```

### Important notes

#### Rebuilding images

When you modify source code, `docker compose` does not automatically
pick up these changes. You must run:

```text
docker compose build
docker compose restart
```

#### Viewing logs

To view logs in a separate terminal, run:

    $ docker compose logs [service] [-f]

#### Clean up

When you're finished testing, ensure you either

stop services:

```text
docker compose stop
```

or fully clean up by stopping and removing containers and netorks:

```text
docker compose down
```
