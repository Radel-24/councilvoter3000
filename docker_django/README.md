![42 Council Voter 3000](logo.png)

## This Docker container is build to run on server an provide an easy to use interface for every student to vote for their councillors.

To run docker on 42 school macs use the toolbox and ./init_docker.sh
https://github.com/alexandregv/42toolbox

```
docker build -t poll_app .
```
```
docker run -ti -p 8000:8000 -v $PWD:/poll_app poll_app
```

## The Team
42 Heilbronn students (https://www.42heilbronn.de/en/):
[Robin](https://github.com/Radel-24), [Alex](https://github.com/42akurz), [Kevin](https://github.com/khirsig)
