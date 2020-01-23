rm -rf budgetappapi/migrations
rm db.sqlite3
python manage.py makemigrations vendingTestapi
python manage.py migrate