
pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
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
            }
        }
    }
}
