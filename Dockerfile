FROM ghcr.io/astral-sh/uv:python3.12-bookworm

RUN apt-get update -y && \
  apt-get install -y \
  g++ \
  musl-dev \
  libffi-dev \
  python3-dev \
  openssl \
  libssl-dev \
  build-essential 

WORKDIR /code
COPY pyproject.toml pyproject.toml
RUN uv pip install --system .

COPY server server/

RUN mkdir /ea-hub-data && \
    addgroup ea-hub && \
    adduser --system ea-hub-user --uid 11000 --ingroup ea-hub && \
    chown -R ea-hub-user:ea-hub /code && \
    chown -R ea-hub-user:ea-hub /ea-hub-data

# Switch to the new user
USER ea-hub-user

CMD ["gunicorn", "--config", "/code/server/gunicorn.conf.py", "--chdir" , "/code/server", "wsgi:app"]
