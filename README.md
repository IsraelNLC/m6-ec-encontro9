
https://github.com/IsraelNLC/m6-ec-encontro9/assets/99210055/a18808c0-0165-4b01-a79c-b6410fff82a2
## Transmissão e armazenamento de imagens + YOLOv8
Esta implementação se trata de uma transmissão de imagens ou vídeos, utilizando tópicos do ros e servidor FastApi, o qual envia para um bucket na nuvem. Além disso, na etapa de transformar o vídeo em imagem e salvá-las localmente, ocorre uma varredura com o Yolo para verificar se há rostos na imagem.

# Arquivos
main.py -> Implementa uma API que permite o armazenamento local, upload e o acesso a imagens, utilizando o framework FastAPI e o serviço de armazenamento Supabase.
image_publisher_ros.py -> Programa ROS 2 que publica um fluxo de vídeo, convertendo os quadros em mensagens de imagem do ROS 2 e publicando no tópico 'video_frames'.
enviar.py -> Programa ROS 2 que recebe o fluxo de vídeo, realiza detecção de objetos usando um modelo pré-treinado e envia as imagens processadas para o main.py, pela rota /upload.

# Vídeo

Uploading 20230618_160650.mp4…
