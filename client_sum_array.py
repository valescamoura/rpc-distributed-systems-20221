import rpyc
import sys
import time
from random import randint
 
def generate_and_sum_vector(conn, n):
   array = []
   for i in range(n):
      array.append(randint(0, n-1))
   
   sum = conn.sum_array(array)
   return sum

if __name__ == "__main__":
   if len(sys.argv) < 3:
      exit("Usage {} SERVER LEN_ARRAY".format(sys.argv[0]))
   
   server = sys.argv[1]
   start = time.time()
   conn = rpyc.connect(server, 18861)
   conn._config['sync_request_timeout'] = None
   conn._config['allow_pickle'] = True
   print('Sum array = ', generate_and_sum_vector(conn.root, int(sys.argv[2])))
   end = time.time()
   print('Time client = ', end-start)






