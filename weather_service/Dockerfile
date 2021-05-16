FROM python:3.7-alpine

WORKDIR /weather_service

# ENV FLASK_APP=server.py
# ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# EXPOSE 5200
# COPY . .
# CMD ["flask", "run"]

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5200

CMD ["python","-u", "server.py"]
