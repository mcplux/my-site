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
3. Install TailwindCSS binary
   ```bash
   curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v4.1.18/tailwindcss-linux-x64
   mv tailwindcss-linux-x64 tailwindcss
   chmod +x tailwindcss
   ```
4. Activates the virtual environment to easily execute commands

   ```bash
   source .venv/bin/activate # linux
   ```

   If you don't activate the virtual environment, you'll have to add `uv run` before each command.

5. Run migrations
   ```bash
   python manage.py migrate
   ```
6. Create a superuser to access the admin panel
   ```bash
   python manage.py createsuperuser
   ```
7. Start tailwind server
   ```
   ./tailwindcss -i static/css/input.css -o static/css/output.css --watch
   ```
8. Run development server
   ```bash
   python manage.py runserver
   ```
