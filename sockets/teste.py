import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    print("Realizando prueba de velocidad...")
    download_speed = st.download() / 10**6  # Convertir a Mbps
    upload_speed = st.upload() / 10**6  # Convertir a Mbps
    
    print(f"Velocidad de descarga: {download_speed:.2f} Mbps")
    print(f"Velocidad de subida: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    test_speed()
