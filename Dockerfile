FROM python:3.11.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Required to install mysqlclient with Pip
RUN apt update \
  && apt install python3-dev default-libmysqlclient-dev gcc -y

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system --dev

# Add a non-root user for security
RUN useradd -m appuser

# Switch to the non-root user for security
USER appuser

# Copy the application code
COPY --chown=appuser:appuser . /app/

# Expose port 8000 on the container
EXPOSE 8000