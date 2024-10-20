import requests

# Mock form data for contractor
def test_contractor_form_submission():
    response = requests.post('http://localhost:5000/submit-form', data={
        'name': 'John Doe',
        'email': 'john@example.com',
        'license': 'XYZ123'
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'Form submitted successfully'

def test_admin_receives_email():
    # Assume there's a function to check the admin's email inbox
    email = check_admin_inbox()
    assert 'New contractor form submission' in email.subject

def test_admin_authorizes_contractor():
    response = requests.post('http://localhost:5000/admin/authorize', data={
        'contractor_id': 1
    })
    assert response.status_code == 200
    assert response.json()['status'] == 'authorized'

def test_contractor_receives_activation_email():
    email = check_contractor_inbox('john@example.com')
    assert 'Your account is now active' in email.subject
