# Word Count Service
An extremely useful little program helps you count number of words in a file

# Assumptions
- we are able to access k8s cluster and have the enough permissions to do things
- worker nodes are schedulable
- the file has a "reasonable" line length
- the file has a "reasonable" size
- We use the split() function in python builtin to determine how many words in a given line here
- will deploy to `default` namespace -- not addressing k8s namespace here

# Run unit tests

```bash
# locally
python3 -m unittest discover ./tests -p "*_tests.py"
# in virtualenv
python -m unittest discover ./tests -p "*_tests.py"
```

# Test running a local server
```bash
# in word_count/ directory
FLASK_APP=server.py FLASK_ENV=development flask run
curl -i "localhost:5000" -H "Content-Type: multipart/form-data" -F "data=@PATH_TO_YOUR_FILE"
# response will be like
{"fileName": "YOUR_FILE_NAME", "wordCount": 12345}
```

# Build (Docker image)
```bash
# substitute 0.0.1 to other tag to build updated images
sudo docker build . -t word_count:0.0.1
```

# Test running a docker container locally
```bash
sudo docker run --network=host word_count:0.0.1
```

# Deploy
```bash
# double check the image tag
kubectl apply -f word-count.yaml
```

# Upgrades
1. Make code changes
2. Commit to local git repo
3. run the `Build` step above, with `updated` image tag
4. modify the image tag of `word-count` container in word-count.yaml
5. run the `Deploy` step

# Scale
```bash
# scale to 88 replicas, make sure you of enough worker nodes!
kubectl scale --replicas=88 deployment/word-count
```

# Monitor
- The application is monitored using Prometheus client, which comes with out-of-the-box metrics for python-related and process related metrics
   - 
