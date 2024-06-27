## xerpa-test

### Running the development environment

* `docker-compose build `
* `docker-compose up  -d`


### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000

### how to run the tests
* `docker-compose exec web bash`
* `pytest`

### how to test our endpoint
`curl -X POST \
  http://your_domain/api/enrichment/ \
  -H 'Content-Type: application/json' \
  -d '{
    "transactions": [
      {
        "id": "ff1f557e-2aea-4b57-9088-2deeccd67e68",
        "description": "keyword1",
        "amount": 100.0,
        "date": "2024-06-28"
      },
      {
        "id": "6b4da43a-bf51-4451-9523-4a54823f9cd3",
        "description": "KEYWORD2 * BLAH",
        "amount": 150.0,
        "date": "2024-06-28"
      }
    ]
  }'
`