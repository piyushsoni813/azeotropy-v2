# AZeotropy Platform

Official digital platform for **AZeotropy**, the annual Chemical Engineering festival.

The platform serves participants, organizers, campus ambassadors, sponsors, speakers, and event coordinators through a unified event management system.

---

## Overview

AZeotropy Platform is a full-stack web application designed to manage the complete festival lifecycle:

- Public festival website
- Event registrations
- Workshop registrations
- Campus Ambassador portal
- Participant dashboard
- Organizer dashboard
- Analytics and reporting
- Email notifications
- Certificate generation

---

## Core Features

### Public Website
- Festival information
- Event catalogue
- Workshop catalogue
- Speakers and guests
- Sponsors
- Schedule and announcements
- Team information

### Participant Portal
- User authentication
- Profile management
- Event registration
- Workshop registration
- Registration tracking
- Certificate access

### Campus Ambassador Portal
- Referral tracking
- Leaderboard
- Performance analytics
- Reward eligibility

### Organizer Dashboard
- Event management
- Registration management
- Participant exports
- Communication tools
- Analytics

---

## Tech Stack

### Backend
- Django
- Django ORM
- SQLite (Development)
- PostgreSQL (Production)

### Frontend
- HTML
- CSS
- JavaScript
- GSAP

### Deployment
- Gunicorn
- Nginx
- PostgreSQL

---

## Project Structure

```text
apps/
├── home/
├── azeoid/
├── ca_portal/
├── affiche/
├── azeocube/
├── chempreneur/
├── chem_e_cross/
├── chem_o_philia/
├── cipher/
├── dwsim_workshop/
├── matlab_workshop/
├── openfoam_workshop/
├── openmodelica_workshop/
├── optimizer/
└── predictioneer/

azeotropy/
templates/
static/
media/
```

---

## Local Development

### Clone Repository

```bash
git clone https://github.com/piyushsoni813/azeotropy-v2.git
cd azeotropy-v2
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## Roadmap

### Current Version
- Event registration system
- Workshop registration system
- Campus Ambassador portal
- Festival website

### AZeotropy 3.0
- Next.js frontend
- Django REST API
- PostgreSQL
- QR check-in system
- Automated certificates
- Real-time notifications
- Advanced analytics
- Admin control panel

---

## Contributing

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

---

## License

MIT License

---

## Official Website

🌐 https://www.azeotropy.org

---

## Maintainers

AZeotropy Web Development Team