from src.infra.db import PostgresRepository
from src.application.use_cases import sync_repo_data

WORKFLOWS_DIR = "/workspace/n8n/repo-data/workflows"
CREDENTIALS_DIR = "/workspace/n8n/repo-data/credentials"

repo = PostgresRepository()
result = sync_repo_data(repo, WORKFLOWS_DIR, CREDENTIALS_DIR)

for path in result["workflows"]:
    print(f"Saved workflow: {path}")

for path in result["credentials"]:
    print(f"Saved credential: {path}")

print(
    f"Done. {len(result['workflows'])} workflow(s), "
    f"{len(result['credentials'])} credential(s) saved."
)
