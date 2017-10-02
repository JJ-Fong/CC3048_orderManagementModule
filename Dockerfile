# Use an official Python runtime as a parent image
#FROM python:2.7-slim
#WORKDIR /app
#ADD . /app
#RUN pip install -r requirements.txt
#EXPOSE 8000
#ENV NAME World
#CMD ["python", "manage.py", "runserver"]
#
#
FROM jenkins
# Change to root user to install required packages
USER root
RUN apt-get update -qq &amp;&amp; apt-get install -qqy python27
#python3-pip chromedriver
# Change to the jenkins user for jenkins-specific modifications
USER jenkins
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
# Back to root again?!??
USER root
RUN pip install -r requirements.txt
# Update per (Jason) Voorhees - Thanks!
# switch back to jenkins user instead of
# continuing to run as root!
USER jenkins