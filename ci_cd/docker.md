# Continuos Integration adn Continuos Deployment

## Docker
  <!-- For Implementation of  code See: ci_cd\docker.md  -->
  - Docker is an open platform for developing, shipping, and running applications.

  - Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
  
  - With Docker, you can manage your infrastructure in the same ways you manage your applications.
  
  - By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

## Docker architecture

  - Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers.

  - The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon.

  - The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.

  ### The Docker daemon

  - The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

  ### The Docker client

  - The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

  ### Docker registries

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
<!-- 
FROM [--platform=<platform>] <image> [AS <name>]
Or
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
Or
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
-->

FROM node:18-alpine
  - The FROM instruction initializes a new build stage and sets the Base Image for subsequent instructions. As such, a valid Dockerfile must start with a FROM instruction.

<!-- 
WORKDIR /path/to/workdir
-->

WORKDIR /app
  - The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile. If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction.
  
  - The WORKDIR instruction can be used multiple times in a Dockerfile. If a relative path is provided, it will be relative to the path of the previous WORKDIR instruction. For example: <!-- WORKDIR /a WORKDIR b WORKDIR c -->

<!-- 
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
-->

COPY . .
  - The COPY instruction copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.

  - Multiple <src> resources may be specified but the paths of files and directories will be interpreted as relative to the source of the context of the build.

  - Each <src> may contain wildcards and matching will be done using Go’s filepath.Match rules. For example:
  <!-- 
  To add all files starting with “hom”: COPY hom* /mydir/ 
  In the example below, ? is replaced with any single character, e.g., “home.txt”: COPY hom?.txt /mydir/
  -->

<!-- 
RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
RUN ["executable", "param1", "param2"] (exec form)
-->

RUN yarn install --production
  - The RUN instruction will execute any commands in a new layer on top of the current image and commit the results.
  
  - The resulting committed image will be used for the next step in the Dockerfile.

  - In the shell form you can use a \ (backslash) to continue a single RUN instruction onto the next line. For example, consider these two lines:
  <!-- RUN /bin/bash -c 'source $HOME/.bashrc; \ echo $HOME' -->

  - Together they are equivalent to this single line:
  <!-- RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME' -->

<!-- 
CMD ["executable","param1","param2"] (exec form, this is the preferred form)
CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
CMD command param1 param2 (shell form)
-->

CMD ["node", "src/index.js"]
  - There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect.

  - If CMD is used to provide default arguments for the ENTRYPOINT instruction, both the CMD and ENTRYPOINT instructions should be specified with the JSON array format.

<!--
EXPOSE <port> [<port>/<protocol>...]
-->

EXPOSE 3000
  - The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. 
  
  - You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified.

  - To actually publish the port when running the container, use the -p flag on docker run to publish and map one or more ports, or the -P flag to publish all exposed ports and map them to high-order ports.

  - By default, EXPOSE assumes TCP. You can also specify UDP:
  <!-- EXPOSE 80/udp -->

  - To expose on both TCP and UDP, include two lines:
  <!-- EXPOSE 80/tcp EXPOSE 80/udp -->

  -Regardless of the EXPOSE settings, you can override them at runtime by using the -p flag. For example:
  <!-- docker run -p 80:80/tcp -p 80:80/udp ... -->


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


## Steps

  ### Get the App
  
  - Before you can run the application, you need to get the application source code onto your machine.

  ### Build App container Image

  - In the app directory, the same location as the package.json file, create a file named Dockerfile.

  `cd app_name`
  
  `touch Dockerfile`

  Dockerfile:

  ```
    # syntax=docker/dockerfile:1
    FROM node:18-alpine
    WORKDIR /app
    COPY . .
    RUN yarn install --production
    CMD ["node", "src/index.js"]
    EXPOSE 3000
  ```

  Build container image:
    `docker build -t getting-started .`

  ```
  The docker build command uses the Dockerfile to build a new container image. You might have noticed that Docker downloaded a lot of “layers”. This is because you instructed the builder that you wanted to start from the node:18-alpine image. But, since you didn’t have that on your machine, Docker needed to download the image.

  After Docker downloaded the image, the instructions from the Dockerfile copied in your application and used yarn to install your application’s dependencies. The CMD directive specifies the default command to run when starting a container from this image.

  Finally, the -t flag tags your image. Think of this simply as a human-readable name for the final image. Since you named the image getting-started, you can refer to that image when you run a container.

  The . at the end of the docker build command tells Docker that it should look for the Dockerfile in the current directory.
  ```

### Start an app container
```
You use the -d flag to run the new container in “detached” mode (in the background).

You also use the -p flag to create a mapping between the host’s port 3000 to the container’s port 3000.

Without the port mapping, you wouldn’t be able to access the application.
```

- After a few seconds, open your web browser to `http://localhost:3000`. You should see your app.

### Update the application
- Update the source code

Build your updated version of the image, using the same docker build command you used.

`docker build -t getting-started .`

Start a new container using the updated code

`docker run -dp 3000:3000 getting-started`
```
Error response from daemon: driver failed programming external connectivity on endpoint recursing_boyd (6bd02285f1155e67754526fba5e5a4583cd0ee2b43012b70de2c299dc9301846): Bind for 0.0.0.0:3000 failed: port is already allocated
```

### Remove the old container
Get ID of the container:
`docker ps`
```
CONTAINER ID
12690dd1e684
```

Use the docker stop command to stop the container, with the ID from docker ps.
`docker stop <the-container-id>`
`docker stop 12690dd1e684`
```
STATUS
Exited
```

Once the container has stopped, you can remove it by using the docker rm command.
`docker rm <the-container-id>`
`docker rm 12690dd1e684`
```

```
You can stop and remove a container in a single command by adding the force flag to the docker rm command. For example: `docker rm -f <the-container-id>`

Restart updated app
`docker run -dp 3000:3000 getting-started`

### Share the application
1. Docker Hub: sign-in || sign-up
2. Create repo: name repo

Commands:
- You can push a new image to this repository using the CLI

`docker tag local-image:tagname new-repo:tagname`
`docker push new-repo:tagname`

- In the command line, try running the push command you see on Docker Hub. Note that your command will be using your namespace, not “docker”.

`docker push docker/getting-started`

`docker push rayxavier/getting-started:tagname`

- The push refers to repository [docker.io/rayxavier/getting-started]

- An image does not exist locally with the tag: rayxavier/getting-started

3. Tag existing image
- Login: `docker login -u YOUR-USER-NAME`
- Use the docker tag command to give the getting-started image a new name:
`docker tag getting-started YOUR-USER-NAME/getting-started`

4. Now try your push command again:
`docker push YOUR-USER-NAME/getting-started`