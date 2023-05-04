

class DrawHelpers():

    @staticmethod
    def get_text_dimensions(text_string, font):
        # https://stackoverflow.com/a/46220683/9263761
        ascent, descent = font.getmetrics()
        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent
        return (text_width, text_height)
    
    @staticmethod
    def invertColor(hex):

        if (hex[0] == '#'):
            hex = hex[1::]
    
        if (len(hex) == 3):
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
        
        if (len(hex) != 6):
            raise Exception('Invalid HEX color.')

        
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
          
        r = (255 - r)
        g = (255 - g)
        b = (255 - b)

        return f"#{r:02x}{g:02x}{b:02x}" 
    