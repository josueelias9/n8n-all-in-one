import json
import os
from typing import Optional
from src.application.ports import AppRepository


def _clear_directory(directory: str) -> None:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def sync_repo_data(repo: AppRepository, workflows_dir: str, credentials_dir: str) -> dict:
    _clear_directory(workflows_dir)
    _clear_directory(credentials_dir)

    saved_workflows = []
    for workflow_id, _ in repo.list_workflows():
        data = repo.get_workflow_json(workflow_id)
        if data:
            path = os.path.join(workflows_dir, f"{workflow_id}.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            saved_workflows.append(path)

    saved_credentials = []
    for cred_id in repo.list_credential_ids():
        data = repo.get_credential_json(cred_id)
        if data:
            path = os.path.join(credentials_dir, f"{cred_id}.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            saved_credentials.append(path)

    return {"workflows": saved_workflows, "credentials": saved_credentials}
