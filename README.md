# pw-checker-app
Password Checker application in Linux VM

# Password Strength Checker Project

## Project Overview
This project is a **Password Strength Checker** web application, designed to assess password security by performing both basic and advanced validation. The project utilizes **Python, Flask, and zxcvbn** (an open-source library for password strength estimation) to validate passwords based on common security rules and measure the password's resistance against potential attacks. 

Hosted on an **Azure VM** configured with **Ubuntu 22.04 LTS**, the project showcases the integration of Flask for web development, Azure for cloud services, and GitHub for version control.

## Key Features
- **Basic Validation**: Enforces rules such as length, inclusion of uppercase and lowercase letters, numbers, and special characters.
- **Advanced Strength Checking**: Utilizes zxcvbn to evaluate password strength based on common patterns and potential attack methods, providing specific feedback to users.
- **Web Interface**: Built with Flask, allowing users to check their password's security interactively via a browser.

## Setup and Configuration
1. **Create Azure VM**: An Azure VM was created with the following specifications:
    - **Name**: `vm-pwchecker`
    - **Operating System**: Ubuntu 22.04 LTS
    - **VM Size**: Standard B1ms
    - Opened **Port 5000** to allow HTTP access for the web application.
    - SSH access configured for remote setup and management.

2. **SSH into the VM and Configure Environment**:
    - Updated the system and installed Python 3.11, Pip, and Git:
      ```bash
      sudo apt update
      sudo apt install python3.11 python3-pip git -y
      ```
    - Installed required Python packages, including Flask and zxcvbn:
      ```bash
      pip3 install zxcvbn regex flask requests
      ```

3. **Set Up GitHub Repository**:
    - Created a GitHub repository ([repository link here](https://github.com/marvioncriddle/pw-checker-app)) and cloned it onto the VM.
    - Configured Git for version control and generated SSH keys to connect securely with GitHub.

4. **Password Checker Script**: Developed a password checker script (`pwcheck.py`) to evaluate password strength through both basic regex rules and zxcvbn's advanced checking capabilities. Here’s a sample of the basic validation function:
    ```python
    def regex_check(password):
        if len(password) < 24:
            return "Password must be at least 24 characters long."
        if not re.search("[A-Z]", password):
            return "Password must have at least one uppercase letter (A-Z)."
        # Additional rules for lowercase, numbers, and special characters
    ```
    For the complete code, please refer to the [repository here](https://github.com/marvioncriddle/pw-checker-app).

## Web Interface with Flask
A Flask application (`app.py`) was created to provide a web interface, allowing users to enter passwords and receive feedback on their strength. The application leverages Flask's templating to render a user-friendly HTML page.

- **Sample Code for Flask Route**:
    ```python
    @app.route('/', methods=['GET', 'POST'])
    def password_check():
        # Handles password input and returns strength feedback
    ```

The HTML interface, styled with simple forms, is located in the `templates/` folder. This web-based interaction was tested by running the Flask application, accessible at `http://<vm-public-ip>:5000`.

## Testing and Deployment
- **Testing**: After starting the Flask app on the VM, several passwords were tested to verify the application’s validation logic. Screenshots of different password checks can be found in the repository’s `/screenshots` folder.
- **Deployment**: The application is deployed on the VM and can be accessed publicly via the VM’s IP and port 5000.

## GitHub and Version Control
All changes were tracked using Git. Commits were made at each major development phase, from environment setup to final testing. The repository can be found here: [Password Checker Repository](https://github.com/marvioncriddle/pw-checker-app).

## Key Takeaways
This project demonstrates my proficiency in:
- **Cloud Configuration**: Setting up and managing VMs on Azure for hosting web applications.
- **Security Validation**: Building applications with security-first considerations, especially for user data.
- **Flask Web Development**: Using Flask to develop web applications and deploy them on cloud infrastructure.
- **Version Control**: Utilizing Git and GitHub for efficient source control and collaboration.

For detailed code, screenshots, and documentation, please visit the [project repository on GitHub](https://github.com/marvioncriddle/pw-checker-app).

---

By building and deploying this project, I have further honed my skills as a Security Engineer in creating secure and accessible applications. This project reflects my ability to combine security standards with practical web development and cloud deployment practices.

