pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Environment Detection') {
            steps {
                script {
                    // Try to detect environment
                    try {
                        sh 'echo "Bash detected!"'
                        env.IS_BASH = 'true'
                    } catch (Exception e) {
                        bat 'echo "Windows detected!"'
                        env.IS_BASH = 'false'
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    if (env.IS_BASH == 'true') {
                        // Bash method
                        sh '''
                            echo "Running in Bash environment"
                            export PATH=$PATH:/usr/bin
                            echo "Checking Python version..."
                            which python3 || which python || echo "Python not found in Bash!"
                            python3 --version || python --version
                            python3 stop_instance.py || python stop_instance.py
                        '''
                    } else {
                        // Windows method
                        bat '''
                            @echo off
                            echo "Running in Windows environment"
                            python --version 2>nul && (
                                echo Python found, running script...
                                python stop_instance.py
                            ) || (
                                echo Python not found in regular PATH, trying system Python
                                where python 2>nul || echo Cannot locate Python, please check installation!
                                py -3 --version || echo Failed to run with py launcher
                                py -3 stop_instance.py || echo Failed to run with py launcher
                            )
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
