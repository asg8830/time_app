FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 asg8830 && \
    useradd -r -u 999 -g asg8830 asg8830

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask

USER asg8830

COPY --chown=asg8830:asg8830 . .

CMD [ "python", "./run.py" ]
