# berlin-housing

This repos shows how to:
1. Train a Random Forest Regressor to predict rent prices from historical data.
2. Create a Streamlit web application to use the model.
3. Deploy the model following MLOps good practices.

## Usage

![streamlit-app](https://user-images.githubusercontent.com/50741878/147391147-52f44eb1-6c9b-4cac-9d7a-749e27a34a0f.png)

### Docker

Build the Docker image locally:

```
docker build -t berlin-housing:latest .
```

Run the container exposing port 8501:

```
docker run -p 8501:8501 berlin-housing:latest
```

The terminal should print the local address where you can access the application

## Dataset


## Modeling
