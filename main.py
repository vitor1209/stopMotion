# bibliotecas
from moviepy.editor import ImageSequenceClip
import cv2
import time
import os

# acesso a camera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

# nome do frame
frame_count = 0

# criar pasta para guardar as fotos
pasta_unicos = 'fotos'

os.makedirs(pasta_unicos, exist_ok=True)

try:
    while frame_count < 15:
        ret, frame = camera.read()

        # salvar as fotos
        cv2.imwrite(f"fotos\\frame_{frame_count}.png", frame)
        frame_count += 1
        
        # uma foto a cada .... tempo
        time.sleep(0.5)        
        
        # tecla para parar
        if cv2.waitKey(1) == 27:
            break
finally:
    camera.release()
    cv2.destroyAllWindows()

# Define o caminho das imagens e cria um vídeo
image_files = [f"fotos\\frame_{i}.png" for i in range(frame_count)]
clip = ImageSequenceClip(image_files, fps=5)  

# Salva o vídeo
clip.write_videofile("stop_motion_video.mp4")