# TechTrends

TechTrends is a Python Flask web application that serves as a Blog website. It displays a list of IT articles and allows for the creation of new articles.

This project was developed as a part of the Cloud Native Fundamentals Scholarship Program Nanodegree Program by [Udacity](https://www.udacity.com/).

## Getting Started

The project uses Python and Flask for the web service, and SQLite for the database.

### Prerequisites

- Python 3.8+
- Pip package manager (usually comes with Python)

### Local Setup

1. Clone this repository and navigate into it:

    ```bash
    git clone https://github.com/estonezzz/TechTrends.git
    cd TechTrends
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the application:

    ```bash
    python app.py
    ```

Access the application at `http://localhost:3111`.

### Docker Setup

The application can also be containerized and run as a Docker container.

1. Build the Docker image (from the directory containing the Dockerfile):

    ```bash
    docker build -t techtrends .
    ```

2. Run the application as a Docker container:

    ```bash
    docker run -d -p 3111:3111 techtrends
    ```

Access the application at `http://localhost:3111`.

## Continuous Integration

This repository utilizes GitHub Actions for continuous integration. Every time a new commit is pushed to the main branch, an automated process is triggered. This process includes setting up the required environments, checking out the latest code, building a new Docker image from it, and then pushing this Docker image to Docker Hub.

Through this CI pipeline, we ensure that our Docker image always represents the latest version of the application in a production-ready state. This streamlines development and prepares for seamless continuous delivery.


## Continuous Deployment

For Continuous Deployment (CD), this project uses ArgoCD, a declarative GitOps continuous delivery tool for Kubernetes. Application definitions, configurations, and environments should be declaratively modeled and versioned in a Git repository. You'll also use Helm, a package manager for Kubernetes, to define, install, and upgrade complex Kubernetes applications.

### Prerequisites

- ArgoCD installed on your Kubernetes cluster.
- Helm v3 installed.

### Steps

1. Start by packaging your application with Helm. This involves creating a Helm chart, which is a collection of files that describe a related set of Kubernetes resources. 

    ```bash
    helm create techtrends
    ```

    Modify the generated templates to fit your application's needs. Create `values.yaml`, `values-prod.yaml`, and `values-staging.yaml` for different environments.

2. The application Docker image is built and pushed to Docker Hub automatically by the GitHub Actions CI pipeline whenever changes are pushed to the main branch.

3. Use ArgoCD to create an application for each environment:

    For staging:

    ```bash
    argocd app create techtrends-staging --repo https://github.com/<your-github-username>/TechTrends.git --path helm --dest-server https://kubernetes.default.svc --dest-namespace staging --values values-staging.yaml
    ```

    For production:

    ```bash
    argocd app create techtrends-prod --repo https://github.com/<your-github-username>/TechTrends.git --path helm --dest-server https://kubernetes.default.svc --dest-namespace production --values values-prod.yaml
    ```

4. You can then sync the applications:

    For staging:

    ```bash
    argocd app sync techtrends-staging
    ```

    For production:

    ```bash
    argocd app sync techtrends-prod
    ```

    This will deploy your application to your Kubernetes cluster.

This guide provides an overview of the deployment process and might need to be adjusted to fit your specific use case or environment. Ensure to replace `<your-github-username>` with your actual GitHub username.
