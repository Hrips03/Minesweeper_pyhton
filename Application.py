from controller import controller
from view import ui
from model import gameLogic

class Application:
    _instance = None
    m_controller = None
    m_view = None
    m_model = None
          
    @classmethod 
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = Application()
        return cls._instance
    
    def getview(self):
        self.m_view = ui.UI()
        return self.m_view
    
    def getmodel(self):
        self.m_model = gameLogic.Model()
        return self.m_gan
    
    def run(self):
        self.m_controller = controller.Controller()
        self.m_controller.run()