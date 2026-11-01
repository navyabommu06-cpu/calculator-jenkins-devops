
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Fetching code from GitHub'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v --junitxml=test-results.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-calculator .'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'test-results.xml'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
stage('Check Docker') {
    steps {
        bat 'echo %PATH%'
        bat 'where docker'
        bat 'docker --version'
    }
}