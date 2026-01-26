# My Site

## Run in development

### Steps

1. Clone repository
   ```bash
   git clone https://github.com/mcplux/my-site.git
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
4. Duplicate .env.example file
   ```
   cp .env.example .env
   ```
5. Run migrations
   ```bash
   uv run manage.py migrate
   ```
6. Create a superuser to access the admin panel
   ```bash
   uv run manage.py createsuperuser
   ```
7. Start Django and Tailwind in development
   ```bash
   uv run honcho start
   ```
