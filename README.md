# AZeotropy

The website behind **AZeotropy**, the annual chemical engineering symposium run by students at IIT Bombay. It's the public face of the festival — event and workshop pages, the team and sponsor sections, the schedule — and it also handles the parts that need a database: participant registration, the AZeo ID system, and the campus ambassador portal.

This is a server-rendered Django application. There's no separate frontend framework and no API layer in active use yet. Pages are Django templates with vanilla JavaScript and a bit of GSAP driving the animations.

## What's actually in here

The project lives in a single Django project package (`azeotropy/`), with the real work split across apps under `apps/`. Five of those apps are wired into the project today:

- **`home`** renders the public site: the landing page, header and footer, and the competitions, events, workshops, team, sponsors, and schedule pages.
- **`azeoid`** is the registration flow. A participant submits their name, email, phone, college, and level of study (BTech / MTech / PhD), and the app issues them a unique AZeo ID. Note that this is registration-and-identity, not full password authentication — there are no login sessions tied to it yet.
- **`ca_portal`** is the Campus Ambassador portal, where ambassadors register and receive their own AZeo ID. The models capture contact and college details; the link to Django's built-in `User` model is stubbed out (commented) for now.
- **`chem_e_cross`** and **`chem_o_philia`** cover two of the symposium's competitions.

You'll also notice a dozen more folders under `apps/` — `affiche`, `azeocube`, `chempreneur`, `cipher`, `idp`, `optimizer`, `predictioneer`, and the workshop apps (`dwsim_workshop`, `matlab_workshop`, `openfoam_workshop`, `openmodelica_workshop`). These are scaffolding for individual events and workshops. They exist in the tree but aren't registered in `INSTALLED_APPS`, so they don't do anything until someone wires them up. Worth knowing before you go hunting for where their logic lives.

Data sits in SQLite for now. Registrations and ambassador entries are managed through the Django admin, with `django-import-export` available there for pulling participant data out as spreadsheets.

## Tech stack

Django 5.1.4 on Python, SQLite for storage, and the Django admin for back-office work. The front end is plain HTML, CSS, and JavaScript, with GSAP 3.12.5 and Splitting.js handling the motion and text effects.

A few libraries show up in `requirements.txt` but aren't switched on yet. Django REST Framework, django-ckeditor, and django-cors-headers are installed but missing from `INSTALLED_APPS` and the middleware — groundwork for an API and rich-text editing that hasn't landed. Don't be surprised when they turn out to be inert.

## Running it locally

You'll need Python 3.12+ and git.

Clone the repo and step into it:

```bash
git clone https://github.com/piyushsoni813/azeotropy-v2.git
cd azeotropy-v2
```

Set up a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Now the part the app won't start without. `settings.py` loads its secrets from a `.env` file and raises an error immediately if `DJANGO_SECRET_KEY` is missing. That file has to sit *next to the settings* — at `azeotropy/.env`, inside the package, not in the project root. This trips people up, so create it there:

```ini
# azeotropy/.env
DJANGO_SECRET_KEY=replace-with-a-long-random-string
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Only needed if you're actually sending email:
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_HOST_USER=you@example.com
EMAIL_HOST_PASSWORD=your-app-password
```

For everyday local work, `DJANGO_SECRET_KEY` plus `DEBUG=True` is enough; the email block only matters once a view tries to send mail. You can generate a key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then run the migrations, create an admin user, and start the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The site comes up at http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/.

## Environment variables

Everything `settings.py` reads, in one place:

| Variable | Required | Default | Notes |
| --- | --- | --- | --- |
| `DJANGO_SECRET_KEY` | Yes | — | App refuses to start without it. |
| `DEBUG` | No | `False` | Set `True` for local development. |
| `ALLOWED_HOSTS` | No | empty | Comma-separated; required once `DEBUG=False`. |
| `EMAIL_HOST` | No | — | SMTP server. |
| `EMAIL_PORT` | No | `465` | |
| `EMAIL_USE_SSL` | No | `False` | |
| `EMAIL_HOST_USER` | No | — | Also used as the default "from" address. |
| `EMAIL_HOST_PASSWORD` | No | — | |

There's no `.env.example` committed — the `.gitignore` is set up to allow one if it's ever added — so the table above is the reference until then.

## Project layout

```text
azeotropy/          # Django project: settings, root URLs, WSGI/ASGI
apps/               # Feature apps (see "What's actually in here")
templates/          # Server-rendered HTML, grouped by section
static/             # CSS, JS (GSAP, Splitting), and images
manage.py
requirements.txt
```

Routing lives in `azeotropy/urls.py`: the home app sits at the root, `azeoid` under `/azeoid/`, the ambassador portal under `/ca/`, and the admin under `/admin/`.

## Contributing

The usual flow — fork, branch, commit, open a pull request. If you're picking up one of the scaffolded event or workshop apps, start by registering it in `INSTALLED_APPS` and giving it a `urls.py` that the project includes. The apps that are already wired up are the pattern to copy.

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Links

Festival site: https://www.azeotropy.org
