FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY libc/include/global.h      libc/include/
COPY libc/src/predict.c         libc/src/
COPY libc/specs/predict.json    libc/specs/
COPY Makefile .
RUN make

COPY api/ api/

COPY bindings/utils.py      bindings/
COPY bindings/loader.py     bindings/
COPY bindings/predict.py    bindings/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]