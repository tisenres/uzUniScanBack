# UzUniScan

UzUniScan is an application designed to verify the reliability of organizations by checking their licenses and official activities by government laws. The application is built using the Python Django framework for the backend API, allowing seamless communication with the front end. The front end fetches datasets from Open Data sources locally and shares them using GET and POST requests.

## Features

- **License Verification:** UzUniScan checks organizations' licenses to ensure compliance with government regulations.
  
- **Official Activity Confirmation:** The application verifies the official activities of organizations to guarantee adherence to legal requirements.

- **Open Data Integration:** Utilizing Open Data sources, UzUniScan fetches datasets locally, providing up-to-date and accurate information.

## Technology Stack

- **Backend Framework:** Python Django
- **API:** Django API for seamless communication with the frontend
- **Data Fetching:** Open Data sources
- **Frontend Communication:** GET, POST requests

## Demo Version

The current demo version focuses on checking Lombards, providing a glimpse into the capabilities of UzUniScan.

## Frontend

To explore the frontend of UzUniScan, follow the instructions below:

1. **[Link to Frontend](https://github.com/sodikovikhtiyor/uzuniscan)** (Replace with the actual link)

   Explore the user-friendly interface to interact with the application and access verified information about organizations.

## Getting Started

To set up UzUniScan locally, follow these steps:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/tisenres/UzUniScan.git
   cd UzUniScan
   ```
   
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
5. Run migrations:
   
   ```bash
   python manage.py migrate
   ```
   
7. Start the development server:
   
   ```bash
   python manage.py runserver
   ```
