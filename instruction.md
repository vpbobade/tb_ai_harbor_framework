# Kubernetes Deployment Recovery

A microservice application has been deployed to a Kubernetes cluster but is currently not reachable.

Your task is to investigate the environment and fix the deployment so the service becomes accessible.

The repository contains:
- a simple Python microservice
- Kubernetes deployment manifests
- service configuration

The deployment is currently misconfigured.

You may modify any files under `/app/`.

Once fixed, the application should start successfully and respond to HTTP requests.

Expected behavior:
The service should respond successfully when accessed locally.

Constraints:
- Work only within the `/app` directory.
- Do not modify the test files.

Goal:
Ensure the microservice runs correctly and the health endpoint returns a successful response.
