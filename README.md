# Word Count Service
An extremely useful little program helps you count number of words in a file

# Assumptions
- NOT addressing uWSGI / Python Web Server Production mode
- the file has a "reasonable" line length
- the file has a "reasonable" size
- We use the split() function in python builtin to determine how many words in a given line here
- will deploy to `default` namespace -- not addressing k8s namespace here



# Run unit tests

```bash
python3 -m unittest tests/word_count_tests.py
```

# Test running a local server
```bash
# in word_count/ directory
FLASK_APP=server.py FLASK_ENV=development flask run
curl -i "localhost:5000" -H "Content-Type: multipart/form-data" -F "data=@PATH_TO_YOUR_FILE"
```

# Build (Docker image)
```bash
# substitute 0.0.1 to other build number to publish upgrade
sudo docker build . -t word_count:0.0.1 
```

# Test running a docker container locally
```bash
sudo docker run --network=host word_count:latest
# 
curl -i localhost:5000/
```

