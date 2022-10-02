FROM centos

RUN yum install httpd net-tools -y

WORKDIR /var/www/html

RUN echo Hello  We set Webserver inside container > /var/www/html/index.html

RUN echo  httpd >>  /root/.bashrc
#ENTRYPOINT ["   httpd   "]
#CMD [ " -DFOREGROUND  "  ]


