FROM kraar200/iqso:slim-buster

RUN git clone https://github.com/kraar200/iqthon.git /root/iqso

WORKDIR /root/iqso

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/iqso/bin:$PATH"

CMD ["python3","-m","iqso"]
