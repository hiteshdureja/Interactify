FROM jenkins/jenkins:lts
WORKDIR /jenkins
ENV JENKINS_OPTS=--httpPort=8080
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false
USER root
COPY . .
RUN apt-get update
RUN uname -m
RUN apt-get install awscli vim -y
RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh
RUN jenkins-plugin-cli --plugins ant:latest antisamy-markup-formatter:latest build-timeout:latest \
  cloudbees-folder:latest configuration-as-code:latest credentials-binding:latest \
  email-ext:latest git:latest github-branch-source:latest gradle:latest ldap:latest \
  mailer:latest matrix-auth:latest pam-auth:latest pipeline-github-lib:latest pipeline-stage-view:latest \
  ssh-slaves:latest timestamper:latest workflow-aggregator:latest ws-cleanup:latest
EXPOSE 8080