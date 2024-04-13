FROM ubuntu:latest
LABEL authors="agabi"

ENTRYPOINT ["top", "-b"]