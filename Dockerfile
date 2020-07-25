FROM python:2.7

# Set the working directory to /app
#WORKDIR /app

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY README.md /
COPY src/server /
COPY src/server/run.py /


# Make port 12345 available to the world outside this container
EXPOSE 12345

CMD [ "python", "-u", "run.py" ]