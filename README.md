# DotaClient on K8s

---

DotaClient is a reinforcement learning system to train RL agents to play Dota 2 through self-play.

<img src="dotaclient.png" alt="dotaclient schema" width="400"/>

* Distributed Agents self-playing Dota 2.
* Experience/Model Broker (rmq).
* Distributed Optimizer (PyTorch)

## Prerequisites

* Kubeflow's [PyTorch Operator](https://github.com/kubeflow/pytorch-operator)
* Google Cloud Storage (GCS)
* Kubernetes Cluster (e.g. GKE).
* Build the [dota docker image](https://github.com/TimZaman/DotaService)
* Build the [dotaservice docker image](https://github.com/TimZaman/DotaService)
* Build the [rabbitmq docker image](docker/Dockerfile-rmq)
* Install [ksonnet](https://ksonnet.io/)

## Launch distributed dota training

```bash
cd ks-app
ks show default  # Shows the full manifest
ks param list  # Lists all parameters
ks apply default  # Launches everything you need
```

Note: A typical job has 40 agents per optimizer. One optimizer does around 1000 steps/s.
