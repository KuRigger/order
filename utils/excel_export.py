import pandas as pd
from datetime import datetime

def export_to_excel(data):
    df = pd.DataFrame(data)
    if 'user_id' in df.columns:
        df = df.drop(columns=['user_id'])
    filename = f"approved_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(filename, index=False)
    return filename