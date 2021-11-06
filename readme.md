# "Answer correctly to go further" telegram bot

## How to use

Create `config.json` in the root using [config.example.json](config.example.json) as an example

```json
{
  "token": "A telegram bot token",
  "logger_chat": {
    "token": "A logging telegram bot token. This section is optional",
    "chat_id": "A logging chat ID. Integer, not string"
  },
  "quiz": {
    "welcome_message": "Welcome!",
    "welcome_again_message": "Welcome, again!",
    "steps": [
      {
        "question": "2 + 2?",
        "correct_answer": "4",
        "correct_answer_message": "Yes",
        "wrong_answer_message": "No"
      },
      {
        "question": "5 x 5?",
        "correct_answer": "25",
        "correct_answer_message": "Yes, it is",
        "wrong_answer_message": "No, no, no"
      }
    ],
    "complete_message": "The game is completed"
  }
}
```

Run the application by `docker-compose`

```shell
$ docker-compose up app
```
