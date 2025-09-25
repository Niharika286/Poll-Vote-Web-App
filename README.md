# Poll-Vote-Web-App

A real-time polling application built using **Django** and **SQLite**, allowing users to create and participate in polls with instant results.

## 📌 Features

* **Admin Interface**: Manage polls and choices easily.
* **User Interaction**: Vote on active polls and view results.
* **Real-Time Updates**: Instant display of voting results.

## 🛠️ Technologies Used

* **Backend**: Django (Python)
* **Database**: SQLite
* **Frontend**: HTML, CSS (Bootstrap)
* **Authentication**: Django Admin for user management

## 🚀 Installation

### Prerequisites

Ensure you have Python 3.13 and Django installed. If not, you can install Django using:

```bash
pip install django
```

### Steps to Run Locally

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Niharika286/Poll-Vote-Web-App.git
   cd Poll-Vote-Web-App
   ```

2. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

3. **Create a Superuser** (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the admin credentials.

4. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:

   * Visit the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   * Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 🧪 Usage

* **Admin Panel**: Log in using the superuser credentials to add and manage polls and choices.
* **Voting**: Navigate to the homepage to participate in available polls.
* **Results**: View live results after casting your vote.

## 🧩 Future Enhancements

* Implement user authentication for non-admin users.
* Add support for multiple-choice questions.
* Integrate real-time voting updates using WebSockets.

## 🤝 Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

