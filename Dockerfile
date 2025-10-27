# Базовий образ Jenkins
FROM jenkins/jenkins:lts

USER root

# Оновлення та установка python + pip + venv + бібліотек для Chrome
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv \
                       wget unzip curl gnupg2 libnss3 libxss1 libasound2 libatk-bridge2.0-0 \
                       libgtk-3-0 libgbm1 fonts-liberation libappindicator3-1 xdg-utils \
                       && rm -rf /var/lib/apt/lists/*

# Встановлення Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Встановлення Selenium (у Jenkins user)
USER jenkins
RUN python3 -m pip install --upgrade pip selenium pytest

# Робоча директорія за замовчуванням
WORKDIR /var/jenkins_home