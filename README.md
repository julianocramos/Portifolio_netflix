# 🎬 DevFlix

A Netflix-inspired streaming platform built with **Python and Django**, modernized as a portfolio project to demonstrate backend development, authentication, database integration, responsive UI design, and cloud deployment.

> Originally developed during my Python/Django studies and revisited in 2026 with an updated architecture, current dependencies, improved security, an English recruiter-facing interface, and a production deployment on Vercel.

## 🌐 Live Demo

**[Open DevFlix](https://portifolio-netflix.vercel.app/)**

### Demo Access

Recruiters and visitors can explore the application with the public demo account:

```text
Username: demo@devflix.app
Password: DevFlixDemo2026!
```

You can also click **Use Demo Account** on the login page to fill the credentials automatically.

The demo account is intentionally restricted: it has no staff or administrator privileges, and profile/password changes are disabled for that account.

> The catalogue contains educational technology videos from the original version of the project. Some video titles and audio are in Portuguese, while the application interface is in English.

## ✨ Key Features

- User authentication and session management
- Public recruiter demo account
- Automatic demo-account provisioning in production
- Show / hide password control
- User profile management for regular accounts
- Responsive streaming-style catalogue
- Featured content hero section
- Recently added content
- Trending content based on views
- Continue Watching history
- Content search
- Detailed content pages
- Category-based related content
- Embedded YouTube video player
- View tracking
- Secure logout flow
- Responsive Netflix-inspired interface

## 🛠️ Tech Stack

| Area | Technologies |
| --- | --- |
| Backend | Python, Django 5.2 |
| Database | PostgreSQL in production, SQLite locally |
| ORM | Django ORM |
| Frontend | Django Templates, HTML5, CSS, Tailwind CSS, Bootstrap 5 |
| Forms | django-crispy-forms, crispy-bootstrap5 |
| Static Files | WhiteNoise |
| Images | Pillow |
| Database Configuration | dj-database-url |
| PostgreSQL Driver | psycopg |
| Deployment | Vercel |
| Video | YouTube Embed |

## 🏗️ Application Architecture

```text
Browser
   │
   ▼
Django Templates / Views
   │
   ├── Authentication
   ├── Catalogue & Search
   ├── User Profiles
   ├── View History
   └── Video Detail Pages
   │
   ▼
Django ORM
   │
   ├── SQLite       → Local development
   └── PostgreSQL   → Production
```

The application automatically switches database backends based on the `DATABASE_URL` environment variable. SQLite is used for local development, while production uses PostgreSQL.

## 📂 Project Structure

```text
Portifolio_netflix/
│
├── devflix/          # Django project configuration
├── filme/            # Main Django application
├── static/           # Static assets
├── templates/        # Global templates
├── media/            # Catalogue images
├── manage.py
├── requirements.txt
└── runtime.txt
```

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/julianocramos/Portifolio_netflix.git
cd Portifolio_netflix
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

The application will use a local SQLite database when `DATABASE_URL` is not defined.

## 🔐 Environment Variables

Sensitive production credentials are not stored in the repository.

The main production variables are:

```env
DJANGO_SECRET_KEY=your-secret-key
DATABASE_URL=your-postgresql-connection-string
```

The Vercel deployment provides its own runtime variables such as `VERCEL` and `VERCEL_URL`.

Local environment files, Vercel project metadata, and SQLite databases are excluded from version control.

## 🚀 Deployment

DevFlix is deployed on **Vercel** from the `main` branch.

Production URL:

**https://portifolio-netflix.vercel.app/**

The production configuration includes:

- PostgreSQL through `DATABASE_URL`
- secure session and CSRF cookies over HTTPS
- proxy-aware HTTPS configuration
- WhiteNoise for static assets
- environment-based secret management
- automatic demo-account availability

## 🔄 Modernization Work

The original application was developed in 2022. In 2026, I revisited the project and modernized it as a portfolio application.

Key improvements include:

- upgraded to Django 5.2
- updated Python dependencies
- migrated production database configuration to PostgreSQL-compatible environment variables
- added Vercel deployment support
- redesigned login and catalogue interfaces
- converted the recruiter-facing UI to English
- added a dedicated public demo experience
- improved authentication and logout handling
- protected the demo account from profile and password modifications
- added production security settings
- improved responsive catalogue and content-detail layouts
- removed legacy project branding from the public interface

## 🎯 What This Project Demonstrates

DevFlix demonstrates practical experience with:

- Django application architecture
- authentication and authorization
- relational data modelling
- ORM-based database access
- environment-specific configuration
- PostgreSQL and SQLite
- server-rendered interfaces
- reusable templates
- production deployment
- security-conscious configuration
- maintaining and modernizing an existing codebase

## 👨‍💻 Author

**Juliano Ramos**

GitHub: [@julianocramos](https://github.com/julianocramos)

---

⭐ Part of my software development, data, and technology portfolio.
