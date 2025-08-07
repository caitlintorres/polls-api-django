# Django Polls API

A simple backend API built using Django and Django REST Framework to manage polls, questions, and voting.

## Features

- Create and manage polls with multiple questions
- Vote on questions with multiple choices
- API endpoints for polls, questions, and choices

## Requirements

- Python 3.8+
- pip (Python package installer)
- virtualenv (recommended)

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/polls-api-django.git
cd polls-api-django
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

## API Endpoints

| Method | Endpoint              | Description             |
|--------|-----------------------|-------------------------|
| GET    | /api/polls/           | List all polls          |
| POST   | /api/polls/           | Create a new poll       |
| GET    | /api/polls/<id>/      | Retrieve poll details   |
| POST   | /api/polls/<id>/vote/ | Vote on a poll question |
