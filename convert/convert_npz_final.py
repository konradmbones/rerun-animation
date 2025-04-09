import numpy as np
import os

def convert_file(input_file, output_file):
    # Ładowanie oryginalnego pliku NPZ
    print(f"\nKonwersja pliku: {os.path.basename(input_file)}")
    data = np.load(input_file)

    print("\nOryginalne kształty:")
    for key in data.files:
        arr = data[key]
        print(f"{key}: shape={arr.shape}, dtype={arr.dtype}")

    # Konwersja na float32 i przygotowanie danych
    converted_data = {}
    for key in data.files:
        arr = data[key]
        if arr.dtype == np.float64:
            converted_data[key] = arr.astype(np.float32)
        else:
            converted_data[key] = arr

    # Konwersja pozy
    poses = converted_data['poses']
    num_frames = poses.shape[0]
    num_joints = poses.shape[1] // 3

    print(f"\nLiczba stawów w oryginalnych danych: {num_joints}")

    # Przekształć poses na format (num_frames, num_joints, 3)
    poses_reshaped = poses.reshape(num_frames, num_joints, 3)

    # Weź tylko pierwsze 24 stawy (standardowy model SMPL)
    poses_reshaped = poses_reshaped[:, :24, :].astype(np.float32)

    print(f"\nSzczegóły przekonwertowanej pozy:")
    print(f"Liczba klatek: {poses_reshaped.shape[0]}")
    print(f"Liczba stawów: {poses_reshaped.shape[1]}")
    print(f"Parametry na staw: {poses_reshaped.shape[2]}")
    print(f"Zakres wartości: min={poses_reshaped.min()}, max={poses_reshaped.max()}")

    # Aktualizacja danych w pliku NPZ
    converted_data['poses'] = poses_reshaped

    # Zapisanie przekonwertowanych danych
    np.savez(output_file, **converted_data)
    print(f"Zapisano przekonwertowane dane do: {output_file}")

# Konwersja obu plików
convert_file(
    "/Users/konradmakosa/Documents/Bones/rerun/rerun_animation3/npz_models/Acrobatics Bridge A415 Model.npz",
    "/Users/konradmakosa/Documents/Bones/rerun/rerun_animation3/npz_models/converted_models/bridge_24joints_v7.npz"
)

convert_file(
    "/Users/konradmakosa/Documents/Bones/rerun/rerun_animation3/npz_models/Flick Flack Acrobatics Model.npz",
    "/Users/konradmakosa/Documents/Bones/rerun/rerun_animation3/npz_models/converted_models/flick_flack_24joints_v7.npz"
)
