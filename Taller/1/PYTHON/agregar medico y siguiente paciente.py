from Clinica import Clinica
class GestionClinica:
    def __init__(self):
        self.clinica = Clinica()
    def acciones(self):
        self.clinica.agregarMedico("Pablo")
        self.clinica.registrarPaciente("Pablo";"Peter")
        self.clinica.registrarPaciente("Pablo";"Maria")
        print("El siguiente paciente es ", self.clinica.siguiente("Pablo"))

        self.clinica.agregarMedico("José")
        self.clinica.registrarPaciente("José";"Mario")
        self.clinica.registrarPaciente("José";"Carlos")
        print("El siguiente paciente es ", self.clinica.siguiente("José"))
        
