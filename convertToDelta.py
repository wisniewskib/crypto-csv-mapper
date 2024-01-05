from datetime import datetime
import csv
from record import DeltaRecord

records = []


def processXeggexTrades(row):
    _, time, pair, side, price, quantity, totalwithFee, _ = row
    left, right = pair.split("/")
    parsed_date = datetime.strptime(time, "%m/%d/%Y, %I:%M:%S %p")
    formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S%z")

    record = DeltaRecord(
        formatted_date,
        side,
        quantity,
        left,
        "CRYPTO",
        totalwithFee,
        right,
        "Xeggex",
        None,
        None,
        None,
        None,
        None,
        None,
    )
    records.append(record)


def processXeggexDeposits(row):
    (_, time, ticker, amount, _, _, _, address, _, _, _) = row
    parsed_date = datetime.strptime(time, "%m/%d/%Y, %I:%M:%S %p")
    formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S%z")
    record = DeltaRecord(
        formatted_date,
        "DEPOSIT",
        amount,
        ticker,
        "CRYPTO",
        None,
        None,
        None,
        address,
        "Xeggex",
        None,
        None,
        None,
        None,
    )
    records.append(record)


def processXeggexDeposits(row):
    (_, time, ticker, amount, _, _, _, address, _, _, _) = row
    parsed_date = datetime.strptime(time, "%m/%d/%Y, %I:%M:%S %p")
    formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S%z")
    record = DeltaRecord(
        formatted_date,
        "DEPOSIT",
        amount,
        ticker,
        "CRYPTO",
        None,
        None,
        None,
        address,
        "Xeggex",
        None,
        None,
        None,
        None,
    )
    records.append(record)


with open("./trading_csvs/trading.csv", mode="r") as file:
    csv_reader = csv.reader(file)

    for i, row in enumerate(csv_reader):
        if i > 0:
            processXeggexTrades(row)


with open("deltaTransactions.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(
        [
            "Date",
            "Way",
            "Base Amount",
            "Base Currency",
            "Base Type",
            "Quote Amount",
            "Quote Currency",
            "Exchange",
            "Sent From",
            "Sent To",
            "Fee Amount",
            "Fee Currency",
            "Broker",
            "Notes",
        ]
    )

    # Write the data rows
    for record in records:
        writer.writerow(
            [
                record.date,
                record.way,
                record.baseAmount,
                record.baseCurrency,
                record.baseType,
                record.quoteAmount,
                record.quoteCurrency,
                record.exchange,
                record.sentFrom,
                record.sentTo,
                record.feeAmount,
                record.feeCurrency,
                record.broker,
                record.notes,
            ]
        )
