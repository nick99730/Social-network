# Social network
This Django tutorial app was created for the purpose of demonstrating Django. It shows the basics
of writing a MVC endpoint. With this application you can edit personal data, as well as upload a new photo.

If you just want to try my code out, I suggest using the Quick Start.

## Quick Start
Installation Steps if you want to try it out
```bash
git clone https://github.com/nick99730/Social-network.git
virtualenv -p python3.6.3 venv
source venv/bin/activate
pip install -r requirements.txt
cd Social network
python manage.py migrate
python manage.py collectstatic
python manage.py runserver # starts the server 
```
To edit personal data, click the "Edit" button under the photo.

## Requirements
* Python 3.6+
* Django 2.0.1
* Pillow

Please see [requirements.txt](requirements.txt) for more information.
