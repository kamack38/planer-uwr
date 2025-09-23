FROM node:14.17-slim AS builder

RUN useradd -ms /bin/bash appuser
COPY --chown=appuser:appuser ./planer-uwr-webapp/.meteor ./planer-uwr-webapp/package*.json /home/appuser/planer-uwr-webapp
USER appuser
WORKDIR /home/appuser

RUN mkdir ~/.npm-global && npm config set prefix '~/.npm-global' && export PATH=~/.npm-global/bin:$PATH
RUN npm install -g meteor@2.16.0 
WORKDIR /home/appuser/planer-uwr-webapp
RUN npm install --production

COPY --chown=appuser:appuser ./planer-uwr-webapp /home/appuser/planer-uwr-webapp
RUN /home/appuser/.meteor/meteor build /home/appuser/build
WORKDIR /home/appuser/build
RUN tar -xzf planer-uwr-webapp.tar.gz

FROM node:14.17-slim

COPY --from=builder /home/appuser/build/bundle /bundle
WORKDIR /bundle/programs/server
RUN npm install
ENTRYPOINT [ "/usr/local/bin/node", "/bundle/main.js" ]
