# - N8N - All in One

## -- pre-requisites
- ngrok
- docker compose

## -- How to use it

- start the project with compose

```sh
docker compose --profile gpu-nvidia up --build
```

- create a reverse proxy using ngrok. This is necesasary when using Telegram because Telegram needs to know how to reach our local n8n service.

```sh
ngrok http 5678
```

- (optional) use a template to start working

![](README-images/readme-image-1.png)


- Go to `http://localhost:5678`. When you are done working, save your project.


![](README-images/readme-image-2.png)

- Just saving the workflow is ok, but it will only live on `n8n container` memory. To push the workflow and credentials to github, execute the following command. It will take the id of the workflow or the credential and use it as the name of the json file.

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


## -- protect the env variables

encrypt
```sh
sops encrypt --age PUBLIC_KEY .env > enc.env
```

decrypt
```sh
SOPS_AGE_KEY_FILE=../key.txt sops decrypt enc.env > .env