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
    git clone https://github.com/<your-github-username>/TechTrends.git
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

This repository is set up with GitHub Actions to automatically build and push Docker images to Docker Hub whenever changes are pushed to the main branch.

## Acknowledgements

This project was forked from [Cloud Native Fundamentals Scholarship Program Nanodegree Program](https://sites.google.com/udacity.com/suse-cloud-native-foundations/home), with instruction from [Kaslin Fields](https://github.com/kgamanji).

## License

This project is open source, licensed under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file in this repository.

Please replace `<your-github-username>` with your actual GitHub username. And of course, make any additional changes you feel necessary to fit your project specifics.
