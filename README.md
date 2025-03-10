# 📖 Blog-Website

Blog-Website is a powerful and user-friendly blog website built with Django. It enables users to create, read, update, and delete blog posts, fostering an engaging blogging experience.

## Features
- User authentication and authorization
- CRUD functionality for blog posts
- Commenting system
- Responsive design
- SEO-friendly URLs

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip (Python package manager)
- Virtualenv

### Steps to Install
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/blog-website.git
   cd blog-website
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv .env
   source .env/bin/activate  # On Windows use: .env\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the superuser account.

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure
```
blog-website/
│-- manage.py
│-- .env/
│-- app/ (Main application)
│-- templates/ (HTML templates)
│-- static/ (CSS, JS, Images)
│-- db.sqlite3
│-- requirements.txt
│-- README.markdown
```

## Contact
For inquiries, feel free to reach out:
- Email: your-email@example.com
- GitHub: [yourusername](https://github.com/abhi-jais-11)
