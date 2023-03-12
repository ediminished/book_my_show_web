FROM python:3.9-alpine

COPY book_my_show /book_my_show/

WORKDIR /book_my_show

RUN pip install -r requirements.txt

EXPOSE 8005
CMD ["python", "local_app.py"]
