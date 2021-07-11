# tarabut

I have created the application with the API, using Python and Flask.
The deployment is through Kubernetes manifest files. 
The build of Docker Image is automated through Github Action which gets triggered for every push. 

If building the Docker image locally, install the pre-requisites 
python
pip

The other requirements are installed using pip through the requirements.txt file, which includes Flask and Flask-RESTful

pip/pip3 install -r requirements.txt 

The application has an API with the endpoint {BASE URL}/name exposed. 
The endpoint returns current date and time in the UAE timezone with values of the NAME and PASSWORD variables. 

The variable "NAME" takes its value from the Configmap at the time of deployment from the Kubernetes manifest
The variable "PASSWORD" takes its value from the secret at the time of deployment from the Kubernetes manifest

Have used pytz to set the timezone to UAE


If deploying locally, please set the test URL against localhost (127.0.0.1) inside your hosts file as shown below,
For example, tarabut.example.com/name

If deploying on cloud, the service type can be set to 'loadbalancer' which will provision a load balancer for access from the outside world. 

The application has been containerized using Dockerfile. 
The Docker image gets built and pushed by the Github Action which gets triggered for every push to the main branch.

Liveness and Readiness probes have been configured to perform health checks







