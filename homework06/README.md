
# Homework 6: Deploying Flask API to k8s

## Step 1

Create a persistent volume claim for Redis data.

yaml file used:

```bash
zcw268-test-redis-pvc.yml
```

To create PVC:

```bash
[zcw268@isp02 homework06]$ kubectl apply -f zcw268-test-redis-pvc.yml
persistentvolumeclaim/zcw268-test-pvc-data created
```


## Step 2

Create a deployment for the Redis database.

yaml file used:

```bash
zcw268-test-redis-deployment.yml
```

To create deployment:

```bash
[zcw268@isp02 homework06]$ kubectl apply -f zcw268-test-redis-deployment.yml
deployment.apps/zcw268-test-pvc-deployment created
```


## Step 3

Create a service for the Redis database.

yaml file used:

```bash
zcw268-test-redis-service.yml
```

To create service:

```bash
[zcw268@isp02 homework06]$ kubectl apply -f zcw268-test-redis-service.yml
service/zcw268-test-redis-service created
```


## Check Steps 1-3

yaml file used:

```bash
zcw268-test-debug.yml
```

To look up service IP address for test redis service:

```bash
[zcw268@isp02 homework06]$ kubectl get services
NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app1                        NodePort    10.99.183.32    <none>        5000:31834/TCP   6d5h
hello-service               ClusterIP   10.104.114.8    <none>        5000/TCP         12d
zcw268-test-flask-service   ClusterIP   10.108.152.68   <none>        5000/TCP         18h
zcw268-test-redis-service   ClusterIP   10.105.45.120   <none>        6379/TCP         18h
```

To exec into Python debug container:

```bash
[zcw268@isp02 homework06]$ kubectl get pods --selector "app=py-app"
NAME                                   READY   STATUS    RESTARTS   AGE
py-debug-deployment-5cc8cdd65f-c22z8   1/1     Running   0          12d
```
```bash
kubectl exec -it py-debug-deployment-5cc8cdd65f-c22z8 -- /bin/bash
```

Proceed to check work inside debug container:

```bash
root@py-debug-deployment-5cc8cdd65f-c22z8:/# pip3 install redis
Requirement already satisfied: redis in /usr/local/lib/python3.9/site-packages (3.5.3)
root@py-debug-deployment-5cc8cdd65f-c22z8:/# python3
Python 3.9.2 (default, Mar 31 2021, 12:13:11)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>>
>>> rd = redis.StrictRedis(host='10.105.45.120', port=6379, db=8)
>>>
>>> rd.set('checking', 'it works!')
True
```

In separate shell, delete redis pod:
```bash
[zcw268@isp02 ~]$ kubectl get pods --selector "app=zcw268-test-redis"
NAME                                          READY   STATUS    RESTARTS   AGE
zcw268-test-pvc-deployment-64fcb9464c-gk6nh   1/1     Running   0          18h
```
```bash
[zcw268@isp02 ~]$ kubectl delete pods zcw268-test-pvc-deployment-64fcb9464c-gk6nh
pod "zcw268-test-pvc-deployment-64fcb9464c-gk6nh" deleted
```

Confirm that k8s creates a new redis pod:
```bash
[zcw268@isp02 ~]$ kubectl get pods --selector "app=zcw268-test-redis"
NAME                                          READY   STATUS    RESTARTS   AGE
zcw268-test-pvc-deployment-64fcb9464c-hcz2p   1/1     Running   0          103s
```

Return to python shell inside debug container:

```bash
>>> rd.get('checking')
b'it works!'
```

--> I can still get the key I created using the same IP, therefore my service is working and my Redis database is persisting data to the PVC.


## Step 4

Create a deployment for the flask API.

yaml file used:

```bash
zcw268-test-flask-deployment.yml
```

To create deployment:

```bash
[zcw268@isp02 homework06]$ kubectl apply -f zcw268-test-flask-deployment.yml
deployment.apps/zcw268-test-flask-deployment created
```


## Step 5

Create a service for the flask API.

yaml file used:

```bash
zcw268-test-flask-service.yml
```

To create service:

```bash
[zcw268@isp02 homework06]$ kubectl apply -f zcw268-test-flask-service.yml
service/zcw268-test-flask-service created
```

