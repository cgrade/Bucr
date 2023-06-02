# Bucr App
Bucr App is a web application that allows users to discover and make reservations at various restaurants. It provides an intuitive interface for users to search for restaurants, view their details, and create reservations.

## Features
### User Registration and Authentication
* Users can create an account to access the full featuresw of the app.
* Registration requrires providing basic user information.
* Users can log in and log out of their accounts.
* Only authenticated users can make reservations and leave reviews.

### Restaurnt Listings
* Users can browse a list of restaurants available in the app.
* Each restaurant listing provides essential information like name, cuisine type, and location.
* Clicking on a restaurant takes the user to the detailed view of the restaurant.

### Restaurant Details
* Users can view detailed information about a specific restaurant.
* Details include restaurant name, description, contact information, and opening hours.
*  Users can see the average rating and reviews left by other users.
* The restaurant detail page provides a reservation form for making reservations.

### Reservation Creation
* Authenticated users can create reservations at their desired restaurants.
* The reservation form includes fields for selecting the date, time, party size, and table.
* Users can add special requests or notes to their reservation.
* Successful reservation creation redirects users to the reservation confirmation page.

### My Reservations
* Authenticated users can view a list of their reservations.
* The list displays reservation details like the restaurant name, date, time, and status.
* Users can access individual reservation details for more information.
* Users have the option to cancel or modify their reservations.

### Reviews and Ratings
* Authenticated users can leave reviews and ratings for restaurants.
* Users can share their dining experiences and provide feedback.
* Each review includes the user's name, rating, and comments.
* Reviews are displayed on the restaurant detail page.

### Technologies Used
* Django: Python web framework for building the backend of the application.
* HTML/CSS: Markup and styling for the frontend templates.
* Bootstrap: CSS framework for responsive and visually appealing designs.
* PostgreSQL: Database management system for storing restaurant and user data.

### Setup and Installation
* Clone the repository: git clone <repository-url>
* Set up the database: python manage.py migrate
* Run the development server: python manage.py runserver
* Access the application in your browser at http://localhost:8000

