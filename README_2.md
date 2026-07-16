# - How to use it

start the project with compose

```sh
docker compose --profile gpu-nvidia up --build
```

(optional) use a template to start working

![](README-images/readme-image-1.png)


- Go to `http://localhost:5678`. When you are done working, save your project.


![](README-images/readme-image-2.png)

- Just saving the workflow is ok, but it will only live on `n8n container` memory. To push the workflow and credentials to github, execute the following command. 

```sh
docker compose up extract-workflow --build
```


- Then you can use your git tool to have control over the changes you have made. Whe you are done, delete everything:

```sh
docker compose --profile gpu-nvidia down -v
```


# - Keep in sync

## -- test original repo

- delete local main branch
- checkout to upstream/main
- test

## -- sync

TODO

## -- misc

- it takes the id of the json, the file name is just a reference