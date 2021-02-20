FROM python:3.8-slim

RUN useradd --create-home --shell /bin/bash factory_facker

WORKDIR /factory_facker

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

USER factory_facker

COPY . .

CMD ["bash"]