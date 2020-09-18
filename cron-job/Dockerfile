FROM alpine:3.7
LABEL maintainer="rodion43pv@gmail.com>"

# Install curl
RUN apk --no-cache add curl

# Copy hello-cron file to the cron.d directory
COPY script.sh /etc/cron.d/

# Give execution rights on the cron job and apply the job
RUN chmod 0644 /etc/cron.d/script.sh && \
    crontab /etc/cron.d/script.sh

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

CMD crond && tail -f /var/log/cron.log
