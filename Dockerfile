FROM ubuntu:19.10

RUN apt-get update && apt-get install pandoc openjdk-8-jdk wget curl xvfb -y && wget https://github.com/cytoscape/cytoscape/releases/download/3.7.2/cytosc$
ENTRYPOINT ["/bin/sh", "-c", "/usr/bin/xvfb-run /cytoscape-unix-3.7.2/cytoscape.sh"]
CMD ["/bin/sleep", "60"]

# You can try this Dockerfile with
# docker build -t test .
# docker run -d -it -p 1234:1234 test
# curl http://localhost:1234/
