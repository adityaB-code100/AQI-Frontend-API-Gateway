# AQI Prediction & Visualization Platform

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-red?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-purple?logo=render&logoColor=white)](https://render.com/)

</div>

## Overview
This is a comprehensive 
AQI Prediction & Visualization Platform that serves as the **Frontend and API Gateway** for the AQI project. The application provides real-time AQI data, health alerts, and personalized recommendations based on user profiles and location.

> **Note:** The machine learning backend for AQI predictions is available in a separate repository: [AQI-ML-Backend](https://github.com/adityaB-code100/AQI-ML-Backend/)

## Features
- 🔐 User authentication (personal and institutional accounts)
- 📊 Real-time AQI data visualization
- ⚕️ Health alerts and recommendations
- 🎯 Personalized alerts based on user health conditions
- 📝 Note-taking functionality with AQI context
- 🔄 Village comparison tools

## Architecture
- **Frontend & API Gateway**: Flask web application (this repository)
- **ML Backend**: Python-based machine learning models (separate repository)
- **Database**: MongoDB Atlas
- **Frontend**: HTML templates with CSS/JavaScript

### Prerequisites
- A MongoDB Atlas cluster with connection string

### Environment Variables
The following environment variable must be set in your Render dashboard:
- `MONGO_URI`: Your MongoDB Atlas connection string



## Technologies Used
- **Backend**: Python 3.x, Flask
- **Database**: MongoDB
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: Google Translate API, Twilio API
- **Deployment**: Docker, Render

## Local Development

### Prerequisites
- Python 3.7+
- MongoDB instance (local or Atlas)

#
## Repository Links
- **Frontend & API Gateway (This Repo)**: [AQI Frontend + API Gateway](https://github.com/adityaB-code100/AQI-Frontend-API-Gateway/)
- **ML Backend**: [AQI-ML-Backend](https://github.com/adityaB-code100/AQI-ML-Backend/)

## Support
If you encounter any issues or have questions, please file an issue in the GitHub repository.

---
<div align="center">
<p>Developed with ❤️ for cleaner air awareness</p>
</div>