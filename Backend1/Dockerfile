FROM python:3.8-slim
WORKDIR /opt/MTS_Task
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "backend1.py"]
