FROM python:3

WORKDIR /app

#ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt

RUN python -m venv almacenTeleCable
RUN /bin/bash -c "source almacenTeleCable/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]