pipeline {
    agent any

    stages {

        stage('Run tests') {
            agent {
                docker {
                    image 'python:3.11-slim'
                }
            }

            steps {
                sh '''
                    pip install -r requirements.txt
                    pip install pytest httpx
                    pytest -v
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t msjapp-notes_api .
                '''
            }
        }
    }
}