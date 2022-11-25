
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
                sh 'pip install black; black .'
            }
        }
        stage('Lint with isort'){
            steps {
                sh 'pip install isort; isort .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "SpartanDevs"'
                sh 'pip install virtualenv'
                sh 'python -m venv spartandevs'
                sh 'source spartandevs/bin/activate'
                sh 'pip install awscli'
                sh 'touch calorietracker.tar.gz'
                sh 'pip install -r ./requirements.txt'
                sh 'pip install awscli'
                sh 'touch bookhouse.tar.gz'
                sh 'tar --exclude=bookhouse.tar.gz   -zcvf bookhouse.tar.gz .'
                sh 'DATE=`date '+%s'`'
                sh 'aws s3 cp bookhouse.tar.gz s3://calorietracker283/bookhouse-$DATE.tar.gz'
                sh 'aws s3 cp bookhouse.tar.gz s3://calorietracker283/bookhouse.tar.gz'
            }
        }
    }
}
