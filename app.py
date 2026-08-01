import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["DATABASE_URL"] = os.getenv(
        "DATABASE_URL",
        "postgresql://localhost:5432/portfolio_db",
    )

    def init_db() -> None:
        schema_path = BASE_DIR / "schema.sql"
        with psycopg2.connect(app.config["DATABASE_URL"]) as connection:
            with connection.cursor() as cursor:
                cursor.execute(schema_path.read_text(encoding="utf-8"))

    def insert_message(name: str, email: str, message: str) -> None:
        with psycopg2.connect(app.config["DATABASE_URL"]) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO contact_messages (name, email, message)
                    VALUES (%s, %s, %s)
                    """,
                    (name, email, message),
                )

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            message = request.form.get("message", "").strip()

            errors = []
            if len(name) < 2:
                errors.append("Name must be at least 2 characters long.")
            local, _, domain = email.partition("@")
            if not local or not domain or "." not in domain or domain.startswith(".") or domain.endswith("."):
                errors.append("Please provide a valid email address.")
            if len(message) < 10:
                errors.append("Message must be at least 10 characters long.")

            if errors:
                for error in errors:
                    flash(error, "error")
                return render_template("contact.html", form_data=request.form), 400

            try:
                init_db()
                insert_message(name=name, email=email, message=message)
                flash("Thanks for your message! I will get back to you soon.", "success")
                return redirect(url_for("contact"))
            except psycopg2.Error:
                flash(
                    "Could not save your message right now. Please try again later.",
                    "error",
                )
                return render_template("contact.html", form_data=request.form), 500

        return render_template("contact.html", form_data={})

    @app.post("/init-db")
    def initialize_database():
        try:
            init_db()
            flash("Database initialized successfully.", "success")
        except psycopg2.Error:
            flash("Database initialization failed.", "error")
        return redirect(url_for("index"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
