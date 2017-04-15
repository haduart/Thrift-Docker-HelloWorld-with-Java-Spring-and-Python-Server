FROM alpine:latest
MAINTAINER eduard@iot-partners.com

RUN apk add --no-cache openjdk8
COPY jre-policy/* /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/

ENV SERVER_PORT=8080
ENV DB_ADDRESS=localhost:3306
ENV DB_USERNAME=root
ENV DB_PASSWORD=changeme

ENV MAX_HEAP_SIZE="384M"
ENV PYTHON_THRIFT_SERVER=192.168.99.100
ENV PYTHON_THRIFT_PORT=9090

COPY target/*.jar /demo.jar

EXPOSE $SERVER_PORT
ENTRYPOINT ["sh", "-c", "/usr/bin/java -Xms${MAX_HEAP_SIZE} -Xmx${MAX_HEAP_SIZE} -Ddb.address=${DB_ADDRESS} -Ddb.username=${DB_USERNAME} -Ddb.password=${DB_PASSWORD} -Dserver.port=${SERVER_PORT} -Dthrift.server=${PYTHON_THRIFT_SERVER} -Dthrift.port=${PYTHON_THRIFT_PORT}  -jar /demo.jar"]
