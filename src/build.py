from landslide import generator

def build():
    generator.Generator("AMS93/config.cfg").execute()
    
if __name__ == "__main__":
    build()
    
