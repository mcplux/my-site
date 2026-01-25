# My Site

## Run in development

### Steps

1. Clone repository
   ```bash
   git clone https://github.com/mcplux/my-site
   cd my-site
   ```
2. Install dependencies
   ```bash
   uv sync
   ```
3. Activates the virtual environment to easily execute commands

   ```bash
   source .venv/bin/activate # linux
   ```

   If you don't activate the virtual environment, you'll have to add `uv run` before each command.

4. Run migrations
   ```bash
   python manage.py migrate
   ```
5. Create a superuser to access the admin panel
   ```bash
   python manage.py createsuperuser
   ```
6. Run development server
   ```bash
   python manage.py runserver
   ```
