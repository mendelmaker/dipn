# Making GPU docker image
*You should run this code on a GPU computer*

dependencies: 
- CUDA 10.2
- Python 3.6
- Python 2.7
- Pytorch 1.6.0
- ROS(Melodic)

**Building docker image**
```
    $ source build.sh
```

**How to run**
```
    $ source docker_run.sh
    Docker $ source environment.sh
```
**If you want to enter same container**
```
    $ source docker_join.sh
    Docker $ source environment.sh
```
