pipeline {
  agent {
    docker {
      image 'python:3.12'    // pulls the official Python 3.12 image
      args  '-u'             // (optional) keeps logs unbuffered
    }
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build') {
      steps { echo 'Building…' }
    }
    stage('Test') {
      steps { echo 'Testing…' }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying – stopping instances…'
        sh 'python stop_instance.py'
      }
    }
  }

  post {
    success { echo 'Deployment completed successfully!' }
    failure { echo 'Deployment failed :(' }
  }
}
