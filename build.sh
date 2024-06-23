apt-get install libpq-dev
pip3 install -r requirements.txt
python3.9 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate


