pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Running in Bash environment"
                            python3 stop-instances.py || python stop-instances.py
                        '''
                    } else {
                        bat '''
                            @echo off
                            python stop-instances.py
                        '''
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
