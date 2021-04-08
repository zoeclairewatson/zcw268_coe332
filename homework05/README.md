
# Homework 5: Kubernetes

## Part A

yaml file used:

```bash
pod-A.yml
```

To create pod:

```bash
kubectl apply -f pod-A.yml
```

```bash
pod/hello-a created
```

To get pod using selector (--selector "<label_name> = <label_value>"):

```bash
kubectl get pods --selector "greeting = personalized"
```

Output:

```bash
NAME      READY   STATUS    RESTARTS   AGE
hello-a   1/1     Running   0          14m
```

To check the logs of the pod (logs <pod_name>):

```bash
kubectl logs hello-a
```

Output:

```bash
Hello,
```

-> This is the expected output, given that no value was assigned to the environmental variable.

To delete the pod (delete pods <pod_name>):

```bash
kubectl delete pods hello-a
```

```bash
pod "hello-a" deleted
```


## Part B

yaml file used:

```bash
pod-B.yml
```

To create pod:

```bash
kubectl apply -f pod-B.yml
```

```bash
pod/hello-b created
```

To check the logs of the pod:

```bash
kubectl logs hello-b
```

Output:

```bash
Hello, Zoe Watson!
```

To delete the pod:

```bash
kubectl delete pods hello-b
```


## Part C

yaml file used:

```bash
deployment-C.yml
```

To create deployment:

```bash
kubectl apply -f deployment-C.yml
```

```bash
deployment.apps/hello-c created
```

To get all pods in the deployment and their IP addresses:

```bash
kubectl get pods --selector "app = hello-c" -o wide
```

Output:

```bash
NAME                       READY   STATUS    RESTARTS   AGE   IP             NODE                         NOMINATED NODE   READINESS GATES
hello-c-74b8bdd597-2l2qc   1/1     Running   0          10m   10.244.4.156   c02                          <none>           <none>
hello-c-74b8bdd597-jxfd9   1/1     Running   0          10m   10.244.3.200   c01                          <none>           <none>
hello-c-74b8bdd597-m6dh4   1/1     Running   0          10m   10.244.10.21   c009.rodeo.tacc.utexas.edu   <none>           <none>
```

To check the logs of each pod:

```bash
kubectl logs hello-c-74b8bdd597-2l2qc
```

Output:

```bash
Hello, Zoe Watson from IP 10.244.4.156!
```

```bash
kubectl logs hello-c-74b8bdd597-jxfd9
``` 

Output:

```bash
Hello, Zoe Watson from IP 10.244.3.200!
```

```bash
kubectl logs hello-c-74b8bdd597-m6dh4
```

Output:

```bash
Hello, Zoe Watson from IP 10.244.10.21!
```

-> These outputs match those of part B, with the addition of the associated IP addresses for each pod, which match the IPs found when using kubectl to get all pods in the deployment. 
