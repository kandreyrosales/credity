FROM python:3
RUN mkdir /credity
WORKDIR /credity
COPY . /credity
CMD [ "python", "./main_problem_credity.py" ]