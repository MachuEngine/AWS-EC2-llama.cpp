curl --request POST \
    --url http://localhost:8080/completion \
    --header "Content-Type: application/json" \
    --data '{"prompt": "Please tell me about Docker in 10 sentences.","n_predict": 128}'
