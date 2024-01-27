# UzInfoScan

UzInfoScan is an application designed to verify the reliability of organizations by checking their licenses and official activities in accordance with government laws. The application is built using the Python Django framework for the backend API, allowing seamless communication with the frontend. The frontend fetches datasets from Open Data sources locally and shares them using GET and POST requests.

## Features

- **License Verification:** UzInfoScan checks the licenses of organizations to ensure compliance with government regulations.
  
- **Official Activity Confirmation:** The application verifies the official activities of organizations to guarantee adherence to legal requirements.

- **Open Data Integration:** Utilizing Open Data sources, UzInfoScan fetches datasets locally, providing up-to-date and accurate information.

## Technology Stack

- **Backend Framework:** Python Django
- **API:** Django API for seamless communication with the frontend
- **Data Fetching:** Open Data sources
- **Frontend Communication:** GET, POST requests

## Demo Version

The current demo version focuses on checking Lombards, providing a glimpse into the capabilities of UzInfoScan.

## Frontend

To explore the frontend of UzInfoScan, follow the instructions below:

1. **[Link to Frontend](#)** (Replace with the actual link)

   Explore the user-friendly interface to interact with the application and access verified information about organizations.

## Getting Started

To set up UzInfoScan locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/UzInfoScan.git
   cd UzInfoScan
   ```

   ```
   pip install -r requirements.txt
   ```

   ```
   python manage.py migrate
   ```

   ```
   python manage.py runserver
   ```
