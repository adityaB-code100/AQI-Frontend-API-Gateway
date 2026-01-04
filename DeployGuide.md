# Deployment Guide for AQI Monitoring System

## Prerequisites
- Python 3.7 or higher
- MongoDB database (Atlas or local)
- Access to required API keys (Google, Twilio, etc.)

## Step 1: Environment Setup

### 1.1 Clone or Download the Application
```bash
git clone <your-repo-url>
# or download the project files directly
```

### 1.2 Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 2: Install Dependencies

### 2.1 Create requirements.txt
Create a `requirements.txt` file with the following content:
```txt
Flask==2.3.3
pymongo==4.5.0
werkzeug==2.3.7
```

### 2.2 Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 3: Configure the Application

### 3.1 Update Configuration
Update the `config.json` file with your actual API keys and database connection string:
```json
{
    "params": {
        "gmail_user": "your-email@gmail.com",
        "gmail_password": "your-app-password",
        "mail_server": "smtp.gmail.com",
        "mail_port": 465,
        "mail_use_tls": false,
        "mail_use_ssl": true
    },
    "twilio": {
        "account_sid": "your-account-sid",
        "auth_token": "your-auth-token",
        "from_number": "your-twilio-number",
        "profile_no": "default-phone-number"
    },
    "API_KEY": {
        "key": "your-google-api-key"
    },
    "GOOGLE_TRANSLATE_API_KEY": {
        "key": "your-translate-api-key"
    },
    "MONGO_URI": "your-mongodb-connection-string",
    "MONGO_URI1": "mongodb://localhost:27017/"
}
```

## Step 4: Database Setup

### 4.1 MongoDB Connection
Ensure your MongoDB instance is running and accessible with the connection string in `config.json`.

### 4.2 Collections
The application expects the following collections in the "AQI_Project" database:
- `users` - For personal user accounts
- `institutions` - For institutional accounts
- `notes` - For user notes
- `processed_data` - For AQI data

## Step 5: Running the Application

### 5.1 Local Development
```bash
python main.py
```
The application will run on `http://localhost:5000` by default.

### 5.2 Production Deployment
For production, consider using a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

## Step 6: Deployment to Different Platforms

### 6.1 Heroku Deployment
1. Create a `Procfile` with content:
   ```
   web: gunicorn main:app
   ```
2. Add runtime.txt to specify Python version:
   ```
   python-3.11.5
   ```
3. Deploy using Heroku CLI

### 6.2 PythonAnywhere Deployment
1. Upload files to PythonAnywhere
2. Create virtual environment and install dependencies
3. Configure web app to use your main.py file as the WSGI entry point

### 6.3 AWS/Google Cloud Deployment
1. Containerize the application with Docker (optional)
2. Set up appropriate cloud instance
3. Configure domain and SSL if needed

## Security Considerations

### Environment Variables
For production, move sensitive information from config.json to environment variables:
```bash
export MONGO_URI="your-mongodb-uri"
export SECRET_KEY="your-secret-key"
```

### SSL Configuration
Enable SSL for production environments to secure user data transmission.

## Troubleshooting

### Common Issues
1. **Database Connection Errors**: Verify your MongoDB connection string and network access
2. **Missing Dependencies**: Ensure all packages in requirements.txt are installed
3. **Configuration Errors**: Double-check all API keys and service configurations

### Logs
Check application logs for errors. The application logs errors using Python's logging module.

## Post-Deployment Checklist
- [ ] Verify all routes are accessible
- [ ] Test user registration and login
- [ ] Confirm database connections work
- [ ] Verify API integrations (Google, Twilio)
- [ ] Test email/SMS notifications
- [ ] Check security configurations
- [ ] Note: The chatbot functionality is incomplete - UI exists but backend endpoint not implemented