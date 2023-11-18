FROM python
RUN apt-get update && apt upgrade -y
RUN pip install boto3 
ADD ./mycode .
WORKDIR .
CMD ["python3","main.py"]