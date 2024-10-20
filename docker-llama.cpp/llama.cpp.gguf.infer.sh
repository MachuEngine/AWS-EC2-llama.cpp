$HOME/llama.cpp/llama-cli \
	-m $HOME/models/gemma-2-2b-it/gemma-2-2b-it-q5.gguf \
	-p "Please tell me about Tesla." \
    -n 400 \
	-e \
	#--n-gpu-layers 60 
	--log-disable