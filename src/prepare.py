import pandas as pd
import os
RAW_DATA_PATH = '../data/raw/raw_export.csv'
PROCESSED_DATA_PATH = '../data/processed/dataset_for_labeling.csv'
def prepare_data():
    print("1. Загрузка сырых данных...")
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Ошибка: Файл не найден по пути {RAW_DATA_PATH}")
        return
    df = pd.read_csv(RAW_DATA_PATH, sep='\t', dtype=str) 
    print(f"Исходный размер датасета: {len(df)} строк.")
    columns_to_keep = ['Author', 'Date', 'Content']
    df = df[columns_to_keep]
    df = df.dropna(subset=['Content'])
    df = df[df['Author'] != 'Deleted User']
    df['label'] = '' 
    print(f"Размер после очистки: {len(df)} строк.")
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, sep=';', index=False, encoding='utf-8-sig')
    print(f"Файл для разметки сохранен сюда: {PROCESSED_DATA_PATH}")
if __name__ == "__main__":
    prepare_data()
