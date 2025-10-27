# Базовий образ Jenkins (LTS, зі встановленим JDK)
FROM jenkins/jenkins:lts

USER root

# Оновимо пакети і доставимо python3 + pip + venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# (опційно) оновити pip до останнього
RUN python3 -m pip install --upgrade pip

# Повертаємось до jenkins user (важливо для прав доступу в контейнері)
USER jenkins

# Робоча директорія Jenkins за замовчуванням /var/jenkins_home
# Порти і volume налаштуємо в docker-compose