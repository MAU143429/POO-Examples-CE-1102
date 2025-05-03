from cola import Cola
class Clinica:
    def __init__(self):
        self.dict = { }
    def agregarMedico(self,medico,pacientes):
        #self.dict[medico] = Cola()
        self.dict[medico] = pacientes
    def actualizarMedico(self,medico,cola):
        self.dict[medico] = cola
    def registrarPaciente(self,medico,paciente):
        mCola = self.dict[medico]
        mCola.actualizarMedico(medico, mCola)
    def siguiente(self,medico):
        mCola = self.dict[medico]
        pacinete = mCola.dequeue()
        self.actualizarMedico(medico,mCola)
        return paciente
    def test(self):
        cola= Cola()
        cola.enqueue("Pedro")
        cola.enqueue("Marco")
        self.agregarMedico("Pablo",cola)
        mCola = self.dict["Pablo"]
        print(mCola.dequeue())
        print(mCola.dequeue())
