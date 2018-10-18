# example docker app

I have `docker`-ized the **DEEP NEURAL PRINT** (tm rzl 2018) `tacoworld` application, and am sharing it with the world here.

to recreate from scratch:

1. clone this repository and change into the resulting directory
2. run `docker build -t REPOSITORY_NAME[:tag] .` to create a `docker` `image`
3. run `docker run REPOSITORY_NAME[:tag]` to build a `container` from that `image` and execute the application.
