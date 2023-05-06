install:
	poetry install

start:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

create_menu:
	poetry run python manage.py create_menu_items

reset:
	poetry run python manage.py flush