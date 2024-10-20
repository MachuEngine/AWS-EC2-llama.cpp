docker run --rm -d \
	-p 8080:8080 \
	-v $HOME/models/:/models \
	--gpus all \
	ghcr.io/ggerganov/llama.cpp:server-cuda \
	-m models/gemma-2-2b-it/gemma-2-2B-it-Q5_K_S.gguf \
	-c 512 --host 0.0.0.0 --port 8080 \
    --n-gpu-layers 60
