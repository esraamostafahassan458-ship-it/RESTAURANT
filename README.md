# 🍽️ Restaurant Menu Project (Django)

A simple **Django** project for displaying a restaurant menu with admin panel management.  
It uses **Django Template Language (DTL)**, **CSS styling**, image upload, and pagination.


## ✨ Features
- Add, edit, and delete menu items from the Django admin panel.
- Each menu item includes:
  - 📝 Name
  - 📖 Description
  - 💵 Price
  - 🖼️ Image (optional)
- Display the menu in a dedicated page.
- **Image resizing and styling** with CSS.
- **Pagination** for menu items.
- Support for **static files** and **media files**.


## 🛠️ Requirements
- Python 3.11+
- Django 5+
- Pillow (for image handling)

Install dependencies:
```bash
pip install -r requirements.txt
🚀 How to Run
Clone the project:

bash

git clone https://github.com/USERNAME/restaurant.git
cd restaurant
Apply migrations:

bash

python manage.py migrate
Create a superuser (for admin access):

bash
python manage.py createsuperuser
Run the development server:

bash
python manage.py runserver
Open in browser:

Menu: http://127.0.0.1:8000/menu/

Admin panel: http://127.0.0.1:8000/admin/

📂 Project Structure
csharp

restaurant/
│── pages/
│   ├── models.py      # MenuItem model
│   ├── views.py       # Views (home & menu)
│   ├── templates/
│   │   ├── home.html
│   │   └── menu.html
│   └── static/
│       └── css/
│           └── style.css
│── media/             # Uploaded images
│── restaurant/
│   ├── settings.py    # Static & media configuration
│── db.sqlite3
│── manage.py
📸 Screenshots
Add screenshots of Home Page and Menu Page here.

