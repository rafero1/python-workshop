import os
from datetime import datetime
from t5 import t_escrever_log, t_ler_log

if __name__ == "__main__":
  current_file_path = os.path.dirname(__file__)
  log_path = os.path.join(current_file_path, "log.txt")

  t_escrever_log(log_path, "Linha 1")
  t_escrever_log(log_path, "Linha 2")

  log_content = t_ler_log(log_path)
  print(log_content)
