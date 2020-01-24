rm -rf budgetappapi/migrations
rm db.sqlite3
python manage.py makemigrations vendingTestapi
python manage.py migrate
python manage.py loaddata coin
python manage.py loaddata inventory

# 1. Save that in a Reset_db.sh file
# 2. Run chmod +x Reset_db.sh (in bash only not Windows Terminal)
# 3. Run ./Reset_db.sh