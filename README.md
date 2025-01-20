# django-signature-api-task
Task: Implement a Django REST API to sign hash codes using RSA encryption.

## Overview
This task involves setting up a new Django project and implementing a REST API endpoint that:
- Accepts a hash code as input.
- Signs the hash code using a private RSA key.
- Returns the digital signature in a JSON response.

## Expected Output

1. A Django project with an API endpoint at `/api/sign/`:
    2. Input: hash_code (string).
    3. Output: A JSON response containing the digital signature.
4. Documentation and test cases.

## Task Breakdown

1. **Set Up the Django Project**
   - Create a new Django project named `signature_service`.
   - Add an app named `api`.

2. **Install Dependencies**
   - Include `Django REST Framework` and `cryptography` in your project:
     ```bash
     pip install djangorestframework cryptography
     ```

3. **API Endpoint Specification**
   - URL: `/api/sign/`
   - Method: `POST`
   - Input: JSON payload containing `hash_code` (string).
     Example:
     ```json
     {
         "hash_code": "abcd1234"
     }
     ```
   - Output: JSON response with the generated signature:
     ```json
     {
         "signature": "base64_encoded_signature"
     }
     ```

4. **Digital Signature Implementation**
   - Use an RSA private key to sign the hash code.
   - Store the RSA key locally in the project directory (`task/example_rsa_key.pem`) or generate one dynamically.
   - Use the `cryptography` library to perform signing.

5. **Validation**
   - Ensure `hash_code` is a valid hex string. If invalid, return a 400 error.

6. **Unit Tests**
   - Add at least two test cases:
     - Valid hash code → Returns 200 with a signature.
     - Invalid hash code → Returns 400 with an error message.

7. **Documentation**
   - Document how to set up and run the project in the README file.