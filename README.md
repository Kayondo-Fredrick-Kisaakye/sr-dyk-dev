# Portfolio Starter (Flask + PostgreSQL)

A beginner-friendly full-stack portfolio starter built with:

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** PostgreSQL

## Features

- Responsive portfolio layout (hero, about, projects)
- Contact page with form
- PostgreSQL-powered contact message storage
- Basic server-side validation and flash feedback
- Mobile nav toggle, smooth scrolling, active nav state, and simple form UX text

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── schema.sql
├── .env.example
├── templates/
│   ├── base.html
│   ├── index.html
│   └── contact.html
└── static/
    ├── css/
    │   └── styles.css
    └── js/
        └── main.js
```

## 1) Clone and Enter Project

```bash
git clone https://github.com/Kayondo-Fredrick-Kisaakye/sr-dyk-dev.git
cd sr-dyk-dev
```

## 2) Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3) Install Dependencies

```bash
pip install -r requirements.txt
```

## 4) Create PostgreSQL Database

Open PostgreSQL and run:

```sql
CREATE DATABASE portfolio_db;
```

## 5) Configure Environment Variables

Copy `.env.example` to `.env` and update values if needed:

```bash
cp .env.example .env
```

Default values in `.env.example`:

- `FLASK_APP=app.py`
- `FLASK_ENV=development`
- `SECRET_KEY=change-me`
- `DATABASE_URL=postgresql://localhost:5432/portfolio_db`

> If your local PostgreSQL requires username/password, use a connection string like:
> `postgresql://<username>:<password>@localhost:5432/portfolio_db`

## 6) Run the App

```bash
flask run
```

Open: `http://127.0.0.1:5000`

## Contact Form + Database

- The `/contact` route handles form display and submission.
- On submission, Flask validates input (`name`, `email`, `message`).
- The app runs `schema.sql` to ensure the `contact_messages` table exists.
- Valid submissions are inserted into PostgreSQL.

Table schema:

- `id` (serial primary key)
- `name`
- `email`
- `message`
- `created_at` (timestamp)

## Quick Customization

- Update name/title/project cards in `templates/index.html`
- Adjust colors/layout in `static/css/styles.css`
- Extend interactions in `static/js/main.js`
