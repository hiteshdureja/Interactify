properties([pipelineTriggers([githubPush()])])
pipeline {
    $regionName = "ap-southeast-1"
    $serviceName = "interactify"
    $taskDefinitionFile = "task-definition.yaml"
    $deployConfig = "deploy-config.yaml"
    $dockerHost = ""
    stages {
        stage("Source Code Management") {
            withCredentials([gitUsernamePassword(credentialsId: "github-creds", gitToolname: "git-tool")]) {
                sh "git clone https://github.com/hiteshdureja/interactify"
            }
        }
        stage("Docker Build") {
            sh "cd interactify"
            sh "docker build -t ${serviceName}:latest ."
        }
        stage("Docker Push") {
            sh "aws ecr get-login-password --region ${regionName} | docker login --username AWS " + \
               "--password-stdin ${dockerHost}"
            sh "docker tag ${serviceName}:latest ${dockerHost}/${serviceName}:latest"
            sh "docker push ${dockerHost}/${serviceName}:latest"
        }
        stage('Docker Cleanup') {
            sh "docker system prune -f"
            sh """docker images | grep """ + serviceName + """ | awk '{print \$1":"\$2}' | xargs docker rmi"""
        }
        stage("Deploy") {
            sh "aws ecs register-task-definition --cli-input-yaml file://${taskDefinitionFile}"
            sh "aws --region ${regionName} ecs update-service --cli-input-json file://${deployConfig}"
        }
    }
}