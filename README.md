# Dummy Model Backend

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jayraj-kl/dummy-model-backend.git
   cd dummy-model-backend
   npm install
   pip install sys pickle pandas
   ```

## API Endpoints
GET /
Description: Returns a welcome message.

Response:
```bash
    {
    "message": "Hello, TypeScript with Express!"
    }
```
POST /
Description: Accepts a movie title in the request body and returns a list of recommended movies.

Request Body:
```bash
{
  "title": "Big Hero 6"
}
```
Response:
```bash
{
  "movies": [
    {
      "movie": "Robots"
    },
    {
      "movie": "Heartbeeps"
    },
    {
      "movie": "I, Robot"
    },
    {
      "movie": "Bill & Ted's Bogus Journey"
    },
    {
      "movie": "Real Steel"
    }
  ]
}
```
