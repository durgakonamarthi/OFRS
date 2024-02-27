from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with actual user authentication logic)
dummy_users = [
    {"email": "durgakonamarthi@gmail.com", "password": "durga0309"},
    {"email": "user2@example.com", "password": "password2"}
]

# Route for displaying the login form
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# Route for handling login form submission
@app.route('/login', methods=['POST'])
def login_post():
    # Retrieve form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Print form data for debugging
    print(f"Email: {email}")
    print(f"Password: {password}")

    # Validate user input
    if not email or not password:
        error_message = "Email and password are required."
        return render_template('login.html', error_message=error_message)
    
    # Dummy authentication logic (replace this with actual user authentication logic)
    user = next((user for user in dummy_users if user["email"] == email and user["password"] == password), None)
    
    if user:
        # User authenticated successfully, redirect to dashboard or home page
        print(f"User authenticated: {user}")
        return redirect(url_for('dashboard'))  # Assuming you have a route named 'dashboard'
    else:
        # Authentication failed, display error message on login page
        print("Authentication failed")
        error_message = "Invalid email or password. Please try again."
        return render_template('login.html', error_message=error_message)

# Route for rendering the dashboard page
@app.route('/dashboard')
def dashboard():
    # Logic for rendering the dashboard page goes here
    return render_template('dashboard.html')

# Route for displaying the registration form
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

# Route for handling registration form submission
@app.route('/register', methods=['POST'])
def register_post():
    # Retrieve form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Print form data for debugging
    print(f"Email: {email}")
    print(f"Password: {password}")

    # Validate user input
    if not email or not password:
        error_message = "Email and password are required."
        return render_template('register.html', error_message=error_message)

    # Dummy registration logic (replace this with actual user registration logic)
    # For now, let's assume registration is successful
    print("Registration successful!")
    return redirect(url_for('login'))  # Redirect to login page after registration


if __name__ == '__main__':
    app.run(debug=True)

