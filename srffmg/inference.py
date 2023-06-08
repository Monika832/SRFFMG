import cv2
from image_loader import image_loader
def load_model(path):
    '''
        Loads the model from the path
    '''
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(path)
    sr.setModel("lapsrn",8)
    return sr

def upscale_image_and_convert(model,path):
    '''
    Code to read the image and convert to upscale format
    '''
    _,img = image_loader(path)
    result = model.upsample(_)
    return img,result
    