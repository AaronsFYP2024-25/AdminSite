document.querySelector('.form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = {
        firstName: document.getElementById('field1').value,
        lastName: document.getElementById('field2').value,
        email: document.getElementById('field3').value,
        companyName: document.getElementById('field4').value,
        ciriName: document.getElementById('field5').value,
        memberships: document.getElementById('field6').value,
        liabilityInsurance: document.getElementById('field7').value,
        taxCertificate: document.getElementById('field8').value,
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/submit', {  // Ensure this URL is correct
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            alert('Your application has been submitted successfully!');
        } else {
            alert('Failed to submit the form. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
});
