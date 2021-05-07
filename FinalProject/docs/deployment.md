
# Instructions for deploying app (how an operator should deploy system on a k8s cluster)

	
Install this project by cloning the repository, then navigating to the FinalProject directory. For example:

```bash
git clone https://github.com/zoeclairewatson/zcw268_coe332.git 
cd FinalProject
```

Pull the existing image from DockerHub:

```bash
docker pull zoeclairewatson/final:latest
```


## Deploying Flask API Test Environment to Kubernetes

Within this FinalProject, navigate to the test redis directory within the deploy directory:

```bash
cd deploy/test/redis
```

Create a Persistent Volume Claim for Redis data:

```bash
kubectl apply -f test-redis-pvc.yml
```

Create a Deployment for the Redis database:

```bash
kubectl apply -f test-redis-deployment.yml
```

Create a Service for the Redis database:

```bash
kubectl apply -f test-redis-service.yml
```

Now that the Redis Service has been created, there are manual changes that need to be executed within the api and worker deployments to update the Redis Service IP. First, check the Redis service Cluster-IP using:\

Note: This procedure of manually updating the Redis Service IP will need to be re-executed when deploying the production environment for the new Production Redis Service IP - this selector can be adjusted to "app=kz-prod-redis"

```bash
kubectl get services --selector "app=kz-test-redis"
```

Navigate to test api directory and update the flask deployment yml file to use this Redis service IP:

```bash
cd ../api
vim test-flask-deployment.yml
```

Manually replace the value of the environment variable named REDIS_IP:

```bash
env:

  ...

- name: REDIS_IP
  value: "<enter Redis Service IP here>"
```

Create a Deployment for the flask API:

```bash
kubectl apply -f test-flask-deployment.yml
```

Create a service for the flask API:

```bash
kubectl apply -f test-flask-service.yml
```

Navigate to test worker directory and update the worker deployment yml file to use this same Redis service IP:

```bash
cd ../worker
vim test-worker-deployment.yml
```

Manually replace the value of the environment variable named REDIS_IP in the same way:

```bash
env:

  ...

- name: REDIS_IP
  value: "<enter Redis Service IP here>"
```

Create a Deployment for the worker:

```bash
kubectl apply -f test-worker-deployment.yml
```

Navigate out of the worker and test directories and into the deployment tmp directory:

```bash
cd ../../tmp
vim service.yml
```

Create NodePort Service:\
(this will later be used to download image to browser)\

Manually check service.yml to ensure that spec.selector matches the ```kz-test-flask``` app label for the api test environment.\
Note: This procedure of manually checking/updating the selector will need to be re-executed when deploying the production environment - this selector can be adjusted to "app=kz-prod-redis" to match the label for the api production environment

```bash
...

spec:
  selector:
    app: kz-test-flask

...
```

```bash
kubectl apply -f service.yml
```

## Deploying Flask API Production Environment to Kubernetes

Using the following yaml files:

```bash
prod-redis-pvc.yml
prod-redis-deployment.yml
prod-redis-service.yml

prod-flask-deployment.yml
prod-flask-service.yml

prod-worker-deployment.yml
```

Repeat the process for deploying the kubernetes test environment, using each production environment yaml in place of the corresponding test environment yaml.

In summary:

-Create a Persistent Volume Claim for the Redis database\
-Create a Redis Deployment\
-Create a Redis Service\
-Retrieve the new Redis Service IP\
-Manually provide the flask and worker deployments with this new IP\
-Create a Flask Deployment\
-Create a Flask Service\
-Create a Worker Deployment\
-Recongifure existing NodePort Service to match the spec.selector with the ```kz-prod-flask``` app label for the api production environment



