pipeline {
    agent any


environment {
//Git settings
GIT_ID = '9749b59b-6190-482e-ab62-1d26e216d555'
GIT_SECRET = credentials("${GIT_ID}")
GIT_CRED_USER = "${GIT_SECRET_USR}"
GIT_CRED_PASS = "${GIT_SECRET_PSW}"
BRANCH = "${env.BRANCH}"
}
stages {

        stage("Clean up workspace") {
        steps {
            dir('.') {
            deleteDir()
            cleanWs()

                }
            }
        }

        stage("Checkout to Branch") {
            steps {
                script {
                  checkout([$class: 'GitSCM',
                        branches: [[name: "*/${env.BRANCH}"]],
                        browser:
                            [$class: 'Stash',
                            repoUrl: 'https://github.com/yurinozhuk/GetGrant.git'],
                            doGenerateSubmoduleConfigurations: false,
                                extensions: [],
                                submoduleCfg: [],
                                    userRemoteConfigs:
                                        [[credentialsId: "${env.GIT_ID}",
                                        name: 'origin',
                                        refspec: "+refs/heads/${env.BRANCH}:refs/remotes/origin/${env.BRANCH}",
                                        url: "https://${env.GIT_CRED_USER}@github.com/yurinozhuk/GetGrant.git"]]])
                }
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Run tests') {
            steps {
                script {
                    sh 'python3 -m venv testenv && . testenv/bin/activate && pip install -r requirements.txt && pytest -v --alluredir=report'
                    // sh '. testenv/bin/activate'
                    // sh 'pip install -r requirements.txt'
                    // sh 'pytest'
                }
            }
        }

}
}