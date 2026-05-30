pipeline {
    agent any 

    stages {
        stage('1. Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('2. Install Dependencies') {
            steps {
                echo 'Installing python testing libraries...'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest playwright'
            }
        }

        stage('3. Install Browsers') {
            steps {
                echo 'Downloading Chromium binaries...'
                bat 'playwright install chromium'
            }
        }

        stage('4. Run Playwright Suite') {
            steps {
                echo 'Executing Headless Automation Run...'
                bat 'python -m pytest tests/testsaucedemo.py'
            }
        }
    }
}