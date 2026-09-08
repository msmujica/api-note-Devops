pipeline {
    agent any

    stages {

        stage('Run tests') {
            steps {
                sh '''
                    docker run --rm \
                        -v "$WORKSPACE:/app" \
                        -w /app \
                        python:3.11-slim \
                        sh -c "pip install -r requirements.txt pytest httpx && pytest -v"
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t msjapp-notes_api:latest .
                '''
            }
        }
    }

    post {
        success {
            echo 'Tests OK - Imagen construida correctamente'
        }

        failure {
            echo 'La pipeline fallo'
        }
    }
}