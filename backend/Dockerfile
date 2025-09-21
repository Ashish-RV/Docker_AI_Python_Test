FROM python:3.13.4-slim-bullseye

# python virtual environment
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH


WORKDIR /app

# Copy local folder to static folder
#RUN mkdir -p /static_folder
#COPY /static_html /static_folder

#Both command are same
#COPY ./static_html /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src .

#RUN echo "Hello" > index.html

# docker build -f Dockerfile -t pyapp .
# docker run -it pyapp
# docker login
# docker push pyapp
# docker build -f Dockerfile -t ashish14141/ai-agent-test:latest .
# Docker push ashish14141/ai-agent-test:latest

# python -m http.server 8000
# docker run -it -p 3000:8000 pyapp
# docker run -it -p 8000:8000 pyapp
CMD ["python","-m","http.server","8000"]