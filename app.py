from flask import Flask, render_template, request, jsonify, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True
app.config['MAIL_DEBUG'] = True

# Configure Flask-Mail with Gmail SMTP settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')



mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')  # Renders Index.html from the templates folder

@app.route('/test-email')
def test_email():
    # admin_email = "FYPAccepter@gmail.com"
    admin_email = "ACronnelly15@gmail.com"
    msg = Message("Test Email", sender=app.config['MAIL_USERNAME'], recipients=[admin_email])
    msg.body = "This is a test email from Flask."
    try:
        mail.send(msg)
        return "Test email sent!"
    except Exception as e:
        return f"Failed to send email: {e}"

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    admin_email = "FYPAccepter@gmail.com"

    approve_url = url_for('approve_contractor', contractor_id=data['email'], _external=True)
    deny_url = url_for('deny_contractor', contractor_id=data['email'], _external=True)

    email_body = f"""
    Contractor Registration Request:
    First Name: {data['firstName']}
    Last Name: {data['lastName']}
    Email: {data['email']}
    Company Name: {data['companyName']}
    CIRI Name: {data['ciriName']}
    Memberships: {data['memberships']}
    Public/Employer's Liability Insurance: {data['liabilityInsurance']}
    Tax Clearance Certificate: {data['taxCertificate']}

    Review and take action:
    Approve: {approve_url}
    Deny: {deny_url}
    """
    
    msg = Message("Contractor Registration Request", sender=app.config['MAIL_USERNAME'], recipients=[admin_email])
    msg.body = email_body
    print(email_body)

    try:
        mail.send(msg)
        print("Email sent successfully.")
        return jsonify({"message": "Form submitted successfully"}), 200
    except Exception as e:
        print("Failed to send email:", e)
        return jsonify({"message": "Failed to send email", "error": str(e)}), 500
    
    


# Approval and denial routes
@app.route('/approve/<contractor_id>', methods=['GET'])
def approve_contractor(contractor_id):
    return f"Contractor {contractor_id} approved."

@app.route('/deny/<contractor_id>', methods=['GET'])
def deny_contractor(contractor_id):
    return f"Contractor {contractor_id} denied."
