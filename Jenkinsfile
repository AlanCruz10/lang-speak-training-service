pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'lang-speak-training-service-prod-deploy'
        PORT = '8082:8082'
        DOCKER_IMAGE_TAG = "${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
        REMOTE_USER = "ubuntu"
        REMOTE_HOST = "184.73.214.98"
//         EMAIL_ADDRESS = "213376@ids.upchiapas.edu.mx"
        SSH_CREDENTIALS_ID = "ssh-credentials-lang-speak-training-prod-ec2"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Pre-build') {
            steps {
                script {
                    echo 'Pre-building...'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE_TAG}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Testing...'
                }
            }
        }
        stage('Pre-deploy') {
            steps {
                script {
                    sshagent(credentials: ["${env.SSH_CREDENTIALS_ID}"]) {
                        sh "ssh -o StrictHostKeyChecking=no ${env.REMOTE_USER}@${env.REMOTE_HOST} 'docker stop ${env.DOCKER_IMAGE} || true && docker rm ${env.DOCKER_IMAGE} || true'"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sshagent(credentials: ["${env.SSH_CREDENTIALS_ID}"]) {
                        sh "ssh -o StrictHostKeyChecking=no ${env.REMOTE_USER}@${env.REMOTE_HOST} 'docker run --name ${env.DOCKER_IMAGE} -d -p ${env.PORT} ${env.DOCKER_IMAGE_TAG}'"
                    }
                }
            }
        }
    }
//     post {
//         success {
//             mail to: "${env.EMAIL_ADDRESS}",
//                  subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
//                  body: "Good news! The build ${env.BUILD_NUMBER} was successful."
//         }
//         failure {
//             mail to: "${env.EMAIL_ADDRESS}",
//                  subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
//                  body: "The build ${env.BUILD_NUMBER} failed. Please check the logs for details."
//         }
//     }
}