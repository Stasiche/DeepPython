sudo docker build -t hard $(pwd) && sudo docker run --mount src="$(pwd)/artifacts",target=/DeepPython/hw_2/artifacts,type=bind -it hard
