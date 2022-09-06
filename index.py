#Función para calcular histograma de una imágen ingresada por parámetro

def calculoHistograma(img):
  hist:int = np.zeros(256)
  (F,C) = img.shape
  for i in range (F):
    for j in range(C):
      valor = img[i,j]
      hist[valor] = hist[valor] + 1
    
  
  return(hist)
  
  
  #Estirar un histograma
  
  def estiramientoHistograma(img):
  (F,C)=img.shape
  estiramiento = np.zeros((F,C),np.uint8)
  min = np.min(img)
  max = np.max(img)
  for i in range(F):
    for j in range(C):
      estiramiento[i,j] = (((img[i,j]-min)/(max-min))*255)
  return estiramiento;
  
  
  #Ecualización de un histograma
  
  def ecualizamiento(img):
  cs = np.cumsum(calculoHistograma(img))    #Funcion de distribucion acumulada
  (F,C)=img.shape
  ecualizacion = np.zeros((F,C),np.uint8)
  for i in range(F):
    for j in range(C):
      pixel = img[i,j]
      ecualizacion[i,j] = (cs[pixel]/cs[255])*255
  return ecualizacion;
  
 
