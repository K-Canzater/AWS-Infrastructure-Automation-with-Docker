pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Get code from GitHub repository
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                // If you need to build anything before deploying
                echo 'Building...'
                // Add build commands here if needed
            }
        }
        
        stage('Test') {
            steps {
                // Run tests if you have any
                echo 'Testing...'
                // Add test commands here if needed
            }
        }
        
        stage('Deploy') {
            steps {
                // This is where your stop instance code would run
                echo 'Deploying - stopping instances...'
                // Example if you're using a script:
                sh 'chmod +x ./stop_instance.sh'
                sh './stop_instance.sh'
                
                // If you're using Python:
                // sh 'python stop_instance.py'
            }
        }
    }
    
    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed :('
        }
    }
}