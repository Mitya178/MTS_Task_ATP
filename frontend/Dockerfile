FROM python:3.8-slim
WORKDIR /opt/MTS_Task
COPY requirements2.txt .
RUN pip install --no-cache-dir -r requirements2.txt
COPY . .
CMD ["python", "frontend.py"]
