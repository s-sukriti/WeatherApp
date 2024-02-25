# Django Weather App

This is a simple Django weather app that allows users to add cities and view the current weather information for those cities using the OpenWeatherMap API.

## Getting Started

Follow these steps to clone the repository and run the project on your local system.

### Prerequisites

- Python (3.6 or higher)
- Django
- Requests library

### Installation

1. Clone the repository to your local machine:
   
2. Navigate to the project directory:

   cd your-django-weather-app
  
3. Create a virtual environment (optional but recommended):

4. Install the required library:

   pipenv install requests
   

### Configuration

1. Get your OpenWeatherMap API key:

   - Visit [OpenWeatherMap](https://openweathermap.org/) and sign up for a free account.
   - Generate your API key.

2. Configure the API key:

   - Open `the_weather/weather/views.py`.
   - Replace `'your-api-key'` with your actual OpenWeatherMap API key.
     

### Run the Application

1. Apply initial migrations:

   - python manage.py migrate

2. Run the development server:

   - python manage.py runserver

4. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.


## Usage

- Add cities using the provided form.
- View the current weather for each added city.


### Remember to replace placeholder texts like `your-username`, `your-django-weather-app`, and `'your-api-key'` with actual values. 
