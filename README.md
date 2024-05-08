# Be-Trendy Backend

Be-Trendy Backend is the Django-based backend for the Be-Trendy Ionic mobile app. It provides the necessary APIs and functionalities to support the e-commerce features of the Be-Trendy app.

## Description

Be-Trendy is an e-commerce platform built with Ionic for the frontend mobile app and Django for the backend. The backend serves as the central component responsible for managing products, user authentication, orders, and other essential functionalities required for the e-commerce operations of the Be-Trendy mobile app.

### Features

- **API Endpoints:** Provide RESTful APIs to support communication between the Ionic mobile app and the backend.
- **User Authentication:** Implement user authentication and authorization mechanisms to secure user accounts and data.
- **Product Management:** Enable administrators to add, edit, and remove products from the platform.
- **Order Management:** Facilitate the creation, processing, and management of user orders.
- **Data Storage:** Utilize databases to store product information, user data, and order details securely.
- **Security Measures:** Implement security measures to protect sensitive data and prevent unauthorized access.
- **Scalability:** Design the backend with scalability in mind to accommodate the growing user base and product catalog.

## Installation

To install and run the Be-Trendy Backend project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/rihabcherni/be-trendy-backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ionic-backend
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up Django environment:

   - Configure the database settings in `settings.py` according to your preferences.
   - Perform any necessary setup steps for your Django project, such as database migrations (`python manage.py migrate`).

5. Run the Django server:

   ```bash
   python manage.py runserver
   ```

   This command starts the Django development server, and you should be able to access the Be-Trendy Backend APIs at `http://localhost:8000` in your web browser.

   
   Or specify the IP address and port to bind to using the following command:
     ```bash
      python manage.py runserver your_ipv4_address:8000
     ```
   Replace 'your_ipv4_address' with the IPv4 address of your PC. This will make the Django server accessible via the specified IP address and port.For example, if your PC's IPv4 address is 192.168.1.10, you would run:

      ```bash
      python manage.py runserver 192.168.1.10:8000
      ```

   The Django server will now be accessible at `http://192.168.1.10:8000`.

## Contributors

- Rihab Cherni
- Molka Elloumi
- Wiem Hammemi

---