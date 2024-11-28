# saveit-live3
Master branch has the code.

Customer Management Web Application
This web application is designed to help store owners manage customer data efficiently.
It provides a role-based access control system to support multiple levels of access for store owners and administrators.

Project Overview
The application allows store owners to:

a. Store customer records securely.
b. Manage hierarchical access levels (e.g., Admins and Store Owners).
c. Provide user-friendly interaction for viewing and managing records.

Features
a. Role-Based Access Control (RBAC): Multi-level user hierarchy for controlled data access.
b. Data Management: Efficient storage and retrieval of customer records.
c. Multi-User Access: Separate dashboards for administrators and store owners.
d. Secure Authentication: Login and registration with encryption.

Installation:
Prerequisites
1. Python 3.8 or higher
2. Virtual environment setup (optional but recommended)

Steps
1. Clone this repository:
gh repo clone Rishabh07gupta/saveit-live3
2. Navigate to the project directory:
cd <project-folder>
3. Install dependencies:
pip install -r requirements.txt
4. Run migrations to set up the database:
python manage.py migrate
5. Start the development server:
python manage.py runserver

Usage
1. Navigate to http://127.0.0.1:8000 in your browser.
2. Login with an admin or store owner account.
3. Explore the dashboard for features like adding customers, viewing records, and managing users.

File Structure
1. app/: Contains the main application code (views, models, forms).
2. static/: Static assets like CSS, JS, and images.
3. templates/: HTML templates for the frontend.
4. manage.py: Entry point for Django commands.
5. requirements.txt: List of dependencies.
6. Technologies Used
7. Backend: Python, Django Framework
8. Frontend: HTML, CSS, JavaScript
9. Database: SQLite (default), with support for other RDBMS
10. Version Control: Git

