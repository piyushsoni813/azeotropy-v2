# AZeotropy

Official website and management platform for **AZeotropy**, the annual Chemical Engineering technical festival of IIT (replace with official institute name if needed).

AZeotropy serves as a centralized platform for participants, organizers, campus ambassadors, sponsors, and event coordinators. The platform manages event registrations, workshops, competitions, participant data, communication, and festival information.

---

## Features

### Public Website
- Festival information
- Event listings
- Workshop details
- Sponsor showcase
- Team and coordinator profiles
- Schedule and announcements

### Participant Portal
- User registration and authentication
- Event registrations
- Workshop registrations
- Participant dashboard
- Registration status tracking

### Campus Ambassador Portal
- CA registration
- Referral tracking
- Performance leaderboard
- Certificate eligibility management

### Organizer Dashboard
- Event management
- Participant management
- Registration analytics
- Communication tools
- Data export utilities

---

## Tech Stack

### Backend
- Django
- SQLite (development)
- PostgreSQL (recommended for production)

### Frontend
- Django Templates
- HTML
- CSS
- JavaScript
- GSAP Animations

### Deployment
- Gunicorn
- Nginx
- PostgreSQL
- Redis (future)

---

## Project Structure

```text
apps/
├── azeoid/
├── ca_portal/
├── affiche/
├── azeocube/
├── chempreneur/
├── chem_e_cross/
├── chem_o_philia/
├── cipher/
├── optimizer/
├── predictioneer/
├── workshops/
└── home/

azeotropy/
templates/
static/
media/