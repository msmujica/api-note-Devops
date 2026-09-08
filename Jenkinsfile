pipeline {
    agent any

    stages {

        stage('Build test image') {
            steps {
                sh '''
                    docker build -t msjapp-notes_api:test .
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    docker run --rm \
                        msjapp-notes_api:test \
                        pytest -v
                '''
            }
        }

        stage('Build final image') {
            steps {
                sh '''
                    docker tag \
                        msjapp-notes_api:test \
                        msjapp-notes_api:latest
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