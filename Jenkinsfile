pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                checkout scm
                sh 'sudo ./jobs/docker_build.sh'
                //stash includes: '**/target/*.jar', name: 'app' 
            }
        }
        stage('Test on Docker') {
            /*agent { 
                label 'linux'
            }*/
            agent any
            steps {
                sh 'sudo ./jobs/docker_run_tests.sh'
            }
            //post {
            //    always {
            //        junit '**/target/*.xml'
            //    }
            //}
        }
        //stage('Test on Windows') {
        //    agent {
        //        label 'windows'
        //    }
        //    steps {
        //        unstash 'app'
        //        bat 'make check' 
        //    }
        //    post {
        //        always {
        //            junit '**/target/*.xml'
        //        }
        //    }
        //}
    }
}