pipeline {
    agent any

    stages {

        stage('Pre-check Docker') {
            steps {
                powershell '''
                    Write-Host "Checking Docker availability on Windows..."

                    docker --version
                    if ($LASTEXITCODE -ne 0) {
                        Write-Error "Docker is NOT installed or not in PATH."
                        exit 1
                    }

                    docker info
                    if ($LASTEXITCODE -ne 0) {
                        Write-Error "Docker daemon is NOT running. Start Docker Desktop."
                        exit 1
                    }

                    Write-Host "Docker is available. Continuing..."
                '''
            }
        }

        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/SNIGDHA-VIJAY/cie2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                powershell '''
                    Write-Host "Building docker image zipgo-svc:5 ..."
                    docker build -t zipgo-svc:5 .
                    if ($LASTEXITCODE -ne 0) {
                        Write-Error "Docker build failed"
                        exit 1
                    }
                '''
            }
        }

        stage('Run Container') {
            steps {
                powershell '''
                    Write-Host "Stopping old container if exists..."
                    docker rm -f zipgo-container 2>$null

                    Write-Host "Starting container on port 12120..."
                    docker run -d --name zipgo-container -p 12120:5000 zipgo-svc:5

                    if ($LASTEXITCODE -ne 0) {
                        Write-Error "Failed to start container"
                        exit 1
                    }

                    Write-Host "Container started successfully!"
                '''
            }
        }
    }

    post {
        success {
            powershell 'Write-Host "SUCCESS: zipgo-svc:5 deployed on port 12120"'
        }
        failure {
            powershell 'Write-Host "FAILURE: Check Jenkins logs"'
        }
    }
}
