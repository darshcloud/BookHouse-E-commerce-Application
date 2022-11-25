pipeline { 
    agent jenkins

    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('cleanup') { 
            steps { 
                sh 'rm -rf spartandevs' 
            }
        }
        stage('Build') { 
            steps { 
                sh 'pip3 install -r requirements.txt' 
            }
        }
        stage('Lint with Black'){
            steps {
                sh 'pip3 install black; export PATH=$PATH:/var/lib/jenkins/.local/bin ;    black .'
            }
        }
        stage('Lint with isort'){
            steps {
                sh 'pip3 install isort;export PATH=$PATH:/var/lib/jenkins/.local/bin;isort .'
            }
        }
        stage('Deploy') {
            environment {
                AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
                REGION = 'us-east-1'
            }
            steps {
                sh 'echo "SpartanDevs"'
                sh 'pip3 install virtualenv'
                sh 'python3 -m venv spartandevs'
                sh 'source spartandevs/bin/activate'
                sh 'pip3 install awscli'
                sh 'touch calorietracker.tar.gz'
                sh 'pip3 install -r ./requirements.txt'
                sh 'pip3 install awscli'
                sh 'touch bookhouse.tar.gz'
                sh 'tar --exclude=bookhouse.tar.gz   -zcvf bookhouse.tar.gz .'
                sh 'aws s3 cp bookhouse.tar.gz s3://spartandevscmpe272/bookhouse-1234.tar.gz'
                sh 'aws s3 cp bookhouse.tar.gz s3://spartandevscmpe272/bookhouse.tar.gz'
                sh 'rm -rf spartandevs'
            }
        }
    }
    post {
        success {
            withCredentials([usernamePassword(credentialsId: 'sirishacyd', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh 'curl -X POST --user $USERNAME:$PASSWORD --data  "{\\"state\\": \\"success\\"}" --url https://api.github.com/repos/hegdebhavya/Spartandevs/statuses/$GIT_COMMIT'}
            }
        failure {
            withCredentials([usernamePassword(credentialsId: 'sirishacyd', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh 'curl -X POST --user $USERNAME:$PASSWORD --data  "{\\"state\\": \\"failure\\"}" --url https://api.github.com/repos/hegdebhavya/Spartandevs/statuses/$GIT_COMMIT'}
            }
    }
}
}