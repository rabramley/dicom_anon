FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN git clone https://github.com/chop-dbhi/dicom-anon.git

RUN pip install --no-cache-dir -r dicom-anon/requirements.txt

COPY ./input /usr/src/app/input
COPY ./output /usr/src/app/output

CMD [ "python", "dicom-anon/dicom_anon.py" ]