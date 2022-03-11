In the video, I said the exam is 3 hours. With the latest version of the exam, it is now only 2 hours. The contents of this course has been updated with the changes required for the latest version of the exam.

**Below are some references:**

Certified Kubernetes Administrator: [https://www.cncf.io/certification/cka/](https://www.cncf.io/certification/cka/)

Exam Curriculum (Topics): [https://github.com/cncf/curriculum](https://github.com/cncf/curriculum)

Candidate Handbook: [https://www.cncf.io/certification/candidate-handbook](https://www.cncf.io/certification/candidate-handbook)

Exam Tips: [http://training.linuxfoundation.org/go//Important-Tips-CKA-CKAD](http://training.linuxfoundation.org/go//Important-Tips-CKA-CKAD)

We have created a repository with notes, links to documentation and answers to practice questions here. Please make sure to go through these as you progress through the course:

[https://github.com/kodekloudhub/certified-kubernetes-administrator-course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course)



# Core Concepts
## Cluster Architecture
- Kube scheduleer i
- etcd
	- stores all information about the cluster 
- Controllers: 
	- Controller Manager: monitors all controller items 
	- Nodes - takes care of all nodes 
	- Replication - Desired number of containers are running as designed. 
- kubeAPI server - responsible for orchestrating all activities within the K8 cluster 
	- manages engagements between master and worker nodes. 
- CRI
	- docker - installed on all nodes
	- containerd - 
	- rocket (rkt)
- kublet - 
	- engine that runs on each node in the cluster
	- listens for cmds from the master about require activities
	- provides status of pods / systems / containers back to the master server
- kube-proxy 
	- service running on each node to ensure that all 
	- rule in place to allow containers to read each other

## etcd for beginners 
* etcd is a distributed reliable key-value store that is simple, secure, and fast
* Key-Value stores
	* sql and other tabular / relational databases 
		* store data in "tables" with rows and columns of data 
		* typically each row represents a data type, and each row contains data for each field type as a record 
		* SQL is NOT a key-value Store db format
	* Key value Store is based on a key and value 
	* cannot have duplicate keys
* etcd listens on port 2379 by default
* etcdctl  is the client software 
	* i.e.  store value: $> etcdctl set key1 value 1
	* i.e. get value: $> etcdctl get key1
	* i.e. list of options:  $> etcdctl 

## etcd in kubernetes
* stores information regarding: 
	* nodes
	* pods
	* configs
	* secrets
	* accounts
	* roles
	* bindings
	* others.....
* if installing cluster from scratch, you will need to download an install the binaries yourself. 
* Lots of options to pass to etcd service on start, examples: 
	* name
	* cert-file
	* key-file
	* peer-cert-file
	* peer-key-file
	* trusted-ca-file
	* peer-trusted-ca-file
	* per-client-cert-auth
	* client-cert-auth
	* initial-advertise-pper-urls
	* etc......
* Most important config for now is the: 
>
> --advertise-client-urls https://${internal_ip}:3279}
> 

* kubeadmin 
	* deploys etcd as a pod within the cluster. 
* to list all keys in the cluster: 
>
>kubectl exec etcd-master -n kube-system etcdctl get / --prefix -keys-only
>

## etcd commands: 
Additional information about ETCDCTL UtilityETCDCTL is the CLI tool used to interact with ETCD.ETCDCTL can interact with ETCD Server using 2 API versions – Version 2 and Version 3.  By default its set to use Version 2. Each version has different sets of commands.

For example ETCDCTL version 2 supports the following commands:

> etcdctl backup  
> etcdctl cluster-health  
> etcdctl mk  
> etcdctl mkdir  
> etcdctl set

Whereas the commands are different in version 3



> etcdctl snapshot save  
> etcdctl endpoint health  
> etcdctl get  
> etcdctl put

To set the right version of API set the environment variable ETCDCTL_API command

> export ETCDCTL_API=3

When API version is not set, it is assumed to be set to version 2. And version 3 commands listed above don’t work. When API version is set to version 3, version 2 commands listed above don’t work.

Apart from that, you must also specify path to certificate files so that ETCDCTL can authenticate to the ETCD API Server. The certificate files are available in the etcd-master at the following path. We discuss more about certificates in the security section of this course. So don’t worry if this looks complex:

> –cacert /etc/kubernetes/pki/etcd/ca.crt  
> –cert /etc/kubernetes/pki/etcd/server.crt  
> –key /etc/kubernetes/pki/etcd/server.key

So for the commands I showed in the previous video to work you must specify the ETCDCTL API version and path to certificate files. Below is the final form:

> kubectl exec etcd-master -n kube-system — sh -c “ETCDCTL_API=3 etcdctl get / –prefix –keys-only –limit=10 –cacert /etc/kubernetes/pki/etcd/ca.crt –cert /etc/kubernetes/pki/etcd/server.crt –key /etc/kubernetes/pki/etcd/server.key”


## Kube API Server
* kubectl is just interacting with the Kube-APIserver
* Similarly you can send a POST command via curl with the "kubectl get nodes" and receive the same data back. 
* process of API processing is: 
	* Authenticate User
	* Validate Request
	* Retrieve Data
	* update ETCD
	* Scheduler
	* Kubelet
* The API  server is the only component that directly interacts with the etcd database
	* all other components interact with the API Server

 ## Kube Controller Manager
 * Controller is like a departement of a business that has it's  own responsibilities. 
 * They: 
	 * Watch status
	 * Remediate Status
* Node Controller 
	* Checks the status of all nodes every 5 seconds 
	* uses the Kube-apiserver  
	* waits for 40 seconds to mark something unreachable
	* allows 5 minutes to come bac k online
	* if not, will move pods to new nodes. 
* Examples of other controllers
	* Replication Controllers
	* deployement controllers
	* namespace controllers
	* endpoint controllers
	* cronjob controllers
	* job controllers
	* pv-protection controllers
	* service account controllers
	* Stateful set controller
	* replica-set controller
	* Node Controller
	* pv-binder controller
* all controllers located within Kube-controller-manager
	* should run as a service
	* by default, all are likely enabled. 

## Kube Scheduler
* Scheduling pods and nodes
* only deciding which pod goes on which node
* doesn't create the pods on the nodes
* why?
	* sizes of ships
	* different destination to correct place
* process for selection 
	* filter nodes based on profile of pod
	* Ranks nodes to identify best node for pod. 
		* calculates the resources free after standing up pod on node. 
* Scheduler can be custom built or modified as well. 
* runs as a service
* 
## Kubelet
* like captain on the ship
* Leads the ship and engages the master. 
* provides regular updates to master on health / status
* General Requirements
	* Registers node
	* Create PODs
	* Monitor Node & PODs
* MUST always manually install kubelet 

## Kube Proxy
* Every pod talks to every other pod
* POD Network
* Service cannot join a POD network
* virtual component only living in memory
* Kube-proxy runs on each node in the cluster
	* looks for new services
	* creates appropriate role to transfer services to the back end pod
	* ip table rule to receive and foward traffic to pod
* Installing Kube-proxy & run as service
* on proxy pod on each node in cluster. 
 

## PODs
* assumes 
	* docker image is available via known registry
	* Kubernetes Cluster is in place and configured
* containers are encapsulated within PODS
* PODS are the smallest object you can create in Kubernetes
* how to run pods
>kubectl run nginx --image  nginx
>kubectl get pods   #see currently running  pods
>
>
* 
## Replica Sets
* ensures that specific number of pods are running at all times. 
* Share the load by creating additional pods as necessary in the same node or across many nodes. 
* replication controller ar emade from rc-definitions.yaml file. for data sets
	* apiverion:  v1
	* kind: ReplicationController
	* metadata
		* name: myapp-rc
		* labels: 
			* app: myapp
			* type: front-end
	* specs: 
		* '-template: 
		* - replicas: 3

## Deployments: 
* Deployments can be done rolling methods (staged roll out)
* Roll backs
* pause, deploy, restart
* all in deployments
* Deployments is a step above replicasets
* Deployments have a definition file
* kind: deployment
* Spec defines what group of images it impacts 
* NEW COMMAND: 
 > kubectl get all      # will return all item times for given environment

## Certification Tip
Here’s a tip!

As you might have seen already, it is a bit difficult to create and edit YAML files. Especially in the CLI. During the exam, you might find it difficult to copy and paste YAML files from browser to terminal. Using the `kubectl run` command can help in generating a YAML template. And sometimes, you can even get away with just the `kubectl run` command without having to create a YAML file at all. For example, if you were asked to create a pod or deployment with specific name and image you can simply run the `kubectl run` command.

Use the below set of commands and try the previous practice tests again, but this time try to use the below commands instead of YAML files. Try to use these as much as you can going forward in all exercises

Reference (Bookmark this page for exam. It will be very handy):

[https://kubernetes.io/docs/reference/kubectl/conventions/](https://kubernetes.io/docs/reference/kubectl/conventions/)

**Create an NGINX Pod**

`kubectl run nginx --image=nginx`

**Generate POD Manifest YAML file (-o yaml). Don’t create it(–dry-run)**

`kubectl run nginx --image=nginx --dry-run=client -o yaml`

**Create a deployment**

`kubectl create deployment --image=nginx nginx`

**Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run)**

`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml`

**Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) with 4 Replicas (–replicas=4)**

`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml`

**Save it to a file, make necessary changes to the file (for example, adding more replicas) and then create the deployment.**

`kubectl create -f nginx-deployment.yaml`

**OR**

**In k8s version 1.19+, we can specify the –replicas option to create a deployment with 4 replicas.**

`kubectl create deployment --image=nginx nginx --replicas=4 --dry-run=client -o yaml > nginx-deployment.yaml`


## Namespaces
- a way to differentiate between families and family memebers
	- mark williams
		- dad
		- mom
		- brother
		- own rules
		- own resources
	- mark smith
		- mom
		- sister
		- rules
		- resources
- so far, only been working in the default namespace. Everything in the same house. 
- Kubernetes isolate system is all in the kube-system namespace
- Kube-public 
	- Namespace used for all resources that will be accesses via users outside the cluster 
- if small cluster, should not have to worry about name spaces. 
- Namespace isolate resources to a unique space and rules
	- System
	- default
	- public
	- dev
	- etc....
- prevents unintentional impact to other namespaces
- can assign quota's to name space. 
- can assign resources per node in clusters 
- resources within same namespace can refer to each other simply by their short name: 
	- calling your brother:   Hey John!
		- Namespace is assumed as current namespace of resource calling short name
	- Calling a guy named john somewhere else: John Mitchell
		- a person named john  outside of the current namespace
- default namespace of the cluster: `cluster.local`
- Full name: `bb-service.dev.svc.cluster.local` will break down too: 

| Service Name | Namespace | Service | domain        |
| ------------ | --------- | ------- | ------------- |
| db-service   | dev       | svc     | cluster.local |

Examples of namespace in cmld: 

> kubectl get pods                                                           # list all pods in current namespace
> kubectl get pods --namespace=kube-system           # list all pods in identified namespace

If no namespace is identified during the creation of the POD or object, it will be created in the default namespace. 
If you want to create the pod in a specific namespace, use the namespace option. 
can move namespace definition into the yaml file 
create new namespace:  use namespace definition file
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
```

command to create namespaces: 
> kubectl create -f namespace-dev.yml      # Uses the yaml file to create the desired namespace
> kubectl create namespace dev                 # doesn't require the yaml file and will create the dev namespace

Move namespace from default: 
> kubectl config set-context $(kubectl config current-context) --namespace=dev     # Sets the namespace to the one defined in the argument
> kubectl get pods          # validate you are in the right namespace based on the PODs running 
> kubectl get pods --all-namespaces      # Gets pods from all namespaces, you can do this for any command

 Resource Quotas per namespace using yaml file, and can be across nodes in a cluster: 
 ```yaml
 apiVersion: v1
 kind: ResourceQuota
 metadata: 
   name: compute-quota
   namespace: dev
 spec: 
   hard:
     pods: "10"
	 requests.cpu: "4"
	 requests.memory: 5Gi
	 limits:cpu: "10"
	 limits.memory: 10Gi
 ```
 Run the following to create the quota from the yaml: 
 > kubectl create -f compute-quota.yaml

## Services
Services are provided to all pods within a node or cluster 
top down external communications: 
* Overall user network for entire office 
* Each node within cluster has an IP accessible to the network. 
	* External 
	* Internal 
	* ?? Node run Kube-proxy which manages internal & external traffic. 
* each pod has it's own IP address
	* External
	* Internal 
* Kubernete service is an object just like a pod, replicaset, deployment, etc on the node
	* listens on node  on port
	* node-port service
	* Listens on port on node and foward traffic to internal network... (proxy)
* Type of services
	* node-port
	* cluster-ip
	* load-balancer 
* NODE-PORT
	* mapping a port on the node to a port on the POD
	* i.e.  node:30008 (3) -> service-ip (2) -> pod-ip:80 (1)
	* nodeport service has it's own IP address (cluster-ip)
* create service yaml file 
```yaml 
apiVersion: v1
kind: Service
metadata: 
  name: myapp-service

spec: 
  type: NodePort
  ports:
    - targetPort: 80
      port: 80
	  nodePort: 30008
  selector: 
    app: myapp
	type: front-end
```
* if `port` is not provided, it is assumed to be the same as the `targetPort`
* if `nodePort` is not specified, as  node port between 30000 and 32767 is automatically allocated
* the `-` previous to `targetPort` indicates an array of information for the previously indented field / argument
* the `selector` argument identifies the pod the service will connect the port too. 
	* the `app` and `type` fields are pulled directly from the pod-definition yaml. 
* once created, run the `kubectl create` command and check services. 
> kubectl create -f services-definition.yaml
> kubectl get services 
* now access the web browser of the service, if available, by visiting the IP of the POD and the `nodePort` of the service. 
* If multiple pods on a node share the same `lables: \n app: myapps` or `selector: \n app: myapp` then the service will automatically map all pods to the same `nodePort` and load balance between them on the node
	* no additional work required to balance this load across the pods. 
	* algo used is random. 
* If the same is exists, but within a cluster regardless of pods, i.e. 3 pods where each pod is on a different node... 
	* the service will create a similar service on all nodes and map the same `nodePort` on each node to the same port
	* it will then create a cluster service that will load balance between the nodes. 
	* you can then access the `myapp`  using any `nodeIP:nodePort` and the service will balance across all nodes regardless. 

## Services Clusters IP 
One application may have many components across pods. 
- front-end
- back-end
- redis-db 

How would you establish connectivity between these different tiers of the application. 
- IPs for pods can change constantly. 
- a front end needs to connect to a back end... how? 
- a back-end label / service will group all back-ends via one back-end service
- a front-end label / service will group all front ends under one service.... 
- a redis-db label / service will group all redis-db under one service.... 
- how to group them each service together as one solution? 
- Each layer needs to have the full flexibility of k8s but need to remain organized... 
- CLUSTER IP is it

```yaml
apiVersion: v1
kind: Service
metadata: 
  name: back-end
  
spec: 
	type: ClusterIP
	ports:
		- targetPort: 80
	    port: 80
  selector: 
	  app: myapp
	  type: back-end
```

now create the service and check if it's operational or loaded correctly 
> kubectl create -f service-definition.yaml
> kubectl get services 

The service can be access via the service `ip:port` or services domain name 

## Service - Load Balancer  
Load Balancing services concepts: 
- services at the node level are accessible via a `nodePort`
- each `node` within the `service` group has it's own IP
- A user could access the application via any `nodeIP:nodePort` 
- how to create one address all users can access all apps regardless of which node, port, container, etc... is available? 
- This will allow for maintenance, rolling update, upgrades, and faults to occur w/o any impact to the customer. 
- NOTE: even if `pods` are only loaded on two out of for `nodes` in a cluster, you can access the app by using any `nodeIP:nodePort` associated to that cluster and the app `service` will direct traffic to the `nodeIP:nodePort` of the `nodes` that are hosting / housing the `pods` the noted within the `service` regardless if that `node` has a `pod`  running on itself. 
- This is accomplished via load balancing within a cluster. 
- How do you acheive a simple URL that allows users to easily access apps? 
	- i.e.  http://example-vote.com ; https://example-myapp.com
- one option: Soft Appliance load balancing with rules installed as a `pod` and added to the `service`? 
- option 2: native loadbalander of service provide i.e.  GPS, AWS, Azure, etc.... 
- example yaml config file: 
```yaml 
apiVersion: v1
kind: Service
metadata:
	name: myapp-services

spec: 
	type: LoadBalancer
	ports: 
		- targetPort: 80
		  port: 80
		  nodePort: 30008
```
* NOTE!! Above method only works with supported platforms 

## Imperative vs. Declarative 
Terms: 
- **Imperative**: very clear and specific instructions on how to accomplish a task with clear boundaries. 
- **Declarative**: To give only  the final objective w/o detailed or specific steps to accomplish the task

Infrastructure as Code: 
* **imperative**: very detailed, step by step, process lined out in very deep detail including identification of every location to store data, what to store it as, what to call it, how it works, and all potential specification for the item to exist. 
* **Declarative:**  Specify the end state of the requirements, and let the system determine the best method to reach that goal. 

Concepts: 
- **imperative:** what if you want to create a server with an IP and Name... with an application... you have to first manually validate all the parameters you want to set will not create conflict with the rest of the operational environment. Once you create the system, you need to validate all components are operating as designed. Someone needs to test the system. If something is wrong, checks of every component would be required. The manual investment to instantiate a system are exhaustive and can take very long / extended periods of time. 
- **Declarative:** Kubernetes is a declarative system that does not require you to research and validate every aspect before deployment. The K8S system will perform all that activity for you based on what's configured in the system / manifests / yaml files.  It will validate resources against what is in use. It will start up the service.  It will validate the service is operational. it will configure monitors for the system. It will do quite a bit in a short time due to a declarative nature.  

Kubernetes:
- **Imperative**: an example is to manually run each yaml file for each function to get an information system online. i.e. 
> ### Create Objects: 
> kubectl run --image=nginx nginx
> kubectl create deployment --image=nginx nginx
> kubectl expose deployment nginx --port 80
> ### Update Objects
> kubectl edit deployment nginx
> kubectl scale deployment nginx --replicas=5
> kubectl set image deployment nginx nginx=nginx:1.18
> ### 
> kubectl create -f nginx.yaml
> kubectl replace -f nginx.yaml
> kubectl delete -f nginx.yaml

- **Declarative:** an exampl of how Kubernetes can be declarative is by doing all the tasks above with little input is: 
> kubectl apply -f nginx.yaml

NOTES: 
* using the `kubectl edit` command only updates the file in memory, it does not update the `*.yaml` used to create the function (unsure if this means the manifest files)
* best method to update configuration files is to: 
	* update the local configuration file  
	* use the `replace` function of `kubectl` to update the configuration in memory
* If you run a `create` command and the `pod` already exists, you will receive an error
* When you run a `replace`  command you must make sure the `pod` already exists, or the command will fail
* If you have one configuration file you would like to use to create objects: 
> kubectl apply -f nginx.yaml

- if you have a directory full of configuration files to create objects, use: 
> kubectl apply -f /path/to/config-files

- if you have one update file you will use to update objects: 
> kubectl apply -f nginx.yaml

- if you have many configuration files in a directory to update objects: 
> 

## Certification Tips - Imperative Command with Kubectl 
While you would be working mostly the declarative way – using definition files, imperative commands can help in getting one time tasks done quickly, as well as generate a definition template easily. This would help save considerable amount of time during your exams.

Before we begin, familiarize with the two options that can come in handy while working with the below commands:

`--dry-run`: By default as soon as the command is run, the resource will be created. If you simply want to test your command , use the `--dry-run=client` option. This will not create the resource, instead, tell you whether the resource can be created and if your command is right.

`-o yaml`: This will output the resource definition in YAML format on screen.

Use the above two in combination to generate a resource definition file quickly, that you can then modify and create resources as required, instead of creating the files from scratch.

### POD

**Create an NGINX Pod**

`kubectl run nginx --image=nginx`

**Generate POD Manifest YAML file (-o yaml). Don’t create it(–dry-run)**

`kubectl run nginx --image=nginx --dry-run=client -o yaml`

### Deployment

**Create a deployment**

`kubectl create deployment --image=nginx nginx`

**Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run)**

`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml`

**Generate Deployment with 4 Replicas**

`kubectl create deployment nginx --image=nginx --replicas=4`

You can also scale a deployment using the `kubectl scale` command.

`kubectl scale deployment nginx --replicas=4` 

**Another way to do this is to save the YAML definition to a file and modify**

`kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml`

You can then update the YAML file with the replicas or any other field before creating the deployment.

### Service

**Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379**

`kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml`

(This will automatically use the pod’s labels as selectors)

Or

`kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml` (This will not use the pods labels as selectors, instead it will assume selectors as **app=redis.** [You cannot pass in selectors as an option.](https://github.com/kubernetes/kubernetes/issues/46191) So it does not work very well if your pod has a different label set. So generate the file and modify the selectors before creating the service)

**Create a Service named nginx of type NodePort to expose pod nginx’s port 80 on port 30080 on the nodes:**

`kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml`

(This will automatically use the pod’s labels as selectors, [but you cannot specify the node port](https://github.com/kubernetes/kubernetes/issues/25478). You have to generate a definition file and then add the node port in manually before creating the service with the pod.)

Or

`kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml`

(This will not use the pods labels as selectors)

Both the above commands have their own challenges. While one of it cannot accept a selector the other cannot accept a node port. I would recommend going with the `kubectl expose` command. If you need to specify a node port, generate a definition file using the same command and manually input the nodeport before creating the service.

### **Reference:**

[https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)

[https://kubernetes.io/docs/reference/kubectl/conventions/](https://kubernetes.io/docs/reference/kubectl/conventions/)
## Kubectl Apply Command
- Manage things in a declarative way
- if the object does not already exist: 
	- A new object will be created 
	- when created: an object configuration is created within k8s
		- live configuration of the object of the cluster
	- yaml version of file is changed to a json version of the file

Three versions of a configuration may exist at anytime: 
- local configuration file 
	- stored on local harddrive 
	- `*.yaml`  file
	- access using Nano or vi
- last applied configuration: (json)
	- stored on k8s live object configuration 
	- noted as `annotations:` in file in the `live configurations`
	- `*.json` file format
- Live configuration file  
	- Stored in K8S memory 
	- `*.yaml` format
	- accessed using `kubectl edit` command 

>kubectl apply -f my-config.yaml

Update the local file (no change to last applied configs or Live configs)
Using `kubectl edit` changes only the live configuration 
Using `kubectl apply` command reads the `local configuration` file and updates the `last applied configuration` AND the `live configuration` in K8S. 
`last applied configuration`  is used to see differences between `local file` and the `live configuration` and updated the `live configuration` to match

# Scheduling 
## Scheduling Section Introduction
- Labels & Selectors
- Daemon Sets
- Resource Limits
- Manual Scheduling 
- Multiple Schedulers
- Scheduler Events
- Configure Kubernetes Scheduler

## Manual Scheduling Pods on Nodes
How scheduling works
ever pod has a field `nodeName:`
Schedule goes through all pods and look for all pods w/o this set
Scheduler will find pods w/o this set and set it to the node's name that the pod resides on
nodeName can only be specified at creation time
to perform scheduling type of task via `*.yaml`.... `kind:` must be set to `Binding`
i.e. 

## Labels and Selectors
- Kind, Color, Type
- Filters...   Green - Bird
- Labels are properties added to each item
	- class, kind, color
- Labels provide a way to filter resources in a k8s cluster
- Labels are up to you
- suggestions
	- app
	- function
-  i.e. 
```yaml
apiVersion: v1
kind: Pod
metadata: 
	name: simple-webapps
	labels:
		app: App1
		function: Front-end

spec: 
	containers: 
		-name: simple-webapp
			image: simple-webapp
			ports: 
				- containerPort: 8080
				- 
```
- you can add all the labels you like. 
- Labels can be used to group resources together such as pods to a replica set. i.e. 
```
apiVersion: apps/v1
kind: ReplicaSet
metadata: 
	name: simple-webapp
	labels:
		app: App1
		function: Front-end

spec: 
	replicas: 3
	selector: 
		matchLabels: 
			app: App1
	template: 
		metadata:
			labels:
				app: App1
				function: Front-end
		spec: 
			containers: 
				- name: simple-webapp
				  image: simple-webapp
```
The `labels` near the top are the `labels` of the `replicaset`
the `labels` in the `template` section are the `labels` of the `pods`
To configure the `object` to affect the correct `pods` the `selector` must match the `label` of the `objects` you want it affect. 
This works for other `objects` as well such as a `service` 
```
apiVersion: v1
kind: Service
metadata: 
	name: my-service
spec: 
	selector: 
		app: App1
	ports: 
		- protocol: TCP
		  port: 80
		  targetPort: 9376
	  
```
**Annotations**: are used to record other purposeful information in informational purposes. 
```
apiVersion: v1
kind: ReplicaSet
metadata: 
	name: simple-webapp
	labels: 
		app: App1
		function: Front-end
	annotations: 
		buildVersion: 1.34

... etc.... 

```

## Taints and Tolerations 
- analogy: bug approaching a person, we spray the person with repellant spray (taint)
	- the smell on the person cause the bug to leave
	- other bugs may be ok with the smell and land on the person 
	- two factors feed into taint success: 
		- The type of taint defined
		- the objects resistance to the taint
- Taints and toleration have no impact on security of the cluster
- `Taints` can resist or allow specific `pods` based on `taint labels`
- `tolerations` can allow pods to resides on tainted nodes
- `taints` are set on nodes
- `tolerations` are set on pods
- how to apply a taint via cli: 
> kubectl taint nodes node-name key=value:taint-effect

In this case the `value:taint-effect` are a keypair and require each other 
The `value` is the identifier of the taint existing like  `blue`
the `taint-effect` is what will occur if a `pod` does not tolerate the `taint`
There are 3 taint effects: 
	- NoSchedule
	- PreferNoSchedule
	- NoExecute
Example of more likely command: 
> kubectl taint nodes node01 app-blue:NoSchedule

`Toleration` declaration in `pod` config yaml
```
apiVersion 
kind: pod
metadata: 
	name: myapp-pod
spec: 
	containers: 
		- name: nginx-container
		  image: nginx
	tolerations:
		- key: "app"
		  operator: "Equal"
		  value: "blue"
		  effect: "NoSchedule"
```
 All `values` for `tolerations` must be in double quotes 

 Taint - NoExecute 
 If tainted with NoExecute all pods without tolerance will be evicted. 
 Although `taints` may prevent unwanted `pod`s from running on a `node` it does not guarantee that the `tolerant pod`s will run on it. 

`Scheduler` does not schedule any `pods` from being scheduled on the `master node`
to find the `taints` of the master run the following command 
> kubectl describe node kubemaster | grep Taint

 ## Node Selector
Two ways to force `pods` to specific `nodes`
The first way is to use a `nodeSelector` property in the definition files. 
* `nodeSelector` can use `labels` to identify `nodes` that meet the requirements
* `node01` may have a `lable` that is `size: Large` and the definition example is: 
```yaml
apiVersion: 
kind: Pod
metadata: 
	name: myapp-pod
spec: 
	containers: data-processing
		- name: data-processor
		  image: data-processor
  nodeSelector:
	  size: Large
```
To `lable`  a `node` you can use the following command: 
> `kubectl label nodes <node-name> <lable-key>=<label-value>

`nodeSelctor` is very limited and only allows for simple `selector` to be made. It does not work well if you want conditional or complex `selector` criteria.  That is where we find `Node Affinity`

## Node Affinity
- advanced capabilities to limit `pod` placement on nodes. 
```yaml 
apiVersion: 
kind: 
metadata: 
	name: myapp-pod
spec: 
	containers: 
		- name: data-processing
		  image: data-processing
   affinity:
	  nodeAffinity: 
		  requiredDuringSchedulingIgnoreDuringExecution: 
			  nodeSelectorTerms: 
				  - matchExpressions: 
					  - key: size
					    operator: In
					    
					    values: 
						    - Large
```
- The `affinity` is based on `nodeAffinity`
	- the `nodeAffinity` controls only during the `scheduling` activity, not during the `execution` activity
	- The `matches` required to attain `affinity` are that: 
		- The `node` to match must have a key pair of `size: Large` in it's labels
		- If this key pair exists in the `node` definition file, the `scheduler` can move this `pod` to that `node`

You could allow the `pod` to operate on a large and medium node by changing the `values` at the end appear like: 
```yaml 
......
				  - matchExpressions: 
					  - key: size
					    operator: In
					    values: 
						    - Large
						    - Medium
```

You can also change up the to identify the `affinity` rule to disallow the `pod` from moving to a pod by using the `operator: NotIn` key pair and specify the `values:` to base this `affinity` on. 
```yaml 
				  - matchExpressions: 
					  - key: size
					    operator: NotIn
					    values: 
						    - Small
```

Another `operator:` value is `exists` which looks to ensure that the key only exists in a `node` definition file. This only requires the `size:` key exists in the `node` definition file in order for the `scheduler` to move or instantiate pods on that node. 

There are many more `operators:` available,  but look it up in documentation.

If the node `affinity` is unable to locate a `node` that contains the `key pairs` specified in the `pod` definition? 
- i.e.:  someone changes a `lable` on a node which then invalidates the `affinity` rule in the `pod` definition.. 
	- The second context in the `affinity rule` in the `node` definition file will help determine this. 
	- i.e. the first example above there the second context is `requriedDuringSchedulingIgnoreDuringExecution`
	- Available `node affinity types` are: 
		- Available: 
			- `requriedDuringSchedulingIgnoreDuringExecution`
			- `preferredDuringSchedulingIgnoreDuringExecution`
		- Planned:  (future version of kubernetes)
			- `requriedDuringSchedulingRequriedDuringExecution`
			- `preferredDuringSchedulingRequiredDuringExecution`
- Of the two `affinity` types: 

| Status    | `Affinity Type`                                    | During Scheduling | During Execution |
| --------- | -------------------------------------------------- | ----------------- | ---------------- |
| Available | `requiredDuringSchedulingIgnoredDuringExecution`   | Required          | Ignored          |
| Available | `preferredDuringSchedulingIgnoredDuringExecution`  | Preferred         | Ignored          |
| Planned   | `requiredDuringSchedulingRequiredDuringExecution`  | Required          | Required         |
| Planned   | `preferredDuringSchedulingRequiredDuringExecution` | Preferred         | Required         | 

* `requiredDuringSchedulingIgnoredDuringExecution`
	* If a `node` with appropriate `key pair` does not exist, the `pod` will **NOT** be scheduled 
	- If a `node` with the appropriate `key pair` does not exist, the `pod` will continue to execute, no impact
* `preferredDuringSchedulingIgnoredDuringExecution` 
	* if a `node` with appropriate `key pair` does not exist, the `pod` will still be scheduled 
	- If a `node` with the appropriate `key pair` does not exist, the `pod` will continue to execute, no impact
- `requriedDuringSchedulingRequriedDuringExecution`
	- if a `node` with appropriate `key pair` does not exist, the `pod` will **NOT** still be scheduled 
	- If a `node` with the appropriate `key pair` does not exist, the `pod` will **NOT** continue to execute
- `preferredDuringSchedulingRequiredDuringExecution`
	* if a `node` with appropriate `key pair` does not exist, the `pod` will still be scheduled 
	- If a `node` with the appropriate `key pair` does not exist, the `pod` will **NOT** continue to execute

## Taints and Tolerations vs. Node Affinity
- Will likely need to use a mixture of `taints and tolerations` along with `node affinity` to ensure optimal placement of `pods` across `nodes`
	- `taints and tolerance` is set to prevent `pods` from moving to `nodes` based on `labels` 
		- `nodes` have `taints` declared in their `definition` files 
		- `pods` have `lables` identifying specific attributes declared in their `definition` files 
		- the `scheduler` will compare `node taints` to `pod labels` and determine where to place the `pod` 
		- The control mechanism of a `taint` resides on the `node` and the identifier or matching characteristic resides on the `pod` as a `key pair`
		- **ISSUES**: a `pod` can start on any host with a `taint` that matches the `pod` definition BUT a `pod` could also start on any other `node` that does not have a similar `taint` resulting in `pods` running on `nodes` they were not intended to run on. 
	- `node affinity` is set to allow specific `pods` to run on specific `nodes` based on the `affinity` declarations in the `definition` files 
		- `nodes` have `labels` declared in their `definition` files 
		- `pods` have `affinity` declaration in their `definition` files 
		- the `pod` defines what `labels` must exist on a `node` and what the `scheduler` is allowed to do with this `pod - node` match if the `affinity` exists. 
		- The control mechanism resides on the `pod` and the criteria resides on the `node` as `labels` in `key pairs`
- To entirely dedicate `nodes` to `pods` a mixture of `taints and tolerations` AND `node affinity` must be used. 
	- `taints and tolerations` are controlled by the `nodes`
	- `affinity` is controlled by the `pods`
	- if you have both control mechanisms in place and properly configured, `pods` will only run on the correct `nodes` as defined by both mechanisms. 
	- ISSUES: This will take reasonable planning to ensure works properly. 
	- EARLY RECOMMENDATION: Keep a catalog of `Taints and Tolerations` AND catalog of `node affinity` 
		- reviewed to ensure `node` and `pod` relationships remain in tact
		- ensure `pods` execute on the appropriate `nodes` for their functions
		- Don't confuse the hot snot out of the `scheduler`
		- retain enough modularity  and non-conformance to prevent resource contention on `nodes` 
		- DO NOT over complicate the relationships between these control mechanisms. 

## Resource Limits 
- based on cpu, memory, and disk space on each `node`
- each `pod` consumes resources on the `node` it executes
- the `scheduler` determines what node a `pod` will execute on 
- if a `pod` has insufficient `resources` to execute the `pods` workload, the `scheduler` should move that `pod` to a different `node`
- if any `node` in the `cluster` does not have the `resources` available to execute the `pods` workload, the `scheduler` will not `schedule` the pod on any `node` to prevent `resource` issues
- `pod` will indicate a pending state under `status`  and the `events` section of the `description` will indicate the issues
- `pod` minimum `resource` requirements assumed by the `scheduler` are 
	- 0.5 x CPU
	- 256MB x Mem
	- 0MB x Stroage / Disk
- If a `pod` or `deployment` needs more `resources` than this to run, you can specify this in the `definitions` file. The money shot is in the `spec -> resources -> memory & cpu`
```yaml
apiVersion: v1
kind: Pod
metadata: 
  name: simple-webapp-color
  labels: 
    name: simple-webapp-color
spec: 
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
    ports: 
      - containerPort: 8080
    resources: 
      requests:
        memory: "1Gi"
        cpu: 1
```

- CPU Resource Allocations: 
	- a count of 1 cpu indicates a singular vCPU
	- you can specify as low as .01 vCPU 
	- Increments of vCPU are identified in units of `m` such as `1m` 
	- `1m` is equivalent to `.1 vCPU` 
	- `100m` is equivalent to `1 vCPU`
	- Whole increments of a vCPU are identified by a standing whole number `1`, `2`, `12`, ect....
	- In cloud environments, a increment of `1 vCPU` will consume `1 vCPU` as specified by the cloud environment and rack up the associated costs
	- In a on-premise `node` the `1 vCPU` will consume on `hyperthread` on the `node` that `pod` resides on 
- Memory Resource Allocations
	- memory is similar to vCPU allocation and absolute in nature 
	- Memory allocation can be specified in a mix of methods 

| allocation unit | actual byes allocated |
| --------------- | --------------------- |
| 1G (Gigabyte)   | 1,000,000,000         |
| 1M (Megabyte)   | 1,000,000             |
| 1K (Kilobytes)  | 1,000                 |
| 1Gi (Gibibyte   | 1,073,741,824         |
| 1Mi (Mebibyte)  | 1,048,576             |
| 1Ki (Kibibyte)  | 1,024                 | 

- `Containers` do NOT have a mechanism to control the maximum amount of `resources` a container can consume. 
- `pods` do have a mechanism to control resource max consumption of a `container`
- Since `containers` reside within `pods` you are able to manage the resource consumptions of the `containers` by configuring it in the `pod` or `deployment` definition files 
- By default Kubernetes sets the following limits on `resources`:
	- 1 x vCPU Limit per `container`
	- 512Mi x Memory limit per `container`
- If these limits do not provide `resources` necessary to execute the given `container` you can customize the limits in your definition files
	- The below limits the `containers` within the `pod` to `2 x vCPU` and `2 Gibibytes x memory` 
	- looking in the section `spec -> resources -> limits` for this specification 
```yaml
apiVersion: v1
kind: Pod
metadata: 
  name: simple-webapp-color
  labels: 
    name: simple-webapp-color
spec: 
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
    ports: 
      - containerPort: 8080
    resources: 
      requests:
        memory: "1Gi"
        cpu: 1
      limits: 
        memory: "2Gi"
        cpu: 2
```
With these configurations we can now specify the min and max `resources` for each `containers` within the `pod` 
**REMEMBER**: The `resource` are per `container` within a `pod`. If the `pod` encapsulates 3 `containers` expect the `pod` to potentially consume 3 x the `resource` allocations 
Exceeding Limits: 
- Any given `container` cannot consume more `vCPU` then specified in the `pod definition` files 
- Any given `container` CAN consume more `memory` then specified in the `pod definition` files 
- IF any `container` exceeds it's memory allocations continuously, the `pod` will be terminated 

## Notes on default resource requirements and limits
In the previous lecture, I said – “When a `pod` is created the `containers` are assigned a default `CPU` request of .5 and `memory` of 256Mi”. For the `POD` to pick up those defaults you must have first set those as default values for `request` and `limit` by creating a `LimitRange` in that `namespace`.

``` yaml 
apiVersion: v1
  kind: LimitRange
  metadata:
    name: mem-limit-range
  spec:
    limits:
    - default:
        memory: 512Mi
      defaultRequest:
        memory: 256Mi
      type: Container
```
[https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

```yaml 
  apiVersion: v1
  kind: LimitRange
  metadata:
    name: cpu-limit-range
  spec:
    limits:
    - default:
        cpu: 1
      defaultRequest:
        cpu: 0.5
      type: Container
```
[https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

**References:**

[https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource)
## Quick note on editing Pods and Deployments
#### Edit a POD

Remember, you CANNOT edit specifications of an existing POD other than the below.

-   spec.containers[*].image
-   spec.initContainers[*].image
-   spec.activeDeadlineSeconds
-   spec.tolerations

For example you cannot edit the environment variables, service accounts, resource limits (all of which we will discuss later) of a running pod. But if you really want to, you have 2 options:

1. Run the `kubectl edit pod <pod name>` command.  This will open the pod specification in an editor (vi editor). Then edit the required properties. When you try to save it, you will be denied. This is because you are attempting to edit a field on the pod that is not editable.

![[Pasted image 20220309091339.png]]

![[Pasted image 20220309091404.png]]

A copy of the file with your changes is saved in a temporary location as shown above.

You can then delete the existing pod by running the command:

`kubectl delete pod webapp`

Then create a new pod with your changes using the temporary file

`kubectl create -f /tmp/kubectl-edit-ccvrq.yaml`

2. The second option is to extract the pod definition in YAML format to a file using the command

`kubectl get pod webapp -o yaml > my-new-pod.yaml`

Then make the changes to the exported file using an editor (vi editor). Save the changes

`vi my-new-pod.yaml`

Then delete the existing pod

`kubectl delete pod webapp`

Then create a new pod with the edited file

`kubectl create -f my-new-pod.yaml`

#### Edit Deployments

With Deployments you can easily edit any field/property of the POD template. Since the pod template is a child of the deployment specification,  with every change the deployment will automatically delete and create a new pod with the new changes. So if you are asked to edit a property of a POD part of a deployment you may do that simply by running the command

`kubectl edit deployment my-deployment`


## Daemon Sets
- `daemonSets` are similar to `replicaSets` however: 
	- `relicaSets` run multiple `pods` on any grouping of `nodes` based on `resources`
	- `daemonSets` 
		- run a single `pod` on each `node` allowed
		- if a new `node` is added to the cluster, the `daemonSet` automatically adds a new `pod` to that node
		- If a `node` is removed from the cluster, the `daemonSet` automatically removes that `pod` from the `node` 
- Some use cases of a `daemonSet` are: 
	- Monitoring Solution 
	- Logs Viewer
	- Networking Solutions - i.e. weave-net 
- `daemonSet` definition file are similar to `replicaSet`
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata: 
  name: monitoring-daemon
spec: 
  selector: 
    matchLabels:
      app: monitoring-agent
  template: 
    metadata:
      labels: 
        app: monitoring-agent
    spec: 
      containers:
        - name: monitoring-agent
        - image: monitoring-agent

```
You then can use the kubectl create -f command... i.e. 
> kubectl create -f daemonSet-definition.yaml

To view `daemonSets` you can run the command: 
> kubectl get daemonsets
> kubectl describe daemonsets monitoring-daemon

`daemonSets` uses `node affininty` and the default `scheduler` to ensure one `pod` runs on each `node` in a cluster 

## Static Pods
The example indicate that maybe a `node` loses all connectivity with the master `node` 
The example then asks what would  happen, would the kubelet know what to do? 
- To create a `pod` you need a `pod` definition file. 
- the `node` and `kubelet` can be configured to read definition files from a specific locations
- the location is called `manifests` and it at `/etc/kubernetes/manifests` but can be configured when the service is ran
	- all `pod` definition files are located in the directort
	- `kubelet` checks this directory regularly and creates the `pod` based on any definition file here. 
	- when `pods` are made from the files from the `manifests` directory when an `api-server` is not available are considered `static pods`
	- **NOTE**: you can only create `pods` at this level
- the `kubelet` can only operate at the `pod` level 
- the option to change the manifest direct at service start is `--pod-manifest-path=<path to manifest directory>`
- You may also provide a config file in the services or systemd file
	- `--kubeconfig=<path to configuration file>`
	- configuratoin file resides in `/var/lib/kubelet/config.yaml`
	- The configuration file should be a `*.yaml`
	- the configuration file should contain `staticPodPath= <path to files>`
- Once created, you can view `pods` using the container runtime interface (docker, containerd, etc....)
- Use Cases: 
	- manually build a master server since components will not migrate between `agent nodes` 
		- controller-manager
		- apiserver
		- etcd

## Multiple Schedulers
- In the case where the taints, tolerance, affinities, static nodes, and other tools do not satisfy your needs? 
- you are able to deploy custom schedulers to nodes within the kubernetes cluster
- K8S allows this capability and it is supported. 
- can run cluster schedule, and one application can use custom scheduler. 
- you are able to define a custom scheduler for a `pod` via the definition files
- you can download the `kube-scheduler` binary from the internet and configure as needed. 
	- Binary Download: https://storage.googleapis.com/kubernetes-release/release/v1.12.0/bin/linux/amd64/kube-scheduler
	- Run it as a service with options: 
		-  `--config=/etc/kubernetes/config/kube-scheduler.yaml`
			- default name is: `--scheduler-name=default-scheduler"  # you'll likely want to make this more specific to it's purpose`
		- to deploy another scheduler, you can use the same binary and name it something else 
	- General  `kube-scheduler` config file located at `/etc/kubernetes/manifests/my-kube-scheduler.yaml`
```yaml 
apiVersion: v1
kind: Pod
metadata: 
	name: kube-scheduler
	namespace: kube-system
spec: 
	containers: 
	- command: 
	  - kube-scheduler
	  - --address=127.0.0.1
	  - --kubeconfig=/etc/kukbernetes/scheduler.conf
	  - --leader-elect=true
	  - --scheduler-name=my-custom-scheduler
	  - --lock-object-name=my-custom-scheduler

	  image= k8s.gcr.io/kube-scheduler-amd64:v1.11.3
	  name: kube-scheduler
```
Use the kubectl create command to make the scheduler 
use the kubectl get command to view the POD in the given namespace
Configure a `pod` to use the new `scheduler` by specifying it in the `pod` definition file in the `pod specification` section 
```yaml
apiVersion: v1
kind: Pod
metadata: 
  name: nginx
spec: 
  containers: 
  - image: nginx
    name: nginx
  schedulerName: my-custom-scheduler

```
using `kubectl get events` you can see what scheduler picked up the `pod` when looking up `reason = scheduled` 
view the logs of the scheduler using the `kubectl logs my-custom-scheduler --namespace=kube-system`

## Configuring Kubernetes Scheduler 
References for advanced scheduling configurations: 
- https://github.com/kubernetes/community/blobl/master/contributors/devel/scheduler.md
- https://kubernetes.io/blog/2017/03/advanced-scheduling-in-kubernetes
- https://jvns.ca/blog/2017/07/27/how-does-the-kubernetes-scheduler-work/
- https://stackoverflow.com/question/28857993/how-does-kubernetes-scheduler-work


# Logging & Monitoring
## Monitoring Cluster Components
- what would we like to monitor? 
	- nodes in a cluster
	- node level metrics? 
		- how many are healthy
		- performance metrics
			- cpu
			- memory
			- drives
		- pod level metrics
			- resources performance
			- resource consumption
- Kubernetes does not come with a built in metrics / monitoring system 
- suggested solutions: 
	- metrics server
	- prometheus
	- elastic stack 
	- proprietary - datadog
	- proprietary - dynatrace
- Heapster - one of the original projects although deprecated
- Metrics Server - as slimmed down version of heapster
	- Metrics Server is an "in memory" monitoring system 
	- Does not have historical information, only live / current info
	- Must use alternatives for historical retention of monitoring data 
- Kubelet interacts with Metrics Server using subcomponents
	- cAdvisor - exposes metrics through API 
- To install metrics server 
> git clone https://github.com/kubernetes-incubator/metrics-server
> kubectl create -f deploy/1.8+/
- you can view metrics after the install by running: 
> kubectl top node

## Managing Application Logs
* setup log simulation image to run in the background. 
```yaml
apiVersion: v1
kind: Pod
Metadata:
	name: event-simulator-pod
spec: 
	containers: 
	  - name: event-simulator
	    image: kodekloud/event-simulator
	    
```
>kubectl create -f event-simulator.yaml
>kubectl logs -f event-simulator-pod

* The `-f`  option runs them live

| command | resource | argument | pod                 | container       |
| ------- | -------- | -------- | ------------------- | --------------- |
| kubectl | logs     | -f       | event-simulator-pod | event-simulator | 

This is all there is with monitoring for Kubernetes..... holy crap that trash.... Prometheus it is. 


# Application Lifecycle Management
## Rolling Updates and Rollbacks
- Rollout and Versioning
- When you introduce a new version, it triggers a roll out and a new revision is created. 
- You can view the status of any rollout by using the following command: 
> kubectl rollout status <deployment/myapp>   # Current roll out history 
> kubectl rollout history <deployment/myapp>  # past roll out history 

- Recreate Strategy 
	- Not the default method
	- destroy all instances
	- build all new instances of the app
	- Period of time where application is not available. 
- Rolling Update
	- Default upgrade strategy 
	- upgrade each instanced one by one individually 
- How do you do this update process? 
	- update definition.yaml for resource you are changing
	- run apply command referencing the definition file
> kubectl apply -f deployment-definition.yaml

A rollout is then triggered after the apply. 
You can also use the set command 
> kubectl set image deployment/myapp

however, using this method will cause the definition file having a different configuration then the live system. 
upgrades to a `deployment` will cause: 
- a new `replicaset` to be created for the `deployment`
- while new `pods` are being created on the new `replicaset` the `pods` in the old `replicaset` are being terminated
- If things have gone wrong with the update, youcan `rollback` the deployment\
>kubectl rollout undo deployment/myapp

The old replica set will be filled with new pods
the upgraded replicaset will no long erhav epods in it. 
summary of commands: 
- create = `kubectl create -f deployment-definition.yaml`
- get = `kubectl get deployments`
- update = 
	- `kubectl apply -f deployment-definition.yaml`
	- `kubectl set image deployment/myapp nginx=nginx:1.9.1`
- status = 
	- `kubectl rollout status deployment/myapp`
	- `kubectl rollout history deployment/myapp`
- rollback = `kubectl rollout undo deployment/myapp`

## Commands and Arguments in Docker
- Containers are not meant to host an operating system 
- Containers are meant to host an application 
- Containers only lives as long as the process within it is alive
- Who defines what process is ran within the container?
	- This is defined in the docker config file using the `CMD [""]` line items
- By default, docker does not attach a terminal to a docker container
	- so when `CMD ["bash"]` is defined, the container instantly and terminates instantly. 
- an option to continue the run of a operating system is to append an argument to the docker command that will overide the docker config
> docker run ubuntu sleep 5
 - this will cause the operating system to start, sleep for 5 seconds, and then terminates
 - if you want the image to to always run the sleep command, you will create your own image from the operating system image and apply your own command. 
	 - `from ubuntu
	 - `CMD sleep 5
 - commands can be defined in may different ways. 
	 - `CMD command param1` ie. `CMD Sleep 5`
	 - `CMD ["command", "parameter1"]` ie. `CMD ["sleep", "5"]`
 - ENTRYPOINT instruction 
	 - can specify the program that will run when the container starts
	 - whatever you specify on the command line will be appended to the entry point 
	 - i.e.  `ENTRYPOINT ["sleep"]`  &&  `docker run ubuntu-sleeper 10` will result in a start command of `sleep 10`
	 - if you don't specify an argument in the command line when calling a docker image with a ENTRYPOINT that requires a parameter, you will receive an error
	 - to get around this you can append more data to the docker file... 
```docker
FROM Ubuntu

ENTRYPOINT ["sleep"]

CMD ["5"]
```
- by doing this you can supply a default parameter that can be overridden by the command line parameter. 
- Always define the ENTRYPOINT and CMD in JSON format. 
-  you can override the ENTRYPOINT setting in the docker file by using the `--entrypoint argument`  in the docker run command. 

## Command and Arguments in Kubernetes
Continuing from the previous section where we made a docker image called Ubuntu-sleeper, we'll now make a pod that uses this image. 
```yaml 
apiVersion: v1
kind: Pod
metadata:
	name: ubuntu-sleeper-pod
spec: 
	containers: 
	- name: ubuntu-sleeper
	  image: ubuntu-sleeper
	  args: ["10"]
```

The `args` are the parameters passed to the command. 
the `args` override the `CMD` in the docker file 
To override the `ENTRYPOINT` defined in the docker file you will add the following
```yaml 
apiVersion: v1
kind: Pod
metadata:
	name: ubuntu-sleeper-pod
spec: 
	containers: 
	- name: ubuntu-sleeper
	  image: ubuntu-sleeper
	  command: ["sleep2.0"]
	  args: ["10"]
```
The `command` function overrides the `ENTRYPOINT` definition in the docker file. 

## Configure Environment Variables in Applications
* environment variable for applications can be set in the `pod` definitions 
```yaml
apiVersion: v1 
kind: Pod
metadata: 
  name: simple-webapp-color
spec: 
	containers: 
	- name: simple-webapp-color 
	  image: simple-webapp-color
	  ports:
		containersPort: 8080
	  env: 
	    - name: APP_COLOR
	      value: pink
```
- The above is an environment variable as a plain key value.
- There are 3 ways to provide values to Environment Variables
	- Plain Key Value
	- ConfigMap
	- Secrets
## Configure ConfigMaps in Applications
- when you have a lot of environment variable data and files with that data, to define them in the pod can be very cumbersome. 
- In comes ConfigMaps
- Two ways to create `configMap`
> (imperative) `kubectl create configmap <config-name> --from-literal=<key>=<key-value> --from-literal=<key>=<key-value>` 
> i.e. `kubectl create configmap app-config --from-literal=APP_COLOR=blue --from-literal=APP_MOD=prod`
> OR 
> i.e. `kubectl create configmap app-config --from-file=app_config.properties`
> OR
> (declarative) `kubectl create -f <configmap filename>`

A sample yaml file  used by the declarative method noted above is similar to: 
```yaml 
apiVersion: v1 
kind: ConfigMap
metadata: 
	name: app-config
data: 
	APP_COLOR: blue
	APP_MODE: prod
```

- a reference in a `pod` definition file will reside in the `spec -> envFrom: -> configMapRef: -> name:`
```yaml
.......
spec: 
  containers: 
  - name: simple-webapp
    image: simple-webapp
    ports: 
    - containerPOr: 8080
  envFrom: 
  - configMapRef:
      name: app-config 
```

To view configMaps run: 
> kubectl get configmaps
> kubectl describe configmaps

So, overall process is: 
Go declarative.... It's easier in the long run. 
1. create a configMap yaml file
2. run the `kubectl create -f configMap.yaml`
3. in the `pod` definition file add the `envFrom:` and subsequent fields 
4. point the `name` fields to the name of the configMap you created previously

Overall, 3 total options to inject environment variables. 
- Single Environment variables defined in `pod` definitions
- Multiple environment variables in a `configMap`
- in a `volume` definition 

## Secrets
- All about passwords and keys
- Store sensitive information 
- stored in an encoded or hashed format. 
- 2 steps involved in working with secrets
	- Creating the secret
	- injecting it into a `pod`
- command to setup a secret. 
- Imperative methods to create secrets
	- (syntax) - `kubectl create secret generic <secret-name> --from-literal=<key>=<value>
	- (example) - `kubectl create secret app-secret --from-literal=db_host=mysql`
	- (syntax) - `kubectl create secret generic <secret-name> --from-file=<path-to-file>`
	- (example) - `kubectl create secret generic app-secret --from-file=app_secret.properties`
- Imperative file structure: `secrets_file.properties`
```Text 
DB_HOST: mysql
DB_User: root
DB_Password: paswrd
```
- Declarative 
	- Summary: uses a yaml file as normal for declarative methods, This method is assumed to be recommended. 
	- (cmd syntax) - `kubectl create -f secret-data.yaml`
- Declarative File Format: 
- *ATTENTION - !!!!NOTE!!!!  Data must be in an encoded format*
``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_Host: bXlzcWw=
  DB_User: cm9vdA==
  DB_Password: cGFzd3Jk
```
- When using declarative format, how do you encode the data an ensure that the creation is able to consume it? 
- With a linux host you can use the `base64` encoding available from the cli using the below example
	- (syntax) - `echo -n 'string' | base64` which result in an encoded string format that you can use in the config file
	- (example) -  `echo -n 'mysql' | base64` will result in `bXlzcWW=` 
	- (example) - `echo -n 'root' | based64` will result in `cm9vdA==`
	- Copy and past each result into the properties file or yaml used by the commands 
- To view secrets you can use `kubectl` as we do with all other things 
	- (example syntax) - `kubectl get secrets`
	- (example syntx) - `kubectl get secrets <secret-name> --namespace=<namespace>`
- To display the configs of a secrets you can output them in a yaml format
	- (syntax) - `kubectl get secret <secret-name> -o yaml`
	- (example ) - `kubectl get secret app-secret -o yaml`
- The `kubectl describe` option is also available and used in the same manner
- The secrets can be decoded by reversing the same algo used to encode the secrets
	- (syntax) - `echo -n 'encoded-string' | based64 --decode`
	- (example) - `echo -n 'bXlzcWw==' | based64 --decode` will result in a string response of `mysql`
- To pass the secrets in a `pod-definition` use the `envFrom` group of declarations in the `yaml`
- Below is an example of the full `yaml` file. The section of value starts at `envFrom` inside the `container` specification
```yaml 
apiVersion: v1
kind: Pod
metadata: 
  name: simple-webapp-color
  labels: 
    name: simple-webapp-color
spec:
  containers: 
  - name: simple-webapp-color
    image: simple-webapp-color
    ports:
    - containerPort: 8080
    envFrom:
    - secretRef:
      name: app-secret
```
- `app-secret` in the `name` field for the `secretRef` is the name of the secret you created earlier for the SQL login. 
- Secrets can be used for many functions: 
	- ENV - Environment Variables
	- SINGLE ENV - Singular environment variables defined explicity in the `object definition` files
	- VOLUME - as a volume for retaining data in an encoded format. 
- Secrets in `Pods` as `Volumes`
	- If you declare a secret as a volume, each peice of the secret will be stored in the volume as an individual file. 
	- Using the example secret from earlier, if used as a volume, would result in three files in the volume
		- DB_Host
		- DB_Password
		- DB_User
	- if you look at the contents of the files in the volume, you will see the pasword as it was stored...  clear text or encoded
- Below is a `yaml` snippet of the volume definition for a secret
```yaml
volumes: 
- name: app-secret-volume
  secret: 
    secretName: app-secret
```

-- data collection for practice: 
sql01  | c3FsMDE=
root | cm9vdA==
password123 | cGFzc3dvcmQxMjM=

## Notes on Secrets Lab 
Remember that secrets encode data in base64 format. Anyone with the base64 encoded secret can easily decode it. As such the secrets can be considered not very safe.

The concept of safety of the Secrets is a bit confusing in Kubernetes. The [kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/secret) page and a lot of blogs out there refer to secrets as a “safer option” to store sensitive data. They are safer than storing in plain text as they reduce the risk of accidentally exposing passwords and other sensitive data. In my opinion it’s not the secret itself that is safe, it is the practices around it.

Secrets are not encrypted, so it is not safer in that sense. However, some best practices around using secrets make it safer. As in best practices like:

-   Not checking-in secret object definition files to source code repositories.
-   [Enabling Encryption at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) for Secrets so they are stored encrypted in ETCD.

Also the way kubernetes handles secrets. Such as:

-   A secret is only sent to a node if a pod on that node requires it.
-   Kubelet stores the secret into a tmpfs so that the secret is not written to disk storage.
-   Once the Pod that depends on the secret is deleted, kubelet will delete its local copy of the secret data as well.

Read about the [protections](https://kubernetes.io/docs/concepts/configuration/secret/#protections) and [risks](https://kubernetes.io/docs/concepts/configuration/secret/#risks) of using secrets [here](https://kubernetes.io/docs/concepts/configuration/secret/#risks)

Having said that, there are other better ways of handling sensitive data like passwords in Kubernetes, such as using tools like Helm Secrets, [HashiCorp Vault](https://www.vaultproject.io/). I hope to make a lecture on these in the future.

## Multi-Container Pods: 
- Drivers to setup multi-container pods: 
	- two components of a singular information 
	- same lifecycle
	- share same network space
	- share same storage volumes
- This will: 
	- remove the needs for shared storage between two pods
	- remove the services needed to allow the pods to communicate 
- the `yaml definitions` file allows for mutliple containers within a `pod`
- each `container` in a `pod definition` is an `array` within the `spec:` section of the file. 
- each `container` will have it's own declarations within the `definitions` file under the `container:` section 
- in the example below, two `containers` are defined within the `spec:` section
	- simple-webapp
	- log-agent
```yaml 
apiVersion: v1
kind: Pod
metadata: 
  name: simple-webapp
  labels: 
    name: simple-webapp
spec: 
  containers: 
  - name: simple-webapp
    image: simple-webapp
    ports:
    - containersPort: 8080
  - name: log-agent
    image: log-agent
```


## Multi-Container Pods Design Patterns
* 3 different designs for Multi-Container pods 
	* SideCar
	* Adapter
	* Ambassador
* Topic is not covered in the CKA exam. Only in the CKAD exam (app dev)
*
## Init Containers: 
In a multi-container pod, each container is expected to run a process that stays alive as long as the POD’s lifecycle. For example in the multi-container pod that we talked about earlier that has a web application and logging agent, both the containers are expected to stay alive at all times. The process running in the log agent container is expected to stay alive as long as the web application is running. If any of them fails, the POD restarts.

But at times you may want to run a process that runs to completion in a container. For example a process that pulls a code or binary from a repository that will be used by the main web application. That is a task that will be run only one time when the pod is first created. Or a process that waits for an external service or database to be up before the actual application starts. That’s where **initContainers** comes in.

An **initContainer** is configured in a pod like all other containers, except that it is specified inside a `initContainers` section, like this:
```yaml 
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'git clone <some-repository-that-will-be-used-by-application> ;']
```
When a POD is first created the initContainer is run, and the process in the initContainer must run to a completion before the real container hosting the application starts.

You can configure multiple such initContainers as well, like how we did for multi-pod containers. In that case each init container is run **one at a time in sequential order**.

If any of the initContainers fail to complete, Kubernetes restarts the Pod repeatedly until the Init Container succeeds.
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox:1.28
    command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
  - name: init-mydb
    image: busybox:1.28
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done;']
```

Read more about initContainers here. And try out the upcoming practice test.

[https://kubernetes.io/docs/concepts/workloads/pods/init-containers/](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

## Self Healing Application 
Kubernetes supports self-healing applications through ReplicaSets and Replication Controllers. The replication controller helps in ensuring that a POD is re-created automatically when the application within the POD crashes. It helps in ensuring enough replicas of the application are running at all times.

Kubernetes provides additional support to check the health of applications running within PODs and take necessary actions through Liveness and Readiness Probes. However these are not required for the CKA exam and as such they are not covered here. These are topics for the Certified Kubernetes Application Developers (CKAD) exam and are covered in the CKAD course.

# Cluster Maintenance: 
## OS Upgrades
- If a pod becomes inaccessible for more than 5 minutes, K8S considers the `pod` to be dead. 
- If a `pod` is considered dead the scheduler will start any required `pods` on another `node` as defined in replica or deployment sets. 
- The 5 minute tolerance for `pod` eviction is set at the control manager via the: `kube-controller-manager --pod-eviction-timeout=5m0s` declaration 
- if a node returns to service after 5 minutes, the node will not have any `pods` assigned. Any pods with static affininty will be offline if this was the only node able to support the affinity rule. 
- Since a return to service of any `node` is not guaranteed after an upgrade, you will want to prevent a node from being rendered `evicted` due to `node timeout`
- Prepare a `node` for upgrade by running the following: `kubectl drain <node-name>`
	- This will move all `pods` on the node to different nodes allowing for no impact while performing maintenance. 
	- the `node` that is drained will set into a `no schedule` state called `cordon` that prevents  any new `pods` from being scheduled on it until the maintenance is done and the `node` is rebooted. 
	- validate all `pods` are no longer running on the `node` before maintenance begins
	- one the `node` is rebooted and maintenance is done, it has to be pulled out of `cordon` before any `pods` are scheduled on it
		- to remove the `cordon` status: `kubectl uncordon <node-name>`
	- Another option is to mark a node a `cordon` without draining: `kubectl cordon <node-name>`
		- this will not terminate the `pods` on the node
		- no new `pods` will be scheduled on the node 

## Kubernetes Software Versions: 
