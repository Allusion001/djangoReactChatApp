set -o errexit

pip install -r requirements.txt

python3 manage.py collectstatic --no-input