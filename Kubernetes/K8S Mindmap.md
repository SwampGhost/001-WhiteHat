---

mindmap-plugin: basic

---

# Kubernetes (K8)

## Cluster Architecture
- Nodes
   - link: https://kubernetes.io/docs/concepts/architecture/nodes/
   - Management
      - Node Name Uniqueness
      - Self-Registration of Nodes
      - Manual Node Administration
   - Node Status
      - Addresses
      - Conditions
         - Ready
         - Disk Pressure
         - Memory Pressure
         - PID Pressure
         - NetworkUnavailable
      - Capacity and Allocatable
   - Heartbeats
   - Node Controller
      - Rate Limit on Evictions
   - Resource Capacity Tracking
   - Node Topology
   - Swap Memory Management
- Control Plane-Node Communications
   - Node to Control Plane
   - Control Plane to Node
      - apiserver to nodes, pods, and services
      - SSH Tunnels
      - Konnectivity Services
- Controllers
   - Control Patterns
   - Control via API Server
   - Direct Control
   - Desired versus current state
   - Design
   - Ways of running controllers
- Cloud Controller Manager
   - Design
   - Cloud Controller manager functions
      - Node Controllers
      - Route Controllers
      - Service Controllers
   - Authorizations
      - Node Controllers
      - Route Controllers
      - Service Controllers
      - Others
   - Link: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
- Container Runtime Interface (CRI)
   - API
   - Upgrading
- Garbage Collection
   - Owners and Dependants
   - Casading Deletion
      - Foreground Cascading Deletion
      - Background Cascading Deletion
      - Orphaned Dependants
   - Garbage collection of unused containers and images
      - Container Image Lifecycle
      - Container Garbage Collection
   - Configuring Garbage Collection

## Containers
- Container Images
- Container Runtimes

## Workloads

## Services, Load Balancing, and Networking
- Service
- Topology aware traffic Routing with Topology Keys
- DNS for Services and Pods
- Connecting Applications with Service
- Ingress
- Ingress Controllers
- EndPointSlices
- Service Internal Traffic Policy
- Topology Aware Hints
- Network Policies
- IPv4/IPv6 Dual-Stack

## Storage
- Volumes
- Persistent Volumes
- Ephemeral Volumes
- Storage Classes
- Dynamic Volume Provisioning
- Volume SnapShots
- CSI Volume Cloning
- Storage Capacity
- Node-Specific Volume Limits
- Volume Health Monitoring

## Configurations
- json
- yaml
- Best Practices
- Config Maps
- Secrets
- Resource Management for Pods and Containers
- Organizing Cluster Access Using Kubeconfig files

## Security
- Overview of Cloud Native Security
- Pod Security Standards
- Pod Security Admissions
- Controlling Access to the Kubernetes API

## Policies
- Limit Ranges
- Resource Quotas
- Pod Security Policies
- Process ID Limits and Reservations
- Node Resource Managers

## Scheduling, Preemption, and Eviction
- Kubernetes Scheduler
- Assigning Pods to Notes
- Pod Overhead
- Taints and Tolerations
- Pod Priority and Preemption
- Node-Pressure Eviction
- API-Initiated Eviction
- Resource Bin Packing for Extended Resources
- Scheduling Framework
- Scheduler Performance Tuning

## Cluster Administration
- Certificates
- Managing Resources
- Cluster Networking
- Logging Architecture
- Metrics for Kubernetes
- Metrics for Kubernetes System Components
- System Logs
- Traces for Kubernetes System Components
- Proxies in Kubernetes
- API Priority in Fairness
- Installing Addons

## Extending Kubernetes
- Extending Kubernetes
- Compute, Storage, and Networking Extensions
- Operator Pattern
- Service Catalog