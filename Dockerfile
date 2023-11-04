# 
FROM python:3.9

# 
WORKDIR /CleanText

# 
COPY ./requirements.txt /CleanText/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /CleanText/requirements.txt

RUN python -m spacy download en_core_web_sm
# 
COPY ./app /CleanText/app

ENV PYTHONPATH "${PYTHONPATH}:/CleanText"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]