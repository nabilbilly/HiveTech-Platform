# HiveTech-Platform

## Contributing

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/Raven-Hive-platform.git`
3. Create a new branch: `git checkout -b my-feature-branch`
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin my-feature-branch`
6. Submit a pull request


## Project Structure
Raven-Hive-platform/
├── venv/ # Virtual environment
├── HiveProject/ # Django project folder
│ ├── HiveProject/
│ ├── Mainapp/
│ ├── static/
│ ├── templates/
│ ├── manage.py
├── README.md # 


## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Node.js and npm (for frontend dependencies)

### Installation

1. **Fork the repository:**

    Go to the GitHub repository and click on the `Fork` button in the top right corner.

2. **Clone your forked repository:**

    ```bash
    git clone https://github.com/yourusername/Raven-Hive-platform.git
    cd Raven-Hive-platform
    ```

3. **Set up the virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**

    ```bash
    pip freeze > requirements.txt

    ```bash
    python -m pip install --upgrade pip

    ```bash
    pip install -r requirements.txt
    ```

5. **Install frontend dependencies (optional):**

    ```bash
    npm install tailwind
    ```

 **Install Tailwind CSS:**

    ```bash
    npm install -D tailwindcss
    npx tailwindcss init

    - for use to be on the same page Tailwind to your HTML file:
      ```html
     <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
      ```

**Install Bootstrap:**

    ```bash
    npm install bootstrap
    ```

    - Add Bootstrap to your HTML file:
      ```html
      <link href="node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
      <script src="node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
      ```

**Start the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the application:**

    Open your browser and navigate to `http://localhost:8000`.

## Technologies Used

- **Backend:**
  - Django
- **Frontend:**
  - HTML
  - CSS
  - Tailwind CSS
  - Bootstrap
- **Others:**
  - Git
  - Virtualenv

