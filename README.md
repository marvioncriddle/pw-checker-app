# Python Password Strength Checker
![Password Checker](https://i.imgur.com/o0KgQwF.jpg)

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
    - **SSH Key Authentication**: Configured SSH keys during Azure VM creation to secure remote access, ensuring only authorized users could access the VM.

![pwck1](https://i.imgur.com/zU7XEPl.jpg)

2. **SSH (via PowerShell) into the VM and Configure Environment**:
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
    - Created a GitHub repository and cloned it onto the VM.
    - Configured Git for version control and generated SSH keys to connect securely with GitHub.

![githubsshkey](https://i.imgur.com/kOyNKsx.jpg)

4. [**Password Checker Script**](https://github.com/marvioncriddle/pw-checker-app/blob/main/pwcheck.py): Developed a password checker script (`pwcheck.py`) to evaluate password strength through both basic regex rules and zxcvbn's advanced checking capabilities. Here’s a sample of the basic validation function:
    ```python
    def regex_check(password):
        if len(password) < 24:
            return "Password must be at least 24 characters long."
        if not re.search("[A-Z]", password):
            return "Password must have at least one uppercase letter (A-Z)."
        # Additional rules for lowercase, numbers, and special characters
    ```

## Web Interface with Flask
A Flask [application](https://github.com/marvioncriddle/pw-checker-app/blob/main/app.py) (`app.py`) was created to provide a web interface, allowing users to enter passwords and receive feedback on their strength. The application leverages Flask's templating to render a user-friendly HTML page.

- **Sample Code for Flask Route**:
    ```python
    @app.route('/', methods=['GET', 'POST'])
    def password_check():
        # Handles password input and returns strength feedback
    ```

The HTML interface, styled with simple forms, is located in the `templates/` folder. This web-based interaction was tested by running the Flask application, accessible at `http://<vm-public-ip>:5000`.

## Testing and Deployment
- **Testing**: After starting the Flask app on the VM, several passwords were tested to verify the application’s validation logic. 
- **Deployment**: The application is deployed on the VM and can be accessed publicly via the VM’s IP and port 5000.
-------------------
**Test Password(1)**:  11111  

<img src="https://i.imgur.com/zALVfVr.jpg" alt="pass1" width="400"/>

**Test Password(2)**:  Mushroom156  

<img src="https://i.imgur.com/JPARS01.jpg" alt="pass2" width="400"/>

**Test Password(3)**:  jkjflkajdkdasfsdfdfd1242%#  

<img src="https://i.imgur.com/cwa0NYZ.jpg" alt="pass3" width="400"/>

**Test Password(4)**:  fg@43BDDvj45242%$@^22kjD3  

<img src="https://i.imgur.com/OxKdn3p.jpg" alt="pass4" width="400"/>

-------------------

## GitHub and Version Control
All changes were tracked using Git. Commits were made at each major development phase, from environment setup to final testing. 

## Key Takeaways
This project demonstrates my proficiency in:
- **Cloud Configuration**: Setting up and managing VMs on Azure for hosting web applications.
- **Security Validation**: Building applications with security-first considerations, especially for user data.
- **Flask Web Development**: Using Flask to develop web applications and deploy them on cloud infrastructure.
- **Version Control**: Utilizing Git and GitHub for efficient source control and collaboration.

---

By building and deploying this project, I have further honed my skills as a Security Engineer in creating secure and accessible applications. This project reflects my ability to combine security standards with practical web development and cloud deployment practices.

