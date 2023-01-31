# Continuos Integration adn Continuos Deployment

## Docker
  <!-- For Implementation of  code See: ci_cd\docker.md  -->
  - Docker is an open platform for developing, shipping, and running applications.

  - Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
  
  - With Docker, you can manage your infrastructure in the same ways you manage your applications.
  
  - By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

  ### Docker architecture

    - Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers.

    - The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon.
    
    - The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.

    #### The Docker daemon

      - The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

    #### The Docker client

      - The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

    #### Docker registries

      - A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. 
      
      - You can even run your own private registry.

      - When you use the docker pull or docker run commands, the required images are pulled from your configured registry.
      
      - When you use the docker push command, your image is pushed to your configured registry.

  ### Docker objects

    - When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.

    #### Images

      - An image is a read-only template with instructions for creating a Docker container. 
      
      - Often, an image is based on another image, with some additional customization.
      
      - For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

      - You might create your own images or you might only use those created by others and published in a registry. 
      
      - To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. 
      
      - Each instruction in a Dockerfile creates a layer in the image.

      - When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt.
      
      - This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.
    
    #### Containers
    
      - A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI.
      
      - You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.

      - By default, a container is relatively well isolated from other containers and its host machine. You can control how isolated a container’s network, storage, or other underlying subsystems are from other containers or from the host machine.

      - A container is defined by its image as well as any configuration options you provide to it when you create or start it. When a container is removed, any changes to its state that are not stored in persistent storage disappear.

### Dockerfile

  - In order to build the container image, you’ll need to use a Dockerfile.

  - A Dockerfile contains a script of instructions that Docker uses to create a container image.

# Install the base requirements for the app.
```
# syntax=docker/dockerfile:1
- FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000

# This stage is to support development.
- FROM --platform=$BUILDPLATFORM python:alpine AS base
- WORKDIR /app
- COPY requirements.txt .
- RUN pip install -r requirements.txt

- FROM --platform=$BUILDPLATFORM node:18-alpine AS app-base
- WORKDIR /app
- COPY app/package.json app/yarn.lock ./
- COPY app/spec ./spec
- COPY app/src ./src

# Run tests to validate app
FROM app-base AS test
- RUN yarn install
- RUN yarn test

# Clear out the node_modules and create the zip
FROM app-base AS app-zip-creator
- COPY --from=test /app/package.json /app/yarn.lock ./
- COPY app/spec ./spec
- COPY app/src ./src
- RUN apk add zip && \
    zip -r /app.zip /app

# Dev-ready container - actual files will be mounted in
- FROM --platform=$BUILDPLATFORM base AS dev
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]

# Do the actual build of the mkdocs site
- FROM --platform=$BUILDPLATFORM base AS build
- COPY . .
- RUN mkdocs build

# Extract the static content from the build
# and use a nginx image to serve the content
- FROM --platform=$TARGETPLATFORM nginx:alpine
- COPY --from=app-zip-creator /app.zip /usr/share/nginx/html/assets/app.zip
- COPY --from=build /app/site /usr/share/nginx/html
```