# we select the base image for the base of our container
FROM python:3.6.3

COPY /appv1 /tmp/appv1
WORKDIR /temp/appv1

# RUN mkdir working
RUN pip install --upgrade pip
# RUN pip install --upgrade cython
# RUN pip install numpy
# also you can use the requirements.txt
RUN pip install --no-cache-dir -r /tmp/appv1/newrequirements.txt 

# EXPOSE 5001

# ENTRYPOINT [ "python" ]
# RUN cd /tmp/appv1
# RUN export FLASK_APP=/tmp/appv1/app
CMD ["python", "/tmp/appv1/app.py"]
# CMD ["flask", "run", "--host", "0.0.0.0"]



