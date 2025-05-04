pipeline {
  agent any

  parameters {
    string(name: 'INSTANCE_ID', defaultValue: 'i-0afe301dba1e3e310', description: 'EC2 instance ID to stop')
  }

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
            sh """
              echo "Running in Bash environment"
              python3 aws-tools/stop/stop-instances.py ${INSTANCE_ID}
            """
          } else {
            bat """
              @echo off
              python aws-tools\\stop\\stop-instances.py %INSTANCE_ID%
            """
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
