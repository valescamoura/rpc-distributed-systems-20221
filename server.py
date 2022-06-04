import rpyc
import time

class MyService(rpyc.Service):
    start = 0
    end = 0
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        print('Connected!')
        self.start = time.time()
        pass
    def on_disconnect(self, conn):
        self.end = time.time()
        print('Time server = ', self.end-self.start)
        print('Disconnected!')
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        pass
    def exposed_get_answer(self): # este é um método exposto
        return 42
    exposed_the_real_answer_though = 43     # este é um atributo exposto
    def get_question(self):  # este método não é exposto
        return "Qual é  a cor do cavalo branco de Napoleão?"
    def exposed_sum_array(self, array):
        sum = 0
        for i in range(len(array)):
            sum += array[i]
        return sum

#Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
