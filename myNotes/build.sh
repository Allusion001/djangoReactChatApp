set -o errexit

pip install -r requirements.txt

pyhton3 manage.py collectstatic --no-input