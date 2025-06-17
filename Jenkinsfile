// Jenkinsfile
// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // MODIFICATION ICI : Utilisez l'URL de votre dépôt actuel
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
            echo 'Build successful. Performing fast-forward merge to main.' // Mis à jour le message
            script {
                withCredentials([usernamePassword(credentialsId: 'github-jenkins-pat', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    sh '''
                    git config user.name "${GIT_USERNAME}"
                    git config user.email "jenkins@example.com"
                    git checkout main // MODIFICATION ICI : Ciblez la branche 'main'
                    git pull origin main // MODIFICATION ICI : Tirez depuis 'main'
                    git merge --ff-only dev
                    git push origin main // MODIFICATION ICI : Poussez vers 'main'
                    '''
                }
            }
        }
        failure {
            echo 'Build failed. Reverting dev and pushing failing commit to a new branch.'
            script {
                withCredentials([usernamePassword(credentialsId: 'github-jenkins-pat', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    def timestamp = new Date().format('yyyyMMddHHmmss')
                    def failureBranch = "failures/${timestamp}"

                    // Capture le hash du commit qui a causé l'échec
                    def failedCommitHash = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()

                    sh """
                    git config user.name "${GIT_USERNAME}"
                    git config user.email "jenkins@example.com"

                    # Réinitialise la branche dev au commit PRÉCÉDENT celui qui a causé l'échec
                    # C'est une réécriture d'historique ! Utilisez avec prudence.
                    git reset --hard HEAD~1
                    git push origin dev --force # Push forcé nécessaire

                    # Crée et pousse la branche d'échec à partir du commit échoué
                    git checkout -b ${failureBranch} ${failedCommitHash}
                    git push origin ${failureBranch}
                    """
                }
            }
        }
    }
}