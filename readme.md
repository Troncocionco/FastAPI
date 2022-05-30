    cd /path/to/local/repository

    git init

    git status

    git add fileToAdd
    git commit -m "commit msg"

    git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git

Su Linux:

    pip3 install fastapi

Per esporre le API, analogo di Django (versione light)

    pip3 install uvicorn

Per eseguire il WebServer:

    uvicorn myapi:app --reload
    