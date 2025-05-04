pipeline {
  agent any

  parameters {
    string(name: 'INSTANCE_ID', defaultValue: 'i-0afe301dba1e3e310', description: 'EC2 instance ID to stop')
  }

  environment {
    // Map the single-ID parameter into the variable your script expects
    INSTANCE_IDS = "${INSTANCE_ID}"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Deploy') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 aws-tools/stop/stop-instances.py'
          } else {
            bat 'python aws-tools\\stop\\stop-instances.py'
          }
        }
      }
    }
  }

  post {
    success { echo 'Successful!' }
    failure { echo 'Deployment failed!' }
  }
}
