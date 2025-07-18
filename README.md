# Flourish App

A Django application for managing thrift savings.

## Features

- Customer management
- Savings tracking
- Transaction history
- Reports and analytics

## Technologies Used

- Django 5.2.4
- Bootstrap 5.3.7
- Tailwind CSS (with prefix to avoid conflicts with Bootstrap)
- SQLite (development) / PostgreSQL (production)

## Setup and Installation

1. Clone the repository
2. Create a virtual environment and activate it
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```
3. Install Python dependencies
   ```
   pip install -r requirements.txt
   ```
4. Install Node.js dependencies (for Tailwind CSS)
   ```
   npm install
   ```
5. Run migrations
   ```
   python manage.py migrate
   ```
6. Start the development server
   ```
   python manage.py runserver
   ```

## CSS Framework Setup

This project uses both Bootstrap and Tailwind CSS for styling:

- **Bootstrap** is used for the main layout and components
- **Tailwind CSS** is used for additional utility classes with a `tw-` prefix to avoid conflicts

### Bootstrap

Bootstrap is loaded via CDN and requires no additional setup.

### Tailwind CSS Setup

Tailwind CSS is configured with a prefix (`tw-`) to avoid conflicts with Bootstrap classes. The CDN version is currently implemented for simplicity, but you can also use the build process for production:

1. Install Node.js dependencies
   ```
   npm install
   ```

2. Build the CSS (one-time build)
   ```
   npm run build:css
   ```

3. Or watch for changes during development
   ```
   npm run watch:css
   ```

### Using Both Frameworks Together

When using both frameworks together:

- Use Bootstrap classes without any prefix: `class="container"`
- Use Tailwind classes with the `tw-` prefix: `class="tw-text-blue-500"`
- You can mix both in the same element: `class="btn btn-primary tw-rounded-xl tw-shadow-lg"`

## Deployment

This application is configured for deployment on Render.com. See `render.yaml` for configuration details.