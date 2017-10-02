FROM jenkins
# Change to root user to install required packages
USER root
RUN apt-get update -qq &amp;&amp; apt-get install -qqy python3 python3-pip chromedriver
RUN pip3 install -q pymongo coverage jinja2 django==1.8.4
RUN pip3 install --upgrade selenium
# Change to the jenkins user for jenkins-specific modifications
USER jenkins
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
# Back to root again?!??
USER root
RUN pip3 install django-jenkins
RUN pip3 install pylint
# Update per (Jason) Voorhees - Thanks!
# switch back to jenkins user instead of
# continuing to run as root!
USER jenkins