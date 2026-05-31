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
                bat 'python -m pip install pytest playwright pytest-html' 
            }
        }

        stage('3. Install Browsers') {
            steps {
                echo 'Downloading Chromium binaries...'
                bat 'python -m playwright install chromium'
            }
        }

        stage('4. Run Playwright Suite') {
            steps {
                echo 'Executing Headless Automation Run...'
                bat 'python -m pytest tests/testsaucedemo.py -v --html=report.html''
            }
        }
    }
    post {
        always {
            echo 'Archiving test execution artifacts...'
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}