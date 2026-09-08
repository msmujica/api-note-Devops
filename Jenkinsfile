pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-test.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t notes-app:v2 .
                '''
            }
        }
    }

    post {
        success {
            echo 'Tests OK - Imagen Docker creada correctamente'
        }

        failure {
            echo 'La pipeline fallo'
        }
    }
}