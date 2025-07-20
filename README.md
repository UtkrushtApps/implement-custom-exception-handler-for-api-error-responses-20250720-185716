# Task Overview
You are tasked with ensuring a FastAPI application's user endpoint returns structured JSON errors when authentication fails. The API currently provides unstructured error messages for unauthorized requests, breaking downstream clients and QA automation. You must ensure consistent, schema-compliant error responses for all unauthorized requests, and that the OpenAPI schema accurately describes these responses.

# Guidance
- Focus on error handling for the /users/me endpoint, particularly unauthorized cases.
- Ensure all responses for authentication failures are predictable and structured as per the API documentation.
- Do not introduce external dependencies or alter authentication logic, only adjust error response structure and docs.
- Pay attention to the OpenAPI documentation so it properly reflects the structured error response for 401 errors.

# Objectives
- Guarantee that 401 Unauthorized responses return a JSON error object matching the documented schema.
- Update or confirm the OpenAPI schema so it documents JSON error structure for 401 responses.
- Enable clients and QA automation to reliably parse and handle authentication errors from /users/me.

# How to Verify
- Make a request to /users/me without authentication or with an invalid token and examine the response.
- Ensure the response body is a JSON object with an appropriate error structure and a 401 status code.
- Check the OpenAPI docs that the 401 response for /users/me matches the error format expectations.
- Confirm a valid token request still receives the user data without error.
