import speedtest
import schedule
import time
from datetime import datetime

def run_speedtest():
    # Criar objeto para teste de velocidade
    st = speedtest.Speedtest()
    
    # Realizar o teste
    st.get_best_server()
    download_speed = st.download() / 1024 / 1024  # Convertendo para Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convertendo para Mbps
    
    # Obter a data e hora do teste
    test_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Salvar os resultados em um arquivo de log
    with open('speedtest.log', 'a') as f:
        f.write(f'Horario do teste: {test_time}\nVelocidade de Download: {download_speed:.2f}Mbps\nVelocidade de Upload: {upload_speed:.2f} Mbps\n===============================================================================================\n')

def hourly_speedtest():
    # Realizar um teste de velocidade no início da execução
    run_speedtest()
    
    # Agendar os testes de velocidade para serem executados de hora em hora
    schedule.every().hour.do(run_speedtest)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    hourly_speedtest()
