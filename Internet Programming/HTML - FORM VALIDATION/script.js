function validateForm() {
    document.querySelectorAll('.error').forEach(function(el) {
        el.textContent = '';
    });

    let isValid = true;

    const name = document.getElementById('student_name').value;
    if (name === '') {
        document.getElementById('nameError').textContent = 'Student name is required';
        isValid = false;
    }

    const rollno = document.getElementById('rollno').value;
    if (rollno === '') {
        document.getElementById('rollnoError').textContent = 'Roll number is required';
        isValid = false;
    }

    const gender = document.querySelector('input[name="gender"]:checked');
    if (!gender) {
        document.getElementById('genderError').textContent = 'Please select a gender';
        isValid = false;
    }

    const year = document.getElementById('year').value;
    if (year === '' || isNaN(year)) {
        document.getElementById('yearError').textContent = 'Valid year is required';
        isValid = false;
    }

    const department = document.getElementById('department').value;
    if (department === '') {
        document.getElementById('departmentError').textContent = 'Department is required';
        isValid = false;
    }

    const section = document.getElementById('section').value;
    if (section === '') {
        document.getElementById('sectionError').textContent = 'Section is required';
        isValid = false;
    }

    const mobile_no = document.getElementById('mobile_no').value;
    const mobilePattern = /^[0-9]{10}$/;
    if (mobile_no === '' || !mobilePattern.test(mobile_no)) {
        document.getElementById('mobileError').textContent = 'Valid 10-digit mobile number is required';
        isValid = false;
    }

    const email = document.getElementById('email').value;
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (email === '' || !emailPattern.test(email)) {
        document.getElementById('emailError').textContent = 'Valid email is required';
        isValid = false;
    }

    const address = document.getElementById('address').value;
    if (address === '') {
        document.getElementById('addressError').textContent = 'Address is required';
        isValid = false;
    }

    const city = document.getElementById('city').value;
    if (city === '') {
        document.getElementById('cityError').textContent = 'City is required';
        isValid = false;
    }

    const country = document.getElementById('country').value;
    if (country === '') {
        document.getElementById('countryError').textContent = 'Country is required';
        isValid = false;
    }

    const pincode = document.getElementById('pincode').value;
    const pincodePattern = /^[0-9]{6}$/;
    if (pincode === '' || !pincodePattern.test(pincode)) {
        document.getElementById('pincodeError').textContent = 'Valid 6-digit pincode is required';
        isValid = false;
    }

    if (isValid) {
        document.getElementById('successMessage').style.display = 'block';
    }

    return false;
}