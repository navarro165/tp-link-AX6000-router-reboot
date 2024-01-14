FROM python:3.10-slim

WORKDIR /app

# udpate with your login credentials
ENV ROUTER_REBOOT_USERNAME=your-user-name
ENV ROUTER_REBOOT_PASSWORD=your-password

RUN pip install selenium

COPY . .

CMD ["python", "reboot.py"]
