FROM python:3.7-alpine

WORKDIR /weather_service

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE 5200

CMD ["python","-u", "server.py"]