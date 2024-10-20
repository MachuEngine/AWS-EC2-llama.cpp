docker run --rm -d \
	-p 8080:8080 \
	-v $HOME/models/:/models \
	ghcr.io/ggerganov/llama.cpp:server \
	-m models/gemma-2-2b-it/gemma-2-2B-it-Q5_K_S.gguf \
	-c 512 --host 0.0.0.0 --port 8080 \

