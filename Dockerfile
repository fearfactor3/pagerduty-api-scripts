FROM ubuntu:latest

# get the essentials
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install -y curl 
RUN apt-get install -y wget
RUN apt-get install -y less
RUN apt-get install -y vim

# install nodejs/npm
RUN curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
RUN sh /tmp/nodesource_setup.sh
RUN rm -rf /tmp/nodesource_setup.sh
RUN apt-get install -y nodejs

# install python & pip
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3.10
RUN rm /usr/bin/python3
RUN ln -s /usr/bin/python3.10 /usr/bin/python3
RUN ln -s /usr/bin/python3.10 /usr/bin/python
RUN apt-get install -y python3-pip

# install go
RUN curl -sL https://go.dev/dl/go1.18.linux-amd64.tar.gz  -o /tmp/go.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf /tmp/go.tar.gz
RUN rm -rf /tmp/go.tar.gz
RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc

# install ruby & gem
RUN apt-get install -y ruby-full

# install java
RUN apt-get install -y default-jre

# install pagerduty-cli
RUN npm install -g pagerduty-cli
ENTRYPOINT /bin/bash