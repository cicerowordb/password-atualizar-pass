FROM     python:3.7.14-alpine3.16
LABEL    owner cicerow
LABEL    base_image python_3.7.14_alpine3.16
LABEL    app atualizar-data-base
WORKDIR  /opt/app/
RUN      adduser --home /opt/app --disabled-password user
COPY     requirements.txt /opt/app
RUN      pip3 install -r requirements.txt --no-warn-script-location
COPY     main.py /opt/app/
CMD      ["/usr/local/bin/python","/opt/app/main.py"]
