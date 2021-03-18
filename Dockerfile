
FROM tensorflow/tensorflow:nightly
ADD . emodetext/

WORKDIR /emodetext
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt 
CMD ["python", "emodetext-app.py"]