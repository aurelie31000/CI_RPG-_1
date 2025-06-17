// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'dev', url: 'https://github.com/aurelie31000/CI_RPG-_1.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt || true'
            }
        }
        stage('Test') {
            steps {
                sh 'PYTHONPATH=src python3 -m unittest discover src/test/python'
            }
        }
    }
    post {
        success {
            echo 'Build successful. Performing fast-forward merge to master.'
            script {
                withCredentials([usernamePassword(credentialsId: 'github-jenkins-pat', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    sh '''
                    git config user.name ""
                    git config user.email "jenkins@example.com"
                    git checkout main
                    git pull origin main
                    git merge --ff-only dev
                    git push origin main
                    '''
                }
            }
        }
        failure {
            echo 'Build failed. Reverting dev and pushing failing commit to a new branch.'
            script {
                withCredentials([usernamePassword(credentialsId: 'github-jenkins-pat', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    def timestamp = new Date().format('yyyyMMddHHmmss')
                    def failureBranch = "failures/"

                    def failedCommitHash = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()

                    sh """
                    git config user.name ""
                    git config user.email "jenkins@example.com"

                    git reset --hard HEAD~1
                    git push origin dev --force

                    git checkout -b  
                    git push origin 
                    """
                }
            }
        }
    }
}
