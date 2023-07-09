import csv

# 監視ログと紐づけテーブルのパス
LOG_FILE_PATH = "C:\\Users\\hltoy\\OneDrive\\ドキュメント\\python\\zabbix\\log\\snmptrap.txt"
CSV_FILE_PATH = "C:\\Users\\hltoy\\OneDrive\\ドキュメント\\python\\zabbix\\csv\\link_table.csv"
OUTPUT_FILE_PATH = "C:\\Users\\hltoy\\OneDrive\\ドキュメント\\python\\zabbix\\output\\output.csv"

def get_last_line(file_path):
    """指定したテキストファイルの最終行を取得します。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            last_line = file.readlines()[-1]
        return last_line
    except Exception as e:
        print(f"Error occurred while reading file {file_path}: {e}")
        return None

def get_link_table(file_path):
    """CSVファイルから紐づけテーブルを取得します。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            link_table = list(csv_reader)
        return link_table
    except Exception as e:
        print(f"Error occurred while reading CSV file {file_path}: {e}")
        return []

def search_in_log(log, link_table):
    """ログの中からリンクテーブルに存在するデータを探します。"""
    found_records = []
    for record in link_table:
        ip, port, _, _ = record
        if ip in log and port in log:
            found_records.append(record)
    return found_records

def write_output(file_path, log, records):
    """出力をCSVファイルに書き込みます。"""
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            if records:
                for record in records:
                    writer.writerow([log] + record)
            else:
                writer.writerow([log, "不明", "不明", "不明", "不明"])
    except Exception as e:
        print(f"Error occurred while writing to CSV file {file_path}: {e}")

def main():
    # ファイルからデータを取得
    log = get_last_line(LOG_FILE_PATH)
    if log is None:
        return

    link_table = get_link_table(CSV_FILE_PATH)

    # ログの中から該当するレコードを探す
    found_records = search_in_log(log, link_table)

    # 出力を書き込む
    write_output(OUTPUT_FILE_PATH, log, found_records)

if __name__ == "__main__":
    main()