FROM python:2.7

# Copy and install requirements for container
COPY README.md /
COPY src/server /
COPY src/server/run.py /

# Make port 12345 available to the world outside this container
EXPOSE 12345

CMD [ "python", "-u", "run.py" ]