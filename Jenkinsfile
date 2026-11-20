
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out project files'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python installation'
                bat 'python --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Analysis') {
            steps {
                echo 'Analyzing server logs'
                bat 'python app.py'
                bat 'python app.py > analysis_report.txt'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Preparing deployment folder'
                bat 'if not exist staging mkdir staging'
                bat 'copy /Y app.py staging\\app.py'
                bat 'copy /Y sample.log staging\\sample.log'
                bat 'copy /Y README.md staging\\README.md'
                echo 'Files copied to staging folder'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check Console Output.'
        }

        always {
            archiveArtifacts artifacts: 'analysis_report.txt',
                             allowEmptyArchive: true
        }
    }
}
