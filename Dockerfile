FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN  pip install --no-cache-dir -r requirements.txt

COPY . .

ENV WEBEX_TOKEN=ODM2ZDA0ZTUtNzdlNS00NWIxLThiZDAtNGJiYmI0YzY5ZDQ5YmQzNDMzOTUtN2Ew_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d 

# Command to run the Webex bot
CMD ["python", "Navales_Finals.py"]